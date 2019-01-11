from flaskapp import app, db
from flask import request

@app.route('/order', methods=['GET', 'POST'])
def order():
    order = request.values.get('text')
    user = request.values.get('user_name')
    db.orders.insert_one({
        'name': user,
        'order': order,
    })
    return f'ok {user}, I ordered you a {order}.'

@app.route('/orders', methods=['GET', 'POST'])
def orders():
    past_orders = list(db.orders.find())
    if len(past_orders) == 0:
        return 'no past orders!'
    
    past_order_strings = []
    for order in past_orders:
        string = f'{order["name"]} ordered a {order["order"]}'
        past_order_strings.append(string)
    return ', '.join(past_order_strings)
