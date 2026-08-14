def find_closest_route(target_distance, routes):
    closest_route = None
    smallest_difference = float("inf")

    for route in routes:
        difference = abs(target_distance - (route['routes'][0]['summary']['distance']/1609.34))

        if difference < smallest_difference:
            smallest_difference = difference
            closest_route = route['routes']#[0]['geometry']
            #closest_distance = route['routes'][0]['summary']['distance']/1609.34

    return closest_route