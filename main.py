import random


class Elevator:
    def __init__(self, max_floor):
        self.max_floor = max_floor
        self.position = random.randint(-2, max_floor)

    def go_up(self, counter):
        while counter:
            token = counter - 1
            print(f'Going up {self.position + token}')
            return self.go_up(token)

    def go_down(self, counter):
        while counter:
            token = counter - 1
            print(f'Going down {self.position + token}')
            return self.go_down(token)


def building(height):
    elevator1 = Elevator(height)
    users_position = int(input('Which floor are you on now?'))
    counter = abs(users_position - elevator1.position)

    if elevator1.position > users_position:
        print(f'The elevator is on the {elevator1.position}th floor.')
        elevator1.go_down(counter)
    elif elevator1.position < users_position:
        print(f'The elevator is on the {elevator1.position}th floor.')
        elevator1.go_up(counter)
    else:
        print('The elevator is on this floor.')
        print('*Doors are opening*')


building(8)
