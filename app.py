from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/whatsapp", methods=["POST"])
def whatsapp_reply():
    incoming_msg = request.values.get("Body", "").lower()
    resp = MessagingResponse()
    msg = resp.message()

    if "horarios" in incoming_msg:
        msg.body("Nuestro horario es de 9 AM a 6 PM.")
    elif "cita" in incoming_msg:
        msg.body("Puedes agendar tu cita en: www.ejemplo.com")
    else:
        msg.body("Hola! ¿Cómo puedo ayudarte?")

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
