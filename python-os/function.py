#!/usr/bin/env python3

birthdays = {'Alice':'1st jan', 'Namira':'1st July', 'Rana':'16th July'}
while True:
  name = input('Enter your name (Press Blank to Quit) : ')
  if name == "":
    break
  if name in birthdays:
    print(birthdays[name] + ' is the Birthday of '+name)
  else:
    print('The name not in the Database!')
    print('what is the birthday of{} ?'.format(name))
    dob = input()
    birthdays[name] = dob
    print('Database Updated Successfully')


