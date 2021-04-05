import random



def randinputs(n_limit, lower, upper):
    n = 0
    # n_limit=10
    while n < n_limit:
        print(random.randint(lower, upper))
        n = n + 1


# input()