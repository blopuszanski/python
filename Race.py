class vehicle:
    def __init__(self, vehicle_type, color, brand, velocity):
        self.vehicle_type = vehicle_type
        self.color = color
        self.brand = brand
        self.velocity = velocity

    def move(self):
        vehicle_type = input('Please input your vehicle car/moto/aeroplane/boat: ')
        self.vehicle_type == vehicle_type

        if self.vehicle_type == 'car':
            print('Drive!')
        elif self.vehicle_type == 'moto':
            print('Drive!')
        elif self.vehicle_type == 'aeroplane':
            print('Fly!')
        elif self.vehicle_type == 'boat':
            print('Swim!')
        else:
            print('You chose a wrong vehicle!')

    def specification(self):
        print(
            f'Your vehicle is {self.vehicle_type} in color {self.color} from brand {self.brand} with the maximum velocity {self.velocity}')


if __name__ == '__main__':
    car = vehicle('car', 'black', 'Audi', 180)
    car.specification()
    plane = vehicle('aeroplane', 'silver', 'Boeing', 400)
    plane.specification()
    boat = vehicle('boat', 'blue marine', 'Corvette', 300)
    boat.specification()

    road = int(input('Please input a race length in kilometres: '))
    car_result = road / car.velocity
    print(f'The car needs time to fullfil the race {car_result}')
    plane_result = road / plane.velocity
    print(f'The aeroplane needs time to fullfil the race {plane_result}')
    boat_result = road / boat.velocity
    print(f'The boat needs time to fullfil the race {boat_result}')