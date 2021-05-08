from flask import Response, request
from database.models import Students
from flask_restful import Resource

class StudentAPI(Resource):
    def get(self):
        student = Students.objects().to_json()
        return Response(student, mimetype="application/json", status=200)
    
    def post(self):
        body = request.get_json()
        student = Students(**body, ).save()
        s_id =  student.s_id
        return {'Success' : body}, 200
    
class SingleStudent(Resource):
    def get(self, id):
        student = Students.objects.get(s_id= id).to_json()
        return Response(student, mimetype="application/json", status=200)
    
    def put(self, id):
        body = request.get_json()
        Students.objects.get(s_id=id).update(**body)
        return 'Student updated Successfull!!'

    def delete(self, id):
        student = Students.objects.get(s_id=id).delete()
        return "Student Deleted Success"
