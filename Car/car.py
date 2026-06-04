from car_run import Car
if __name__ == '__main__':
    car_year = input("Enter car year's model:")
    car_make = input("Enter car make's name:")

    my_car = Car(car_year, car_make)

    print(f"\nTesting the vehicle: {my_car.get_model_info()}")
    print(f"Starting speed: {my_car.get_speed()}")

    print("Accelerating")
    for i in range(5):
