def find_closest_route(target_distance, routes):

    closest_route = None
    smallest_difference = float("inf") #sets smallest difference to positive infinity

    for route in routes:
        #difference of the target distance compared to the found route
        difference = abs(target_distance - (route['routes'][0]['summary']['distance']/1609.34))

        if difference < smallest_difference:
            smallest_difference = difference
            closest_route = route['routes']

    return closest_route