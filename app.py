import os
from flask import Flask, flash, request, redirect, url_for
from werkzeug.utils import secure_filename

app = Flask(__name__)

@app.route('/upload/<username>', methods=['GET', 'POST'])
def upload_file(username):
    UPLOAD_FOLDER = '{}'.format(username)
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
    if not os.path.exists(UPLOAD_FOLDER):
        os.mkdir(UPLOAD_FOLDER)
        
    if request.method == 'POST':
        f = request.files['file']
        f.save('{}/{}'.format(UPLOAD_FOLDER, secure_filename(f.filename)))
        if os.path.isfile('{}/{}'.format(UPLOAD_FOLDER, f.filename)):
            return {'response': 200}
        else:
            return {'response': 400}

if __name__ == '__main__':
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SECRET_KEY'] = os.urandom(64)
    app.debug = True
    app.run()
