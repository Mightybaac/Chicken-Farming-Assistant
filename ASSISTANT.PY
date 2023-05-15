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

# Example usage
farm = Farm("My Farm")

chicken1 = Chicken("Henrietta", "Rhode Island Red", "2022-01-01")
chicken2 = Chicken("Clucky", "White Leghorn", "2022-02-15")

farm.add_chicken(chicken1)
farm.add_chicken(chicken2)

chicken1.lay_egg()
chicken1.lay_egg()
chicken2.lay_egg()

print("Total eggs collected:", farm.collect_eggs())

print(farm.generate_health_report())

farm.feed_chickens()
