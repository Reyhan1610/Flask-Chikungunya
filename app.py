from flask import Flask, flash, redirect, render_template, request, session, abort, send_from_directory
import model_loader as dt
import json
import os

app = Flask(__name__)
app.config['DEBUG'] = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    result = dt.predict(request.json)
    return json.dumps(result)

@app.route('/favicon.ico') 
def favicon(): 
    return send_from_directory(os.path.join(app.root_path, 'static'), 'favicon.ico', mimetype='image/vnd.microsoft.icon')

@app.after_request
def add_header(r):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    r.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    r.headers["Pragma"] = "no-cache"
    r.headers["Expires"] = "0"
    return r

if __name__ == "__main__":
    app.run(debug=True)

