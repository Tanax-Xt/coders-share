from flask_restful import reqparse

parser_all_parameters = reqparse.RequestParser()
parser_all_parameters.add_argument("language_title", required=True)
parser_all_parameters.add_argument("language_sign", required=True)

parser_not_all_parameters = reqparse.RequestParser()
parser_not_all_parameters.add_argument("language_title")
parser_not_all_parameters.add_argument("language_sign")
