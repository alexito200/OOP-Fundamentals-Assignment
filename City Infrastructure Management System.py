# Task 1: Vehicle Registration System

class Vehicle:
    def __init__(self, reg_num, type, owner):
        self.registration_number = reg_num
        self.type = type
        self.owner = owner

    def update_owner(self, new_owner):
        self.owner = new_owner
        print(f"\nThe owner of vehicle {self.registration_number} has been updated to {self.owner}.")

vehicle1 = Vehicle("D15SNP", "Car", "Alex Lizandro")
vehicle2 = Vehicle("XYZ330", "Motorcycle", "Vitoria Silva")

print(f"\nVehicle 1: {vehicle1.registration_number}, Type: {vehicle1.type}, Owner: {vehicle1.owner}")
print(f"Vehicle 2: {vehicle2.registration_number}, Type: {vehicle2.type}, Owner: {vehicle2.owner}")

vehicle1.update_owner("Chris Hemsworth")
vehicle2.update_owner("Margot Robbie")

print(f"\nUpdated Vehicle 1 Owner: {vehicle1.owner}")
print(f"\nUpdated Vehicle 2 Owner: {vehicle2.owner}")

# Task 2: Event Management System Enhancement

class Event:
        def __init__(self, name, date):
            self.name = name
            self.date = date
            self.participant_count = 0

        def add_participant(self):
            self.participant_count += 1
            print(f"\nA participant has been added. Current participant count: {self.participant_count}")

        def get_participant_count(self):
            return self.participant_count

my_event = Event("Birthday Bash", "07-12-1954")

print(f"\nEvent: {my_event.name} on {my_event.date}")
print(f"\nInitial Participant Count: {my_event.get_participant_count()}")

my_event.add_participant()
my_event.add_participant()

print(f"\nUpdated Participant Count: {my_event.get_participant_count()}")


