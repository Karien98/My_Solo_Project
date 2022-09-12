from flask_app.config.mysqlconnections import connectToMySQL
from flask import flash
from flask_app.models import user 

class Upload: 

    db = "solo_project"
    def __init__(self, data):
        self.id = data['id']
        self.photograph_title = data['photograph_title']
        self.photographer_username = data['photographer_username']
        self.photograph_description = data['photograph_description']
        self.location = data['location']
        self.photo_type = data['photo_type']
        self.subject = data['subject']
        self.shutter_speed = data['shutter_speed']
        self.aperture = data['aperture']
        self.iso = data['iso']
        self.focal_length = data['focal_length']
        self.lighting_condition = data['lighting_condition']
        self.time_of_day = data['time_of_day']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user = None


    @classmethod
    def save(cls, data):
        query = "INSERT INTO uploads (photograph_title, photographer_username, photograph_description, location, photo_type, subject, shutter_speed, aperture, iso, focal_length, lighting_condition, time_of_day, user_id) VALUES (%(photograph_title)s, %(photographer_username)s, %(photograph_description)s, %(location)s, %(photo_type)s, %(subject)s, %(shutter_speed)s, %(aperture)s, %(iso)s, %(focal_length)s, %(lighting_condition)s, %(time_of_day)s, %(user_id)s);"
        return connectToMySQL(cls.db).query_db(query, data)
    
    @classmethod
    def get_all_(cuploadsls):
        query = "SELECT * FROM uploads;"
        results = connectToMySQL(cls.db).query_db(query)
        uploads = []
        for row in results:
            print(row['photographer_username'])
            uploads.append(cls(row))
        return uploads
    
    @classmethod
    def get_by_id(cls, data):
        query = "SELECT * FROM uploads LEFT JOIN users on uploads.user_id = users.id WHERE uploads.id = %(id)s;"
        results = connectToMySQL(cls.db).query_db(query, data)
        return cls(results[0])
    
    @classmethod
    def update(cls, data):
        query = "UPDATE uploads SET photograph_title = %(photograph_title)s, photographer_username = %(photographer_username)s, photograph_description = %(photograph_description)s, location = %(location)s, photo_type = %(photo_type)s, subject = %(subject)s, shutter_speed = %(shutter_speed)s, aperture = %(aperture)s, iso = %(iso)s, focal_length = %(focal_length)s, lighting_condition = %(lighting_condition)s, time_of_day = %(time_of_day)s, updated_at = NOW() WHERE id = %(id)s; "
        return connectToMySQL(cls.db).query_db(query, data)

    @classmethod
    def get_user_report(cls):
        query = "SELECT * FROM uploads LEFT JOIN users ON uploads.user_id = users.id;"
        uploads = connectToMySQL(cls.db).query_db(query)
        results = []
        for upload in uploads:
            data = { 

                'id': upload['users.id'],
                'first_name': upload['first_name'],
                'last_name': upload['last_name'],
                'username' : upload['username'],
                'email': upload['email'],
                'password': upload['password'],
                'created_at': upload['users.created_at'],
                'updated_at': upload['users.updated_at']
            }
            s = cls(upload)
            s.user = user.User(data)
            results.append(s)
        return results

    @classmethod
    def destroy(cls, data):
        query = "DELETE FROM uploads WHERE id = %(id)s;"
        return connectToMySQL(cls.db).query_db(query, data)

    @staticmethod
    def validate_upload(upload):
        is_valid = True
        if upload['photograph_title'] == "":
            is_valid = False 
            flash("Please enter photograph title", "upload")
        if upload['photographer_username'] == "":
            is_valid = False 
            flash("Photographer username required", "upload")
        if upload['photograph_description'] == "":
            is_valid = False 
            flash("Describe the process of this photograph", "upload")
        if upload['location'] == "":
            is_valid = False 
            flash("Please enter the location where photograph was taken", "upload")
        if upload['photo_type'] == "":
            is_valid = False 
            flash("Photo type required", "upload")
        if upload['subject'] == "":
            is_valid = False 
            flash("Subject required", "upload")
        if upload['aperture'] == "":
            is_valid = False 
            flash("Aperture required", "upload")
        if upload['iso'] == "":
            is_valid = False 
            flash("ISO required", "upload")
        if upload['focal_lenght'] == "":
            is_valid = False 
            flash("Focal length required", "upload")
        if upload['lighting_condition'] == "":
            is_valid = False 
            flash("Lighting condition required", "upload")
        if upload['time_of_day'] == "":
            is_valid = False 
            flash("Time of day required", "upload")
        return is_valid