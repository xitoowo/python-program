# Обработка данных из файла
import csv


class Car:
    car_list = []

    def __init__(self, name, mpg, year, status):
        # self.name, self.mpg, self.year, self.status = name, mpg, year, status
        self.name = name
        self.mpg = mpg
        self.year = year
        self.status = status
        self.__class__.car_list.append(self)
        # Car.car_list.append(self)

    def __str__(self):
        return f"Name: {self.name}, Year: {self.year}"

    def list_view(self):
        return [self.name, self.mpg, self.year, self.status]


with open('cars.csv', 'r') as cars, open('car_status.csv') as car_statuses:
    car_reader = csv.reader(cars)
    status_reader = csv.reader(car_statuses)
    for car, status in zip(car_reader, status_reader):
        name, mpg, year = car
        stat = status[0]
        Car(name, mpg, year, stat)

with open('report.csv', 'w', newline='') as report:
    report_writer = csv.writer(report)
    for car in Car.car_list:
        report_writer.writerow(car.list_view())
