class Employee:
    def __init__(self, name, position, hourly_rate, availability):
        self.name = name
        self.position = position
        self.hourly_rate = hourly_rate
        self.availability = availability

    def __str__(self):
        return f"{self.name} ({self.position}) - ${self.hourly_rate} per hour\nAvailability: {self.availability}"
