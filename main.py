from flask import Flask, url_for

app = Flask(__name__)

@app.route('/')
@app.route('/index')
def index():
    return 'Адмирал!<br><a href="/slogan">Слоган</a>'

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


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
