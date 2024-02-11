def find_sets_on_the_board(board, completed_sets,d,n):
    """ 
    Look at a list of cards and find a set amongst them. 
    

    The purpose of this function is to look at a list of cards (the "board"), 
    determine if any sets are present and append them to a list of sets found 
    previously. 
    
    The function takes four variables: `board` (list), a list of cards that
    make up the "board" or currently dealt cards; `completed_sets` (list), a list of 
    lists where each sub-list is a set of three cards that have previously been 
    found in the game; `d` (integer), the dimension of the game being played i.e. how many 
    attributes each card has; and `n` (integer), the number of values per attribute. The 
    function returns two variables, `board` and `completed_sets` which will either 
    be 
        the same as when the variables were inputted if no sets are found on the 
        board 
    OR 
        have three cards which form a set removed from `board` and appended to 
        `completed_sets` if sets are found.

    The function iterates over every possible combination of n cards on the board 
    in a random order and testing if those cards form a set by calling the 
    `is_it_a_set` function until a set is found. Once a set is found, the cards 
    that form the set are appended to the list `completed_sets` and removed 
    from the list `board` and the new values of `completed_sets` and `board` are 
    returned. 
    
    The function takes d and n as input as it is designed to be dimension- and 
    value- agnostic and can be used for versions of set with any dimensions and 
    any values per dimension. 

    """
    # First, create the list to iterate over. In the normal game of set, we have 
    # 12 cards on the board and n is three, so the following three lines would
    # calculate all possible combinations of 3 items from 12. The list is then
    # shuffled so the combinations are checked in a random order. 
    x = list(range(len(board)))
    iterable = list(itertools.combinations(x,n))
    random.shuffle(iterable)

    # Iterate over every possible combination of cards, 
    for i in range(len(iterable)):
        # Create a temp list to append cards to and input to is_it_a_set.
        cards_to_check = []
        # Append cards to temp list.
        for j in range(n):
            cards_to_check.append(board[iterable[i][j]])
        # If the cards checked form a set, append the cards to completed_sets 
        # list, remove them from the board and exit the for loop. 
        if is_it_a_set(cards_to_check,d,n):
            completed_sets.append(cards_to_check)
            for k in range(n): 
                board.remove(cards_to_check[k])
            
            break

    return [board, completed_sets]