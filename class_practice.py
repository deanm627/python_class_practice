class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def print_info(self):
        print(self.year, self.make, self.model)


car = Vehicle("Nissan", "Leaf", 2015)
car.print_info()

class Person:
    people = []

    def __init__(self, name, email, phone):
        self.name = name
        self.email = email
        self.phone = phone 
        self.friends = []
        self.greeted_people = []
        self.greeting_count = 0
        Person.people.append(name)
    
    def greet(self, other_person):
        print(f'Hello {other_person.name}, I am {self.name}!')
        if other_person.name in self.greeted_people:
            return
        self.greeted_people.append(other_person.name)
        self.greeting_count += 1

    def print_contact_info(self):
        print(f"{self.name}'s email: {self.email}")
        print(f"{self.name}'s phone number: {self.phone}")

    def add_friend(self, person):
        self.friends.append(person)
    
    def num_friends(self):
        print(len(self.friends))

    def __str__(self):
        return f'Person: {self.name}, {self.email}, {self.phone}'
    
    def num_unique_people_greeted(self):
        print(self.greeting_count)

    @staticmethod
    def print_people():
        for person in Person.people:
            print(f"{person} is here!")

sonny = Person("Sonny", "sonny@hotmail.com", "483-485-4948")
jordan = Person("Jordan", "jordan@aol.com", "495-586-3456")
anna = Person("Anna", "", "")
aaron = Person("Aaron", "", "")

sonny.print_contact_info()
jordan.friends.append(sonny)
sonny.friends.append(jordan)

jordan.add_friend(sonny)
jordan.num_friends()

print(str(jordan))
print(str(sonny))

sonny.num_unique_people_greeted()
sonny.greet(jordan)
sonny.num_unique_people_greeted()
sonny.greet(jordan)
sonny.num_unique_people_greeted()
sonny.greet(anna)
sonny.num_unique_people_greeted()
sonny.greet(aaron)
sonny.num_unique_people_greeted()
sonny.greet(anna)
sonny.num_unique_people_greeted()

Person.print_people()