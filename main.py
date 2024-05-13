from flask import Flask, request, jsonify
from flask_cors import CORS
from module import bosohwf84kv as fun832
from module import giiyel7hosx as fun183
from module import imgGenv1 as image_gen_v1
from module import imgGenDetai as image_gen_v2
from module import imageGenPix as image_gen_px
from module import llama3_chat
# Create a Flask app
app = Flask(__name__)
CORS(app, resources={r"/ping": {"origins": r"*"}})
CORS(app, resources={r"/tool-sphere/api/code-gen": {"origins": r"https://tool-sphere.github.io"}})
CORS(app, resources={r"/api*": {"origins": r"https?://([^.]+\.)?rapidapi\.com"}})
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

@app.route("/test2")
def jdkvkrk():
    querye = request.args.get('q')
    return fun832(querye)

@app.route("/test3")
def jdkvkhkrk():
    querye = request.args.get('q')
    return image_gen_v1(querye)


@app.route("/test4")
def jdkvkhhdkejrk():
    querye = request.args.get('q')
    return image_gen_v2(querye)


@app.route("/test5")
def jdkhrvkhkruek():
    querye = request.args.get('q')
    return image_gen_px(querye)
    
    
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
                return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
         
            data = request.json  # Assuming JSON data is sent in the request body
        except Exception as e:
            return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
        
        q = data.get('query')  # Assuming 'port_number' is the key in the JSON data
        sysQ = data.get("sysMsg") or "You are a friendly Chatbot."
        
        if q is None:
            return jsonify({"serverError": False, "clientError": True, "msg": "query is not provided in request body!"})
        else:
            result = fun183(q, sysQ)
            return jsonify({"serverError": False, "clientError": False, "msg": result})
    except Exception as e:
        app.logger.error(e)
        return jsonify({"serverError": True, "clientError": "Maybe", "msg": "Somthing Went Wrong Please Contact with sujoy via email sujoyk211@gmail.com"})


@app.route("/api/post/chat/llama3", methods=['POST'])
def chatLlama3():
    try:
        if not request.is_json:
            return jsonify({"serverError": False, "clientError": True, "msg": "use application/json in request header to complete the request"})

        try:
            if not request.json:
                return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
         
            data = request.json  # Assuming JSON data is sent in the request body
        except Exception as e:
            return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
        
        q = data.get('prompt')  # Assuming 'port_number' is the key in the JSON data
        sysQ = data.get("system_prompt") or "You are a friendly Chatbot."
        
        if q is None:
            return jsonify({"serverError": False, "clientError": True, "msg": "query is not provided in request body!"})
        else:
            result = llama3_chat(q, sysQ)
            return jsonify({"serverError": False, "clientError": False, "msg": result})
    except Exception as e:
        app.logger.error(e)
        return jsonify({"serverError": True, "clientError": "Maybe", "msg": "Somthing Went Wrong Please Contact with sujoy via email sujoyk211@gmail.com"})




@app.route("/tool-sphere/api/code-gen", methods=['POST'])
def idoen():
    try:
        if not request.is_json:
            return jsonify({"serverError": False, "clientError": True, "msg": "use application/json in request header to complete the request"})

        try:
            if not request.json:
                return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
         
            data = request.json  # Assuming JSON data is sent in the request body
        except Exception as e:
            return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
        
        q = data.get('query')  # Assuming 'port_number' is the key in the JSON data
        if q is None:
            return jsonify({"serverError": False, "clientError": True, "msg": "query is not provided in request body!"})
        else:
            result = fun832(q)
            return jsonify({"serverError": False, "clientError": False, "msg": result})
    except Exception as e:
        app.logger.error(e)
        return jsonify({"serverError": True, "clientError": "Maybe", "msg": "Somthing Went Wrong Please Contact with website owner via contact us page"})


@app.route("/api/post/img/ping")
def sendImagePing():
    return "Success"


@app.route("/api/post/img/image_gen_v1", methods=['POST'])
def jdkkdy():
    try:
        if not request.is_json:
            return jsonify({"serverError": False, "clientError": True, "msg": "use application/json in request header to complete the request"})

        try:
            if not request.json:
                return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
         
            data = request.json  # Assuming JSON data is sent in the request body
        except Exception as e:
            return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
        
        q = data.get('query')  # Assuming 'port_number' is the key in the JSON data
        
        if q is None:
            return jsonify({"serverError": False, "clientError": True, "msg": "query is not provided in request body!"})
        else:
            result = image_gen_v1(q)
            return jsonify({"serverError": False, "clientError": False, "imageData": result, "type": "base64"})
    except Exception as e:
        app.logger.error(e)
        return jsonify({"serverError": True, "clientError": "Maybe", "msg": "Somthing Went Wrong Please Contact with sujoy via email sujoyk211@gmail.com"})


@app.route("/api/post/img/image_gen_v2", methods=['POST'])
def jdzkdy():
    try:
        if not request.is_json:
            return jsonify({"serverError": False, "clientError": True, "msg": "use application/json in request header to complete the request"})

        try:
            if not request.json:
                return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
         
            data = request.json  # Assuming JSON data is sent in the request body
        except Exception as e:
            return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
        
        q = data.get('query')  # Assuming 'port_number' is the key in the JSON data
        
        if q is None:
            return jsonify({"serverError": False, "clientError": True, "msg": "query is not provided in request body!"})
        else:
            result = image_gen_v2(q)
            return jsonify({"serverError": False, "clientError": False, "imageData": result, "type": "base64"})
    except Exception as e:
        app.logger.error(e)
        return jsonify({"serverError": True, "clientError": "Maybe", "msg": "Somthing Went Wrong Please Contact with sujoy via email sujoyk211@gmail.com"})



@app.route("/api/post/img/image_gen_pixle_art", methods=['POST'])
def jdmbkdy():
    try:
        if not request.is_json:
            return jsonify({"serverError": False, "clientError": True, "msg": "use application/json in request header to complete the request"})

        try:
            if not request.json:
                return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
         
            data = request.json  # Assuming JSON data is sent in the request body
        except Exception as e:
            return jsonify({"serverError": False, "clientError": True, "msg": "A valid json body is not provided!"})
        
        q = data.get('query')  # Assuming 'port_number' is the key in the JSON data
        
        if q is None:
            return jsonify({"serverError": False, "clientError": True, "msg": "query is not provided in request body!"})
        else:
            result = image_gen_px(q)
            return jsonify({"serverError": False, "clientError": False, "imageData": result, "type": "base64"})
    except Exception as e:
        app.logger.error(e)
        return jsonify({"serverError": True, "clientError": "Maybe", "msg": "Somthing Went Wrong Please Contact with sujoy via email sujoyk211@gmail.com"})
    
    


if __name__ == '__main__':
    # Run the app
    app.run(debug=True,host='0.0.0.0',port=3000)
  
