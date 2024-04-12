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
