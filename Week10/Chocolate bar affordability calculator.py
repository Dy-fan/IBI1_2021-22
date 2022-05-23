def chocolate_cal(money, price):
    """
    input: money, price; all positive int
    calculate the number of bars can buy and the change left
    return None
    """
    bar_number = money // price  # get the result of integer division
    change = money % price  # get the remainder of the division
    print(f'{bar_number} chocolate bars can be bought and {change}$ will be left over')
    return


# example of using the function
total_money = 100
Price = 7
chocolate_cal(total_money, Price)

