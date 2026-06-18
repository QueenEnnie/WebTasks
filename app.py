"""Portfolio version of the Yandex Lyceum Mars training project."""

import os
from pathlib import Path

from flask import Flask, flash, redirect, render_template, url_for
from flask_login import LoginManager, login_required, login_user, logout_user

from data import db_session
from data.jobs import Jobs
from data.login_form import LoginForm
from data.users import User
from data.users_form import RegisterForm


BASE_DIR = Path(__file__).resolve().parent
DATABASE_PATH = BASE_DIR / "db" / "blogs.db"

login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.login_message = "Войдите, чтобы открыть эту страницу."
login_manager.login_message_category = "info"


@login_manager.user_loader
def load_user(user_id):
    session = db_session.create_session()
    try:
        return session.get(User, int(user_id))
    finally:
        session.close()


def create_app(test_config=None):
    """Create the consolidated showcase application."""
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.getenv("SECRET_KEY", "portfolio-development-key"),
        DATABASE=str(DATABASE_PATH),
    )
    if test_config:
        app.config.update(test_config)

    db_session.global_init(app.config["DATABASE"])
    login_manager.init_app(app)
    register_routes(app)
    return app


def register_routes(app):
    @app.get("/")
    def portfolio():
        return render_template("portfolio.html", title="Mars One — учебный проект")

    @app.get("/works")
    def works():
        session = db_session.create_session()
        try:
            jobs = session.query(Jobs).order_by(Jobs.id).all()
            users = {
                user.id: f"{user.surname} {user.name}"
                for user in session.query(User).all()
            }
            return render_template(
                "index.html", title="Журнал работ", jobs=jobs, users=users
            )
        finally:
            session.close()

    @app.route("/login", methods=["GET", "POST"])
    def login():
        form = LoginForm()
        if form.validate_on_submit():
            session = db_session.create_session()
            try:
                user = session.query(User).filter(User.email == form.email.data).first()
                if user and user.check_password(form.password.data):
                    login_user(user, remember=form.remember_me.data)
                    flash("Добро пожаловать на борт!", "success")
                    return redirect(url_for("portfolio"))
            finally:
                session.close()
            flash("Неверная почта или пароль.", "danger")
        return render_template("login.html", title="Вход", form=form)

    @app.get("/logout")
    @login_required
    def logout():
        logout_user()
        flash("Вы вышли из аккаунта.", "info")
        return redirect(url_for("portfolio"))

    @app.route("/register", methods=["GET", "POST"])
    def register():
        form = RegisterForm()
        if form.validate_on_submit():
            if form.password.data != form.password_again.data:
                flash("Пароли не совпадают.", "danger")
                return render_template("register.html", title="Регистрация", form=form)

            session = db_session.create_session()
            try:
                existing = session.query(User).filter(User.email == form.email.data).first()
                if existing:
                    flash("Пользователь с такой почтой уже существует.", "danger")
                    return render_template(
                        "register.html", title="Регистрация", form=form
                    )
                user = User(
                    surname=form.surname.data,
                    name=form.name.data,
                    email=form.email.data,
                    age=form.age.data,
                    position=form.position.data,
                    speciality=form.speciality.data,
                    address=form.address.data,
                )
                user.set_password(form.password.data)
                session.add(user)
                session.commit()
            finally:
                session.close()
            flash("Аккаунт создан. Теперь можно войти.", "success")
            return redirect(url_for("login"))
        return render_template("register.html", title="Регистрация", form=form)

    @app.get("/training/<prof>")
    def training(prof):
        return render_template("training.html", title="Тренажёры", prof=prof)

    @app.get("/professions/<list_type>")
    def professions(list_type):
        return render_template(
            "job_list.html", title="Профессии", list_type=list_type
        )

    @app.get("/answer")
    def answer():
        information = {
            "title": "Анкета",
            "surname": "Watney",
            "name": "Mark",
            "education": "высшее",
            "profession": "инженер-ботаник",
            "sex": "male",
            "motivation": "Всегда мечтал застрять на Марсе!",
            "ready": "Да",
        }
        return render_template(
            "auto_answer.html",
            dictionary=information,
            title=information["title"],
        )

    @app.get("/distribution")
    def distribution():
        crew = [
            "Ридли Скотт",
            "Энди Уир",
            "Марк Уотни",
            "Венката Капур",
            "Тедди Сандерс",
            "Шон Бин",
        ]
        return render_template(
            "distribution.html", title="Размещение экипажа", crew=crew
        )

    @app.get("/table/<sex>/<int:age>")
    def cabin(sex, age):
        if sex not in {"male", "female"}:
            return render_template("404.html", title="Неверный параметр"), 404
        return render_template("table.html", title="Оформление каюты", sex=sex, age=age)

    @app.get("/gallery")
    def gallery():
        images = [f"mars_{number}.{('png' if number in {1, 9} else 'jpeg')}" for number in range(1, 10)]
        return render_template("carousel.html", title="Марсианская галерея", images=images)

    @app.errorhandler(404)
    def not_found(_error):
        return render_template("404.html", title="Страница не найдена"), 404


app = create_app()


if __name__ == "__main__":
    app.run(debug=os.getenv("FLASK_DEBUG") == "1")
