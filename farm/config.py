# 配置数据库
import os

# 配置博客蓝图
BLOG_PER_PAGE = 10

# 配置登录蓝图
LOGIN_DISABLED = False


class Config:
    SECRET_KEY = '011f0563a3bf8a5d63dccafa814979fa'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///data.db'
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get('MAIL_USER')
    MAIL_PASSWORD = os.environ.get('MAIL_PASS')
