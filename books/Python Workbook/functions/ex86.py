# exercise 86: Taxi Fare

def compute_taxi_fare(distance_km):
    base_fare = 4
    variable_fare = 0.25  # 0.25 every 140 mt
    distance_m = distance_km * 1000
    variable_cost = variable_fare * (distance_m // 140)
    tot_cost = base_fare + variable_cost
    return '%.2f €' % tot_cost

def main():
    distance_km = float(input('enter distance in km: '))

    print(compute_taxi_fare(distance_km))


if __name__ == '__main__':
    main()
