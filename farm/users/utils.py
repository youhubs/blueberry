import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flask_mail import Mail, Message

mail = Mail()


def save_picture(picture_file):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(picture_file.filename)
    picture_name = random_hex + f_ext
    picture_path = os.path.join(
        current_app.root_path, 'static/profile_pics', picture_name)

    output_size = 125, 125
    img = Image.open(picture_file)
    img.thumbnail(output_size)
    img.save(picture_path)
    return picture_name


def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request',
                sender='w3clinics@gmail.com', recipients=[user.email])
    msg.body = f'''To reset your password, visit the following link:
{url_for('users.reset_password', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)
