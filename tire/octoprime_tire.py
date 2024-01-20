from tire.tire import Tire 

class OctoprimeTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.tire_needs_service = 3.0

    def needs_service(self):
        sum = 0
        for tire in self.tire_wear:
            sum += tire
            if sum >= self.tire_needs_service:
                return True 
        return False