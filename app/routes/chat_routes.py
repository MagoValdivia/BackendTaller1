# Rutas del chat

from flask import Blueprint

chat_bp = Blueprint("chat", __name__)

@chat_bp.route("/test")
def test_chat():
    return {"message": "Ruta de chat funcionando"}