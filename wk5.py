#1.Design own class
# Base class
class Smartphone:
    def __init__(self, brand, model, storage_gb):
        self.brand = brand
        self.model = model
        self.storage_gb = storage_gb
        self.is_powered_on = False

    def power_on(self):
        self.is_powered_on = True
        print(f"{self.brand} {self.model} is now ON.")

    def power_off(self):
        self.is_powered_on = False
        print(f"{self.brand} {self.model} is now OFF.")

    def install_app(self, app_name):
        if self.is_powered_on:
            print(f"Installing {app_name} on {self.model}...")
        else:
            print("Power on the phone first!")

    def __str__(self):
        return f"{self.brand} {self.model} ({self.storage_gb}GB)"

# Derived class (Inheritance + Polymorphism)
class GamingPhone(Smartphone):
    def __init__(self, brand, model, storage_gb, cooling_system):
        super().__init__(brand, model, storage_gb)
        self.cooling_system = cooling_system  # Extra attribute for gaming phones

    def install_app(self, app_name):
        if self.is_powered_on:
            print(f"Installing {app_name} in Gaming Mode on {self.model}!")
        else:
            print("Power on the gaming phone first!")

    def enable_cooling(self):
        if self.is_powered_on:
            print(f"Cooling system '{self.cooling_system}' activated on {self.model}.")
        else:
            print("Power on the phone to activate cooling.")

# Create instances
phone1 = Smartphone("Apple", "iPhone 15", 128)
gaming_phone1 = GamingPhone("Asus", "ROG Phone 7", 512, "Advanced Liquid Cooling")

# Interact with the objects
print(phone1)
phone1.power_on()
phone1.install_app("Instagram")

print("\n" + "-"*30 + "\n")

print(gaming_phone1)
gaming_phone1.power_on()
gaming_phone1.install_app("PUBG Mobile")
gaming_phone1.enable_cooling()

#2Polymorphism Challenge
# Base class
class Vehicle:
    def move(self):
        raise NotImplementedError("Subclasses must implement this method.")

# Subclasses
class Car(Vehicle):
    def move(self):
        print("🚗 Driving on the road!")

class Plane(Vehicle):
    def move(self):
        print("✈️ Flying through the skies!")

class Boat(Vehicle):
    def move(self):
        print("🚤 Sailing on the water!")

class Train(Vehicle):
    def move(self):
        print("🚆 Running on the tracks!")

# Create a list of different vehicles
vehicles = [Car(), Plane(), Boat(), Train()]

# Call move() on each vehicle
for v in vehicles:
    v.move()
