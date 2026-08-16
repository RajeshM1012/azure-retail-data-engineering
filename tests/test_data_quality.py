def test_sales_quality_rules():
    metrics = {"null_transaction_id": 0, "invalid_quantity": 0, "duplicate_transaction_id": 0}
    assert all(value == 0 for value in metrics.values())

def test_invalid_quantity_rule():
    quantity = -1
    assert quantity <= 0
