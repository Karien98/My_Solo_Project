from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.post import Post

@app.route('/new/post')
def new_post():
    if 'user_id' not in session: 
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template('new_post.html', user = User.get_one(data))

@app.route('/new/post', methods=['POST'])
def create_sight():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Post.validate_post(request.form):
        return redirect('/new/post')
    
    data = { 
        "title": request.form['title'],
        "upload_image": request.form['upload_image'],
        "description": request.form['description'],
        "location": request.form['location'],
        "subject": request.form['subject'],
        "shutter_speed": request.form['shutter_speed'],
        "aperture": request.form['aperture'],
        "iso": request.form['iso'],
        "focal_length": request.form['focal_length'],
        "user_id": session['user_id']
    }

    Post.save(data)
    return redirect('/dashboard')

@app.route('/edit/post/<int:id>')
def edit(id):
    if 'user_id' not in session: 
        return redirect('/logout')
    data = { 
        "id" : id
    }
    user_data = { 
        "id" : session['user_id']
    }
    return render_template("edit_post.html", edit = Post.get_by_id(data), user = User.get_one(user_data))

@app.route('/post/<int:id>')
def show_post(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = { 
        "id" : id
    }
    user_data = { 
        "id" : session['user_id']
    }
    return render_template("show_post.html", post = Post.get_by_id(data), user = User.get_one(user_data), posts = Post.get_user_report())

@app.route('/update/post', methods=['POST'])
def update(): 
    if 'user_id' not in session: 
        return redirect('/logout')
    if not Post.validate_post(request.form):
        return redirect('/edit/post/')
    
    data = { 
        "title": request.form['title'],
        "upload_image": request.form['upload_image'],
        "description": request.form['description'],
        "location": request.form['location'],
        "subject": request.form['subject'],
        "shutter_speed": request.form['shutter_speed'],
        "aperture": request.form['aperture'],
        "iso": request.form['iso'],
        "focal_length": request.form['focal_length'],
        "id": request.form['id']
    }

    Post.update(data)
    return redirect('/dashboard')

@app.route('/destroy/post/<int:id>')
def destroy(id): 
    if 'user_id' not in session:
        return redirect('/logout')
    data = { 
        'id' : id
    }

    Post.destroy(data)
    return redirect('/dashboard')