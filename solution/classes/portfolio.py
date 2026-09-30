from solution.classes.stock import Stock
from solution.classes.recommendation import Recommendation, Action
from dataclasses import dataclass

@dataclass
class Portfolio:
    """
    Represents a portfolio of stocks with target allocations.
    """
    stocks: list[Stock]

    def __post_init__(self):
        target_sum = sum(
            stock.target_allocation
            for stock in self.stocks
        )

        if target_sum != 1:
            raise ValueError("Total allocation must be 1")
    
    def search_stock(self, symbol: str) -> Stock | None:
        """
        Search for a stock in the portfolio by its symbol.
        Returns the Stock object if found, otherwise None.
        """
        for stock in self.stocks:
            if stock.symbol == symbol:
                return stock
        return None

    def total_value(self) -> float:
        """
        Calculate the total value of the portfolio.
        """
        return sum(
            stock.market_value
            for stock in self.stocks
        )
    
    def rebalance(self) -> list[Recommendation]:
        """
        Rebalance the portfolio based on the target allocations.
        Returns a list of recommendations for buying or selling stocks.
        """
        # Calculate the total value of the portfolio
        total_portfolio_value = self.total_value()
        recommendations = []

        # Calculate the current allocation and compare it with the target allocation
        for stock in self.stocks:
            current_value = stock.market_value if stock else 0
            target_value = total_portfolio_value * stock.target_allocation

            difference = target_value - current_value

            # If the difference is positive, we need to buy stock
            if difference > 0:
                recommendations.append(
                    Recommendation(
                        Action.BUY,
                        stock.symbol,
                        abs(difference)
                    )
                )
            
            # If the difference is negative, we need to sell stock
            elif difference < 0:
                recommendations.append(
                    Recommendation(
                        Action.SELL,
                        stock.symbol,
                        abs(difference)
                    )
                )
        
        return recommendations
