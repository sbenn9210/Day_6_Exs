class Person(object):
    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone
        self.friends = []
        self.greeting_count = 0
        self.num_unique_people_greeted = 0

    def greet(self, other_person):
         print(f'Hello {other_person.name}, I am {self.name}!')
         self.greeting_count += 1
         print(self.greeting_count)

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}, {self.name}'s phone number: {self.phone} ")

    def add_friend(self, other_person):
        self.friends.append(other_person)

    def __repr__self():
        print(f"{self.name}, {self.email}, {self.phone}")

    def num_unique_people_greeted(self):
        print("Hello World")
    #     greeted = []
    #     for person in greeted:
    #         if person in greeted:
    #             self.num_unique_people_greeted += 1
    #         else:
    #             self.num_unique_people_greeted = 1
    #     print(f"Unique greetings: {self.num_unique_people_greeted}")








sonny = Person('Sonny', 'sonny@hotmail.com', '483-485-4948')

jordan = Person('Jordan', 'jordan@aol.com', '495-586-3456')

sonny.greet(jordan)
jordan.greet(sonny)
jordan.greet(sonny)

jordan.greet(sonny)
jordan.greet(sonny)


print(sonny.email, sonny.phone)

print(jordan.email, jordan.phone)

sonny.print_contact_info()

jordan.add_friend(sonny)
