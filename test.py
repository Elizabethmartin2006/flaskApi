from flask import *

# initialize your flask app
app=Flask(__name__)


# define the route
@app.route("/api/home")
def home():
    return jsonify({"message":"welcome to home api"})

# create a route for product
@app.route("/api/product")
def product ():
    return jsonify({"message":"welcome to product Api"})
# 
@app.route("/api/services")
def services():
    return jsonify({"message":"welcome to our services API"})

# creating a route to accept user input
@app.route("/api/calc",methods=["post"])
def calc():
    num1=request.form["num1"]
    num2=request.form["num2"]

    sum=int(num1)+int(num2)

    return jsonify({"answer":sum})

@app.route("/api/multiply",methods=["post"])
def multiply():
    num1=request.form["num1"]
    num2=request.form["num2"]

    times=int(num1)*int(num2)

    return jsonify({"answer":times})

app.run(debug=True)