def percentage(*args):
    #   initialise the value of sum to 0
    sum = 0
# to perform a computation of values in args
    for i in args:

        # addition of all the values in args
        sum = sum+i
    # find the average  of values in args
    avg = sum/len(args)
    print("Average=", avg)


# Assigning grade for the average
    if avg > 40:
        print("Pass")
    else:
        print("Fail")


percentage(60,70,80)