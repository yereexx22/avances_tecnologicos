from flask import Flask,request,jsonify,render_template

app = Flask(__name__)
def chatbot_responde(user_mensaje):
    user_message = user_message.lower().strip()