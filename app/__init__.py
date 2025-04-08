from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from flask_socketio import SocketIO
from flask_migrate import Migrate
from app.config import Config
from sqlalchemy import text

db = SQLAlchemy()
socketio = SocketIO(cors_allowed_origins="*")
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # Inicializar extensiones
    db.init_app(app)
    migrate.init_app(app, db)
    CORS(app)
    socketio.init_app(app)

    # Importar y registrar rutas dentro de la función de creación de la app
    from app.routes.auth_routes import auth_bp
    from app.routes.chat_routes import chat_bp

    app.register_blueprint(auth_bp, url_prefix="/api/auth")
    app.register_blueprint(chat_bp, url_prefix="/api/chat")
    
    # Ruta temporal para probar DB
    @app.route("/api/ping-db")
    def ping_db():
        try:
            db.session.execute(text("SELECT 1"))
            return {"message": "Conexión a la base de datos exitosa"}, 200
        except Exception as e:
            return {"error": str(e)}, 500

    return app
