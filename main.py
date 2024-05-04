from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello from Flask!'

@app.route('/home')
def home():
    return 'Home page'
# GitAction WorkFlow is successfull working

#app.run(port=5000, debug=True)

#changed user now trial -5

@app.rout('/test')
def test():
    return 'test page'