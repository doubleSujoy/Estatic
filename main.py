from flask import Flask, request, jsonify
from flask_cors import CORS
from module import bosohwf84kv as fun832
from module import giiyel7hosx as fun183
# Create a Flask app
app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": r"https?://([^.]+\.)?rapidapi\.com"}})
# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, this is the homepage!"

@app.route("/ping")
def pingmeio():
    return "True"

@app.route("/test")
def jdkrk():
    query = request.args.get('q')
    return fun183(query)
@app.route("/api/post/chat/ping")
def sendPing():
    return "Success"


@app.route("/api/post/chat/infinite-gpt", methods=['POST'])
def jdk():
    try:
        if not request.is_json:
            return jsonify({"serverError": False, "clientError": True, "msg": "use application/json in request header to complete the request"})

        try:
            if not request.json:
                return return jsonify({"serverError": False, "clientError": True, "msg": "A valid json request body is not provided!"})
         
            data = request.json  # Assuming JSON data is sent in the request body
        except Exception as e:
            return jsonify({"serverError": False, "clientError": True, "msg": "A valid json request body is not provided!"})
        
        q = data.get('query')  # Assuming 'port_number' is the key in the JSON data
        if q is None:
            return jsonify({"serverError": False, "clientError": True, "msg": "query is not provided in request body!"})
        else:
            result = fun183(q)
            return jsonify({"serverError": False, "clientError": False, "msg": result})
    except Exception as e:
        app.logger.error(e)
        return jsonify({"serverError": True, "clientError": "Maybe", "msg": "Somthing Went Wrong Please Contact with sujoy via email sujoyk211@gmail.com"})



if __name__ == '__main__':
    # Run the app
    app.run(debug=True,host='0.0.0.0',port=3000)
  
