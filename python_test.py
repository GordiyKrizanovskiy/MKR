from datetime import datetime, timedelta
import pytest
from python import read_product_data, get_price_change_last_month

# Fixture for creating product data
@pytest.fixture
def product_data():
    return {
        datetime.today().date(): [100.0, 105.0],
        (datetime.today() - timedelta(days=10)).date(): [95.0],
        (datetime.today() - timedelta(days=20)).date(): [90.0]
    }

# Test for read_product_data function
def test_read_product_data():
    # This should be adjusted based on actual file and data setup
    filename = 'data.txt'
    product_name = 'Товар А'
    # Assume file handling and CSV reading are correct and focus on function logic
    assert read_product_data(filename, product_name) == product_data()

# Parametrized test for get_price_change_last_month function
@pytest.mark.parametrize("prices, expected", [
    ({datetime.today().date(): [100.0, 105.0]}, 5.0),  # Only recent prices
    ({}, 'No data available for the last month'),       # No data case
    ({(datetime.today() - timedelta(days=40)).date(): [90.0]}, 'No data available for the last month')  # Old data
])
def test_get_price_change_last_month(prices, expected):
    assert get_price_change_last_month(prices) == expected
