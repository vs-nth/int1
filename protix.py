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
    :param list_of_bike_positions - list of BikePosition Objects (x,y) containing x and y co-ordinates of bikes
    :param list_of_user_positions - list of UserPosition Objects (x,y) containing x and y co-ordinates of users

    """
    list_of_bike_positions: List[BikePosition] = []
    list_of_user_positions: List[UserPosition] = []
    assigned_bikes: List[tuple] = []

    def __init__(self, bikes: List[BikePosition], users: List[UserPosition]) -> None:
        """
        Initialize vars
        :param bikes:
        :param users:
        """
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
        Assign the bikes to each user in a first come first serve basis
        :return: list containing tuples of UserPosition and matched BikePosition
        """
        for user_pos in self.list_of_user_positions:
            min_distance = 0
            closest_bike = None
            for bike_pos in self.list_of_bike_positions:
                distance = self.calculate_manhattan_distance(user_pos=user_pos, bike_pos=bike_pos)
                if distance < min_distance or min_distance == 0:
                    min_distance = distance
                    closest_bike = bike_pos
            self.assigned_bikes.append((user_pos, closest_bike))
            self.list_of_bike_positions.remove(closest_bike)  # remove bike from available bikes


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
    users_pos = [(0, 0), (1, 1), (2, 0)]
    bikes_pos = [(1, 0), (2, 2), (2, 1)]
    test_ans = [((0, 0), (1, 0)), ((1, 1), (2, 1)), ((2, 0), (2, 2))]

    run_test(users_pos, bikes_pos, test_ans)

    print('test 1 correct')

    users_pos = [(0, 0), (1, 1), (3, 3), (5, 0), (6, 11)]
    bikes_pos = [(1, 0), (2, 2), (2, 1), (6, 6), (10, 10), (2, 3)]
    test_ans = [((0, 0), (1, 0)),
                ((1, 1), (2, 1)),
                ((3, 3), (2, 3)),
                ((5, 0), (2, 2)),
                ((6, 11), (6, 6))]

    run_test(users_pos, bikes_pos, test_ans)
    print('test 2 correct')
