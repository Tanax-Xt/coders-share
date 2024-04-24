from flask_restful import reqparse

parser_all_parameters = reqparse.RequestParser()
parser_all_parameters.add_argument("name", required=True)
parser_all_parameters.add_argument("email", required=True)
parser_all_parameters.add_argument("password", required=True)

parser_not_all_parameters = reqparse.RequestParser()
parser_not_all_parameters.add_argument("name")
parser_not_all_parameters.add_argument("email")
