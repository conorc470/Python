from ryotest import *

eur_coins = [200, 100, 50, 20, 10, 5, 2, 1]
us_coins = [100, 50, 25, 10, 5, 1]


def get_change(amount, coins = eur_coins):
    change = []
    
    for coin in coins:
        while coin <= amount:
            amount -= coin
        change.append(coin)

    return change

assert get_change(1) == [1], "1 cent change should return a 1 cent coin"
assert (get_change(2),[2])
assert (get_change(5),[5])
assert (get_change(10),[10])
assert (get_change(20),[20])
assert (get_change(50),[50])
assert (get_change(100),[100])

print("All tests pass")