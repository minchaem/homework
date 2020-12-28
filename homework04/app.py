from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.dbhomework


## HTML 화면 보여주기
@app.route('/')
def homework():
    return render_template('index.html')


# 주문하기(POST) API
@app.route('/order', methods=['POST'])
def save_order():
    # 1. 클라이언트가 준 name, count, address, number 가져오기.
    name_receive = request.form['name_give']
    count_receive = request.form['count_give']
    address_receive = request.form['address_give']
    number_receive = request.form['number_give']

    # 2. DB에 정보 삽입하기
    doc = {
        'name': name_receive,
        'count': count_receive,
        'address': address_receive,
        'number': number_receive
    }
    db.orders.insert_one(doc)

    # 3. 성공 여부 & 성공 메시지 반환하기
    return jsonify({'result': 'success', 'msg':'주문이 완료되었습니다🐶💚'})


# 주문 목록보기(Read) API
@app.route('/order', methods=['GET'])
def view_orders():
    # 여길 채워나가세요!
    orders = list(db.orders.find({}, {'_id': False}))
    return jsonify({'result': 'success', 'orders': orders})


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
