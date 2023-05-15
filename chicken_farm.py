import datetime


class Chicken:
    def __init__(self, name, breed, date_of_birth):
        self.name = name
        self.breed = breed
        self.date_of_birth = date_of_birth
        self.health_status = "Healthy"
        self.egg_count = 0

    def lay_egg(self):
        self.egg_count += 1

    def update_health_status(self, status):
        self.health_status = status


class Farm:
    def __init__(self, name):
        self.name = name
        self.chickens = []
        self.log_file = self._generate_log_file_name()

    def add_chicken(self, chicken):
        self.chickens.append(chicken)
        self._log("Added chicken: {}".format(chicken.name))

    def remove_chicken(self, chicken):
        self.chickens.remove(chicken)
        self._log("Removed chicken: {}".format(chicken.name))

    def get_chicken_by_name(self, name):
        for chicken in self.chickens:
            if chicken.name == name:
                return chicken
        return None

    def collect_eggs(self):
        total_eggs = 0
        for chicken in self.chickens:
            total_eggs += chicken.egg_count
            chicken.egg_count = 0
        self._log("Collected {} eggs".format(total_eggs))
        return total_eggs

    def generate_health_report(self):
        report = "Health Report - {}\n".format(self.name)
        report += "-" * 40 + "\n"
        for chicken in self.chickens:
            report += "Chicken: {}\n".format(chicken.name)
            report += "Breed: {}\n".format(chicken.breed)
            report += "Date of Birth: {}\n".format(chicken.date_of_birth)
            report += "Health Status: {}\n".format(chicken.health_status)
            report += "-" * 40 + "\n"
        self._log("Generated health report")
        return report

    def feed_chickens(self):
        current_time = datetime.datetime.now()
        if current_time.hour < 6 or current_time.hour > 18:
            self._log("It's not feeding time.")
            return "It's not feeding time."
        for chicken in self.chickens:
            chicken.update_health_status("Healthy")
        self._log("Fed the chickens")

    def _generate_log_file_name(self):
        current_date = datetime.datetime.now().strftime("%Y-%m-%d")
        return "{}_{}.log".format(self.name, current_date)

    def _log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = "[{}] {}\n".format(timestamp, message)
        with open(self.log_file, "a") as file:
            file.write(log_message)


# Main program
farm = Farm("My Farm")

while True:
    print("=== Farm Management System ===")
    print("1. Add Chicken")
    print("2. Remove Chicken")
    print("3. Collect Eggs")
    print("4. Generate Health Report")
    print("5. Feed Chickens")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        name = input("Enter chicken name: ")
        breed = input("Enter chicken breed: ")
        date_of_birth = input("Enter chicken's date of birth (YYYY-MM-DD): ")
        chicken = Chicken(name, breed, date_of_birth)
        farm.add_chicken(chicken)
        print("Chicken added successfully.")

    elif choice == "2":
        name = input("Enter the name of the chicken to remove: ")
        chicken = farm.get_chicken_by_name(name)
        if chicken:
            farm.remove_chicken(chicken)
            print("Chicken removed successfully.")
        else:
            print("Chicken not found.")

    elif choice == "3":
        eggs_collected = farm.collect_eggs()
        print("Collected {} eggs.".format(eggs_collected))

    elif choice == "4":
        health_report = farm.generate_health_report()
        print(health_report)

    elif choice == "5":
        farm.feed_chickens()
        print("Chickens have been fed.")

    elif choice == "6":
        print("Exiting the Farm Management System.")
        break

    else:
        print("Invalid choice. Please try again.")
