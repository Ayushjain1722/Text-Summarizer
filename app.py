from flask import Flask, render_template, request, redirect, url_for, send_file
from summarizer import summarize

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/', methods=['GET'])
def content():
    if request.method == 'GET':
        return redirect(url_for('sendText'))
    return render_template('sendText.html')

@app.route('/sendText', methods=['GET', 'POST'])
def sendText():
    if request.method == 'POST':
        if 'gotoSend' in request.form:
            return render_template('sendText.html')
        else:
            text = request.form.get('w3review')
            summary = summarize(text)
            with open('output/result.txt', 'w') as fp:
                fp.write(summary)
            return send_file('./output/result.txt', attachment_filename='summary.txt', as_attachment=True)

    return render_template('sendText.html')

if __name__ == "__main__":
    app.run()