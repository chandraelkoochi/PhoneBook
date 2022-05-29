from flask import Flask,request, render_template , redirect, url_for
import json
import os

app = Flask(__name__)

headings = ("Name", "Phone Number", "Address")


@app.route('/')
def hello_world():
    return 'Welcome'

@app.route('/home', methods=["GET","POST"])
def home():
    if request.method == "GET":
        table = {}
        with open('dataFile.json', 'r') as f:
            if os.stat("dataFile.json").st_size != 0:
                table = json.loads(f.read())

        return render_template('home.html', data = table)
    if request.method == "POST":
        first_name = request.form.get("uname")
        phone_num = request.form.get("phone")
        address = request.form.get("address")
        data = {"name": first_name, "phone": phone_num, "add": address}
        userData = {"user_details": []}
        with open('dataFile.json', 'r') as f:
            if os.stat("dataFile.json").st_size != 0:
                #print(json.load(f))
                userData = json.load(f)
                userData["user_details"].append(data)
            else:
                userData["user_details"].append(data)
        with open('dataFile.json', 'w') as f:
            json.dump(userData,f)
        with open('dataFile.json', 'r') as f:
            table = json.loads(f.read())

        return render_template('home.html', data = table)

@app.route('/form')
def form():
        return render_template('form.html')


if __name__ == '__main__':
    app.run()
