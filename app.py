# step 1
from flask import *
import pymysql
 
#  initialize flask

app=Flask(__name__)
@app.route("/api/signup",methods=["post"])
def signup():
    # request user input
    username=request.form["username"]
    email=request.form["email"]
    password=request.form["password"]
    phone=request.form["phone"]

    # create conection to datadase
    connection=pymysql.connect(host="localhost",user="root",password="",database="tembo_sokogarden_lizzy")

    # create a cursor
    cursor=connection.cursor()

    # create sql statement to insert the data
    sql="insert into users(username,email,password,phone)values(%s,%s,%s,%s)"

    # prepare data
    data=(username,email,password,phone)

    # execute / run
    cursor.execute(sql,data)
    # commit/save

    connection.commit()

    # respond
    return jsonify({"message":"Thank you for joining"})


# signin api
# signin route
@app.route("/api/signin",methods=["post"])
def signin():
    # request user input
    email=request.form["email"]
    password=request.form["password"]

    #    create a connection
    connection=pymysql.connect(host="localhost",user="root",password="",database="tembo_sokogarden_lizzy")

    # create a cursor

    cursor=connection.cursor(pymysql.cursors.DictCursor)

    # sql statment to cheack if user exist
    sql="select * from users where email=%s and password=%s"

    # prepare data
    data=(email,password)

    cursor.execute(sql,data)


    # response
    if cursor.rowcount==0:
        return jsonify({"message":"login failed"})
    else:
        user=cursor.fetchone()
        user.pop("password",None)
        return jsonify({"message":"login success","user":user})
























































app.run(debug=True)


