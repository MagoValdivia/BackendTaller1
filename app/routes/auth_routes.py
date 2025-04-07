# Rutas de autenticaci�n

from flask import request, jsonify, Blueprint
from werkzeug.security import generate_password_hash
from app import db
from app.models.user import User  # importa tu modelo

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'error': 'Faltan campos obligatorios'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'error': 'Correo ya registrado'}), 400

    hashed_password = generate_password_hash(password)

    new_user = User(username=username, email=email, password_hash=hashed_password)

    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'Usuario registrado con éxito'}), 201