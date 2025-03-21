from flask import Flask
import os

app = Flask(__name__)

@app.route("/details")
def wish():
    
    return f"The username is {os.getenv('USERNAME')}, password is {os.getenv('PASSWORD')} and the port no is {os.getenv('PORT')}!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000)