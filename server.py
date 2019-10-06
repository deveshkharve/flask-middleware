from flask import Flask, request
from middleware import middleware

app = Flask('DemoApp')

# calling our middleware
app.wsgi_app = middleware(app.wsgi_app)

@app.route('/', methods=['GET', 'POST'])
def hello():
    user = request.environ['user']
    return "Hi %s"%user['name']

if __name__ == "__main__":
    app.run('127.0.0.1', '5000', debug=True)
