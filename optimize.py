#import time

def get_gas_cost():
    """
    get gas cost from oracle
    current a placeholder
    """
    return 10

def get_optimal_trades(input_amount, prices, gas_cost):
    n_trades = 1
    optimal_output = 0
    
    for i,price_ in enumerate(prices):

        output_ = input_amount * price_
        cost_ = (i+1) * gas_cost
        output_ -=  cost_
        
        #print(i, cost_, output_)
        
        if output_ > optimal_output:
            n_trades = i + 1
            optimal_output = output_
            
    return n_trades, optimal_output

def get_optimal_interval():
    """
    get optimal interval between trades in minutes
    currently work as a placeholder
    """
    return 5

def optimize(input_amount: float, prices: list):
    """
    main optimization function
    input_amount: input token value in USD
    prices: a list of prices with different input_anount, the i-th-entry is the price corresponding to input_amount / i 
    
    currently using simple gas and interval 
    """
    gas_cost = get_gas_cost()
    n_trades, optimal_output = get_optimal_trades(input_amount, prices, gas_cost)
    interval = get_optimal_interval()
    
    return n_trades, interval, optimal_output
    

if __name__ == '__main__':
    input_amount = 1e6
    prices = [0.995, 0.996, 0.997, 0.998, 0.999]
    
    print(optimize(input_amount, prices))