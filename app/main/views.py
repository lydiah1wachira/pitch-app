from pickletools import read_unicodestringnl
from flask import render_template,request,redirect,url_for,abort,flash
from . import main
from flask_login import login_required, current_user
from ..models import User, Pitch,Comment,Upvote, Downvote
from .forms import UpdateProfile,PitchForm,CommentForm
from .. import db,photos

@main.route('/')
def index():
  '''
  View root page function that returns the index page and its data
  '''
  title = 'One-Minute Pitch'

  return render_template('index.html', title=title)

@main.route('/user/<uname>')
def profile(uname):
    user = User.query.filter_by(username = uname).first()

    if user is None:
        abort(404)

    return render_template("profile/profile.html", user = user)


@main.route('/user/<uname>/update',methods = ['GET','POST'])
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

        return redirect(url_for('.profile',uname=user.username))

    return render_template('profile/update.html',form =form)


@main.route('/user/<uname>/update/pic',methods= ['POST'])
@login_required
def update_pic(uname):
    user = User.query.filter_by(username = uname).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.profile',uname=uname))


@main.route('/general')
@login_required
def general():
    '''
    General page function that returns the page containing general pitches.
    '''
    pitches = Pitch.query.all()
    pitch = Pitch.query.filter_by(category='General').all()

    return render_template('general.html', pitch=pitch, title='General Pitches', pitches=pitches)

@main.route('/pickuplines')
@login_required
def pickuplines():

    '''
    View page function to display the pick up lines file and its data.
    '''
    pitches = Pitch.query.all()
    pitch = Pitch.query.filter_by(category = 'Pickuplines')

    return render_template('pickuplines.html', pitch=pitch,title='Pick Up Lines', pitches=pitches)



@main.route('/career')
@login_required
def career():
    '''
    View page function to display career pitches
    '''
    pitches = Pitch.query.all()
    pitch = Pitch.query.filter_by(category='Career').all()

    return render_template('career.html', pitch=pitch, title='Career Pitches', pitches=pitches)



@main.route('/business')
@login_required
def business():
    '''
    View page function to display business pitches
    '''
    pitches = Pitch.query.all()
    pitch = Pitch.query.filter_by(category='business').all()

    return render_template('business.html',title = 'Business Pitches', pitch= pitch, pitches=pitches )




@main.route('/pitch/new',methods=['GET', 'POST'])
@login_required
def pitch():
    '''
    View page function to display new pitch objects
    '''
    form = PitchForm()
    if form.validate_on_submit():
        pitch=Pitch(category=form.category.data, content=form.content.data, author=current_user)
        db.session.add(pitch)
        db.session.commit()
        flash('New Pitch created successfully!','success')
        return redirect(url_for('main.index'))
    return render_template("pitch.html", title='New Pitch', form=form)