#!/usr/bin/python3.8

import addressbook_pb2


book=addressbook_pb2.AddressBook()


person = addressbook_pb2.Person()
person.id = 1234
person.name = "John Doe"
person.email = "jdoe@example.com"
phone = person.phones.add()
phone.number = "555-4321"
phone.type = addressbook_pb2.Person.HOME
book.people.append(person)


person = addressbook_pb2.Person()
person.id = 1234
person.name = "Mary Doe"
person.email = "marrydoe@sky.com"
phone = person.phones.add()
phone.number = "551-4321"
phone.type = addressbook_pb2.Person.MOBILE
book.people.append(person)

a = book.SerializeToString()
print(f'serialized= {a}')

b = addressbook_pb2.AddressBook()
b.ParseFromString(a)
print(f'restore={b}')
