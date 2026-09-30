from solution.classes.stock import Stock


def test_market_value():

    stock = Stock(
        symbol="META",
        price=100,
        quantity=10,
        target_allocation=1.0
    )

    assert stock.market_value == 1000


def test_update_price():

    stock = Stock(
        symbol="META",
        price=100,
        quantity=10,
        target_allocation=1.0
    )

    stock.current_price(150)

    assert stock.price == 150
    assert stock.market_value == 1500


def test_buy_stock():

    stock = Stock(
        symbol="META",
        price=100,
        quantity=10,
        target_allocation=1.0
    )

    stock.buy_stock(5)

    assert stock.quantity == 15


def test_sell_stock_partial_quantity():

    stock = Stock(
        symbol="META",
        price=100,
        quantity=10,
        target_allocation=1.0
    )

    stock.sell_stock(3)

    assert stock.quantity == 7


def test_sell_stock_all_quantity():

    stock = Stock(
        symbol="META",
        price=100,
        quantity=10,
        target_allocation=1.0
    )

    stock.sell_stock(10)

    assert stock.quantity == 0


def test_sell_stock_more_than_available_quantity():

    stock = Stock(
        symbol="META",
        price=100,
        quantity=10,
        target_allocation=1.0
    )

    stock.sell_stock(20)

    assert stock.quantity == 0


def test_market_value_after_buy():

    stock = Stock(
        symbol="META",
        price=100,
        quantity=10,
        target_allocation=1.0
    )

    stock.buy_stock(5)

    assert stock.market_value == 1500


def test_market_value_after_sell():

    stock = Stock(
        symbol="META",
        price=100,
        quantity=10,
        target_allocation=1.0
    )

    stock.sell_stock(5)

    assert stock.market_value == 500
