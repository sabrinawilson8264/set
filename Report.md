## Modelling End Game Configurations in Set

### Background Information
SET is a pattern recognition card game released in 1991 <sup>[4]</sup> that is beloved by maths students everywhere. The game uses a special deck of cards where every card has 4 attributes (colour, shape, number of shapes, shading) and each attribute can take 3 values

| <img src="SET-Main-Image-2-superJumbo.png" width="75%"> | 
|:--:| 
| <sup>*An example of 12 cards*</sup> |

* colour can be purple, red, or green
* shape can be diamond, squiggle or oval
* number of shapes can be 1, 2 or 3
* shading can be solid, stripe or open

The aim of the game is to identify "sets" amongst the cards on the table that satisfy the following rule: 
> "a SET consists of 3 cards in which each of the cards' features, looked at one-by-one, are the same on each card, or, are different on each card. All of the features must seperately satisfy this rule

> In other words: shape must be either the same on all 3 cards, or different on each of the 3 cards; colour must be either the same on all 3 cards or different on all 3 cards, etc.
> If 2 cards are the same and 1 card is different for any attribute, then it is not a SET" <sup> [3] </sup>


In the standard game of SET, the dealer deals 12 cards onto the table and all players simultaneously look for sets amongst the cards. If none are found, three additional cards are dealt. When a player see's a set, she calls "SET!" and takes the three cards and the dealer lays three more cards onto the table. The game continues like this and ends when all cards the deck is exhausted and there are no more sets on the table. Whoever has collected the most sets at the end of the game is the winner. 

The question that this report aims to answer is to do with how many cards are left on the table at the end of the game that cannot be formed into sets and how likely it is that all the cards form sets and there is none leftover at the end. 

To investigate this question, we will employ a Monte Carlo or stochastic simulation of the game. The Monte Carlo method is a mathematical technique that is used to estimate the probability distribution of the outcome of an uncertain event. The method uses repeated random sampling and the accuracy of the approximation improves as the number of sample increases. 

> "Stochastic simulation methods attempt to mimic or replicate the behaviour of a system by exploiting randomness to obtain a statistical sample of possible outcomes" 



https://people.smp.uq.edu.au/DirkKroese/mccourse.pdf

We can imagine the cards in Set as a set of points in 4 dimensional space. Each "attribute" on the cards (colour, filling, shape, number) corresponds to an axis in four dimensions and each value for that attribute corresponds to a value along that axis. 

We can generalise the game of SET into higher or lower dimensions by imagining that each "attribute" on the cards (colour, shading, shape, number of shapes) 

For example: 
| <img src="set-game-cards 1.png" width="75%"> | 
|:--:| 
| <sup>*Example set card with 2 striped purple squiggles*</sup> |

This card can be represented as the vector ("purple", "two", "squiggle", "stripe"). If we map each value to a digit 0, 1 or 2 (see table below) we can further compress the information contained in this card to (1, 1, 2, 1) 

|Attribute      | Value        | Digit Mapping | 
|---------------| -------------|:-------------:| 
| Colour        | Green        | 0             | 
|               | Purple       | 1             | 
|               | Red          | 2             |  
| Number        | 1            | 0             | 
|               | 2            | 1             | 
|               | 3            | 2             |  
| Shape         | Oval         | 0             | 
|               | Diamond      | 1             | 
|               | Squiggle     | 2             |  
| Shading       | Solid        | 0             | 
|               | Stripe       | 1             | 
|               | Open         | 2             |  


Once the cards have been compressed into a vector, it's easy to imagine a card with any number of dimensions and any number of values per dimension - you just add more elements to the vector and increase the range of digits. For example, we could have a a game of set with 7 attributes each of which had 9 different values. If we used the digits 0-8 to represent the different values for each attribute, a card from this game could be represented as (4, 1, 7, 2, 0, 2, 7) (since the number of the cards is values^dimensions, 9^7 = 4,782,969 which would become a quite long and cumbersome game).

now explain SET(3,3) HERE

The game of SET is governed by chance and probability. Imagining the game in different dimensions naturally invites the question: _Is the probability of particular outcomes in the game SET related to the dimension of the game and the number of values in each dimension?_ This question will be the focus of the rest of this report. 

  
### Introduction
This report is interested in the probability distribution of different configurations in the "end game" of SET. That is, what is the probability that there is a particular number of cards left on the board at the end of the game, none of which make sets with any other cards on the board? 

For now, we will discuss the conventional game of set in which there are 4 dimensions (colour, shape, number, filling) and three possible values for each dimension. From McMahon et al, we know that if there are more than 20 cards on the board, there must be a set amongst them (124). Additionally, if all but three cards have been made into sets, the remaining 3 cards _necessarily_ form a set (McMahon et al, 206). Based on these two facts, the possible number of cards left on the board at the end of the game are: 0, 6, 9, 12, 15, 18. 

The probability distribution for the number of cards left on the table in the conventional game of set is well documented (McMahon p265; Warne; Faulk). The purpose of this report is to ask the question - is the probability distribution the same in different dimensions of the game?      

We assume each shuffled deck equally likely and uniformly distributed
### Body
To simulate the game, three functions were written which are outlined below

#### function `is_it_a_set(x, d, n)`
The purpose of this function is to determine whether a list of cards form a set. The function takes three variables: `x`, a list of lists which contain the details of the cards being checked; `d`, the dimension of the game being played i.e. how many attributes each card has; and `n`, the number of values per attribute. The function either returns 1 if the cards form a set or 0 if they do not. 

An example call of this function is

```python
d = 4
n = 3
card_1 = [0, 1, 2, 0]
card_2 = [1, 1, 1, 1]
card_3 = [2, 1, 0, 2]

is_it_a_set([card_1, card_2, card_3], d, n)
```
The function loops over each position in the card and checks if the value at that position is the same in all cards or different in all cards or otherwise. If the value of an attribute is _not_ the same on all cards or _not_ different on all cards, the function returns 0. 

In the context of the example call, the function appends the 0th value in `card_1` and the 0th value in `card_2` and the 0th value in `card_3` to a list which is then converted to a set (python object) which deduplicates the values. If the set (python object) has length 1, the value at the 0th position must be the same on all 3 cards. Conversely, if the set (python object) has length 3, the value at the 0th position must be different on all 3 cards. If the condition is satisfied, we continue to the next position and repeat. If the condition is not satisfied, the cards do _not_ form a set and the function returns 0. 

In the example call, the values at each position are: in position 0 the values are {0, 1, 2} (all different); in position 1 the values are {1, 1, 1} (all the same), in position 2 the values are {2, 1, 0} (all different) and in position 3 the values are {0, 1, 2} (all different). For this example, the function would return 1. 

Note that the function takes d and n as input as it is designed to be dimension- and value- agnostic and can be used for versions of set with any dimensions and any values per dimension. 

#### function `find_sets_on_the_board(board, completed_sets, d, n)`
The purpose of this function is to look at a list of cards (the "board"), determine if any sets are present and append them to a list of sets found previously. The function takes four variables: `board`, a list of cards that make up the "board" or currently dealt cards; `completed_sets`, a list of lists where each sub-list is a set of three cards that have previously been found in the game; `d`, the dimension of the game being played i.e. how many attributes each card has; and `n`, the number of values per attribute. The function returns two variables, `board` and `completed_sets` which will either be 
* the same as when the variables were inputted if no sets are found on the board
* have three cards which form a set removed from `board` and appended to `completed_sets` if sets are found.

An example call of this function is 
```python
d = 4
n = 3
completed_sets = []
board = [(1, 0, 0, 2), (2, 1, 1, 2), (1, 1, 2, 1),
          (2, 2, 2, 1), (1, 2, 0, 2), (1, 2, 1, 0),
            (2, 1, 0, 1), (0, 0, 2, 2), (0, 1, 1, 0),
              (0, 1, 0, 0), (0, 1, 1, 2), (1, 0, 0, 0)]


board, completed_sets = find_sets_on_the_board(board,completed_sets,d,n)

```

The function iterates over every possible combination of n cards on the board in a random order and testing if those cards form a set by calling the `is_it_a_set` function until a set is found. Once a set is found, the cards that form the set are appended to the list `completed_sets` and removed from the list `board` and the new values of `completed_sets` and `board` are returned. If the function iterates over every possible combination of n cards on the board and no sets are found, `completed_sets` and `board` are returned, unchanged. 

The function makes use of the `itertools.combinations` method to determine the list of all possible combinations of cards on the board, as well as the `random.shuffle` method to iterate over the combinations in a random order. 

In the example call, there are a number of possible sets to find in `board` but for example, the function might find `[(1, 0, 0, 2), (1, 1, 2, 1), (1, 2, 1, 0)]` first and return

```python
board = [(2, 1, 1, 2),(2, 2, 2, 1), (1, 2, 0, 2),
           (2, 1, 0, 1), (0, 0, 2, 2), (0, 1, 1, 0),
            (0, 1, 0, 0), (0, 1, 1, 2), (1, 0, 0, 0)]
completed_sets = [[(1, 0, 0, 2), (1, 1, 2, 1), (1, 2, 1, 0)]]
```

Again, the function takes d and n as input as it is designed to be dimension- and value- agnostic and can be used for versions of set with any dimensions and any values per dimension. 

#### function `lets_play_set(d, n)`
The purpose of this function is to create a deck of cards, shuffle them, incrementally deal them onto the board, look for sets, deal more cards onto the board and look for more sets until the deck is exhausted and no more sets can be formed. 

The function takes two variables:`d`, the dimension of the game being played i.e. how many attributes each card has; and `n`, the number of values per attribute. 

This function uses `itertools.product` function to create every possible card from `n` and `d` and `random.shuffle` to shuffle the cards at the beginning of the game. 

The function returns two variables: `board`, a list of cards leftover at the end that cannot be formed into sets; and `completed_sets` a list of lists where each sub-list contains cards that were formed into sets during the game. 

An example call of this function is 
```python
d = 4
n = 3

board, completed_sets = lets_play_set(d,n)
```

Again, the function takes d and n as input as it is designed to be dimension- and value- agnostic and can be used for versions of set with any dimensions and any values per dimension. 

#### Main
The main section of the code 

Define the dimensions and values per dimension of the game and how many games are to be simulated. For each game, the number of remaining cards at the end of the game is recorded (for clarity, the number of cards remaining at the end of the game is divided by 3). 
```python
for i in range(games):
    board, completed_sets = lets_play_set(d,n)
    remainders.append(len(board)//n)
```

#### Results
Three simulations with the following conditions were run,
* 100,000 games of SET with 3 dimensions and 3 values per dimension
* 100,000 games of SET with 4 dimensions and 3 values per dimension
* 100,000 games of SET with 5 dimensions and 3 values per dimension

#### Analysis 



### Future work and references
#### Future work
#### References
1. McMahon, Liz, et al. The Joy of SET: The Many Mathematical Dimensions of a Seemingly Simple Card Game. Princeton University Press, 2017. 
2. [https://www.setgame.com/sites/default/files/teacherscorner/DEVELOPING%20MATHEMATICAL%20REASONING.pdf]
3. https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20ENGLISH.pdf
4. https://en.wikipedia.org/wiki/Set_(card_game)
5. Heath, Michael T. “13 Random Numbers and Simulation.” Scientific Computing An Introductory Survey, 2nd ed., McGraw-Hill, New York, NY, 2002, pp. 511–517.
6. Warne, Henrik. “SET® Probabilities Revisited.” Henrik Warne’s Blog, 30 Sept. 2011, henrikwarne.com/2011/09/30/set-probabilities-revisited/.
7. Faulk, Mitchell. “Clearing the Table in the Game SET®.” Mitchell Faulk’s Blog, 27 Sept. 2022, mitchellmfaulk.wordpress.com/2022/09/09/clearing-the-table-in-the-game-set/. 
