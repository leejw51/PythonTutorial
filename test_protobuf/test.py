#!/usr/bin/python3.8

import addressbook_pb2
person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME


a = person.SerializeToString()
print(f'serialized= {a}')

b = addressbook_pb2.Person()
b.ParseFromString(a)
print(f'restore={b}')
