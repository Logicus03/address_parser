from flask import (
    Blueprint, 
    Flask,
    request,
    jsonify,
    Response,
    abort
)

from postal.parser import parse_address
from postal.expand import expand_address
from werkzeug.exceptions import BadRequest, InternalServerError

parser_blueprint = Blueprint("address_parser", __name__, url_prefix="/api/parse")

def convert_json(address):
    return {k: v for (v, k) in address}

def address_parser(address):
    
    return convert_json(
        parse_address( 
            expand_address(address)[0]
            )
        )

@parser_blueprint.route("", methods=["POST"])
def address_parse():

    if request.method == 'POST':
        # Get data
        data = request.values

        if 'address' not in data:
            raise BadRequest('Missing address field')

        try:
            address = data["address"]
            return jsonify({
                "code": 200,
                "data": address_parser(address)
            })

        except Exception as e:
            raise InternalServerError()

    raise BadRequest('Not Get')
    # return jsonify({
    #     "error": "No GET"
    # })