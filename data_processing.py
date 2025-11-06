import csv, os

__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

cities = []
with open(os.path.join(__location__, 'Cities.csv')) as f:
    rows = csv.DictReader(f)
    for r in rows:
        cities.append(dict(r))

def filter(condition, dict_list):
    return [item for item in dict_list if condition(item)]

def aggregate(aggregation_key, aggregation_function, dict_list):
    values = [float(item[aggregation_key]) for item in dict_list]
    return aggregation_function(values)

avg_temp = aggregate("temperature", lambda x: sum(x) / len(x), cities)
print("The average temperature of all the cities:", avg_temp)
print()

germany_cities = filter(lambda c: c["country"].lower() == "germany", cities)
print("All cities in Germany:")
for c in germany_cities:
    print(c)
print()

spain_hot = filter(lambda c: c["country"].lower() == "spain" and float(c["temperature"]) > 12, cities)
print("Cities in Spain with temperature above 12°C:")
for c in spain_hot:
    print(c["city"])
print()

unique_countries = set([c["country"].lower() for c in cities])
print("Number of unique countries:", len(unique_countries))
print()

avg_germany_temp = aggregate("temperature", lambda x: sum(x)/len(x), germany_cities)
print("Average temperature for all the cities in Germany:", avg_germany_temp)
print()

italy_cities = filter(lambda c: c["country"].lower() == "italy", cities)
max_italy_temp = aggregate("temperature", max, italy_cities)
print("Max temperature for all the cities in Italy:", max_italy_temp)
print()