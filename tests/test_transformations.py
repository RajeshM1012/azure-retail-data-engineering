import pytest

def test_required_columns():
    required = {"transaction_id", "quantity", "unit_price"}
    actual = {"transaction_id", "quantity", "unit_price", "sale_date"}
    assert required.issubset(actual)

def test_total_amount_logic():
    quantity = 3
    unit_price = 2500
    assert quantity * unit_price == 7500
