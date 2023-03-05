from flask import Flask
from flask_and_minio.minio import FlaskAndMinio


app = Flask(__name__)
app.config['MINIO_ENDPOINT'] = "localhost:900"
app.config['MINIO_ACCESS_KEY'] = "minioadmin"
app.config['MINIO_SECRET_KEY'] = "minioadmin"
app.config['MINIO_SECURE'] = True
minio = FlaskAndMinio(app)

print(minio.get_url('bucket', 'object-name.png'))


if __name__ == "__main__":
    app.run(debug=True)