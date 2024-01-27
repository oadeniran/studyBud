from flask import Flask, request
from pymongo import MongoClient
from dotenv import load_dotenv
import requests
import json
import os

load_dotenv()
connection_str = os.getenv("Connection_string")

def get_database():
 
   # Provide the mongodb atlas url to connect python to mongodb using pymongo
   CONNECTION_STRING = connection_str
 
   # Create a connection using MongoClient. You can import MongoClient or use pymongo.MongoClient
   client = MongoClient(CONNECTION_STRING)
 
   # Create the database for our example (we will use the same database throughout the tutorial
   return client['Userinfo']['users-details']
  

app = Flask(__name__)

@app.route("/")
def index():
    return "studybud User Api"

@app.route("/signup", methods = ["POST"])
def signup():
    signUp_det = request.form.to_dict()

    try:
        client.insert_one(signUp_det)
    except:
        return json.dumps({
                    "message" : "Error with signup",
                    "status_code" : "400"})
    
    return json.dumps({
    "message" : "Sign Up successful",
    "status_code" : "200"})
    


@app.route("/login", methods = ["Post"])
def login():
    login_det = request.form.to_dict()

    try:
        details = client.find_one({"username" : login_det["username"]})
    except:
        return json.dumps({
                    "message" : "User not found",
                    "status_code" : 404
                    })
    
    if details:
        print(str(details["_id"]))
        if details["password"] == login_det["password"]:
            return json.dumps({
                    "message" : "Sign In successful",
                    "status_code" : 200,
                    "uid" : str(details["_id"])})
        else:
            return json.dumps({
            "message" : "Wrong Password",
            "status_code" : 400})

@app.route("/update-conversation-history",methods = ["Post"])
def update_conv_hist():
    pass





if __name__ == "__main__":
    client = get_database()
    app.run(host = "0.0.0.0", debug=True, port=9000)