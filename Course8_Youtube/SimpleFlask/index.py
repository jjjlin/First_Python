from flask import Flask, render_template
app = Flask(__name__)

@app.route('/hello')
def hello():
	return 'hello world'

@app.route('/')
def index():
	title = '這是首頁'
	return render_template('index.html' title=title)

	
if __name__ == '__main__':
		app.run(port=9000)

