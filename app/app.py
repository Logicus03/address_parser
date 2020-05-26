from flask import (
    Flask,
    render_template,
    request,
    jsonify
)

from address_parser import address_parser, parse_json


# Create the application instance
app = Flask(__name__)

@app.errorhandler(400)
def bad_request(e):
    # note that we set the 404 status explicitly
    return jsonify({
        "error": "Bad Request: " + str(e)
    }), 400

@app.errorhandler(404)
def page_not_found(e):
    # note that we set the 404 status explicitly
    return jsonify({
        "error": "Not found"
    }), 404

@app.errorhandler(500)
def internal_server_error(e):
    # note that we set the 404 status explicitly
    return jsonify({
        "error": "Internal Server Error"
    }), 500


# Create a URL route in our application for "/"
@app.route('/parse', methods=['POST'] ) 
def address_parse():
    if request.method == 'POST':
        # data = request.form
        data = request.values

        if 'address' not in data:
            return jsonify({
                "error": "Missing address"
            }), 400

        try:

            address = data["address"]
            return jsonify(
                address_parser(address)
            )

        except Exception as e:
            return jsonify({
                "error": e
            }), 400

    return jsonify({
        "error": "No GET"
    })

@app.route('/', methods=['GET'])
def index():
    return "Here!"

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)