def lets_play_set(d,n): 
    """
    Play a whole game of d-dimensional set and return the cards left at the
    end of the game. 

    
    The purpose of this function is to create a deck of cards, shuffle them, 
    incrementally deal them onto the board, look for sets, deal more cards onto 
    the board and look for more sets until the deck is exhausted and no more sets 
    can be formed. 

    The function takes two variables:`d` (integer) the dimension of the game being
    played i.e. how many attributes each card has; and `n`, (integer) the number of
    values per attribute. 

    The function returns two variables: `board` (list), a list of cards leftover
    at the end that cannot be formed into sets; and `completed_sets` (list) a 
    list of lists where each sub-list contains cards that were formed into sets 
    during the game. 

    """
    # Create the deck of SET cards with a cartesian product of all values in 
    # all dimensions
    dimension = list(range(n))
    attributes = []
    for i in range(d):
        attributes.append(dimension)
    all_cards = list(itertools.product(*attributes))

    
    # Shuffle the cards
    deck = []
    card_order = list(range(len(all_cards)))
    random.shuffle(card_order)
    for i in range(len(all_cards)):
        card = card_order[i]
        deck.append(all_cards[card])

    # Deal cards onto the board. 
    # deck_index keeps track of where we are up to in the deck.
    # board is a list which contains the cards currently dealt which is where
    #   the computer looks for sets of cards. 
    # completed_sets is a list which sets are appended to when they are found. 
    
    deck_index = n*d
    board = deck[0:deck_index]
    completed_sets = []

    # Before the deck is exhausted, look for sets. Deal more cards, 
    # look for sets again and so on and so forth. 
    while deck_index < pow(n,d): 
        board, completed_sets = find_sets_on_the_board(board,completed_sets,d,n)
        for i in range(n):
            board.append(deck[deck_index]+n)
        deck_index += n

    # Once the deck is exhausted, we look for sets a couple more times in 
    # the remaining cards just for completeness
    for i in range(2*n): 
        board, completed_sets = find_sets_on_the_board(board,completed_sets,d,n)

    # The game is now over and we return what cards are left on the board, and 
    # what sets were found during the game. 
    return [board, completed_sets]