from flaskapp import app
from flask import request

@app.route('/order', methods=['GET', 'POST'])
def order():
    order = request.values.get('text')
    user = request.values.get('user_name')
    return f'ok {user}, I ordered you a {order}.'

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    return 'no past orders!'
