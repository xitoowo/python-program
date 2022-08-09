import csv
import sys


class Car:
    car_lists = []

    def __init__(self, name, mpg, year, status):
        self.name = name
        self.mpg = mpg
        self.year = year
        self.status = status
        self.__class__.car_lists.append(self)

    def __iter__(self):
        return iter([self.name, self.mpg, self.year, self.status])

    def __str__(self):
        return f'Car: {self.name}, Status: {self.status}'


with open('../cars.csv', 'r') as cars, open('../car_status.csv', 'r') as statuses:
    car_reader = csv.reader(cars)
    status_reader = csv.reader(statuses)
    for car, status in zip(car_reader, status_reader):
        # if car_reader.line_num == 1:
        #     continue
        name, mpg, year = car
        stat = status[0]
        item = Car(name, mpg, year, stat)

with open('report.csv', 'w', newline='') as report:
    report_writer = csv.writer(report)
    report_writer.writerows(Car.car_lists)

print(sys.getsizeof(Car.car_lists))
