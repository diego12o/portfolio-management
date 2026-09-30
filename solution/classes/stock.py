from dataclasses import dataclass


@dataclass
class Stock:
    """
    Represents a stock with its symbol, current price, and quantity.
    """
    symbol: str
    price: float
    quantity: int
    target_allocation: float

    @property
    def market_value(self) -> float:
        """
        Calculate the market value of the stock.
        """
        return self.price * self.quantity

    def current_price(self, current_price: float) -> None:
        """
        Update the current price of the stock.
        """
        self.price = current_price
    
    def sell_stock(self, quantity: int) -> None:
        """
        Sell a specified quantity of the stock.
        """
        if quantity >= self.quantity:
            self.quantity = 0

        self.quantity = self.quantity - quantity
    
    def buy_stock(self, quantity: int) -> None:
        """
        Buy a specified quantity of the stock.
        """
        self.quantity = self.quantity + quantity
