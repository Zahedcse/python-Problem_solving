#!/usr/bin/env python3
class Student:
    def __init__(self, name, id, phone, email):
        self.name = name
        self.id = id
        self.phone = phone
        self.email = email
        self.address = None

    def view(self):
        print('Student Details: ')
        print()
        print('Name of the student is: {} \nStudent id is: {} \nStudent Phone: {} \nStudent Email: {} '.format(self.name,self.id, self.phone,self.email))
        print()
        print('Address Information :')
        if self.address:
            print(self.address)
        print()
class Address:
    def __init__(self, village, union, post_office, thana, district):
        self.village = village
        self.union = union
        self.post_office = post_office
        self.thana = thana
        self.district = district

    def __str__(self):
        return 'Village: {} \nUnion: {} \nPost_Office: {} \nThana : {} \nDistrict : {}'.format(self.village,self.union,self.post_office,self.thana,self.district)



Zahed = Student('Zahed Alam', 23, '01846899956', 'Zahed@gmail.com')
Zahed.address = Address('Charsaha Bhikari', '5 no union', 'Kasari Pukur', 'Sonagazi','Feni')
Zahed.view()
Namira = Student('Namira Jannat Amaya', 1, '01846899957', 'Namira@gmail.com')
Namira.address = Address('Charsaha Bhikari', '3 no union', 'Chittagong GPO', 'Kotwali','Chattogram')
Namira.view()
