from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Hello World"

@app.route('/vish')
def vish():
    return "Vish - DevOps Engineer"

if __name__ == '__main__':
    # adding host with 0.0.0.0 so that we can hit from browser for ipv4 address to work
    app.run(host="0.0.0.0")