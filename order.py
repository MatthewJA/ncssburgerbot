from flaskapp import app
from flask import request

past_orders = []

@app.route('/order', methods=['GET', 'POST'])
def order():
    order = request.values.get('text')
    user = request.values.get('user_name')
    past_orders.append((order, user))
    return f'ok {user}, I ordered you a {order}.'

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    list_of_orders = [f'{order} for {user}' for order, user in past_orders]
    return ', '.join(list_of_orders)

