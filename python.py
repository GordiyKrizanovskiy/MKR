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

def get_price_change_last_month(prices):
    # We determine the maximum and minimum price for the last month
    one_month_ago = datetime.date.today() - datetime.timedelta(days=30)
    recent_prices = {date: price for date, price in prices.items() if date >= one_month_ago}
    
    if not recent_prices:
        return "No data available for the last month"
    
    min_price = min(min(prices) for prices in recent_prices.values())
    max_price = max(max(prices) for prices in recent_prices.values())
    
    return max_price - min_price

product_name = "Товар А"
filename = "data.txt"
prices = read_product_data(filename, product_name)
price_change = get_price_change_last_month(prices)

print(f"Price change for {product_name} for the last month: {price_change} UAH")