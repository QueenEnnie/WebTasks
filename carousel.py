from flask import Flask
from flask import url_for, request

app = Flask(__name__)
image_name = "static/img/astro.png"


@app.route('/')
def title():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    text = ["Человечество вырастает из детства.",
            "Человечеству мала одна планета.",
            "Мы сделаем обитаемыми безжизненные пока планеты.",
            "И начнем с Марса!",
            "Присоединяйся!"]
    return "</br>".join(text)


@app.route('/image_mars')
def mars_image():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс!</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars_image.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <p>Вот она какая, красная планета.</p>
                  </body>
                </html>"""


@app.route("/promotion_image")
def image_with_promotion():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Колонизация</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марс!</h1>
                    <img src="{url_for('static', filename='img/mars_image.png')}" 
                    alt="здесь должна была быть картинка, но не нашлась">
                    <div class="alert alert-dark" role="alert">
                      Человечество вырастает из детства.
                    </div>
                    <div class="alert alert-success" role="alert">
                      Человечеству мала одна планета.
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      Мы сделаем обитаемыми безжизненные пока планеты.
                    </div>
                    <div class="alert alert-warning" role="alert">
                      И начнем с Марса!
                    </div>
                    <div class="alert alert-danger" role="alert">
                      Присоединяйся!
                    </div>
                  </body>
                </html>"""


@app.route("/astronaut_selection", methods=["POST", "GET"])
def selection():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" href=
                            "{url_for('static', filename='css/selection_style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h3 align="center">Анкета претендента</h3>
                            <h4 align="center">на участие в миссии</h4>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="surname" 
                                    placeholder="Введите фамилию" name="surname">
                                    <input type="text" class="form-control" id="name" 
                                    placeholder="Введите имя" name="name">
                                    <p> </p>
                                    <p> </p>
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" 
                                    placeholder="Введите адрес почты" name="email">
                                    <div class="form-group">
                                        <label for="classSelect">Какое у Вас образование?</label>
                                        <select class="form-select"" id="educationSelect" name="education">
                                          <option>Начальное</option>
                                          <option>Среднее</option>
                                          <option>Высшее</option>
                                        </select>
                                     </div>
                                     <p> </p>
                                     <p>Какие у Вас есть профессии?</p>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="searcher">
                                          <label class="form-check-label" for="searcher">
                                            Инженер-исследователь
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="pilot">
                                          <label class="form-check-label" for="pilot">
                                            Пилот
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="builder">
                                          <label class="form-check-label" for="builder">
                                            Строитель
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="exobiologist">
                                          <label class="form-check-label" for="exobiologist">
                                            Экзобиолог
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="doctor">
                                          <label class="form-check-label" for="doctor">
                                            Врач
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" 
                                          id="terraformingengineer">
                                          <label class="form-check-label" for="terraformingengineer">
                                            Инженер по терраформированию
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="climate">
                                          <label class="form-check-label" for="climate">
                                            Климатолог
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="radioactive">
                                          <label class="form-check-label" for="radioactive">
                                            Специалист по радиационной защите
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="astrogeologist">
                                          <label class="form-check-label" for="astrogeologist">
                                            Астрогеолог
                                          </label>
                                     </div>
                                    <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="glaciologist">
                                          <label class="form-check-label" for="glaciologist">
                                            Гляциолог
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="live">
                                          <label class="form-check-label" for="live">
                                            Инженер жизнеобеспечения
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="meteorologist">
                                          <label class="form-check-label" for="meteorologist">
                                            Метеоролог
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="operator">
                                          <label class="form-check-label" for="operator">
                                            Оператор марсохода
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="cyber">
                                          <label class="form-check-label" for="cyber">
                                            Киберинженер
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="navigator">
                                          <label class="form-check-label" for="navigator">
                                            Штурман
                                          </label>
                                     </div>
                                     <div class="form-check">
                                          <input class="form-check-input" type="checkbox" value="" id="dron">
                                          <label class="form-check-label" for="dron">
                                            Пилот дронов
                                          </label>
                                     </div>
                                    <p> </p>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" 
                                          value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" 
                                          value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <p> </p>
                                    <div class="form-group">
                                        <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <p> </p>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>
                                    <p> </p>
                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов остаться на 
                                        Марсе?</label>
                                    </div>
                                     <p> </p>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        pass
        return "Форма отправлена"


@app.route("/choice/<planet_name>")
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предложение: {planet_name}</h1>
                    <div class="alert alert-light" role="alert">
                      <h4>Эта планета близка к Земле;</h4>
                    </div>
                    <div class="alert alert-success" role="alert">
                      <h4>На ней много необходимых ресурсов;</h4>
                    </div>
                    <div class="alert alert-secondary" role="alert">
                      <h4>На ней есть вода и атмосфера;</h4>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <h4>На ней есть небольшое магнитное поле;</h4>
                    </div>
                    <div class="alert alert-danger" role="alert">
                      <h4>Наконец, она просто красива!</h4>
                    </div>
                  </body>
                </html>"""


@app.route("/results/<nickname>/<int:level>/<float:rating>")
def results(nickname, level, rating):
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Результаты</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <h2>Претендента на участие в миссии {nickname}:</h2>
                    <div class="alert alert-success" role="alert">
                      <h4>Поздравляем! Ваш рейтинг после {level} этапа отбора</h4>
                    </div>
                    <div class="alert alert-light" role="alert">
                      <h4>составляет {rating}!</h4>
                    </div>
                    <div class="alert alert-warning" role="alert">
                      <h3>Желаем удачи!</h3>
                    </div>
                  </body>
                </html>"""


@app.route('/load_photo', methods=['POST', 'GET'])
def load_image():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                             <link rel="stylesheet"
                             href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                             integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                             crossorigin="anonymous">
                            <link rel="stylesheet" type="text/css" 
                            href="{url_for('static', filename='css/selection_style.css')}" />
                            <title>Отбор астронавтов</title>
                          </head>
                          <body>
                            <h1 align="center">Загрузка фотографии</h1>
                            <h3 align="center">для участия в миссии</h3>
                            <div>
                                <form class="login_form" method="post" enctype="multipart/form-data">
                                   <p>Приложите фотографию</p>
                                   <div class="form-group">
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                        <img src="{url_for('static', filename="img/astro.png")}" 
                                        alt="здесь должна была быть картинка, но не нашлась">
                                    </div>
                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                </form>
                            </div>
                          </body>
                        </html>'''
    elif request.method == 'POST':
        file = request.files['file']
        data = file.read()
        with open("static/img/astro.png", "wb") as file:
            file.write(data)
        return "Форма отправлена"


@app.route('/carousel')
def views():
    return f"""<!doctype html>
                <html lang="en">
                  <head>
                    <meta charset="utf-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/css/bootstrap.min.css" 
                    integrity="sha384-Gn5384xqQ1aoWXA+058RXPxPg6fy4IWvTNh0E263XmFcJlSAwiGgFAW/dAiS6JXm" 
                    crossorigin="anonymous">
                    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js" 
                    integrity="sha384-KJ3o2DKtIkvYIK3UENzmM7KCkRr/rE9/Qpg6aAZGJwFDMVNA/GpGFF93hXpG5KkN" 
                    crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.12.9/dist/umd/popper.min.js" 
                    integrity="sha384-ApNbgh9B+Y1QKtv3Rn7W3mgPxhU9K/ScQsAP7hUibX39j7fakFPskvXusvfa0b4Q" 
                    crossorigin="anonymous"></script>
                    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.0.0/dist/js/bootstrap.min.js" 
                    integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" 
                    crossorigin="anonymous"></script>
                    <title>Пейзажи Марса</title>
                  </head>
                  <body>
                    <h1 align="center">Пейзажи Марса</h1>
                    <div id="carouselExampleIndicators" class="carousel slide" data-ride="carousel">
                      <ol class="carousel-indicators">
                        <li data-target="#carouselExampleIndicators" data-slide-to="0" class="active"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="1"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="2"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="3"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="4"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="5"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="6"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="7"></li>
                        <li data-target="#carouselExampleIndicators" data-slide-to="8"></li>
                      </ol>
                      <div class="carousel-inner">
                        <div class="carousel-item active">
                          <img class="d-block w-100" src="{url_for('static', filename="img/mars_1.png")}" 
                          alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{url_for('static', filename="img/mars_7.jpeg")}" 
                          alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{url_for('static', filename="img/mars_2.jpeg")}" 
                          alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{url_for('static', filename="img/mars_6.jpeg")}" 
                          alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{url_for('static', filename="img/mars_8.jpeg")}" 
                          alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{url_for('static', filename="img/mars_4.jpeg")}" 
                          alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{url_for('static', filename="img/mars_5.jpeg")}" 
                          alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{url_for('static', filename="img/mars_3.jpeg")}" 
                          alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                        <div class="carousel-item">
                          <img class="d-block w-100" src="{url_for('static', filename="img/mars_9.png")}" 
                          alt="здесь должна была быть картинка, но не нашлась">
                        </div>
                      </div>
                      <a class="carousel-control-prev" href="#carouselExampleIndicators" role="button" data-slide="prev">
                        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
                        <span class="sr-only">Previous</span>
                      </a>
                      <a class="carousel-control-next" href="#carouselExampleIndicators" role="button" data-slide="next">
                        <span class="carousel-control-next-icon" aria-hidden="true"></span>
                        <span class="sr-only">Next</span>
                      </a>
                    </div>
                  </body>
                </html>"""


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
