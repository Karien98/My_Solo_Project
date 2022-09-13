from flask_app.config.mysqlconnections import connectToMySQL
from flask import flash
from flask_app.models import user 

class Post: 
    db = "photographer's_kaleidoscope"
    def __init__(self, data):
        self.id = data['id']
        self.title = data['title']
        self.upload_image = data['upload_image']
        self.description = data['description']
        self.location = data['location']
        self.subject = data['subject']
        self.shutter_speed = data['shutter_speed']
        self.aperture = data['aperture']
        self.iso = data['iso']
        self.focal_length = data['focal_length']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None

    @classmethod
    def save(cls, data):
        query = "INSERT INTO posts (title, upload_image, description, location, subject, shutter_speed, aperture, iso, focal_length, user_id) VALUES (%(title)s, %(upload_image)s, %(description)s, %(location)s, %(subject)s, %(shutter_speed)s, %(aperture)s, %(iso)s, %(focal_length)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_posts(cls):
        query = "SELECT * FROM posts;"
        results = connectToMySQL(cls.db).query_db(query)
        posts = []
        for row in results:
            print(row['title'])
            posts.append(cls(row))
        return posts
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM posts LEFT JOIN users on posts.user_id = users.id WHERE posts.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE posts SET title = %(title)s, upload_image = %(upload_image)s, description = %(description)s, location = %(location)s, subject = %(subject)s, shutter_speed = %(shutter_speed)s, aperture = %(aperture)s, iso = %(iso)s, focal_length = %(focal_length)s, updated_at = NOW() WHERE id = %(id)s; "
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_user_report(cls):
        query = "SELECT * FROM posts LEFT JOIN users ON posts.user_id = users.id;"
        posts = connectToMySQL(cls.db).query_db(query)
        results = []
        for post in posts:
            data = { 

                'id': post['users.id'],
                'first_name': post['first_name'],
                'last_name': post['last_name'],
                'email': post['email'],
                'password': post['password'],
                'created_at': post['users.created_at'],
                'updated_at': post['users.updated_at']
            }
            s = cls(post)
            s.user = user.User(data)
            results.append(s)
        return results

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM posts WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_post(post):
        is_valid = True
        if post['title'] == "":
            is_valid = False 
            flash("Please add a title", "post")
        if post['upload_image'] == "":
            is_valid = False 
            flash("Please upload an image", "post")
        if post['description'] == "":
            is_valid = False 
            flash("Please enter description", "post")
        if post['location'] == "" :
            is_valid = False 
            flash("Enter location where image was taken", "post")
        if post['subject'] == "" :
            is_valid = False 
            flash("Enter what the subject is", "post")
        if post['shutter_speed'] == "" :
            is_valid = False 
            flash("Enter shutter speed", "post")
        if post['aperture'] == "" :
            is_valid = False 
            flash("Enter aperture", "post")
        if post['iso'] == "" :
            is_valid = False 
            flash("Enter ISO", "post")
        if post['focal_length'] == "" :
            is_valid = False 
            flash("Enter focal length", "post")
        return is_valid