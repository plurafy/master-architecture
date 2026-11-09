class Vehicle {
  getType() {
    throw new Error("Method 'getType()' must be implemented!");
  }
}

class Car extends Vehicle {
  getType() {
    return "Car";
  }
}

class Bike extends Vehicle {
  getType() {
    return "Bike";
  }
}

class VehicleFactory {
  createVehicle() {
    throw new Error("Method 'createVehicle()' must be implemented!");
  }
}

class CarFactory extends VehicleFactory {
  createVehicle() {
    return new Car();
  }
}

class BikeFactory extends VehicleFactory {
  createVehicle() {
    return new Bike();
  }
}

const carFactory = new CarFactory();
const bikeFactory = new BikeFactory();

const myCar = carFactory.createVehicle();
const myBike = bikeFactory.createVehicle();

console.log(myCar.getType()); // Car
console.log(myBike.getType()); // Bike
