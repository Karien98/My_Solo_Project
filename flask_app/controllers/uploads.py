from flask import render_template, redirect, request, session, flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.upload import Upload

@app.route('/new/upload')
def new_upload():
    if 'user_id' not in session: 
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template('new_upload.html', user = User.get_one(data))

@app.route('/create/upload', methods=['POST'])
def create_upload():
    if 'user_id' not in session:
        return redirect('/logout')
    if not Upload.validate_upload(request.form):
        return redirect('/new/Upload')
    
    data = { 
        "photograhp_title": request.form['photograph_title'],
        "photographer_username": request.form['photographer_username'],
        "photograph_descripton": request.form['photograph_description'],
        "location": request.form['location'],
        "photo_type": request.form['photo_type'],
        "subject": request.form['subject'],
        "shutter_speed": int(request.form['shutter_speed']),
        "aperture": int(request.form['aperture']),
        "iso": int(request.form['iso']),
        "focal_lenght": int(request.form['focal_length']),
        "lighting_condition": request.form['lighting_condition'],
        "time_of_day": request.form['time_of_day'],
        "user_id": session['user_id']
    }

    Upload.save(data)
    return redirect('/dashboard')

@app.route('/edit/upload/<int:id>')
def edit(id):
    if 'user_id' not in session: 
        return redirect('/logout')
    data = { 
        "id" : id
    }
    user_data = { 
        "id" : session['user_id']
    }
    return render_template("edit_upload.html", edit = Upload.get_by_id(data), user = User.get_one(user_data))

@app.route('/upload/<int:id>')
def show_upload(id):
    if 'user_id' not in session:
        return redirect('/logout')
    data = { 
        "id" : id
    }
    user_data = { 
        "id" : session['user_id']
    }
    return render_template("show_upload.html", upload = Upload.get_by_id(data), user = User.get_one(user_data), uploads = Upload.get_user_report())

@app.route('/update/upload', methods=['POST'])
def update(): 
    if 'user_id' not in session: 
        return redirect('/logout')
    if not Upload.validate_upload(request.form):
        return redirect('/edit/upload/')
    
    data = { 
        "photograhp_title": request.form['photograph_title'],
        "photographer_username": request.form['photographer_username'],
        "photograph_descripton": request.form['photograph_description'],
        "location": request.form['location'],
        "photo_type": request.form['photo_type'],
        "subject": request.form['subject'],
        "shutter_speed": int(request.form['shutter_speed']),
        "aperture": int(request.form['aperture']),
        "iso": int(request.form['iso']),
        "focal_lenght": int(request.form['focal_length']),
        "lighting_condition": request.form['lighting_condition'],
        "time_of_day": request.form['time_of_day'],
        "id": session['id']
    }

    Upload.update(data)
    return redirect('/dashboard')

@app.route('/destroy/upload/<int:id>')
def destroy(id): 
    if 'user_id' not in session:
        return redirect('/logout')
    data = { 
        'id' : id
    }

    Upload.destroy(data)
    return redirect('/dashboard')