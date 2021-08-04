# You work for a company that leases bikes. Users can rent a bike via their mobile phone.
# Your job today is to assign a bike to each user of your application.
# There will always be at least as many bikes as users.
# Positions are expressed on a traditional grid with (x, y) coordinates: (0, 0) would be the bottom
# left of the grid and (0, 1) the space above.
# Any position can hold at most one user or bike.
# You are given a list of users and a list of bikes.
# Assign each user the closest bike closest to them, using Manhattan distances.
# Users are handled on a “first come, first serve” basis, meaning that an earlier user will get the bike closest to them
# assigned with no regard to later users.
# The output produced by your program should be a bike assignment in the form of a list of user-bikes pairings.

# For example:
# given a list of users: [(0, 0), (1, 1), (2, 0)] (3 users at different positions)
# and a list of bikes: [(1, 0), (2, 2), (2, 1)]
#
# the output would be: [((0, 0) , (1, 0)), ((1, 1), (2, 1)), ((2, 0), (2, 2))]
#
# In other words, first user was assigned the first bike, second user was assigned the  third bike, and third user was
# assigned the second bike.

from typing import List
import sys


class Position:
    """
    x : co-ordinate
    y : co-ordinate
    """
    x: int
    y: int

    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __repr__(self):
        return f'({self.x}, {self.y})'

    def __eq__(self, other):
        if self.x == other.x and self.y == other.y:
            return True
        return False


class UserPosition(Position):
    pass


class BikePosition(Position):
    pass


class BikeLease:
    """
    Bike lease interface to match a user to closest bike on a FCFS basis
    list_of_bike_positions - list of BikePosition Objects (x,y) containing x and y co-ordinates of bikes
    list_of_user_positions - list of UserPosition Objects (x,y) containing x and y co-ordinates of users
    """
    list_of_bike_positions: List[BikePosition] = []
    list_of_user_positions: List[UserPosition] = []
    assigned_bikes: List[tuple] = []

    def __init__(self, bikes: List[BikePosition], users: List[UserPosition]) -> None:
        self.list_of_bike_positions = bikes
        self.list_of_user_positions = users
        self.assigned_bikes = []
        self.assign_bikes()

    def __eq__(self, other):
        for i, v in enumerate(self.assigned_bikes):
            if v != other[i]:
                return False
        return True

    def __repr__(self):
        string = ""
        for i in self.assigned_bikes:
            string += f'User: {i[0]}, Bike: {i[1]} \n'
        return string

    @staticmethod
    def calculate_manhattan_distance(user_pos: UserPosition, bike_pos: BikePosition) -> int:
        """
        Calculates the manhattan distance between a user and a bike's location
        :param user_pos: Position object with x and y co-ordinates
        :param bike_pos: Position object with x and y co-ordinates
        :return: manhattan_distance between the user and bike
        """
        return abs(user_pos.x - bike_pos.x) + abs(user_pos.y - bike_pos.y)

    def assign_bikes(self) -> None:
        """
        Assign the bikes to each user on a first come first serve basis
        for each user:
            for each bike:
                distances-> manhattan(user, bike)
            return bike with min(distances)
            remove current bike from bikelist
        """
        for user_pos in self.list_of_user_positions:
            min_distance = sys.maxsize * 2 + 1  # set minimum distance to largest value possible , sys.maxsize
            closest_bike_index = None
            for i, bike_pos in enumerate(self.list_of_bike_positions):
                distance = self.calculate_manhattan_distance(user_pos=user_pos, bike_pos=bike_pos)
                if distance < min_distance:
                    min_distance = distance
                    closest_bike_index = i
            closest_bike = self.list_of_bike_positions.pop(closest_bike_index)
            self.assigned_bikes.append((user_pos, closest_bike))


def run_test(users: List[tuple], bikes: List[tuple], test_answer: List[tuple]) -> None:
    """
    Converts the user positions list and bikes positions list into PositionObjects and tests for the given answer
    :param users: user positions in tuples
    :param bikes: bike positions in tuples
    :param test_answer: Assigned bikes for users, answer to test
    """
    mod_users = [UserPosition(_[0], _[1]) for _ in users]
    mod_bikes = [BikePosition(_[0], _[1]) for _ in bikes]
    # convert test_ans into (UserPos, BikePos) tuple
    mod_answer = [(UserPosition(_[0][0], _[0][1]), BikePosition(_[1][0], _[1][1])) for _ in test_answer]
    assigned_bikes = BikeLease(mod_bikes, mod_users)

    assert assigned_bikes.assigned_bikes == mod_answer


if __name__ == "__main__":

    # xx denotes an empty space
    # BK denotes a bike
    # Ui denotes User i

    #############################################

    #  xx xx BK
    #  xx U2 BK
    #  U1 BK U3

    users_pos = [(0, 0), (1, 1), (2, 0)]
    bikes_pos = [(1, 0), (2, 2), (2, 1)]
    test_ans = [((0, 0), (1, 0)), ((1, 1), (2, 1)), ((2, 0), (2, 2))]

    run_test(users_pos, bikes_pos, test_ans)

    print('test 1 correct')

    #############################################

    # 5  xx xx U3 xx xx BK
    # 4  xx BK xx U2 xx xx
    # 3  xx xx BK xx U6 xx
    # 2  xx BK xx xx xx U5
    # 1  xx U4 xx BK xx xx
    # 0  U1 xx xx xx BK xx
    #    0  1  2  3  4  5

    users_pos = [(0, 0), (3, 4), (2, 5), (1, 1), (5, 2), (4, 3)]
    bikes_pos = [(1, 2), (4, 0), (2, 3), (5, 5), (1, 4), (3, 1)]

    test_ans = [((0, 0), (1, 2)),
                ((3, 4), (2, 3)),
                ((2, 5), (1, 4)),
                ((1, 1), (3, 1)),
                ((5, 2), (4, 0)),
                ((4, 3), (5, 5))]

    run_test(users_pos, bikes_pos, test_ans)
    print('test 2 correct')

    #############################################

    # 7  xx xx xx xx xx xx xx xx
    # 6  xx xx xx xx xx xx xx xx
    # 5  xx xx U2 xx xx xx xx xx
    # 4  xx BK xx xx xx xx xx xx
    # 3  xx xx xx xx xx xx xx xx
    # 2  xx xx xx xx xx xx xx U1
    # 1  BK U3 xx xx xx xx xx xx
    # 0  BK xx xx xx xx xx xx xx
    #    0  1  2  3  4  5  6  7

    users_pos = [(7, 2), (2, 5), (1, 1)]
    bikes_pos = [(0, 0), (1, 4), (0, 1)]
    test_ans = [((7, 2), (1, 4)),
                ((2, 5), (0, 1)),
                ((1, 1), (0, 0))]

    run_test(users_pos, bikes_pos, test_ans)
    print('test 3 correct')

