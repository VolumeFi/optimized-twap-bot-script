# Twap Optimizer

## Overview

This Python script finds the optimal number of trades to maximize the output value based on a given input amount and a set of prices. It also takes into account the gas costs for each trade. The optimal interval between trades is also calculated but currently serves as a placeholder.

## Requirements

- Python 3.x

## How to Run

1. Save the Python script in a file, for example `trade_optimizer.py`.

2. Open your terminal or command prompt.

3. Run the script with the `--input_amount` and `--prices` parameters. For example:

    ```bash
    python trade_optimizer.py --input_amount 1e6 --prices 0.995 0.996 0.997 0.998 0.999
    ```

## Arguments

- `--input_amount`: The input amount in USD that you are willing to trade.
  
- `--prices`: A list of prices corresponding to different input amounts. The i-th entry is the price corresponding to `input_amount / i`.

## Functionality

- `get_gas_cost()`: Placeholder function to get the gas cost. Currently returns a fixed value.

- `get_optimal_trades(input_amount, prices, gas_cost)`: Calculates the optimal number of trades and the resulting output amount.

- `get_optimal_interval()`: Placeholder function that returns the optimal time interval between trades in minutes.

- `optimize(input_amount: float, prices: list)`: Main function that returns the optimal number of trades, the interval, and the optimal output.

## Output

The script outputs a tuple containing the optimal number of trades, the interval between trades, and the optimal output amount.
