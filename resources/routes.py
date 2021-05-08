from .student import StudentAPI, SingleStudent

def initialize_route(api):
    api.add_resource(StudentAPI,'/students')
    api.add_resource(SingleStudent,'/students/<id>')