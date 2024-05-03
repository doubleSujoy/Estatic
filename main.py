from flask import Flask
from module import bosohwf84kv as fun832
from module import giiyel7hosx as fun183
# Create a Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, this is the homepage!"

if __name__ == '__main__':
    # Run the app
    app.run(debug=True,host='0.0.0.0',port=3000)
  
