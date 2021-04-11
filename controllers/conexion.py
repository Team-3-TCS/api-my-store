from flask import Flask, request,jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
# jdbc:mysql://68.183.23.64:3306/?user=mystorebd
app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://mystorebd:Server123_@68.183.23.64:3306/dbMyStore'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
ma=Marshmallow(app)

def iniciar():
    if __name__=="__main__":
        app.run(debug=True)