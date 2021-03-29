from flask import Flask, render_template
from dotenv import load_dotenv
import os
import requests


app = Flask(__name__)


env_file = '.env'
if os.environ.get("APP_ENV"):
    env_file = '.env.' + os.environ['APP_ENV']
load_dotenv(env_file)


@app.route('/')
def app_index():
    products_url = os.environ['API_URL'] + '/api/products'
    products = requests.get(products_url).json()
    return render_template('index.html', products=products)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)
