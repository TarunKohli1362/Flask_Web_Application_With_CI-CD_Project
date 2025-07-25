from flask import Flask 

app = Flask(_name_)

@app.route("/info")
def lwinfo():
	return "I Am LW From India"

@app.route("/name")
def lwname():
	return "My Name Is TARUN KOHLI"

@app.route("/email")
def lwemail():
	return "My Email ID Is tarunkohli5555@gmail.com"

@app.route("/phone")
def lwphone():
	return "My Phone Number Is 7404650169"

app.run(host="0.0.0.0", port=5000)