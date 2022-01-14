from flask import render_template
from app import app

@app.route('/')
def index():
    """
    Root page view function
    """
    return render_template('index.html')