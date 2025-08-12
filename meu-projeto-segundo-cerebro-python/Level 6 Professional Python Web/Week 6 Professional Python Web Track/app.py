# --------------------------------------------
# Flask Basic Setup - First Route Example
# --------------------------------------------

# Importing Flask from the flask package
from flask import Flask  

# Creating the Flask application instance
# __name__ tells Flask where to look for resources
app = Flask(__name__)  

# Defining a route for the home page ("/")
# The function below will run when someone accesses the home page
@app.route("/")  
def home():
    # This will be the response shown in the browser
    return "Hello, World!"  

# Running the Flask development server
# debug=True enables auto-reload and shows detailed error pages
if __name__ == "__main__":  
    app.run(debug=True)
