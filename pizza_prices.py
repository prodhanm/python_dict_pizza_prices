import sys

pizza_prices = {
    "Cheese Pizza" : 11.99,
    "Pepperoni Pizza" : 14.99,
    "Chicken Pizza" : 13.99,
    "Hawaiian Pizza" : 12.99,
    "Meat Pizza" : 16.99
}

def new_prices(pizza_prices):
    for pizza, prices in pizza_prices.items():
        pizza_prices[pizza] = round(prices * 1.15, 2)
    return pizza_prices

def main():
    print(new_prices(pizza_prices))

if __name__ == "__main__":
    main()