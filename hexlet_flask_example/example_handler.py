from flask import make_response, Flask

app = Flask(__name__)


@app.route('/foo')
def foo():
    response = make_response('foo')
    # Устанавливаем заголовок
    response.headers['X-Parachutes'] = 'parachutes are cool'
    # Меняем тип ответа
    response.mimetype = 'text/plain'
    # Задаем статус
    response.status_code = 418
    # Устанавливаем cookie
    response.set_cookie('foo', 'bar')
    return response


