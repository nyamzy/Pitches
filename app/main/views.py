from flask import render_template
from flask_login import login_required
from . import main


@main.route('/')
def index():
    """
    Root page view function
    """
    title = 'Quick Pitches'

    return render_template('index.html', title = title)


@main.route('/vows')
def vows():
    """
    View page function for the vows
    """
    title = 'Vows'

    return render_template('vows.html', title = title, vows = vows)

@main.route('/product')
def product():
    """
    View page function for product pitches
    """
    title = 'Product'

    return render_template('product.html', title = title, product = product)

@main.route('/jokes')
def jokes():
    """
    View page function for the vows
    """
    title = 'Jokes'

    return render_template('jokes.html', title = title, jokes = jokes)

