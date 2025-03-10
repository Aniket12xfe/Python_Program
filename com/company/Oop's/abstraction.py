class Car:
    """A class representing a car with basic controls.
    
    This class demonstrates abstraction by hiding the complex implementation
    details of car operations while providing a simple interface.
    """
    
    def __init__(self):
        """Initialize a new Car instance with all controls off."""
        self.accelerator: bool = False
        self.brake_engaged: bool = False
        self.clutch: bool = False
        self.engine_running: bool = False
        
    def start(self) -> None:
        """Start the car by engaging clutch and accelerator."""
        if self.engine_running:
            print("Car is already running!")
            return
            
        self.clutch = True
        self.accelerator = True
        self.engine_running = True
        print("Car started successfully!")
        
    def stop(self) -> None:
        """Stop the car safely."""
        if not self.engine_running:
            print("Car is already stopped!")
            return
            
        self.accelerator = False
        self.brake_engaged = True
        self.clutch = True
        self.engine_running = False
        print("Car stopped safely!")
        
    def accelerate(self) -> None:
        """Accelerate the car if it's running."""
        if not self.engine_running:
            print("Start the car first!")
            return
            
        self.accelerator = True
        self.brake_engaged = False
        print("Car is accelerating...")
        
    def apply_brake(self) -> None:
        """Apply brakes to slow down or stop the car."""
        self.accelerator = False
        self.brake_engaged = True
        print("Brakes applied!")

# Example usage
if __name__ == "__main__":
    car = Car()
    car.start()
    car.accelerate()
    car.apply_brake()
    car.stop()