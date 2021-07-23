import os
import csv


class CarBase:

    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)

    def get_photo_file_ext(self):
        return os.path.splitext(self.photo_file_name)[1]


class Car(CarBase):
    car_type = 'car'

    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)


class Truck(CarBase):
    car_type = 'truck'

    def __init__(self, brand, photo_file_name, carrying, body_whl):
        super().__init__(brand, photo_file_name, carrying)
        if body_whl.count('x') == 2:
            try:
                self.body_length = float(body_whl[:body_whl.find('x')])
                self.body_width = float(body_whl[body_whl.find('x') + 1:body_whl.rfind('x')])
                self.body_height = float(body_whl[body_whl.rfind('x') + 1:])
            except ValueError:
                self.body_length = float(0)
                self.body_width = float(0)
                self.body_height = float(0)
        else:
            self.body_length = float(0)
            self.body_width = float(0)
            self.body_height = float(0)

    def get_body_volume(self):
        return self.body_length * self.body_width * self.body_height


class SpecMachine(CarBase):
    car_type = 'spec_machine'

    def __init__(self, brand, photo_file_name, carrying, extra):
        super().__init__(brand, photo_file_name, carrying)
        self.extra = extra


def get_car_list(csv_filename):
    car_list = list()
    pic_list = ['.jpg', '.jpeg', '.png', '.gif']
    with open(csv_filename, encoding="utf8") as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)
        try:
            for row in reader:
                if len(row)==7:
                    # обработка car
                    if row[0] == 'car' and row[1]!='' and isinstance(row[1], str) and row[2].isdigit() and os.path.splitext(row[3])[
                        1] in pic_list and row[4] == '' and row[5].replace('.', '', 1).isdigit() and row[6] == '':
                        car_list.append(Car(row[1],row[3],row[5],row[2]))
                    # обработка truck
                    if row[0] == 'truck' and row[1]!='' and isinstance(row[1], str) and row[2] == '' and os.path.splitext(row[3])[
                        1] in pic_list and row[5].replace('.', '', 1).isdigit() and row[6] == '':
                        try:
                            if row[4] == '':
                                row[4] = '0x0x0'
                                car_list.append(Truck(row[1],row[3],row[5],row[4]))
                            elif float(row[4][:row[4].find('x')]) and float(
                                    row[4][row[4].find('x') + 1:row[4].rfind('x')]) and float(
                                    row[4][row[4].rfind('x') + 1:]):
                                car_list.append(Truck(row[1],row[3],row[5],row[4]))
                            else:
                                row[4] = '0x0x0'
                                car_list.append(Truck(row[1],row[3],row[5],row[4]))
                        except ValueError:
                            pass
                    #обработка spec_machine
                    if row[0] == 'spec_machine' and row[1]!='' and isinstance(row[1], str) and row[2] == '' and os.path.splitext(row[3])[
                        1] in pic_list and row[4] == '' and row[5].replace('.', '', 1).isdigit() and row[6] != '' and isinstance(row[6], str):
                        car_list.append(SpecMachine(row[1],row[3],row[5],row[6]))
        except IndexError:
            pass

    return car_list


# car = Car('Bugatti Veyron', 'bugatti.png', '0.312', '2')
# print(car.car_type, car.brand, car.photo_file_name, car.carrying, car.passenger_seats_count, sep='\n')
# truck = Truck('Nissan', 'nissan.jpeg', '1.5', '3.92x2.09x')
# print(truck.car_type, truck.brand, truck.photo_file_name, truck.body_length, truck.body_width, truck.body_height, sep='\n')
# # spec_machine = SpecMachine('Komatsu-D355', 'd355.jpg', '93', 'pipelayer specs')
# # print(spec_machine.car_type, spec_machine.brand, spec_machine.carrying, spec_machine.photo_file_name, spec_machine.extra, sep='\n')
#
# cars = get_car_list('coursera_week3_cars.csv')
# for car in cars:
#     print(car.__dict__)
# # print(len(cars))

