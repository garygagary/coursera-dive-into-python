import csv
import os
    
def validate(data):
    if len(data) != 7:
        return None
        
    valid_car = [
        data[CarBase.csv_brand], \
        data[CarBase.csv_photo_file_name], \
        data[CarBase.csv_carrying],
        data[CarBase.csv_passenger_seats_count]
    ]
    valid_truck = [
        data[CarBase.csv_brand], \
        data[CarBase.csv_photo_file_name], \
        data[CarBase.csv_carrying], \
        data[CarBase.csv_body_whl]
    ]
    valid_spec_machine = [
        data[CarBase.csv_brand], \
        data[CarBase.csv_photo_file_name], \
        data[CarBase.csv_carrying], \
        data[CarBase.csv_extra]       
    ]
        
    if data[CarBase.csv_car_type] == 'car' \
    and not ('' in valid_car):
        try:
            car = Car(*valid_car)
        except ValueError:
            pass
        try:
            if car.get_photo_file_ext() in \
            ('.jpg', '.jpeg', '.png', '.gif'):
                return car
        except:
            pass
    
    if data[CarBase.csv_car_type] == 'truck' \
    and not ('' in (valid_truck[0], valid_truck[1], valid_truck[2])):
        try:
            truck = Truck(*valid_truck)
        except ValueError:
            pass
        try:
            if truck.get_photo_file_ext() in \
            ('.jpg', '.jpeg', '.png', '.gif'):
                return truck
        except:
            pass
    
    if data[CarBase.csv_car_type] == 'spec_machine' \
    and not ('' in valid_spec_machine):
        try:
            spec_machine = SpecMachine(*valid_spec_machine)
        except ValueError:
            pass
        try:
            if spec_machine.get_photo_file_ext() in \
            ('.jpg', '.jpeg', '.png', '.gif'):
                return spec_machine
        except:
            pass
        
def get_car_list(csv_filename):
    car_list = []
    with open(csv_filename) as csv_fd:
        reader = csv.reader(csv_fd, delimiter=';')
        next(reader)  # пропускаем заголовок
        for row in reader:
            car = validate(row)
            if car:
                car_list.append(car)
    return car_list

class CarBase:
    csv_car_type = 0
    csv_brand = 1
    csv_passenger_seats_count = 2
    csv_photo_file_name = 3
    csv_body_whl = 4
    csv_carrying = 5
    csv_extra = 6
    
    def __init__(self, brand, photo_file_name, carrying):
        self.brand = brand
        self.photo_file_name = photo_file_name
        self.carrying = float(carrying)
        
    def get_photo_file_ext(self):
        ext = os.path.splitext(self.photo_file_name)
        return ext[1]
    
class Car(CarBase):
    
    def __init__(self, brand, photo_file_name, carrying, passenger_seats_count):
        super().__init__(brand, photo_file_name, carrying)
        self.passenger_seats_count = int(passenger_seats_count)
        self.car_type = 'car'
        
class Truck(CarBase):
    def __init__(self, brand, photo_file_name, carrying, body_whl = ''):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'truck'
        try:
            self.body_whl = body_whl.split('x', 2)
            self.body_length = float(self.body_whl[0])
            self.body_width = float(self.body_whl[1])
            self.body_height = float(self.body_whl[2])
        except ValueError:
            self.body_whl = self.body_length = self.body_width = self.body_height = 0.0

            
            
    def get_body_volume(self):
        return(self.body_length * self.body_width * self.body_height)
    
class SpecMachine(CarBase):
    def __init__(self, brand, photo_file_name, carrying, extra=None):
        super().__init__(brand, photo_file_name, carrying)
        self.car_type = 'spec_machine'
        self.extra = extra