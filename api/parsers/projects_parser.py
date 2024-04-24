from flask_restful import reqparse

parser_not_all_parameters = reqparse.RequestParser()
parser_not_all_parameters.add_argument("title")
parser_not_all_parameters.add_argument("about")
parser_not_all_parameters.add_argument("language_id", type=int)
parser_not_all_parameters.add_argument("user_id", type=int)
parser_not_all_parameters.add_argument("price", type=int)
parser_not_all_parameters.add_argument("is_visible", type=bool)
