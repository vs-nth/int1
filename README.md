You work for a company that leases bikes. Users can rent a bike via their mobile phone.

Your job today is to assign a bike to each user of your application.

There will always be at least as many bikes as users.

Positions are expressed on a traditional grid with (x, y) coordinates: (0, 0) would be the bottom left of the grid and (0, 1) the space above.

Any position can hold at most one user or bike.


You are given a list of users and a list of bikes.

Assign each user the closest bike closest to them, using Manhattan distances.

Users are handled on a “first come, first serve” basis, meaning that an earlier user will get the bike closest to them assigned with no regard to later users.


The output produced by your program should be a bike assignment in the form of a list of user-bikes pairings.


For example:

given a list of users: [(0, 0), (1, 1), (2, 0)] (3 users at different positions)

and a list of bikes: [(1, 0), (2, 2), (2, 1)]

the output would be: [((0, 0) , (1, 0)), ((1, 1), (2, 1)), ((2, 0), (2, 2))]

In other words, first user was assigned the first bike, second user was assigned the  third bike, and third user was assigned the second bike.
