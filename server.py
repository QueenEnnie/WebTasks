import datetime
from data import db_session
from flask import Flask
from flask import render_template, redirect

from data.users import User
from data.jobs import Jobs

from data.login_form import LoginForm
from flask_login import LoginManager, login_user, login_required, logout_user


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'

login_manager = LoginManager()
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html',
                               message="Неправильный логин или пароль",
                               form=form)
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


def main():
    db_session.global_init("db/blogs.db")
    # app.run()
    session = db_session.create_session()
    captain = User(surname="Scott", name='Ridley', age=21, position='captain',
                   speciality='research engineer', address='module_1', email='scott_chief@mars.org')
    first_user = User(surname="Potter", name='Harry', age=19, position='colonist',
                      speciality='doctor', address='module_2', email='potter_harry@mars.org')
    second_user = User(surname="Eyre", name='Jane', age=25, position='colonist',
                       speciality='pilot', address='module_3', email='eyre_jane@mars.org')
    third_user = User(surname="Mussolini", name='Benito', age=32, position='colonist',
                      speciality='navigator', address='module_4', email='benito@mars.org')
    session.add(captain)
    session.add(first_user)
    session.add(second_user)
    session.add(third_user)
    session.commit()


if __name__ == '__main__':
    main()
