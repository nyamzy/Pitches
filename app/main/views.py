from unicodedata import category
from flask import render_template, request, redirect, url_for, abort, flash
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


@main.route('/vows', methods = ["GET", "POST"])
def vows():
    """
    View page function for the vows
    """
    title = 'Vow Pitches'
    form = PitchForm()
    
    vows = Pitches.query.filter_by(category = "vows").all()

    if form.validate_on_submit():
        
        category = form.category.data
        text = form.text.data
        new_pitch = Pitches(category = category, text = text)
        new_pitch.save_pitch()

        flash('Pitch successfully add')
        return render_template('vows.html', title = title, vows = vows, form = form)
        
    else:
        flash("Pitch wasn't added")
        return render_template('vows.html', title = title, vows = vows, form = form)
        

@main.route('/product', methods = ["GET", "POST"])
def product():
    """
    View page function for product pitches
    """
    title = 'Product Pitches'
    form = PitchForm()
    
    products = Pitches.query.filter_by(category = "products").all()

    if form.validate_on_submit():
       
        category = form.category.data
        text = form.text.data
        
        new_pitch = Pitches(category = category, text = text)
        new_pitch.save_pitch()


        flash('Pitch successfully add')
        return render_template('product.html', title = title, products = products, form = form)
    else:
        flash("Pitch wasn't added")
        return render_template('product.html', title = title, products = products, form = form)

@main.route('/jokes', methods = ["GET", "POST"])
def jokes():
    """
    View page function for the vows
    """
    title = 'Joke Pitches'
    form = PitchForm()

    jokes = Pitches.query.filter_by(category = "jokes").all()
    
    if form.validate_on_submit():
       
        category = form.category.data
        text = form.text.data
        new_pitch = Pitches(category = category, text = text)
        new_pitch.save_pitch()


        flash('Pitch successfully add')
        return render_template('jokes.html', title = title, jokes = jokes, form = form)
    else:
        flash("Pitch wasn't added")
        return render_template('jokes.html', title = title, jokes = jokes, form = form)


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
def new_comment(pitch_id):
    form = CommentForm()
    pitch = Pitches.query.get(pitch_id)
    all_comments = Comment.query.filter(pitch_id = pitch_id).all()

    if form.validate_on_submit():
        title = form.title.data
        comment = form.comment.data
        pitch_id = pitch_id
        user_id = current_user._get_current_object().id

        new_comment = Comment(title = title, comment = comment, pitch_id = pitch_id, user_id = user_id)

        new_comment.save_comment()
        return redirect(url_for('.new_comment', pitch_id = pitch_id))
    return render_template('comment.html', pitch = pitch, all_comments = all_comments, comment_form = form)