from flask import Flask,request,jsonify,render_template

app = Flask(__name__)
def chatbot_responde(user_mensaje):
    user_message = user_message.lower().strip()
    if"hola" in user_message or "saludos" in user_message:
        return "Hola, ¿cómo puedo ayudarte hoy?"
    elif "adiós" in user_message or "chao" in user_message:
        return "¡Adiós! Que tengas un buen día."
    elif "gracias" in user_message or "gracias por tu ayuda" in user_message:
        return "¡De nada! Estoy aquí para ayudarte."
    elif "cómo estás" in user_message:
        return "Estoy aquí para ayudarte. ¿En qué puedo asistirte hoy?"
    elif "qué puedes hacer" in user_message:
        return "Puedo responder preguntas, proporcionar información y ayudarte con tareas simples. ¿En qué puedo ayudarte hoy?"
     elif "ubicacion" in user_mensaje or "donde estoy" in user_mensaje:
        return "si tu no sabes donde estas menos yo :C" 
        else:
        return "Lo siento, no entiendo tu mensaje. ¿Podrías reformularlo o hacerme otra pregunta?"