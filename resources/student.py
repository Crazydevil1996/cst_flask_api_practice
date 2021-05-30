from flask import Response, request
from database.models import Students,User
from flask_restful import Resource
import datetime
from flask_jwt_extended import create_access_token
from flask_jwt_extended.view_decorators import jwt_required


class StudentAPI(Resource):

    @jwt_required
    def get(self):
        student = Students.objects().to_json()
        return Response(student, mimetype="application/json", status=200)
    
    @jwt_required
    def post(self):
        body = request.get_json()
        student = Students(**body).save()
        id =  student.s_id
        return {'id' : str(id)}, 200
    
class SingleStudent(Resource):

    @jwt_required
    def get(self, id):
        student = Students.objects.get(s_id= id).to_json()
        return Response(student, mimetype="application/json", status=200)
    
    @jwt_required
    def put(self, id):
        body = request.get_json()
        Students.objects.get(s_id=id).update(**body)
        return 'Student updated Successfull!!'

    @jwt_required
    def delete(self, id):
        student = Students.objects.get(s_id=id).delete()
        return Response("Student Deleted Success", mimetype="applicaiton/json", status=200)

class RegisterApi(Resource):

    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id
        return {'id': str(id)}, 200

class LoginApi(Resource):

    def post(self):
        body = request.get_json()
        user = User.objects.get(email = body.get('email'))
        authorised = user.check_password(body.get('password'))
        if not authorised:
            return {'error': 'Invalid Credentials'}, 401
        expiry = datetime.timedelta(days=1)
        access_token = create_access_token(identity= str(user.id), expires_delta= expiry)
        return {'token': access_token}, 200