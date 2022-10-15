from flask import Flask, render_template, request, send_file
from werkzeug.utils import secure_filename
import pandas as pd
import numpy as np
UPLOAD_FOLDER = ''

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def file_up():
    if request.method == 'POST':
        file = request.files['file']
        filename = secure_filename(file.filename)
        print(filename)
        df = pd.read_excel(file)
        df.to_csv('lottery.csv', encoding='utf-8', index=False)
        
        print(request.form['hindi'], request.form['bengali'])
        return send_file('lottery.csv',  as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True)