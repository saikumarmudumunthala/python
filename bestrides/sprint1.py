def get_airport_fare(city, distance, vehicle_type, discount=0):
    #city = 'hyderabad'
    fare = 0
    if 5 <=  distance <= 10:
        fare = 25
    elif 10 < distance <= 15:
        fare = 45
    elif 15 < distance <= 25:
        fare = 65
    elif 25 < distance <= 35:
        fare = 79
    elif 35 < distance <= 45:
        fare = 121
    elif 45 < distance <= 55:
        fare = 154
    else:
        fare = 2 * distance

    total_fare =  fare
    print("The distance fare: ", total_fare)
    if vehicle_type == 'sedan':
        total_fare += 500
    elif vehicle_type == "suv":
        total_fare += 750
    
    print("Adding vehicletype fare: ", total_fare)


    total_fare -= total_fare * (discount / 100)            
    print("The discount fare: ", total_fare)
    return total_fare  



city = "hyderabad"
distance = 20
vehicle_type = "mini"
discount = 0

fare = get_airport_fare(city, distance, vehicle_type, discount)
print("The total fare: ", fare)