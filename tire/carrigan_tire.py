from tire.tire import Tire 

class CarriganTire(Tire):
    def __init__(self, tire_wear):
        self.tire_wear = tire_wear
        self.tire_needs_service = 0.9
    
    def needs_service(self):
        for tire in self.tire_wear:
            if tire >= self.tire_needs_service:
                return True
        return False