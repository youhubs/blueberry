from flask import Flask, render_template, request, redirect, url_for, session
from alipay import AliPay
from wechatpy import WeChatPay
import os
import uuid

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

# AliPay configuration
ALIPAY_APP_ID = 'your_alipay_app_id_here'
ALIPAY_APP_PRIVATE_KEY_PATH = 'path_to_your_private_key_file'
ALIPAY_ALIPAY_PUBLIC_KEY_PATH = 'path_to_alipay_public_key_file'
ALIPAY_RETURN_URL = 'http://yourwebsite.com/return'
ALIPAY_NOTIFY_URL = 'http://yourwebsite.com/notify'

alipay = AliPay(
    appid=ALIPAY_APP_ID,
    app_private_key_path=ALIPAY_APP_PRIVATE_KEY_PATH,
    alipay_public_key_path=ALIPAY_ALIPAY_PUBLIC_KEY_PATH,
    sign_type='RSA2',
    debug=False
)

# WeChat Pay configuration
WECHAT_APP_ID = 'your_wechat_app_id_here'
WECHAT_MCH_ID = 'your_wechat_merchant_id_here'
WECHAT_API_KEY = 'your_wechat_api_key_here'

wechat_pay = WeChatPay(
    appid=WECHAT_APP_ID,
    mch_id=WECHAT_MCH_ID,
    api_key=WECHAT_API_KEY,
    mch_cert_path='path_to_your_wechat_pay_certificate_file',
    mch_key_path='path_to_your_wechat_pay_key_file',
    timeout=10,
    sandbox=False
)

products = [
    {
        'name': 'Product 1',
        'price': 10.99,
        'image': 'product1.jpg'
    },
    {
        'name': 'Product 2',
        'price': 19.99,
        'image': 'product2.jpg'
    },
    {
        'name': 'Product 3',
        'price': 8.99,
        'image': 'product3.jpg'
    }
]


@app.route('/')
def index():
    return render_template('index.html', products=products)


@app.route('/add-to-cart/<int:product_id>')
def add_to_cart(product_id):
    if 'cart' not in session:
        session['cart'] = {}
    if str(product_id) not in session['cart']:
        session['cart'][str(product_id)] = 0
    session['cart'][str(product_id)] += 1
    return redirect(url_for('index'))


@app.route('/cart')
def cart():
    cart_items = []
    total = 0
    for product_id, quantity in session.get('cart', {}).items():
        product = products[product_id]
        item_total = quantity * product['price']
        total += item_total
        cart_items.append({
            'product': product,
            'quantity': quantity,
            'item_total': item_total
        })
    return render_template('cart.html', cart_items=cart_items, total=total)


@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        if request.form.get('payment_method') == 'alipay':
            out_trade_no = str(uuid.uuid4())
            subject = 'Online Store Purchase'
            total_amount = request.form['total']
            order_string = alipay.api_alipay_trade_page_pay(
                out_trade_no=out_trade_no,
                total_amount=total_amount,
                subject=
