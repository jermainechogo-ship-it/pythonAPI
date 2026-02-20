# import flask and its components
from flask import *

# create a flask application and give it a name
app = Flask(__name__)

# below we create the home route
# Routing : this is mapping different resources to different functions . We do this by the help of a decorator
@app.route("/api/home")
def home():
    return  jsonify({"message" : "Home Route Accessed"})


# Below is the products route
@app.route("/api/products")
def products():
    return jsonify({"message" : "welcome to the products route"})



# Below is   a route fo addition
@app.route("/api/calc", methods=["POST"])
def calculator():
    if request.method == "POST":
        number1 = request.form["number1"]
        number2 = request.form["number2"]
        sum = int(number1) + int(number2)

        return jsonify({"the answer is": sum})


# run the application
app.run(debug=True)
