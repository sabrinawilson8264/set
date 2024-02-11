def is_it_a_set(x, d, n): 
    """
    Determine if a list of cards form a set.

    The function takes three variables: `x` (list), a list of lists which contain the 
    details of the cards being checked; `d` (integer), the dimension of the game being 
    played i.e. how many attributes each card has; and `n` (integer), the number of values
    per attribute. The function either returns 1 if the cards form a set or 0 
    if they do not. 

    The function loops over each position in the card and checks if the value at
    that position is the same in all cards or different in all cards or 
    otherwise. If the value of an attribute is _not_ the same on all cards and 
    not different on all cards, the function returns 0. 

    Note that the function takes d and n as input as it is designed to be 
    dimension- and value- agnostic and can be used for versions of set with any 
    dimensions and any values per dimension. 

    """ 

    # Iterate over every dimension of the cards, 
    for i in range(d): 
        # Make a temp list for checking the values dimension i.
        checker = []
        # Iterate over every value in dimension i.
        for j in range(n): 
            # Append the value of dimension i on card j to the temp list.
            checker.append(x[j][i])

        
        # Convert temp list to a set. This deduplicates the values and we can 
        # see how many distinct values of dimension i are on the cards. 
        # if the length of the set is 1, all the cards have the same value for 
        # dimension i. If all the cards have different values for dimension i, 
        # the set will have length n.
        if len(set(checker)) == 1 or len(set(checker)) == n:
            continue
        
        
        # The above test must be satisfied for all dimensions of the cards to 
        # make a set. If the test fails at any point, the cards do not form 
        # a set. Return 0 and exit the loop. 
        else: 
            return 0

    # If all dimensions are iterated over and the if statement is true for all,
    # the cards must form a set and the function returns 1. 
    return 1