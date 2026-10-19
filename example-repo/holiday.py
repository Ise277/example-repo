'''
Holiday Cost Calculator
Calculates holiday's cost, fight, car rental and hotel
Suported cities: Cape Town, Jozi(Johannesburg) and Durban
'''

'''
#Rate: cost per night
#nights: number of nights spent at hotel
#return hotel total cost
'''


def hotel_cost(rate, nights):

    return rate * nights


'''
rent: Cost per day
days: number of days renting
return car rental total cost
'''


def car_rental(rent, days):

    return rent * days


'''
return cost for given cities
city: name of destination
'''


def plane_cost(city):

    if city.lower() == "cape town":
        return 1500
    elif city.lower() == "jozi":
        return 1000
    elif city.lower() == "durban":
        return 1200
    else:
        0


'''
total cost of the holiday using the all components:
hotel, car rental and fight destination
'''


def holiday_cost(city, nights, days):

    hotel = hotel_cost(750, nights)
    car = car_rental(850, days)
    flight = plane_cost(city)

    total = hotel + car + flight

    return total


# Program intruction
print(
    "Calculate the total holiday cost"
    "flight, car rental and hotel prices"
    "only supported is Cape Town, Jozi(Johanneseburg) and Durban"
    )
print()

# Step1 get valid city from user
city = input(
    "Choose the city you're going to fly to (Cape Town/Jozi/Durban): "
).lower()
while city not in ["cape town", "jozi", "durban"]:
    city = input("Invalid input! Please choose (Cape Town/Jozi/Durban): ")

# Step2 get number of nights
nights = int(input("How many nights you'll be staying at a hotel: "))

# Step3 get number of days renting a car
days = int(input("Number of days you'll renting a car: "))

# Step4 Display total cost
print()
print(
    "Total cost of the Holiday is R ",
    holiday_cost(city, nights, days)
)
