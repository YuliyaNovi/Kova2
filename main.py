from flask import Flask, url_for, request, redirect
from flask import render_template, abort
import json
import requests

from forms.add_news import NewsForm
from loginform import LoginForm
from data import db_session
from flask_login import login_manager, LoginManager, login_user, login_required, logout_user, current_user
from data.users import User
from data.news import News
from forms.user import RegisterForm
from flask import make_response, session
import datetime


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.config['SECRET_KEY'] = 'too short key'
app.config['SQLALCHEMY_DATABASE_URL'] = 'sqlite:///db/news.sqlite'
app.config['PERMANENT_SESSION_LIFETIME'] = datetime.timedelta(days=365)  # ГОД

@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)

# @app.route('/')
# @app.route('/index')
# def index():
#     param = {}
#     param['username'] = 'Слушатель'
#     param['title'] = 'Расширяем шаблоны'
#     return render_template('index.html', **param)

@app.route('/odd_even')
def odd_even():
    return render_template('odd_even.html', number=3)

@app.route('/news', methods=['GET', 'POST'])
@login_required
# def news():
    # with open ("news.json", "rt", encoding="utf8") as f:
    #     new_list = json.loads(f.read())
# return render_template('news.html', title="Новости", news=new_list)
def add_news():
    form = NewsForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = News()
        news.title = form.title.data
        news.content = form.content.data
        news.is_private = form.is_private.data
        current_user.news.append(news)
        db_sess.merge(current_user)  # слияние сесси с текущим пользователем
        db_sess.commit()
        return redirect('/')
    return render_template('news.html', title='Добавление новости', form=form)

@app.route('/news/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_news(id):
    print(id)
    form = NewsForm
    if request.method == 'GET':
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user).first()
        print(News.id, id)
        print(current_user, News.user)
        if news:
            form.title.data = news.title
            form.content.data = news.content
            form.is_private.data = news.is_private
        else:
            abort(404)
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        news = db_sess.query(News).filter(News.id == id,
                                          News.user == current_user).first()
        if news:
            news.title = form.title.data
            news.content = form.content.data
            news.is_private = form.is_private.data
            db_sess.commit()
            return redirect('/')
        else:
            abort(404)
        return render_template('news.html', title='Редактирование новости', form=form)



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

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # print(form.password, form.password_again)
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Проблемы с регистрацией',
                                   message='Пароли не совпадают', form=form)
        db_sess = db_session.create_session()
        if db_sess.query(User).filter(User.email == form.email.data).first():
            return render_template('register.html', title='Проблемы с регистрацией',
                                   message='Такой пользователь уже есть', form=form)
        user = User(name=form.name.data, email=form.email.data, about=form.about.data)
        user.set_password(form.password.data)
        db_sess.add(user)
        db_sess.commit()
        return redirect('/login')
    return render_template('register.html', title='Регистрация', form=form)



@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(User.email == form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect('/')
        return render_template('login.html', title='Повторная авторизация',
                               message='Неверный логин или пароль', form=form)
    return render_template('login.html', title='авторизация', form=form)

# if __name__ == '__main__':
#     db_session.global_init('db/news.sqlite')
#     # app.run(host='127.0.0.1', port=5000, debug=True)
    # В сложных запросах:
    # '|' - означает или
    # '&' - означает и
    # Работу с БД начинают с открытия сессии
    # db_sess = db_session.create_session()
    # С помощью объекта сессии происходит обращение к таблице
    # users = db_sess.query(User).first()
    # users = db_sess.query(User).all()  # выполняем запрос к классу
    # users = db_sess.query(User).filter(User.id > 1)
    # users = db_sess.query(User).filter(User.name.notilike('%d%'))  # выводит тех, в которых нет d (не учитывает регистр)
    # users = db_sess.query(User).filter(User.name.notlike('%d%'))
    # for user in users:
    #     print(user)
    # user = db_sess.query(User).filter(User.id == 1).first()  # Voldemar will be changed to Vladimir
    # user.name = 'Vladimir'
    # db_sess.commit()

    # Удаление
    # user = db_sess.query(User).filter(User.id == 2).first()
    # db_sess.delete(user)
    # db_sess.commit()
    #
    # news = News(title='Новости от Владимира', content="Опаздываю на работу",
    #             user_id=1, is_private=False)
    #
    # db_sess.add(news)
    # db_sess.commit()
    #
    # id = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title='Новости от Владимира №2', content="Больше не опаздываю",
    #             user_id=id.id, is_private=False)
    #
    # db_sess.add(news)
    # db_sess.commit()


    # user = db_sess.query(User).filter(User.id == 1).first()
    # news = News(title='Новости от Владимира №3', content="На месте", is_private=False)
    # news = News(title='Новости от Владимира №4', content="Пошел на обед", is_private=False)
    # id.news.append(news)  # добавили новость с помощью append
    # db_sess.commit()
    #
    # user = db_sess.query(User).filter(User.id == 1).first()
    # for news in user.news:
    #     print(news)


@app.route('/')
@app.route('/index')
# @login_required # не позволяет зайти на главную страницу без авторизации
def index():
    db_sess = db_session.create_session()
    if current_user.is_authenticated:
        news = db_sess.query(News).filter(
            (News.user == current_user) | (News.is_private != True))
    else:
        news = db_sess.query(News).filter(News.is_private != True)
    return render_template('index.html', title='Новости', news=news)

# @app.route('/mail', methods=['GET'])
# def get_form():
#     return render_template('mail_send.html')
#
# @app.route('/mail', methods=['POST'])
# def post_form():
#    email = request.values.get('email')
#    if send_mail(email, 'Вам письмо', 'Текст письма'):
#        return f'Письмо на адрес {email} отправлено успешно!'
#    return 'Сбой при отправке'


@app.route('/cookie_test')
def cookie_test():
    visit_count = int(request.cookies.get('visit_count', 0))
    if visit_count != 0 and visit_count < 20:
        res = make_response(f'Были уже {visit_count + 1} раз')
        res.set_cookie('visit_count', str(visit_count + 1),
                       max_age=60 * 60 * 24 * 365 * 2)

    elif visit_count > 5:
        res = make_response(f'Были уже {visit_count + 1} раз')
        res.set_cookie('visit_count', str(visit_count + 1),
                       max_age=0)

    else:
        res = make_response('Вы впервые здесь за 2 года')
        res.set_cookie('visit_count', '1',
                       max_age=60 * 60 * 24 * 365 * 2)

    return res

# @app.route('/session_test')
# def session_test():
#     visit_count = session.get('visit_count', 0)
#     session['visit_count'] = visit_count + 1
#     print(session['visit_count'])
#     session.permanent = True  # Максимум 31 день
#     return make_response(f'Мы тут были уже {visit_count + 1} раз')


# Убить сессию
@app.route('/session_test')
def session_test():
    visit_count = session.get('visit_count', 0)
    session['visit_count'] = visit_count + 1
    if session['visit_count'] > 3:
        session.pop('visit_count', None)
    session.permanent = True  # Максимум 31 день
    return make_response(f'Мы тут были уже {visit_count + 1} раз')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect('/')

@app.errorhandler(401)
def http_401_handler(error):
    return redirect('/login')

if __name__ == '__main__':
    db_session.global_init('db/news.sqlite')
    app.run(host='127.0.0.1', port=5000, debug=True)