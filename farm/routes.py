from flask import render_template, request, Blueprint
from farm.models import Post

main = Blueprint('main', __name__)


@main.route("/")
@main.route("/home")
def home():
    # page = request.args.get('page', 1, type=int)
    # posts = Post.query.order_by(Post.time_stamp.desc()).paginate(page=page, per_page=5)
    return render_template('home.html', )  # posts=posts


@main.route("/about")
def about():
    return render_template('about.html', title='About')


@main.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Process the form data and send an email or save to database
        # ...
        return 'Thank you for your message!'
    else:
        return render_template('contact.html', title='Contact')


@main.route('/products')
def products():
    products = [
        {'name': 'Blueberries', 'description': 'Freshly picked blueberries', 'price': 2.99},
        {'name': 'Dates', 'description': 'Organic medjool dates', 'price': 5.99},
        {'name': 'Carrots', 'description': 'Locally grown organic carrots', 'price': 1.99},
    ]
    return render_template('products.html', products=products)


@main.route('/events')
def events():
    events = [
        {'title': 'Spring Picking Day', 'date': 'April 15, 2023',
            'description': 'Come pick your own blueberries and strawberries!', 'location': '123 Main St.'},
        {'title': 'Fall Harvest Festival', 'date': 'October 21, 2023',
            'description': 'Join us for a day of fun and food!', 'location': '456 Elm St.'},
    ]
    return render_template('events.html', events=events)