import csv
import os

class DataLoader:
    def __init__(self, filename):
        self.filename = filename
        self.location = os.path.realpath(
            os.path.join(os.getcwd(), os.path.dirname(__file__))
        )

    def load(self):
        data = []
        with open(os.path.join(self.location, self.filename)) as f:
            rows = csv.DictReader(f)
            for r in rows:
                data.append(dict(r))
        return Table(data)


class Table:
    def __init__(self, rows):
        self.rows = rows

    def filter(self, condition):
        filtered_rows = [r for r in self.rows if condition(r)]
        return Table(filtered_rows)

    def aggregate(self, key, func):
        values = [float(r[key]) for r in self.rows]
        return func(values)

    def unique(self, key):
        return set([r[key].lower() for r in self.rows])

    def __repr__(self):
        return f"Table({len(self.rows)} rows)"


if __name__ == "__main__":
    loader = DataLoader("Cities.csv")
    cities = loader.load()

    avg_temp = cities.aggregate("temperature", lambda x: sum(x) / len(x))
    print("The average temperature of all the cities:", avg_temp)
    print()

    germany_cities = cities.filter(lambda c: c["country"].lower() == "germany")
    print("All cities in Germany:")
    for c in germany_cities.rows:
        print(c)
    print()

    spain_hot = cities.filter(lambda c: c["country"].lower() == "spain" and float(c["temperature"]) > 12)
    print("Cities in Spain with temperature above 12°C:")
    for c in spain_hot.rows:
        print(c["city"])
    print()

    unique_countries = cities.unique("country")
    print("Number of unique countries:", len(unique_countries))
    print()

    avg_germany_temp = germany_cities.aggregate("temperature", lambda x: sum(x)/len(x))
    print("Average temperature for all the cities in Germany:", avg_germany_temp)
    print()

    italy_cities = cities.filter(lambda c: c["country"].lower() == "italy")
    max_italy_temp = italy_cities.aggregate("temperature", max)
    print("Max temperature for all the cities in Italy:", max_italy_temp)
    print()
