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
   return client['Userinfo']
  

app = Flask(__name__)

@app.route("/")
def index():
    return "studybud User Api"

@app.route("/signup", methods = ["POST"])
def signup():
    signUp_det = request.form.to_dict()
    try:
        details = userinfo_d.find_one({"username" : signUp_det["username"]})
    except:
        return json.dumps({
                    "message" : "Error in signup, please try again",
                    "status_code" : 404
                    })
    if details:
        return json.dumps({
                    "message" : "Username is taken, please use another",
                    "status_code" : 400})
    try:
        userinfo_d.insert_one(signUp_det)
    except:
        return json.dumps({
                    "message" : "Error with signup",
                    "status_code" : 400})
    return json.dumps({
    "message" : "Sign Up successful",
    "status_code" : 200})
    


@app.route("/login", methods = ["Post"])
def login():
    login_det = request.form.to_dict()

    try:
        details = userinfo_d.find_one({"username" : login_det["username"]})
    except:
        return json.dumps({
                    "message" : "Error with DB",
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
    else:
        return json.dumps({
                    "message" : "User not found",
                    "status_code" : 404
                    })

@app.route("/update-conversation-history",methods = ["Post"])
def update_conv_hist():
    pass

@app.route("/get_conversation_history",methods = ["Post"])
def get_conversation_history():
    details = request.form.to_dict()
    uid = details["uid"]
    file_info = details["file_id"]

@app.route("/update-user-categories", methods = ["Post"])
def update_user_cat():
    details = request.json
    #print(details)
    try:
        curr_cats = user_cat.find_one({"uid" : details["uid"]})
    except:
        return json.dumps({
                    "message" : "Error in DB",
                    "status_code" : 404
                    })
    
    if curr_cats:
        print(details)
        try:
            user_cat.find_one_and_update({"uid" : details["uid"]}, {'$set' : details})
        except:
            return {"message": "Error in updating category",
                    "status_code" : 400}
        
        return {"message": "Success in updating category",
                "status_code" : 200}
    else:
        try:
            user_cat.insert_one(details)
            return {"message": "Success in creating category",
                "status_code" : 200}
        except:
            return {"message": "Error in creating category",
                    "status_code" : 400}

@app.route("/get-user-categories", methods = ["Post"])
def get_categories():
    uid = request.form.to_dict()["uid"]
    try:
        details = user_cat.find_one({"uid" : uid})
    except:
        return {"message" : "Error with db",
                "status_code": 400}
    
    print(details)
    
    if details:
        resp = {"status_code": 200, 
                "categories" : details["categories"],
                "category_det" : details["category_det"],
                "categories_dict" : details["categories_dict"],
                "history_dict": details["history_dict"]}
        return resp
    else:
        return {"message" : "No Categories yet",
                "status_code": 300}

@app.route("/save-user-cat-upload")
def save_user_cat_upload():
    pass

@app.route("/post-feedback", methods = ["post"])
def save_user_feedback():
    feedback_details = request.form.to_dict()
    print(feedback_details)
    try:
        feedbacks.insert_one(feedback_details)
        return {"message": "Success!. Your feedback has been well recieved",
                "status_code" : 200}
    except:
        return {"message": "Error in giving feedback, please try again",
                    "status_code" : 400}


@app.route("/update-user-activity", methods = ["Post"])
def update_user_activity():
    details = request.json
    try:
        curr_activies = activities_db.find_one({"uid_date" : details["uid_date"]})
    except:
        return json.dumps({
                    "message" : "Error in DB",
                    "status_code" : 404
                    })
    if curr_activies:
        #print(details)
        try:
            activities_db.find_one_and_update({"uid_date" : details["uid_date"]}, {'$set' : details})
        except:
            return {"message": "Error in updating activity",
                    "status_code" : 400}
        
        return {"message": "Success in updating activity",
                "status_code" : 200}
    else:
        #print("Here")
        try:
            activities_db.insert_one(details)
            return {"message": "Success in creating activity",
                "status_code" : 200}
        except:
            return {"message": "Error in DB",
                    "status_code" : 400}


if __name__ == "__main__":
    client = get_database()
    userinfo_d = client['users-details']
    user_hist = client['users-history']
    user_cat = client["users-categories"]
    feedbacks = client["feedbacks"]
    activities_db = client["activities"]
    app.run(host = "0.0.0.0", debug=True, port=9000)