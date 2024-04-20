py-protobuf
========================

Разбор потока length-prefixed Protobuf сообщений на Python (LEARNING_CENTER-288)

Чтобы сгенерировать Google Protobuf Python api выполниет следующую команду:
```
protoc --proto_path=. --python_out=protobuf_parser wrappermessage.proto

```
Запуск тестов
```
python -m unittest
```
