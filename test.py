from flask import Flask,json, render_template
import os

#create instance of Flask app
app = Flask(__name__)

#decorator 
@app.route("/api/v1")
def hello():
    #it is a good idea to include information on how to use your API on the home route
    text = '''go to /all to see all events'''
    return render_template('index.html', html_page_text=text)

@app.route("/komen")
def hello():
    #it is a good idea to include information on how to use your API on the home route
    text = '''go to /all to see all events'''
    return render_template('index.html', html_page_text=text)  


if __name__ == "__main__":
    app.run(debug=True)