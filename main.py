import os
from flask import Flask

def create_app():
    app = Flask(__name__)

    from dashboard import dashboard
    app.register_blueprint(dashboard, url_prefix='/')

    from models import models
    app.register_blueprint(models, url_prefix='/models')

    return app


PORT = int(os.environ.get("PORT", 4000))
app = create_app()
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=PORT)
