from curses import flash
from unicodedata import category
from flask import render_template, request, redirect, url_for, abort
from ..models import Comment, User, Pitches
from flask_login import login_required, current_user
from . import main
from .forms import CommentForm, UpdateProfile, PitchForm
from .. import db


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
    form = PitchForm()
    
    vows = Pitches.query.filter_by(category = "vows").all()

    if form.validate_on_submit():
        pitch = Pitches()
        pitch.category = form.category.data
        pitch.text = form.text.data
        pitch.user_id = current_user._get_current_object().id

        db.session.add(pitch)
        db.session.commit()

        flash('Pitch successfully add', 'success')
    else:
        flash("Pitch wasn't added", 'error')

    return render_template('vows.html', title = title, vows = vows)

@main.route('/product')
def product():
    """
    View page function for product pitches
    """
    title = 'Product'
    form = PitchForm()
    
    products = Pitches.query.filter_by(category = "product").all()

    if form.validate_on_submit():
        pitch = Pitches()
        pitch.category = form.category.data
        pitch.text = form.text.data
        pitch.user_id = current_user._get_current_object().id

        db.session.add(pitch)
        db.session.commit()

        flash('Pitch successfully add', 'success')
    else:
        flash("Pitch wasn't added", 'error')

    return render_template('product.html', title = title, products = products)

@main.route('/jokes')
def jokes():
    """
    View page function for the vows
    """
    title = 'Jokes'
    form = PitchForm()

    jokes = Pitches.query.filter_by(category = "jokes").all()
    
    if form.validate_on_submit():
        pitch = Pitches()
        pitch.category = form.category.data
        pitch.text = form.text.data
        pitch.user_id = current_user._get_current_object().id

        db.session.add(pitch)
        db.session.commit()

        flash('Pitch successfully add', 'success')
    else:
        flash("Pitch wasn't added", 'error')

    return render_template('jokes.html', title = title, jokes = jokes)


@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template('profile/profile.html', user = user)

@main.route('/user/<uname>/update', methods = ["GET", "POST"])
@login_required
def update_profile(uname):
    user = User.query.filter_by(username = uname).first()
    if user is None:
        abort(404)

    form = UpdateProfile()

    if form.validate_on_submit():
        user.bio = form.bio.data

        db.session.add(user)
        db.session.commit()

        return redirect(url_for('.profile', uname = user.username))
    
    return render_template('profile/update.html', form = form)


@main.route('/pitch/comment/new/<int:id>', methods = ['GET', 'POST'])
@login_required
def new_comment(id):
    form = CommentForm()
    pitch = get_pitch(id)

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data

        new_comment = Comment()