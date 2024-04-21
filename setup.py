import protobuf_parser
from setuptools import setup

setup(
    name='protobuf_parser',
    version=protobuf_parser.__version__,
    author='Osia',
    author_email='somemail@mail.ru',
    url='http://googl.com',
    description='Разбор потока length-prefixed Protobuf сообщений на Python',
    long_description="",
    zip_safe=False,
    packages=['protobuf_parser'],
    install_requires=['protobuf'],
)
