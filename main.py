from app.main import create_app
from app import blueprint

app = create_app()
app.register_blueprint(blueprint)

if __name__ == '__main__':
    app.run()
