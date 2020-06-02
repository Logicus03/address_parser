from flask import ( 
    Flask,
    render_template,
    request,
    jsonify,
    json
)

from werkzeug.exceptions import HTTPException
# from error_blueprint import error_blueprint

from address_parser import parser_blueprint

def create_app():    
    # Create the application instance
    app = Flask(__name__) 
    # app.config['APPLICATION_ROOT'] = '/api/v1'

    @app.errorhandler(HTTPException)
    def handle_exception(e):
        """Return JSON instead of HTML for HTTP errors."""
        # start with the correct headers and status code from the error
        response = e.get_response()
        # replace the body with JSON
        response.data = json.dumps({
            "code": e.code,
            "name": e.name,
            "description": e.description,
        })
        response.content_type = "application/json"
        return response
        
    # /api/v1/parser
    app.register_blueprint(parser_blueprint, url_prefix="/api/v1")

    @app.route('/', methods=['GET'])
    def index():
        return "Here, alive!"

    return app

# If we're running in stand alone mode, run the application
if __name__ == '__main__':
    app = create_app()
    app.run(host='0.0.0.0', port=5000, debug=True)