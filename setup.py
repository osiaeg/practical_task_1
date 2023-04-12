import protobuf_parser
from setuptools import setup

setup(
    name='protobuf_parser',
    version=protobuf_parser.__version__,
    author='R&EC SPb ETU',
    author_email='info@nicetu.spb.ru',
    url='http://nicetu.spb.ru',
    description='Разбор потока length-prefixed Protobuf сообщений на Python',
    long_description="",
    zip_safe=False,
    packages=['protobuf_parser'],
)
