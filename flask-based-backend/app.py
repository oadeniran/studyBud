from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def index():
    return "studybud User Api"

@app.route("/signup", methods = ["POST"])
def signup():
    request.form.to_dict()
    pass

@app.route("/login", methods = ["Post"])
def login():
    pass

@app.route("/update-conversation-history",methods = ["Post"])
def update_conv_hist():
    pass





if __name__ == "__main__":
    app.run(host = "0.0.0.0")