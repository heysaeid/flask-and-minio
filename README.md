# Flask And MinIO
FlaskAndMinio allows you to easily use MinIO in your Flask projects and offers some features to improve and ease things.

## Install
You can either download the source code of this repository or install it via pip:
```
pip install git+https://github.com/heysaeid/flask-and-minio
```

## Usage
You can add it to your program in the following two ways:
```
from flask import Flask
from flask_and_minio import FlaskAndMinio

app = Flask(__name__)
app.config['MINIO_ENDPOINT'] = 'localhost:9000'
app.config['MINIO_ACCESS_KEY	'] = 'minioadmin'
app.config['MINIO_SECRET_KEY'] = 'minioadmin'
minio = FlaskAndMinio(app)

minio.get_url('bucket', 'object-name.png')
minio.remove_file('bucket', 'object-name.png')
```
Or:
```
from flask import Flask
from flask_and_minio import FlaskAndMinio

app = Flask(__name__)
minio = FlaskAndMinio()
app.config['MINIO_ENDPOINT'] = 'localhost:9000'
app.config['MINIO_ACCESS_KEY	'] = 'minioadmin'
app.config['MINIO_SECRET_KEY'] = 'minioadmin'
minio.init_app(app)

minio.get_url('bucket', 'object-name.png')
minio.remove_file('bucket', 'object-name.png')
```

Configurations:
| Variable                               | Default value       | Description                                                    |
| -------------                          |:-------------:      |:-------------:                                                 |
| MINIO_ENDPOINT                         | localhost:9000      | URL to S3 service.                                             |
| MINIO_ACCESS_KEY                       | minioadmin          | Access key (aka user ID) of an account in the S3 service.      |
| MINIO_SECRET_KEY                       | minioadmin          | Secret key (aka password) of an account in the S3 service.     |
| MINIO_SECURE                           | True                | Use HTTPS.                                                     |
| MINIO_REGION                           | None                | Set region.                                                    |
| MINIO_HTTP_CLIENT                      | None                | Customized HTTP client.                                        |
| MINIO_LOAD_BALANCER_URL                | None                | If you use load balancer for s3, you can have urls with this domain by setting this value                                    |