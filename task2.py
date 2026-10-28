# Fuel Consumption and Route Comparison

vehicles = []

n = int(input("Enter number of vehicles: "))

distance = float(input("Enter journey distance (km): "))
fuel_price = float(input("Enter fuel price per litre: "))
reserve = float(input("Enter reserve fuel (litres): "))

for i in range(n):

    print("\nEnter Vehicle Details")

    name = input("Enter vehicle name: ")
    mileage = float(input("Enter mileage (km/litre): "))

    fuel = distance / mileage
    total_fuel = fuel + reserve
    cost = fuel * fuel_price

    vehicles.append([name, total_fuel, cost])

# Display results
print("\n--- VEHICLE COMPARISON ---")

for v in vehicles:
    print("\nVehicle:", v[0])
    print("Fuel Required:", round(v[1], 2), "litres")
    print("Journey Cost: Rs.", round(v[2], 2))

# Find lowest cost vehicle
best = min(vehicles, key=lambda x: x[2])

print("\n--- BEST OPTION ---")
print("Vehicle:", best[0])
print("Lowest Cost: Rs.", round(best[2], 2))