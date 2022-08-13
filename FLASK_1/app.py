from flask import Flask, render_template, jsonify, request
import json
import datetime
from dataclasses import dataclass

app = Flask(__name__)

## APP -> SERVER 
##      HOSTNAME : IP ADDRESS -> 172.0.0.1 (localhost - internal IP) 
##                            -> 89.5.5.25 (external - Seattle, Washington)
##
##      PORT : 0 -> 99999
##          Specifying where to connect in the server
##
##
##      HTTP Protocol 
##          REQUEST -> RESPONSE (html) or (data json)
## 
## 
##      API - Application Protocol Interface
##          Abstraction that provides you methods/functions to use an underlying process.
## 
##      JSON - Javascript Object Notation
##          Python dictionaries
##          { key : {key : {}} }
##          keys must be unique and they must be hashable.
##
##      http://google.com/search -> http://8.8.8.8:4000 -> html page
##      
##      https://127.0.0.1:8080/
##      https://0.0.0.0:8000/ -> you are exposing your external IP (if it exists and your computer is connected to the internet)
##      
##          WARNING: if you are in a development environment and you are not sure if your code works and is not production ready, DON'T EXPOSE YOUR WEBSITE TO THE WORLD
##
##
##          gunicorn and nginx -> forward facing external IP handshakes and communications
##
##
##      (DNS) - Domain name service 
##          Routes IP address and Port -> domain name
## 
##      REST API 
## 
##          GET, PUT, POST, DELETE
## 
##          GET -> retrieve from api
##          POST -> create new data to api
##          PUT -> update existing data in api
##          DELETE -> deletes data from api

@dataclass
class User:

    iduser : int
    username : str
    password : str
    isadmin : bool
    isactive : bool

    def __init__(
        self,
        iduser,
        username,
        password,
        isadmin = False,
        isactive = False
     ):
        self.iduser = iduser
        self.username = username
        self.password = password
        self.isadmin = isadmin
        self.isactive = isactive




def print_hello():
    print('hello')


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")


@app.route("/register", methods=["POST"])
def user_register():
    request_body = request.get_json(force=True)
    print(json.dumps(request_body, indent=4))

    return {'Status': 200}



@app.route('/search', methods=["GET"])
def search():
    return jsonify({'test': 1})

@app.route('/delete/user/<int:iduser>', methods=["DELETE"])
def delete(iduser : int) -> None:
    # deletes a user from the database
    # if successful, return status code 200
    # otherwise, return status code 400
    # must be superuser to access, must have request header authentication token set   
    #   will return forbidden 403 otherwise
    raise NotImplementedError
    

if __name__ == '__main__':
    app.run(debug=True, port=8000)
