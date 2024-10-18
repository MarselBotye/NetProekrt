from flask import Flask
from router.summary import summary_route
from router.improved_prompt import improved_route
from router.message_processor import message_bp
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
app.secret_key = 'your_secret_key'
app.config['CSRF_ENABLED'] = False

app.register_blueprint(summary_route, url_prefix='/api')
app.register_blueprint(improved_route, url_prefix='/api')
app.register_blueprint(message_bp, url_prefix='/api')

# Импортируем и регистрируем blueprint
# from blueprints.example import example_bp
# app.register_blueprint(example_bp, url_prefix='/example')


if __name__ == '__main__':
    app.run(debug=True)