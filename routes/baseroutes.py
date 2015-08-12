__author__ = 'karnikamit'
from flask import render_template, jsonify, request
import os
from routes import app
from werkzeug.utils import secure_filename
ALLOWED_EXTENSIONS = set(['xlsx', 'csv', 'xls', 'zip', 'rar', 'png', 'json'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1] in ALLOWED_EXTENSIONS


@app.route('/', methods=["GET"])
def init():
    return render_template('up.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if request.method == 'POST':
        my_file = request.files['file']
        filename = secure_filename(my_file.filename)
        if my_file and allowed_file(filename):
            path_to_file = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            my_file.save(path_to_file)
        return jsonify({"response": "success"})