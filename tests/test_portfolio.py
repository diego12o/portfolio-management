import pytest

from solution.classes.portfolio import Portfolio
from solution.classes.stock import Stock
from solution.classes.recommendation import Action


def test_empty_portfolio_is_invalid():

    with pytest.raises(ValueError):
        Portfolio(stocks=[])


def test_single_stock_with_100_percent_allocation():

    portfolio = Portfolio(
        stocks=[
            Stock(
                symbol="META",
                price=100,
                quantity=10,
                target_allocation=1.0
            )
        ]
    )

    recommendations = portfolio.rebalance()

    assert recommendations == []


def test_total_value_with_multiple_stocks():

    portfolio = Portfolio(
        stocks=[
            Stock("META", 100, 10, 0.3),
            Stock("AAPL", 200, 5, 0.3),
            Stock("MSFT", 500, 2, 0.4)
        ]
    )

    assert portfolio.total_value() == 3000


def test_search_stock_is_case_sensitive():

    portfolio = Portfolio(
        stocks=[
            Stock("META", 100, 10, 1.0)
        ]
    )

    assert portfolio.search_stock("meta") is None


def test_search_stock_returns_same_instance():

    portfolio = Portfolio(
        stocks=[
            Stock("META", 100, 10, 1.0)
        ]
    )

    stock = portfolio.search_stock("META")

    assert stock is portfolio.stocks[0]


def test_rebalance_generates_only_buy_recommendation():

    portfolio = Portfolio(
        stocks=[
            Stock("META", 100, 2, 0.8),   # 200
            Stock("AAPL", 100, 8, 0.2)    # 800
        ]
    )

    recommendations = portfolio.rebalance()

    buy_recommendations = [
        r for r in recommendations
        if r.action == Action.BUY
    ]

    assert len(buy_recommendations) == 1
    assert buy_recommendations[0].symbol == "META"


def test_rebalance_generates_only_sell_recommendation():

    portfolio = Portfolio(
        stocks=[
            Stock("META", 100, 8, 0.2),   # 800
            Stock("AAPL", 100, 2, 0.8)    # 200
        ]
    )

    recommendations = portfolio.rebalance()

    sell_recommendations = [
        r for r in recommendations
        if r.action == Action.SELL
    ]

    assert len(sell_recommendations) == 1
    assert sell_recommendations[0].symbol == "META"


def test_rebalance_recommendation_amount():

    portfolio = Portfolio(
        stocks=[
            Stock("META", 100, 10, 0.4),
            Stock("AAPL", 200, 5, 0.6)
        ]
    )

    recommendations = portfolio.rebalance()

    meta = next(
        r for r in recommendations
        if r.symbol == "META"
    )

    aapl = next(
        r for r in recommendations
        if r.symbol == "AAPL"
    )

    assert meta.amount == 200
    assert aapl.amount == 200


def test_allocation_less_than_one_fails():

    with pytest.raises(ValueError):
        Portfolio(
            stocks=[
                Stock("META", 100, 10, 0.3),
                Stock("AAPL", 200, 5, 0.3)
            ]
        )


def test_allocation_greater_than_one_fails():

    with pytest.raises(ValueError):
        Portfolio(
            stocks=[
                Stock("META", 100, 10, 0.8),
                Stock("AAPL", 200, 5, 0.5)
            ]
        )


def test_updating_stock_affects_portfolio_value():

    portfolio = Portfolio(
        stocks=[
            Stock("META", 100, 10, 1.0)
        ]
    )

    portfolio.stocks[0].price = 200

    assert portfolio.total_value() == 2000
