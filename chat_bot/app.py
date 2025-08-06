from flask import Flask,request,jsonify,render_template

app = Flask(__name__)
def chatbot_responde(user_mensaje):
    user_mensaje = user_mensaje.lower().strip()
    if"hola" in user_mensaje or "saludos" in user_mensaje:
        return "Hola, ¿cómo puedo ayudarte hoy?"
    elif "adiós" in user_mensaje or "chao" in user_mensaje:
        return "¡Adiós! Que tengas un buen día."
    elif "gracias" in user_mensaje or "gracias por tu ayuda" in user_mensaje:
        return "¡De nada! Estoy aquí para ayudarte."
    elif "cómo estás" in user_mensaje:
        return "Estoy aquí para ayudarte. ¿En qué puedo asistirte hoy?"
    elif "qué puedes hacer" in user_mensaje:
        return "Puedo responder preguntas, proporcionar información y ayudarte con tareas simples. ¿En qué puedo ayudarte hoy?"
    elif "ubicacion" in user_mensaje or "donde estoy" in user_mensaje:
        return "si tu no sabes donde estas menos yo :C" 
    else:
        return "Lo siento, no entiendo tu mensaje. ¿Podrías reformularlo o hacerme otra pregunta?"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat', methods=['POST'])
def get_responde():
    user_mensaje = request.form['user_mensaje']
    response = chatbot_responde(user_mensaje)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)