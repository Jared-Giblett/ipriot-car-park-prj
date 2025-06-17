from car_park import CarPark
from sensor import EntrySensor, ExitSensor
from display import Display
import json
from pathlib import Path


def main():
    car_park = CarPark("Moondalup", 100, "moondalup.txt")
    car_park1 = CarPark("Moondalup", 100, "moondalup.txt")
    car_park1.write_config("moondalup_config.json")
    car_park1.from_config("moondalup_config.json")
    entry_sensor1 = EntrySensor(1, car_park, True)
    exit_sensor1 = ExitSensor(2, car_park, True)
    display = Display(1, car_park, "Welcome to Moondalup", True)
    car_park.register(entry_sensor1)
    car_park.register(exit_sensor1)
    car_park.register(display)
    for number in range(10):
        car_park.sensors[0].detect_vehicle()
    car_park.sensors[1].detect_vehicle()
    car_park.sensors[1].detect_vehicle()


if __name__ == '__main__':
    main()