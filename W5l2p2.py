def fruit_price(**kwargs):
    #  Initialize the sum of  prices
    sum = 0
    # iterate over the values of the keyword arguments
    for i in kwargs.values():
        # add each price to the sum
        sum = sum + i
        # return the total sum of the prices
    return sum
# calculate the total price of fruits and assign it to variable k
k = fruit_price (mango=10, Apple=5, Orange=15)

print(k)