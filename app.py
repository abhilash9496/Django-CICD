from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'hey Iam ABHILASH CA'

@app.route('/health')
def health():
    return 'Server is up and running'
