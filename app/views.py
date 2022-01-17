from flask import render_template
from app import app

@app.route('/')
def index():
    """
    Root page view function
    """
    title = 'Quick Pitches'

    return render_template('index.html', title = title)


@app.route('/vows')
def vows():
    """
    View page function for the vows
    """
    title = 'Vows'

    return render_template('vows.html', title = title)

@app.route('/product')
def product():
    """
    View page function for product pitches
    """
    title = 'Product'

    return render_template('product.html', title = title)

@app.route('/jokes')
def jokes():
    """
    View page function for the vows
    """
    title = 'Jokes'

    return render_template('jokes.html', title = title)