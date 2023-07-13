from flask import Flask, url_for, request, redirect
from flask import render_template
import json
import requests
from loginform import LoginForm
from data import db_session
from data.users import User

app = Flask(__name__)
app.config['SECRET_KEY'] = 'too short key'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db/news.sqlite'

@app.route('/')
@app.route('/index')
def index():
    param = {}
    param['username'] = 'Слушатель'
    param['title'] = 'Расширяем шаблоны'
    return render_template('index.html', **param)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=3)

@app.route('/news')
def news():
    with open ("news.json", "rt", encoding="utf8") as f:
        new_list = json.loads(f.read())
    return render_template('news.html', title="Новости", news=new_list)

@app.route('/vartest')
def vartest():
    return render_template('var_test.html', title='Переменные в HTML')



# @app.route('/')
# @app.route('/index')
# def index():
#     return 'Адмирал!<br><a href="/slogan">Слоган</a>'

@app.route('/poster')
def poster():
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Постер</title>
    <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
<body>
<h1 class="red">Постер к фильму</h1>
<img src="{url_for('static', filename='images/admiral.png')}"
alt="Здесь должна была быть картинка, но не нашлась">
<p>И крепка, как смерть любовь!</p>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
</body>
</html>"""
@app.route('/slogan')
def slogan():
    return 'Ибо крепка, как смерть любовь<br><a href="/">Назад</a>'

@app.route('/countdown')
def countdown():
    lst = [str(x) for x in range(10, 0, -1)]
    lst.append('Start!!!')
    return '<br>'.join(lst)


# @app.route('/nekrasov')
# def nekrasov():
#     return f"""<!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <title>Постер</title>
#     <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
#     <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
# <body>
# <h1 class="red">Некрасов</h1>
# <img src="{url_for('static', filename='images/nekrasov.png')}"
# alt="Здесь должна была быть картинка, но не нашлась">
# <div class="bg-secondary text-white">Я пленен, я очарован,</div>
# <div class="bg-success text-white">Ненаглядная, тобой,</div>
# <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
# <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
# </body>
# # </html>"""
# @app.route('/slogan')
# def slogan():
#     return 'Ибо крепка, как смерть любовь<br><a href="/">Назад</a>'


@app.route('/nekrasov')
def nekrasov():
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Постер</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
</head>
<body>
<div class="container">
<nav aria-label="breadcrumb">
<ol class="breadcrumb">
<li class="breadcrumb-item"><a href="#">Главная</a></li>
<li class="breadcrumb-item"><a href="#">Библиотека</a></li>
<li class="breadcrumb-item active" aria-current="page">Данные</li>
</ol>
</nav>
<div class="row">
<div class="col">
<h1 class="red">Крестьянские дети</h1>
</div>
</div>
<div class="row">
<div class="col">
<img height="429" width="417"  src="{url_for('static', filename='images/nekrasov.png')}"
alt="Здесь должна был быть картинка, но не нашлась">
</div>
<div class="col">
<div class="bg-secondary text-white">Однажды, в студеную зимнюю пору,</div>
<div class="bg-success text-white">Я из лесу вышел; был сильный мороз.</div>
<div class="bg-secondary text-white">Гляжу, поднимается медленно в гору.</div>
<div class="bg-warning text-dark">Лошадка, везущая хворосту воз.</div>
<div class="bg-danger text-white">Читать далее...</div>
</div>
</div>
<script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
</body>
</html>"""

@app.route('/greeting/<username>')
def greeting(username):
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>{username}</title>
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
    </head>
    <body>
    <h1>Привет, {username}</h1>
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
    </body>
    </html>"""

@app.route('/variants/<int:var>')
def variants(var):
    if var == 1:
        return f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Пока</title>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
            </head>
            <body>
            <dl>
            <dt>Пан или пропал</dt>
            <dd>А что нельзя выжить, став паном?</dd>
            </dl>
            <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
            </body>
            </html>"""
    elif var == 2:
        return f"""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <title>Е</title>
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
                <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
            </head>
            <body>
             <dl>
            <dt>Даже если вас съели, у вас есть два</dt>
            <dd>А в рассказах Мюнхаузена естьо другой способ.</dd>
            </dl>
            <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
            <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
            </body>
            </html>"""
    else:
        return "Я не знаю о чем вы!"

@app.route('/slideshow')
def slideshow():
    return f"""<!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>Постер</title>
        <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
        <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
    </head>
    <body>
    <div id="carouselExampleControls" class="carousel slide" data-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="{url_for('static', filename='images/spain1.jpg')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/spain2.jpg')}" class="d-block w-100" alt="...">
    </div>
    <div class="carousel-item">
      <img src="{url_for('static', filename='images/spain3.jpg')}" class="d-block w-100" alt="...">
    </div>
  </div>
 <a class="carousel-control-prev" href="#carouselExampleControls" role="button" data-slide="prev">
    <span class="carousel-control-prev-icon" aria-hidden="true"></span>
    <span class="sr-only">Previous</span>
  </a>
  <a class="carousel-control-next" href="#carouselExampleControls" role="button" data-slide="next">
    <span class="carousel-control-next-icon" aria-hidden="true"></span>
    <span class="sr-only">Next</span>
  </a>
</div>
    <script src="https://cdn.jsdelivr.net/npm/jquery@3.5.1/dist/jquery.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-Fy6S3B9q64WdZWQUiU+q4/2Lc9npb8tCaSX9FK7E8HnRr0Jz8D6OP9dO5Vg3Q9ct" crossorigin="anonymous"></script>
    </body>
    </html>"""


# @app.route('/form_sample', methods=['GET', 'POST'])
# def form_sample():
#     if request.method == 'GET':
#         return f"""<!DOCTYPE html>
#             <html lang="en">
#             <head>
#                 <meta charset="UTF-8">
#                 <title>Пример формы</title>
#                 <link rel="stylesheet" type="text/css" href="{url_for('static', filename='css/style.css')}">
#                 <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.6.2/dist/css/bootstrap.min.css" integrity="sha384-xOolHFLEh07PJGoPkLv1IbcEPTNtaed2xpHsD9ESMhqIYd0nLMwNLD69Npy4HI+N" crossorigin="anonymous">
#             </head>
#             <body>
#             <h1>Форма для регистрации</h1>
#             <div class="container">
#             <form class="login_form" method="post">
#             <input type="text" class="form-control" name="fname" placeholder="Фамилия"><br>
#             <input type="text" class="form-control" name="sname" placeholder="Имя"><br>
#             <input type="text" class="form-control" name="email" placeholder="E-mail"><br>
#             <input type="text" class="form-control" name="password" placeholder="Password"><br>
#             <div class="form-group">
#             <label for="classSelect">Ваше образование</label>
#             <select class="form-control" id="classSelect" name="profession">
#             <option>Высшее</option>
#             <option>Среднее</option>
#             </select>
#             </div>
#             <!--Radio Button - Gender Selection -->
#             <div class="form-group">
#                 <label for=form-check">Укажите пол</label>
#                 <div class="form-check">
#                 <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
#                 <label class="form-check-label" for="male">Мужской</label>
#             </div>
#             <div class="form-check">
#             <input class="form-check-input" type="radio" name="sex" id="female" value="female">
#             <input class="form-check-label" for="female">Женский</label>
#             </div>
#         </div>
#         <!-- End of Gender Selection -->
#         <!-- Text Area -->
#         <div>
#             <label for="about">Немного о себе</label>
#             <textarea class="form-control" id="about" name="about" rows="3"></textarea>
#         </div><br>
#         <!-- End of Text Area -->
#         <div class="form-group">
#             <label for="photo">Прикрепите фото</label>
#             <input type="file" class="form-control-file" id="photo" name="file">
#         </div>
#         <!-- Check Box -->
#         <div class="form-group form-check">
#             <input type="checkbox" class="form-check-input" id="ready" name="ready">
#             <label class="form-check-label" for="ready">Готовы?</label>
#         </div><br>
#         <!--End Check Box -->
#             <button type="submit" class="btn btn-primary">Отправить</button>
#             </form>
#             </div>
#             </body>
#             </html>"""
#     elif request.method == 'POST':
#         print(request.method)
#         print(request.form['fname'])
#         print(request.form['sname'])
#         return 'Форма отправлена'


@app.route('/form_sample', methods=['GET', 'POST'])
def form_sample():
    if request.method == 'GET':
        return render_template('user_form.html', title='Форма')
    elif request.method == 'POST':
        f = request.files['file']
        f.save('./static/images/loaded.png')
        myform = request.form.to_dict()
        return render_template('filled_form.html',
                               title='Ваши данные',
                               data=myform)


@app.route('/load_photo', methods=['GET', 'POST'])
def load_photo():
    if request.method == 'GET':
        return f"""
        <form class="login_form" method="post" enctype="multipart/form-data">
            <div class="form-group">
                <label for="photo">Приложите фото:</label>
                <input type="file" class="from-control-file" id="photo" name="file">
            </div>
            <button type="submit" class="btn btn-primary">Отправить</button>
    
        </form>
        """
    elif request.method == 'POST':
        f = request.files['file']  # request.form.get('file')
        f.save('./static/images/loaded.png')
        return '<h1>Файл у вас на сервере</h1>'

@app.route('/weather_form', methods=['GET', 'POST'])
def weather_form():
    if request.method == 'GET':
        return render_template('weather_form.html',
                               title='Погода')
    elif request.method == 'POST':
        town = request.form.get('town')
        data = {}
        key = 'd2e12e0537ae1587c34635e76e29f336'
        url = 'http://api.openweathermap.org/data/2.5/weather'
        params = {'APPID': key, 'q': town, 'units': 'metric'}
        result = requests.get(url, params=params)
        weather = result.json()
        code = weather['cod']
        icon = weather['weather'][0]['icon']
        temperature = weather['main']['temp']
        data['code'] = code
        data['icon'] = icon
        data['temp'] = temperature
        return render_template('weather.html',
                               title=f'Погода в городе {town}',
                               town=town, data=data, icon=icon)

@app.errorhandler(404)
def http_404_error(error):
    return redirect('/error404')

@app.route('/error404')
def well():
    return render_template('well.html')

@app.route('/success')
def success():
    return 'Success'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация',
                           form=form)

if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    # app.run(host='127.0.0.1', port=5000, debug=True)
    user = User()
    user.name = 'Mark'
    user.about = 'Plumber'
    user.email = 'Mark@mail.ru'
    db_sess = db_session.create_session()
    db_sess.add(user)
    db_sess.commit()
