from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

def chatbot_response(user_message):
    user_message = user_message.lower().strip()

    if "hola" in user_message or "buenos dias" in user_message or "buenas tardes" in user_message:
        return "¡Hola! ¿Cómo puedo ayudarte hoy?"

    elif "como estas" in user_message or "que tal" in user_message:
        return "Estoy bien, gracias por preguntar. ¿Y tú?"

    elif "adios" in user_message or "hasta luego" in user_message or "nos vemos" in user_message:
        return "¡Adiós! Que tengas un buen día."

    elif "ayuda" in user_message or "qué puedes hacer" in user_message:
        return (
            "Puedo responder a preguntas básicas. Intenta preguntar por:\n"
            "- 'horario'\n"
            "- 'contacto'\n"
            "- 'ubicación'\n"
            "- 'servicios'\n"
            "- 'envíos'\n"
            "- 'garantía'\n"
            "- 'pago'\n"
            "- 'promoción'\n"
            "- 'productos'\n"
            "- 'preguntas frecuentes'\n"
            "- 'clima'\n"
            "- 'chiste'\n"
            "- 'nombre'"
        )

    elif "horario" in user_message or "atención" in user_message:
        return "Nuestro horario de atención es de 9:00 a 18:00 de lunes a viernes, y de 10:00 a 14:00 los sábados."

    elif "contacto" in user_message or "teléfono" in user_message or "correo" in user_message:
        return "Puedes contactarnos en el 555-1234, por WhatsApp al +58 424-000-0000, o enviarnos un correo a info@ejemplo.com."

    elif "ubicación" in user_message or "dónde están" in user_message or "dirección" in user_message:
        return "Estamos ubicados en la Calle 123, Sector Centro, Valencia. Puedes encontrarnos en Google Maps como 'Ejemplo S.A.'."

    elif "servicios" in user_message or "qué ofrecen" in user_message:
        return "Ofrecemos atención personalizada, soporte técnico, consultoría especializada y venta de productos tecnológicos."

    elif "envío" in user_message or "entrega" in user_message:
        return "Realizamos envíos a todo el país. El tiempo estimado de entrega es de 2 a 5 días hábiles."

    elif "garantía" in user_message or "devolución" in user_message:
        return "Todos nuestros productos tienen garantía de 1 año. Puedes solicitar devoluciones dentro de los primeros 15 días."

    elif "pago" in user_message or "formas de pago" in user_message:
        return "Aceptamos tarjetas de crédito y débito, transferencias bancarias, pago móvil y efectivo en tienda física."

    elif "promoción" in user_message or "descuento" in user_message:
        return "Actualmente tenemos un 15% de descuento en productos seleccionados. Regístrate en nuestra web para obtener un cupón de bienvenida."

    elif "productos" in user_message or "catálogo" in user_message:
        return "Tenemos una amplia variedad de productos: electrónica, accesorios, software y servicios técnicos."

    elif "preguntas frecuentes" in user_message or "faq" in user_message:
        return (
            "Algunas preguntas frecuentes:\n"
            "1. ¿Aceptan pagos con tarjeta? — Sí, Visa y MasterCard.\n"
            "2. ¿Hacen envíos? — Sí, a todo el país.\n"
            "3. ¿Tienen garantía? — Todos nuestros productos tienen garantía de 1 año."
        )

    elif "clima" in user_message or "tiempo" in user_message:
        return "No tengo acceso en tiempo real al clima, pero puedes consultarlo en apps como Weather o Google."

    elif "chiste" in user_message or "cuéntame algo" in user_message:
        return "¿Por qué el libro de matemáticas estaba triste? Porque tenía demasiados problemas. 😄"

    elif "nombre" in user_message or "quién eres" in user_message:
        return "Soy tu asistente virtual, diseñado para ayudarte con información útil y responder tus preguntas."

    else:
        return "Lo siento, no entiendo tu pregunta. ¿Puedes reformularla o usar una palabra clave como 'horario', 'servicios' o 'ayuda'?"
        
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_message = request.json.get('message')
    response = chatbot_response(user_message)
    return jsonify({'response': response})

if __name__ == '__main__':
    app.run(debug=True)