
class RouteGenerator:

    def __init__(self, route_service):
        self.ors_service = route_service

    def generate_small_loop(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        #scenario 1 code
        #0.002187 degrees ~= 0.15mi
        distance_miles = 0
        offset_lat = 0.000725
        offset_long = 0.000875
        max_attempts = 20
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            attempts += 1

            origin = [origin_long, origin_lat]

            north_pt = [origin_long, origin_lat+offset_lat]
            south_pt = [origin_long, origin_lat-offset_lat]

            northwest_pt = [origin_long-offset_long, origin_lat+offset_lat]
            southwest_pt = [origin_long-offset_long, origin_lat-offset_lat]

            route_points = [
                origin,
                north_pt,
                northwest_pt,
                southwest_pt,
                south_pt,
                origin
            ]

            data = {
            "coordinates": route_points
            }

            route_data = self.ors_service.ors_get_route(data)

            if route_data is None:
                print("Invalid route at offset")
                offset_lat += 0.000725
                offset_long += 0.000875
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.34
            if distance_miles >= target_distance:
                return route_data

            offset_lat += 0.000725
            offset_long += 0.000875

    def generate_long_loop(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 1 code
        # 0.002187 degrees ~= 0.15mi
        distance_miles = 0
        offset_lat = 0.00145
        offset_long = 0.00175
        while distance_miles < target_distance:

            origin = [origin_long, origin_lat]

            north_pt = [origin_long, origin_lat + offset_lat]
            south_pt = [origin_long, origin_lat - offset_lat]

            northwest_pt = [origin_long - offset_long, origin_lat + offset_lat]
            southwest_pt = [origin_long - offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                north_pt,
                northwest_pt,
                southwest_pt,
                south_pt,
                origin
            ]

            data = {
                "coordinates": route_points
            }

            route_data = self.ors_service.ors_get_route(data)

            if route_data is None:
                print("Invalid route at offset")
                offset_lat += 0.00145
                offset_long += 0.00175
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.34
            if distance_miles >= target_distance:
                return route_data

            offset_lat += 0.00145
            offset_long += 0.00175

    def generate_longer_loop(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 1 code
        # 0.002187 degrees ~= 0.15mi
        distance_miles = 0
        offset_lat = 0.0029
        offset_long = 0.0035
        while distance_miles < target_distance:

            origin = [origin_long, origin_lat]

            north_pt = [origin_long, origin_lat + offset_lat]
            south_pt = [origin_long, origin_lat - offset_lat]

            northwest_pt = [origin_long - offset_long, origin_lat + offset_lat]
            southwest_pt = [origin_long - offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                north_pt,
                northwest_pt,
                southwest_pt,
                south_pt,
                origin
            ]

            data = {
                "coordinates": route_points
            }

            route_data = self.ors_service.ors_get_route(data)

            if route_data is None:
                print("Invalid route at offset")
                offset_lat += 0.0029
                offset_long += 0.0035
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.34

            if distance_miles >= target_distance:
                return route_data

            offset_lat += 0.0029
            offset_long += 0.0035

    def generate_super_loop(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 1 code
        # 0.002187 degrees ~= 0.15mi
        distance_miles = 0
        offset_lat = 0.0058
        offset_long = 0.007
        while distance_miles < target_distance:

            origin = [origin_long, origin_lat]

            north_pt = [origin_long, origin_lat + offset_lat]
            south_pt = [origin_long, origin_lat - offset_lat]

            northwest_pt = [origin_long - offset_long, origin_lat + offset_lat]
            southwest_pt = [origin_long - offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                north_pt,
                northwest_pt,
                southwest_pt,
                south_pt,
                origin
            ]

            data = {
                "coordinates": route_points
            }

            route_data = self.ors_service.ors_get_route(data)

            if route_data is None:
                print("Invalid route at offset")
                offset_lat += 0.0058
                offset_long += 0.007
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.

            if distance_miles >= target_distance:
                return route_data

            offset_lat += 0.0058
            offset_long += 0.007

    def generate_ultra_loop(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 1 code
        # 0.002187 degrees ~= 0.15mi
        distance_miles = 0
        offset_lat = 0.0116
        offset_long = 0.014
        while distance_miles < target_distance:

            origin = [origin_long, origin_lat]

            north_pt = [origin_long, origin_lat + offset_lat]
            south_pt = [origin_long, origin_lat - offset_lat]

            northwest_pt = [origin_long - offset_long, origin_lat + offset_lat]
            southwest_pt = [origin_long - offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                north_pt,
                northwest_pt,
                southwest_pt,
                south_pt,
                origin
            ]

            data = {
                "coordinates": route_points
            }

            route_data = self.ors_service.ors_get_route(data)

            if route_data is None:
                print("Invalid route at offset")
                offset_lat += 0.0116
                offset_long += 0.014
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.34

            if distance_miles >= target_distance:
                return route_data

            offset_lat += 0.0116
            offset_long += 0.014