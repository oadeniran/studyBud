import Flask, requests

app = Flask(__name__)

@app.route("/")
def index():
    return "studybud User Api"

@app.route("/signup", method = ["POST"])
def signup():
    requests.form.to_dict()
    pass

@app.route("/login", method = ["Post"])
def login():
    pass

@app.route("/update-conversation-history",method = ["Post"])
def update_conv_hist():
    pass





if __name__ == "__main__":
    app.run(host = "0.0.0.")