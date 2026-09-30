# Portfolio Management

## Statement

Build a portfolio management module that:

- Maintains a collection of stocks.
- Stores a target allocation for each stock.
- Calculates portfolio rebalance recommendations.
- Indicates which stocks should be bought or sold to achieve the target allocation.

## Classes

### Stock

Represents a stock position.

Attributes:

- `symbol`
- `price`
- `quantity`
- `target_allocation`

Operations:

- Calculate market value
- Update price
- Buy shares
- Sell shares

### Portfolio

Represents a collection of stocks.

Operations:

- Search stock by symbol
- Calculate total portfolio value
- Generate rebalance recommendations

## Requirements
 
- Python 3.12+
- Poetry

## Installation

```bash
poetry install
```

## Running Tests

Run all tests:

```bash
poetry run pytest
```

## Example

```python
portfolio = Portfolio(
    stocks=[
        Stock("META", 100, 10, 0.4),
        Stock("AAPL", 200, 5, 0.6)
    ]
)

recommendations = portfolio.rebalance()
```

### Updating a stock price

```python
meta = portfolio.search_stock("META")

if meta:
    meta.current_price(120)
```

The portfolio value and rebalance recommendations will automatically use the updated stock price.
