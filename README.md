 Lab Overview
This lab focuses on transforming procedural-style Python code into an object-oriented (OOP) design.
The goal is to encapsulate data operations and CSV file handling into well-defined classes that make the code more modular, reusable, and easier to maintain.

 Project Structure
oop_lab_2/
│
├── README.md              # Project documentation
├── Cities.csv             # Dataset used in the analysis
└── data_processing.py     # Main Python program (OOP version)

Design Overview
1. Class: DataLoader
Responsible for loading a CSV file and converting it into a Table object.
Attributes
filename: the name of the CSV file to load
location: absolute path to the file directory
Methods
load() → Reads the CSV file and returns a Table object containing the data.
2. Class: Table
Represents a dataset (like a CSV table) as a list of dictionaries.
Each dictionary corresponds to one row.
Attributes
rows: list of dictionaries representing table data
Methods
filter(condition) → returns a new Table with rows that satisfy the given condition
aggregate(key, func) → applies an aggregation function (e.g. sum, max, average) on a column
unique(key) → returns a set of unique values from a given column
__repr__() → displays summary info of the table

Example Operations
After loading the dataset, the following operations are demonstrated:
Compute the average temperature of all cities
Find all cities in Germany
List Spanish cities with temperature above 12°C
Count the number of unique countries
Find average temperature in Germany
Find the maximum temperature in Italy

How to Run
Place the Cities.csv file in the same directory as data_processing.py.
Run the script:
python data_processing.py
The program will display analysis results in the console, such as:
Average temperature of all cities
Cities filtered by country
Aggregated temperature data
