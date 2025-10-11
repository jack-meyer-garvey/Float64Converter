from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return '<h1>Welcome to My Site</h1><p>This is the homepage.</p>'



if __name__ == '__main__':
    app.run()
