city = []
for i in range(5):
    city_name = input("Enter a city name: ")
    city.append(city_name)


print("Cities:", city)

print("Length of the array:", len(city))

city.append("Hong")
print("Updated Cities:", city)

city.pop(0)
print("Cities after removing the first element:", city)

city.reverse()
print("Reversed array:", city)