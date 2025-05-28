from config import *

# модель для хранения задачи
class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(15), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    s_size = db.Column(db.Integer, nullable=True)
    m_size = db.Column(db.Integer, nullable=True)
    l_size = db.Column(db.Integer, nullable=True)
    xl_size = db.Column(db.Integer, nullable=True)
    description = db.Column(db.String(500), nullable=False)

class Promos(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(15), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)


with app.app_context():
    db.create_all()

def present_item(item):
    return {
        "id": item.id,
        "url": item.url,
        "title": item.title,
        "price": item.price,
        "quantity": item.quantity,
        "s_size": item.s_size,
        "m_size": item.m_size,
        "l_size": item.l_size,
        "xl_size": item.xl_size,
        "description": item.description
    }

def present_promo(promo):
    return {
        "id": promo.id,
        "title": promo.title,
        "quantity": promo.quantity,
        "price": promo.price
    }

# добавляем новую задачу
@app.route('/api/get-items', methods=['GET'])
def get_items():
    items = Items.query.all()
    return [present_item(item) for item in items]

@app.route('/api/get-promos', methods=['GET'])
def get_promos():
    promos = Promos.query.all()
    return [present_promo(promo) for promo in promos]

@app.route('/api/get-picture/<picture_url>', methods=['GET'])
def get_picture(picture_url):
    return send_file('static\\' + picture_url + '.png')

@app.route('/api/get-gif', methods=['GET'])
def get_gif():
    return send_file('static\\kk-gif.mp4')

@app.route('/api/delete-promo', methods=['DELETE'])
def delete_promo():
    promo_used = request.get_json()
    promo = Promos.query.filter_by(title=promo_used).first()
    if promo.quantity > 1:
        promo.quantity -= 1
        db.session.commit()
        return jsonify({"used_promo_title": promo_used})
    elif promo.quantity == 1:
        db.session.delete(promo)
        return jsonify({"deleted_promo": promo_used})

@app.route('/api/purchase', methods=['POST'])
def new_purchase():
    purchase = request.get_json()
    msg_to_customer = Message('Заказ успешно создан!', sender='notes@notesservice.ru', recipients=[purchase['email']])
    msg_to_seller = Message('Заказ успешно создан!', sender='notes@notesservice.ru', recipients=['defolt.pon.da@gmail.com'])
    msg_to_customer.body = 'Здравствуйте, ' + purchase['name'] + '! \nМы приняли ваш заказ на сумму ' + str(purchase['sum']) + '. \nВы заказали: \n'
    msg_to_seller.body = 'Данные заказчика: \nИмя: ' + purchase['name'] + '\nНомер телефона: ' + str(purchase['phone']) + '\nПочта: ' + purchase['email'] + '\n'
    if purchase['discount'] > 0:
        msg_to_seller.body += 'Использован промокод ' + str(purchase['promo'] + '\n')
    for item in purchase['cart']:
        msg_to_customer.body += item['title'] + '      ' + item['size'] + '      x' + str(item['quantity']) + '      ' + str(item['price']) + 'P \n'
        msg_to_seller.body += item['title'] + '      ' + item['size'] + '      x' + str(item['quantity']) + '      ' + str(item['price']) + 'P \n'
    msg_to_customer.body += 'Скидка по промокоду составила ' + str(purchase['discount']) + 'P'
    mail.send(msg_to_customer)
    mail.send(msg_to_seller)
    print('sent')
    return jsonify({'purchase': purchase}), 200


@app.route('/')
def index():
    return "Hello"


if __name__ == '__main__':
    app.run(debug=True, port=8080)
