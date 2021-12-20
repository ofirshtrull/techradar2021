from flask import Flask
app = Flask(__name__)

@app.route('/')
def index():
    return "<h1>The Devops is strong with this one. (By Master Yoda)</h1><br><img src='https://media.makeameme.org/created/devops-5cb6df.jpg'>"

@app.route('/user/<name>')
def user(name):
	return '<h1>Hello, {0}!</h1>'.format(name)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9090)
    app.run(debug=True)
