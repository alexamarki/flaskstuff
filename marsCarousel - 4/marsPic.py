from flask import Flask, url_for, request, redirect
import random
import os

UPLOAD_FOLDER = './static/img'
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
def main():
    return "Миссия Колонизация Марса"


@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion_image')
def promotion_image():
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
                        href="{url_for('static', filename='css/style.css')}"/>
                        <title>Жди нас, Марс!</title>
                      </head>
                      <body>
                        <h1>Жди нас, Марс!</h1>
                        <img src="static/img/Mars.png"alt="здесь должна была быть картинка, но не нашлась">
                        <br>
                        <div class="alert alert-dark" role="alert">
                            Человечество вырастает из детства.
                        </div>
                        <div class="alert alert-success" role="alert">
                            Человечеству мала одна планета.
                        </div>
                        <div class="alert alert-dark" role="alert">
                            Мы сделаем обитаемыми безжизненные пока планеты.
                        </div>
                        <div class="alert alert-warning" role="alert">
                            И начнем с Марса!
                        </div>
                        <div class="alert alert-danger" role="alert">
                            Присоединяйся!
                        </div>
                      </body>
                    </html>'''


@app.route('/astronaut_selection', methods=['GET', 'POST'])
def astronaut_selection():
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
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                                <h1 class="text-center">Анкета претендента</h1>
                                <h3 class="text-center">на участие в миссии</h3>
                              </head>
                              <body>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <input type="lastName" class="form-control" id="lastName" placeholder="Введите фамилию" name="lastName">
                                        <input type="firstName" class="form-control" id="firstName" placeholder="Введите имя" name="firstName">
                                        <br>
                                        <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                        <div class="form-group">
                                            <label for="eduSelect">Какое у Вас образование?</label>
                                            <select class="form-control" id="eduSelect" name="edu">
                                              <option>Начальное</option>
                                              <option>Среднее</option>
                                               <option>Высшее</option>
                                              <option>Второе высшее</option>
                                            </select>
                                        </div><br>
                                        <div class="form-group">
                                            <label for="form-check">Какие у Вас есть профессии?</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="eng-research" value="eng-research">
                                              <label class="form-check-label" for="eng-research">
                                                Инженер-исследователь
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="eng-const" value="eng-const">
                                              <label class="form-check-label" for="eng-const">
                                                Инженер-строитель
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="pilot" value="pilot">
                                              <label class="form-check-label" for="pilot">
                                                Пилот
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="meteo" value="meteo">
                                              <label class="form-check-label" for="meteo">
                                                Метеоролог
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="eng-life" value="eng-life">
                                              <label class="form-check-label" for="eng-life">
                                                Инженер по жизнеобеспечению
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="eng-rad" value="eng-rad">
                                              <label class="form-check-label" for="eng-rad">
                                                Инженер по радиационной защите
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="doc" value="doc">
                                              <label class="form-check-label" for="doc>
                                                Врач
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="prof" id="exobio" value="exobio">
                                              <label class="form-check-label" for="exobio">
                                                Экзобиолог
                                              </label>
                                            </div>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="form-check">Укажите пол</label>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                              <label class="form-check-label" for="male">
                                                Мужской
                                              </label>
                                            </div>
                                            <div class="form-check">
                                              <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                              <label class="form-check-label" for="female">
                                                Женский
                                              </label>
                                            </div>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="about">Почему Вы хотите принять участие в миссии?</label>
                                            <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                        </div>
                                        <br>
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <br>
                                        <div class="form-group form-check">
                                            <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                            <label class="form-check-label" for="acceptRules">Готовы остаться на Марсе?</label>
                                        </div>
                                        <br>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        print(request.form['lastName'])
        print(request.form['firstName'])
        print(request.form['email'])
        print(request.form.get('edu'))
        print(request.form['prof'])
        print(request.form['sex'])
        print(request.form['about'])
        file = request.files['file']
        print(file.read())
        print(request.form.get('accept'))
        return "Форма отправлена"


@app.route('/choice/<planet_name>')
def choice(planet_name):
    lines = {1: ['Эта планета - почти как Земля;', 'Эта планета близка к Земле;', 'Эта планета далека от Земли;'],
             2: ['На ней ничего нет;', 'На ней есть все, что пожелаешь;', 'На ней прекрасные виды;',
                 'На ней все дни замечательные;', 'Жить на ней - радость да и только!;', 'Комфортнее места не найти;',
                 'На ней даже есть коты;']}
    first_line = random.choice(lines[1])
    the_rest = random.sample(lines[2], 4)
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
                        href="{url_for('static', filename='css/style.css')}"/>
                        <title>Варианты выбора</title>
                      </head>
                      <body>
                        <h1>Мое предложение: {planet_name}</h1>
                        <h5>{first_line}</h5>
                        <div class="alert alert-success" role="alert">
                            <h5>{the_rest[0]}</h5>
                        </div>
                        <div class="alert alert-secondary" role="alert">
                            <h5>{the_rest[1]}</h5>
                        </div>
                        <div class="alert alert-warning" role="alert">
                            <h5>{the_rest[2]}</h5>
                        </div>
                        <div class="alert alert-danger" role="alert">
                            <h5>{the_rest[3]}</h5>
                        </div>
                      </body>
                    </html>'''


@app.route('/results/<nickname>/<int:level>/<float:rating>')
def results(nickname, level, rating):
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
                        href="{url_for('static', filename='css/style.css')}"/>
                        <title>Результаты</title>
                      </head>
                      <body>
                        <h1>Результаты отбора</h1>
                        <h3>Претендента на участие в миссии {nickname}:</h3>
                        <div class="alert alert-success" role="alert">
                            <h5>Поздравляем! Ваш рейтинг после {level} этапа отбора</h5>
                        </div>
                        <h5>составляет {rating}!</h5>
                        <div class="alert alert-warning" role="alert">
                            <h3>Желаем удачи!</h3>
                        </div>
                      </body>
                    </html>'''


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], 'mission_avatar.png')):
            return f'''<!doctype html>
                                        <html lang="en">
                                          <head>
                                            <meta charset="utf-8">
                                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                            <link rel="stylesheet"
                                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                            crossorigin="anonymous">
                                            <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                            <title>Отбор астронавтов</title>
                                          </head>
                                          <body>
                                            <h1 align="center">Загрузка фотографии</h1>
                                            <h3 align="center">Для участия в миссии</h3>
                                            <div>
                                                <form class="login_form" method="post" enctype="multipart/form-data">
                                                    <div class="form-group">
                                                        <label for="photo">Приложите фотографию</label>
                                                        <br>
                                                        <input type="file" class="form-control-file" id="photo" name="file">
                                                    </div>
                                                    <br>
                                                    <img src="{os.path.join(app.config['UPLOAD_FOLDER'], 'mission_avatar.png')}"/>
                                                    <br>
                                                    <button type="submit" class="btn btn-primary">Отправить</button>
                                                </form>
                                            </div>
                                          </body>
                                        </html>'''
        return f'''<!doctype html>
                            <html lang="en">
                              <head>
                                <meta charset="utf-8">
                                <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                                <link rel="stylesheet"
                                href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                                integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                                crossorigin="anonymous">
                                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}" />
                                <title>Отбор астронавтов</title>
                              </head>
                              <body>
                                <h1 align="center">Загрузка фотографии</h1>
                                <h3 align="center">Для участия в миссии</h3>
                                <div>
                                    <form class="login_form" method="post" enctype="multipart/form-data">
                                        <div class="form-group">
                                            <label for="photo">Приложите фотографию</label>
                                            <br>
                                            <input type="file" class="form-control-file" id="photo" name="file">
                                        </div>
                                        <br>
                                        <button type="submit" class="btn btn-primary">Отправить</button>
                                    </form>
                                </div>
                              </body>
                            </html>'''
    elif request.method == 'POST':
        file = ''
        if 'file' in request.files:
            file = request.files['file']
        if file:
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], 'mission_avatar.png'))


@app.route('/carousel')
def carousel():
    return f'''<!doctype html>
                    <html lang="en">
                      <head>
                        <meta charset="utf-8">
                        <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                        <link rel="stylesheet"
                        href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                        integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                        crossorigin="anonymous">
                        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-KK94CHFLLe+nY2dmCWGMq91rCGa5gtU4mk92HdvYe+M/SXH301p5ILy+dN9+nJOZ" crossorigin="anonymous">
                        <link rel="stylesheet" type="text/css"
                        href="{url_for('static', filename='css/style.css')}"/>
                        <title>Изображения Марса</title>
                      </head>
                      <body>
                        <h1 align="center">Изображения Марса</h1>
                        <div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
                          <div class="carousel-inner">
                            <div class="carousel-item active">
                              <img src="/static/img/carousel1.jpg" class="d-block w-100">
                            </div>
                            <div class="carousel-item">
                              <img src="/static/img/carousel2.jpg" class="d-block w-100">
                            </div>
                            <div class="carousel-item">
                              <img src="/static/img/carousel3.jpg" class="d-block w-100">
                            </div>
                            <div class="carousel-item">
                              <img src="/static/img/carousel4.jpg" class="d-block w-100">
                            </div>
                          </div>
                        </div>
                      </body>
                      <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ENjdO4Dr2bkBIFxQpeoTz1HIcje39Wm4jDKdf19U8gI4ddQ3GYNS7NTKfAdVQSZe" crossorigin="anonymous"></script>
                    </html>'''



if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
