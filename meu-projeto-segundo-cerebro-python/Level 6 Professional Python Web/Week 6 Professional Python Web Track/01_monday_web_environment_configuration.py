# Web Environment Configuration

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




# --------------------------------------------
#  How to run this code:

# 1. Install Flask (only once)
##pip install flask      # if you haven't installed it yet (remove ## to run the command)

# 2. Run the file
##python app.py          # replace app.py with your filename (remove ## to run the command)

# 3. Open your browser and go to:
##http://127.0.0.1:5000/ # you should see "Hello, World!" displayed (remove ## to run the command)



# Output in browser:

# Hello, World!




# Console output when running the server:
# * Serving Flask app 'app'
# * Debug mode: on
# * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)






# --------------------------------------------
# SUMMARY:
# - Imported Flask and created an app instance
# - Defined a route ("/") and a function to return "Hello, World!"
# - Ran the Flask development server in debug mode

# TIPS & BEST PRACTICES:
# 1. Always use `debug=True` only in development, never in production.
# 2. Use clear function names for routes (e.g., home, about, contact).
# 3. Keep routes organized in separate files for bigger projects.
# 4. Use environment variables for configuration (e.g., port, debug mode).
# --------------------------------------------
