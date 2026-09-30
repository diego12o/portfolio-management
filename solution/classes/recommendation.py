from dataclasses import dataclass
from enum import Enum


class Action(Enum):
    """
    Represents the action to be taken for a stock recommendation.
    """
    BUY = 1
    SELL = 2

@dataclass
class Recommendation:
    """
    Represents a recommendation to buy or sell a stock.
    """
    action: Action
    symbol: str
    amount: float
