from flask import Flask
from flask_bootstrap import Bootstrap
# import grabURLs

app = Flask(__name__)
bootstrap = Bootstrap(app)


from app import routes