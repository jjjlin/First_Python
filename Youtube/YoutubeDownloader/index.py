from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
app = Flask(__name__)
@app.route('/')
def index():
	filename = request.args.get('filename')
	return render_template('index.html', filename=filename)


@app.route('/submit', methods=['POST'])
def post_submit():
	yt = YouTube()
	url = request.form.get('url')
	yt.url = url
	video = yt.get('mp4', '720p')
	video.download('/Users/qaz456123789wsx/Desktop/music/')
	filename = yt.filename
	print(yt)
	print(yt.filename)
	return redirect(url_for('index', filename=filename))

	
if __name__ == '__main__':
	app.run(port=9000)


'''
from flask import Flask, render_template, request, redirect, url_for
from pytube import YouTube
app = Flask(__name__)
@app.route('/')
def index():
	filename = request.args.get('filename')
	return render_template('index.html', filename=filename)

@app.route('/submit', methods=['POST'])
def post_submit():
	yt = YouTube()
	url = request.form.get('url')
	yt.url = url
	video = yt.get('mp4', '360p')
	video.download('/Users/qaz456123789wsx/Desktop/music/')
	filename = yt.filename
	print(yt)
	print(yt.filename)
	return redirect(url_for('index', filename=filename))

if __name__ == '__main__':
	app.run(debug=True)

	'''