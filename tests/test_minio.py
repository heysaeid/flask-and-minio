import unittest
from flask import Flask
from flask_and_minio.minio import FlaskAndMinio
from minio import Minio


class TestFlaskAndMinio(unittest.TestCase):

    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['TESTING'] = True
        self.app.config['MINIO_ENDPOINT'] = 'localhost:9000'
        self.app.config['MINIO_LOAD_BALANCER_URL'] = 'http://localhost:9000'
        self.app.config['MINIO_ACCESS_KEY'] = 'minioadmin'
        self.app.config['MINIO_SECRET_KEY'] = 'minioadmin'
        self.app.config['MINIO_SECURE'] = False
        self.minio = FlaskAndMinio(self.app)

    def tearDown(self):
        del self.app
        del self.minio

    def test_get_client(self):
        client = self.minio.get_client()
        self.assertIsInstance(client, Minio)

    def test_get_url(self):
        bucket_name = 'mybucket'
        object_name = 'myobject'
        url = self.minio.get_url(bucket_name, object_name)
        expected_url = 'http://localhost:9000/mybucket/myobject'
        self.assertEqual(url, expected_url)

    def test_remove_file(self):
        bucket_name = 'mybucket'
        object_name = 'myobject'
        self.minio.remove_file(bucket_name, object_name)
        with self.assertRaises(Exception):
            self.minio.client.stat_object(bucket_name, object_name)
