from .student import StudentAPI, SingleStudent, RegisterApi, LoginApi

def initialize_route(api):
    api.add_resource(StudentAPI,'/students')
    api.add_resource(SingleStudent,'/students/<id>')
    api.add_resource(RegisterApi,'/auth/register')
    api.add_resource(LoginApi,'/auth/login')
