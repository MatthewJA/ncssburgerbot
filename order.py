from flaskapp import app, db
from flask import request

@app.route('/order', methods=['GET', 'POST'])
def order():
    order = request.values.get('text')
    user = request.values.get('user_name')
    db.past_orders.insert_one({'order': order, 'user': user})
    return f'ok {user}, I ordered you a {order}.'

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    past_orders = db.past_orders.find()
    if past_orders.count() == 0:
        return 'no past orders!'

    list_of_orders = []
    for order in past_orders:
        order_string = f'{order["order"]} for {order["user"]}'
        list_of_orders.append(order_string)
    return ', '.join(list_of_orders)
