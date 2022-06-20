# def flights(*args):
#     flight = {}
#     destination = []
#     people = []
#     for i in args:
#         if i == 'Finish':
#             break
#         elif isinstance(i, int):
#             people.append(i)
#         else:
#             destination.append(i)
#     for i in range(len(destination)):
#         if destination[i] not in flight:
#
#             flight[destination[i]] = people[i]
#         else:
#             flight[destination[i]] += people[i]
#     return flight


def flights(*args):
    flights_dict = {}
    for i in range(0, len(args) - 1, 2):
        destination = args[i]
        passengers = args[i + 1]

        if destination == 'Finish':
            return flights_dict
        else:
            if destination not in flights_dict:
                flights_dict[destination] = 0
            flights_dict[destination] += int(passengers)

    return flights_dict


print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))
