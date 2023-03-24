from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
def main():
    return "Миссия Колонизация Марса"
@app.route('/index')
def index():
    return "И на Марсе будут яблони цвести!"
@app.route('/promotion')
def promotion():
    list1 = [
        "Человечество вырастает из детства.",
        "Человечеству мала одна планета.",
        "Мы сделаем обитаемыми безжизненные пока планеты.",
        "И начнем с Марса!",
        "Присоединяйся!"
    ]
    return '</br>'.join(list1)
@app.route('/image_mars')
def image():
    return f'''<h1>Жди нас, Марс!</h1><img src="static/Mars.png"
           alt="здесь должна была быть картинка, но не нашлась"><br><span>Вот она какая, красная планета.<span>'''

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')