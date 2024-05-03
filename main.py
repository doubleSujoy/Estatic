from flask import Flask

# Create a Flask app
app = Flask(__name__)

# Define a route for the homepage
@app.route('/')
def home():
    return "Hello, this is the homepage!"

if __name__ == '__main__':
    # Run the app
    app.run(debug=True)
  
