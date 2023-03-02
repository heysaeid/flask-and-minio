from setuptools import setup


with open("README.md", "r") as f:
    long_description = f.read()


setup(
    name="flask-and-minio",
    version='0.0.1',
    url="https://github.com/heysaeid/flask-and-minio.git",
    license="MIT",
    author="Saeid Noormohammadi",
    author_email="heysaeid92@gmail.com",
    description="Everything you need to use MinIO in flask",
    long_description=long_description,
    long_description_content_type="text/markdown",
    keywords=[
        "flask", 
        "minio", 
        "flask minio", 
        "flask ", 
        "flask-minio", 
        "flask-and-minio", 
        "Flask-And-Minio", 
        "MinIO"
    ],
    packages=["flask_and_minio"],
    zip_safe=False,
    platforms="any",
    install_requires=[
        "flask",
        "minio",
    ],
    classifiers=[
        "Framework :: Flask",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)