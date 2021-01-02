import os


class Config:
	SECRET_KEY = os.environ.get('S_K')
	SQLALCHEMY_DATABASE_URI = os.environ.get('S_DB')
	MAIL_SERVER = 'smtp.googlemail.com'
	MAIL_PORT = 587
	MAIL_USE_TLS = True
	MAIL_USERNAME = os.environ.get('DB_USER1')
	MAIL_PASSWORD = os.environ.get('DB_PASS1')