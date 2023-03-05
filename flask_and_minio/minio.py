from flask import Flask
from minio import Minio


class FlaskAndMinio:

    def __init__(self, app: Flask = None) -> None:
        self.domain = None
        self.client = None
        if app is not None:
            self.init_app(app)

    def init_app(self, app: Flask) -> None:
        app.config.setdefault('MINIO_ENDPOINT', 'localhost:9000')
        app.config.setdefault('MINIO_LOAD_BALANCER_URL', app.config['MINIO_ENDPOINT'])
        app.config.setdefault('MINIO_ACCESS_KEY', 'minioadmin')
        app.config.setdefault('MINIO_SECRET_KEY', 'minioadmin')
        app.config.setdefault('MINIO_SECURE', True)
        app.config.setdefault('MINIO_REGION', None)
        app.config.setdefault('MINIO_HTTP_CLIENT', None)

        self.domain = app.config['MINIO_LOAD_BALANCER_URL']
        self.client = Minio(
            endpoint=app.config['MINIO_ENDPOINT'],
            access_key=app.config['MINIO_ACCESS_KEY'],
            secret_key=app.config['MINIO_SECRET_KEY'],
            secure=app.config['MINIO_SECURE'],
            region = app.config['MINIO_REGION'],
            http_client = app.config['MINIO_HTTP_CLIENT']
        )
        app.extensions['minio'] = self

    def get_client(self) -> Minio:
        return self.client
    
    def get_url(self, bucket_name: str, object_name: str, **kwargs) -> str:
        url = self.client.presigned_get_object(bucket_name, object_name, **kwargs)
        return self.domain + '/' + '/'.join(url.split('/')[3:])  

    def remove_file(self, bucket_name: str, object_name: str, **kwargs) -> str:
        return self.client.remove_object(bucket_name, object_name, **kwargs)