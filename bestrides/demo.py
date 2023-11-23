def get_airport_fare(city, distance, vehicle_type, discount=0):
    base_fares = {
        (5, 10): 25,
        (11, 15): 45,
        (16, 25): 65,
        (26, 35): 79,
        (36, 45): 121,
        (46, float('inf')): 2 * distance
    }

    for distance_range, fare in base_fares.items():
        if distance_range[0] <= distance <= distance_range[1]:
            total_fare = fare
            break

    if vehicle_type == 'sedan':
        total_fare += 500
    elif vehicle_type == "suv":
        total_fare += 750

    total_fare -= total_fare * (discount / 100)

    return total_fare
