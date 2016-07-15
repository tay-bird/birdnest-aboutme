from application import app

from flask import redirect

@app.route("/")
def home():
    return redirect('static/index.html')
