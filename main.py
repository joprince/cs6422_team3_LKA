from steering_system import SteeringSystem
from alert_system import AlertSystem
import pyinputplus as pyip
import csv


def main():
    steering_system = SteeringSystem()
    alert_system = AlertSystem()

    # TODO - Can take file names from user
    with open("data.tsv") as file:
        loaded_data = csv.reader(file, delimiter="\t")
        for line in loaded_data:
            # lane - line[0], line[1]
            # speed - line[2]
            # overriden - line[3]
            # lka_status - line[4]
            pass


if __name__ == "__main__":
    main()
