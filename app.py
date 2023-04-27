from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    email = request.form['email']
    message = request.form['message']

    with open('data.txt', 'a') as f:
        f.write(f'{name}, {email}, {message}\n')

    return 'Data written to file successfully!'
@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    filename = file.filename
    file.save(os.path.join('files', filename))
    return 'File uploaded successfully!'

if __name__ == '__main__':
    app.run(host='0.0.0.0')

