#Trip Expenditure
#Write a program to calculate the total trip expenditure. Calculate the hotel cost per day, calculate the plane cost, and price of vehicle rented during trip.
#define  a function called hotel_cost, with 1 argument "nights" as input
def hotel_cost(nights):
    return 140*nights
def plane_ride_cost(city):
    if "Baku"==city:
        return 183
    elif "Moscow"==city:
        return 220
    elif "Delhi"==city:
        return 222
    elif "Cairo"==city:
        return 475
def rental_car_cost(days):
    if days>=7:
        return 40*days-50
    elif days>=3:
        return 40*days-20
    else:
        return 40*days
def trip_cost(city, days, spending_money):
    return rental_car_cost(days)+hotel_cost(days)+plane_ride_cost(city)+spending_money
print("Cost of car rental: ", rental_car_cost(5))
print("Cost of plane ride: ", plane_ride_cost("Baku"))
print("Cost of hotel room: ", hotel_cost(7))
print("Total cost of trip: ", trip_cost("Baku",7,7500))
print(trip_cost("Delhi",2, 6500))