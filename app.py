"""
This is the entry point to the application.
"""
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from farm import create_app, db
from farm.models import User, Post

app = create_app()
admin = Admin(app, name='Farm Admin', template_mode='bootstrap4')

# Register the models with Flask-Admin
admin.add_view(ModelView(User, db.session))
admin.add_view(ModelView(Post, db.session))


if __name__ == "__main__":
    app.run(debug=True, port=5001)
