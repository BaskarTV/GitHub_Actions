from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask!'

@app.route('/home')
def home():
    return 'Hello world'
# GitAction WorkFlow is successfull working


@app.route('/test')
def test():
    return 'Test page'


# test local to server

#app.run(port=5000, debug=True)

#changed user now trial -5
