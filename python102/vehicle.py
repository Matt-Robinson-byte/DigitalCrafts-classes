import time
class Vehicle:
    def __init__(self, top_speed , acceleration, wheels = 4 ):
        
        self.wheels = wheels
        self.speed = 0
        self.top_speed = top_speed
        self.position = 0
        self.acceleration = acceleration
    
    def move(self):
        self.accelerate()
        self.position = self.position + self.speed
       
        

    def accelerate(self):
        if self.speed + self.acceleration < self.top_speed:
            self.speed = self.speed + self.acceleration
        else: self.speed = self.top_speed
        
    def reset(self):
        self.position = 0
        self.speed = 0

all_cars = {
    "sedan" : Vehicle(120,6),
    "small_suv" : Vehicle(100,7),
    "motorcycle" : Vehicle(140,8),
    "large_suv" : Vehicle(90,5),
    "truck" : Vehicle(160,4)

}




def race():
    seconds= int(input("Enter race duration in seconds: "))
    print("*********Race is about to Start!!!***********")
    time.sleep(0.5)
    clock = "five"
    for i in clock:
        print("*")
        time.sleep(0.5)
    i = 0
    for car_name in all_cars:
        all_cars[car_name].reset()
        
    while i < seconds:
        for car_name in all_cars:
            all_cars[car_name].move()
        i += 1
    print("*********Race is over!!!***********")
    for car_name in all_cars:
        print(f"{car_name}  - {all_cars[car_name].position}")

print(race())
