import datetime
import csv
from collections import defaultdict

def read_product_data(filename, product_name):
    # Read data from the file and store information about prices by date for the specified product
    product_prices = defaultdict(list)
    with open(filename, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            name, date_str, price = row
            if name == product_name:
                date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()
                price = float(price)
                product_prices[date].append(price)
    
    return product_prices

product_name = "Товар А"
filename = "data.txt"
prices = read_product_data(filename, product_name)