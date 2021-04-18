import random



def randinputs(n_limit, lower, upper):
    n = 0
    # n_limit=10
    rand_return =[]
    while n < n_limit:
        rand_return = random.randint(lower, upper)
        n = n + 1
        #print(rand_return)
    #return n


#input("Press enter")