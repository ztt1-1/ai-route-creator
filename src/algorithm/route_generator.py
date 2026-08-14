
class RouteGenerator:

    def __init__(self, route_service):
        self.ors_service = route_service

    def generate_small_loop_sec1(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        #scenario 1 code
        #0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.000725 * offset
            offset_long = 0.000875 * offset



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
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_long_loop_sec1(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 1 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0
        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.00145 * offset
            offset_long = 0.00175 * offset

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
                offset += 1
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.34
            if distance_miles >= target_distance:
                return route_data
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_longer_loop_sec1(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 1 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0
        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0029 * offset
            offset_long = 0.0035 * offset

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
                offset += 1
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.34

            if distance_miles >= target_distance:
                return route_data
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_super_loop_sec1(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 1 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0
        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0058 * offset
            offset_long = 0.007 * offset

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
                offset += 1
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.

            if distance_miles >= target_distance:
                return route_data
            if target_distance - distance_miles < 0.25:
                return route_data
            attempts += 1
            offset += 1

    def generate_ultra_loop_sec1(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 1 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0
        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0116 * offset
            offset_long = 0.014 * offset

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
                offset += 1
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.34

            if distance_miles >= target_distance:
                return route_data
            if target_distance - distance_miles < 3:
                return route_data
            attempts += 1
            offset += 1




    def generate_small_loop_sec2(self, origin_lat, origin_long, target_distance):

        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 2 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.000725 * offset
            offset_long = 0.000875 * offset

            origin = [origin_long, origin_lat]

            north_pt = [origin_long, origin_lat + offset_lat]
            south_pt = [origin_long, origin_lat - offset_lat]

            northeast_pt = [origin_long + offset_long, origin_lat + offset_lat]
            southeast_pt = [origin_long + offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                north_pt,
                northeast_pt,
                southeast_pt,
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
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_long_loop_sec2(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 2 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0
        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.00145 * offset
            offset_long = 0.00175 * offset

            origin = [origin_long, origin_lat]

            north_pt = [origin_long, origin_lat + offset_lat]
            south_pt = [origin_long, origin_lat - offset_lat]

            northeast_pt = [origin_long + offset_long, origin_lat + offset_lat]
            southeast_pt = [origin_long + offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                north_pt,
                northeast_pt,
                southeast_pt,
                south_pt,
                origin
            ]

            data = {
                "coordinates": route_points
            }

            route_data = self.ors_service.ors_get_route(data)

            if route_data is None:
                print("Invalid route at offset")
                offset += 1
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.34
            if distance_miles >= target_distance:
                return route_data
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_longer_loop_sec2(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 2 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0
        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0029 * offset
            offset_long = 0.0035 * offset

            origin = [origin_long, origin_lat]

            north_pt = [origin_long, origin_lat + offset_lat]
            south_pt = [origin_long, origin_lat - offset_lat]

            northeast_pt = [origin_long + offset_long, origin_lat + offset_lat]
            southeast_pt = [origin_long + offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                north_pt,
                northeast_pt,
                southeast_pt,
                south_pt,
                origin
            ]

            data = {
                "coordinates": route_points
            }

            route_data = self.ors_service.ors_get_route(data)

            if route_data is None:
                print("Invalid route at offset")
                offset += 1
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.34

            if distance_miles >= target_distance:
                return route_data
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_super_loop_sec2(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 2 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0
        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0058 * offset
            offset_long = 0.007 * offset

            origin = [origin_long, origin_lat]

            north_pt = [origin_long, origin_lat + offset_lat]
            south_pt = [origin_long, origin_lat - offset_lat]

            northeast_pt = [origin_long + offset_long, origin_lat + offset_lat]
            southeast_pt = [origin_long + offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                north_pt,
                northeast_pt,
                southeast_pt,
                south_pt,
                origin
            ]

            data = {
                "coordinates": route_points
            }

            route_data = self.ors_service.ors_get_route(data)

            if route_data is None:
                print("Invalid route at offset")
                offset += 1
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.

            if distance_miles >= target_distance:
                return route_data
            if target_distance - distance_miles < 0.25:
                return route_data
            attempts += 1
            offset += 1

    def generate_ultra_loop_sec2(self, origin_lat, origin_long, target_distance):
        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 2 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0
        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0116 * offset
            offset_long = 0.014 * offset

            origin = [origin_long, origin_lat]

            north_pt = [origin_long, origin_lat + offset_lat]
            south_pt = [origin_long, origin_lat - offset_lat]

            northeast_pt = [origin_long + offset_long, origin_lat + offset_lat]
            southeast_pt = [origin_long + offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                north_pt,
                northeast_pt,
                southeast_pt,
                south_pt,
                origin
            ]

            data = {
                "coordinates": route_points
            }

            route_data = self.ors_service.ors_get_route(data)

            if route_data is None:
                print("Invalid route at offset")
                offset += 1
                continue

            distance_meters = route_data['routes'][0]['summary']['distance']
            distance_miles = distance_meters / 1609.34

            if distance_miles >= target_distance:
                return route_data
            if target_distance - distance_miles < 3:
                return route_data
            attempts += 1
            offset += 1






    def generate_small_loop_sec3(self, origin_lat, origin_long, target_distance):

        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 3 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.000725 * offset
            offset_long = 0.000875 * offset

            origin = [origin_long, origin_lat]

            west_pt = [origin_long - offset_long, origin_lat]
            east_pt = [origin_long + offset_long, origin_lat]

            northwest_pt = [origin_long - offset_long, origin_lat + offset_lat]
            northeast_pt = [origin_long + offset_long, origin_lat + offset_lat]

            route_points = [
                origin,
                west_pt,
                northwest_pt,
                northeast_pt,
                east_pt,
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
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_long_loop_sec3(self, origin_lat, origin_long, target_distance):

        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 3 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.00145 * offset
            offset_long = 0.00175 * offset

            origin = [origin_long, origin_lat]

            west_pt = [origin_long - offset_long, origin_lat]
            east_pt = [origin_long + offset_long, origin_lat]

            northwest_pt = [origin_long - offset_long, origin_lat + offset_lat]
            northeast_pt = [origin_long + offset_long, origin_lat + offset_lat]

            route_points = [
                origin,
                west_pt,
                northwest_pt,
                northeast_pt,
                east_pt,
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
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_longer_loop_sec3(self, origin_lat, origin_long, target_distance):

        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 3 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0029 * offset
            offset_long = 0.0035 * offset

            origin = [origin_long, origin_lat]

            west_pt = [origin_long - offset_long, origin_lat]
            east_pt = [origin_long + offset_long, origin_lat]

            northwest_pt = [origin_long - offset_long, origin_lat + offset_lat]
            northeast_pt = [origin_long + offset_long, origin_lat + offset_lat]

            route_points = [
                origin,
                west_pt,
                northwest_pt,
                northeast_pt,
                east_pt,
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
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_super_loop_sec3(self, origin_lat, origin_long, target_distance):

        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 3 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0058 * offset
            offset_long = 0.007 * offset

            origin = [origin_long, origin_lat]

            west_pt = [origin_long - offset_long, origin_lat]
            east_pt = [origin_long + offset_long, origin_lat]

            northwest_pt = [origin_long - offset_long, origin_lat + offset_lat]
            northeast_pt = [origin_long + offset_long, origin_lat + offset_lat]

            route_points = [
                origin,
                west_pt,
                northwest_pt,
                northeast_pt,
                east_pt,
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
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_ultra_loop_sec3(self, origin_lat, origin_long, target_distance):

        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")
        # scenario 3 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0116 * offset
            offset_long = 0.014 * offset

            origin = [origin_long, origin_lat]

            west_pt = [origin_long - offset_long, origin_lat]
            east_pt = [origin_long + offset_long, origin_lat]

            northwest_pt = [origin_long - offset_long, origin_lat + offset_lat]
            northeast_pt = [origin_long + offset_long, origin_lat + offset_lat]

            route_points = [
                origin,
                west_pt,
                northwest_pt,
                northeast_pt,
                east_pt,
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
            if target_distance - distance_miles < 3:
                return route_data

            attempts += 1
            offset += 1




    def generate_small_loop_sec4(self, origin_lat, origin_long, target_distance):

        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")

        # scenario 4 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.000725 * offset
            offset_long = 0.000875 * offset

            origin = [origin_long, origin_lat]

            west_pt = [origin_long - offset_long, origin_lat]
            east_pt = [origin_long + offset_long, origin_lat]

            southwest_pt = [origin_long - offset_long, origin_lat - offset_lat]
            southeast_pt = [origin_long + offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                west_pt,
                southwest_pt,
                southeast_pt,
                east_pt,
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
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_long_loop_sec4(self, origin_lat, origin_long, target_distance):

        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")

        # scenario 4 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.00145 * offset
            offset_long = 0.00175 * offset

            origin = [origin_long, origin_lat]

            west_pt = [origin_long - offset_long, origin_lat]
            east_pt = [origin_long + offset_long, origin_lat]

            southwest_pt = [origin_long - offset_long, origin_lat - offset_lat]
            southeast_pt = [origin_long + offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                west_pt,
                southwest_pt,
                southeast_pt,
                east_pt,
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
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_longer_loop_sec4(self, origin_lat, origin_long, target_distance):

        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")

        # scenario 4 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0029 * offset
            offset_long = 0.0035 * offset

            origin = [origin_long, origin_lat]

            west_pt = [origin_long - offset_long, origin_lat]
            east_pt = [origin_long + offset_long, origin_lat]

            southwest_pt = [origin_long - offset_long, origin_lat - offset_lat]
            southeast_pt = [origin_long + offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                west_pt,
                southwest_pt,
                southeast_pt,
                east_pt,
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
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_super_loop_sec4(self, origin_lat, origin_long, target_distance):

        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")

        # scenario 4 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0058 * offset
            offset_long = 0.007 * offset

            origin = [origin_long, origin_lat]

            west_pt = [origin_long - offset_long, origin_lat]
            east_pt = [origin_long + offset_long, origin_lat]

            southwest_pt = [origin_long - offset_long, origin_lat - offset_lat]
            southeast_pt = [origin_long + offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                west_pt,
                southwest_pt,
                southeast_pt,
                east_pt,
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
            if target_distance - distance_miles < 0.25:
                return route_data

            attempts += 1
            offset += 1

    def generate_ultra_loop_sec4(self, origin_lat, origin_long, target_distance):

        if target_distance <= 0:
            raise ValueError("Target distance must be greater than 0")

        # scenario 4 code
        # 0.002187 degrees ~= 0.15mi
        offset = 1
        distance_miles = 0

        max_attempts = 15
        attempts = 0

        while distance_miles < target_distance and attempts < max_attempts:

            offset_lat = 0.0116 * offset
            offset_long = 0.014 * offset

            origin = [origin_long, origin_lat]

            west_pt = [origin_long - offset_long, origin_lat]
            east_pt = [origin_long + offset_long, origin_lat]

            southwest_pt = [origin_long - offset_long, origin_lat - offset_lat]
            southeast_pt = [origin_long + offset_long, origin_lat - offset_lat]

            route_points = [
                origin,
                west_pt,
                southwest_pt,
                southeast_pt,
                east_pt,
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
            if target_distance - distance_miles < 3:
                return route_data

            attempts += 1
            offset += 1