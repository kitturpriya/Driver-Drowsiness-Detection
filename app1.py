from flask import Flask,redirect, url_for,render_template,request
import os
from index import d_dtcn

secret_key = str(os.urandom(24))

app = Flask(__name__)
app.config['TESTING'] = True
app.config['DEBUG'] = True
app.config['FLASK_ENV'] = 'development'
app.config['SECRET_KEY'] = secret_key
app.config['DEBUG'] = True

# Defining the home page of our site
@app.route("/",methods=['GET', 'POST'])
def home():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
           return render_template("final.html")
    else:
        # pass # unknown
        return render_template("index1.html")
    
@app.route("/about",methods=['GET', 'POST'])
def about():
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
           return render_template("index1.html")
    else:
        # pass # unknown
        return render_template("about.html")

@app.route("/features",methods=['GET', 'POST'])
def feature():
    if request.method == 'POST':
        if request.form.get('Continue') == 'Continue':
           return render_template("index1.html")
    else:
        # pass # unk
        return render_template("feature.html")

@app.route("/start", methods=['GET', 'POST'])
def index():
    print(request.method)
    if request.method == 'POST':
        if request.form.get('Start') == 'Start':
            # pass
            d_dtcn()
            return render_template("index1.html")
    else:
        # pass # unknown
        return render_template("index1.html")



if __name__ == "__main__":
    app.run()
    
