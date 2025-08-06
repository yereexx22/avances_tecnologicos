from flask import Flask,request,jsonify,render_template

app = Flask(__name__)
def chatbot_responde(user_mensaje):
    user_message = user_message.lower().strip()
    if"hola" in user_message or "saludos" in user_message:
        return "Hola, ¿cómo puedo ayudarte hoy?"