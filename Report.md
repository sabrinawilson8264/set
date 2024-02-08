## Modelling End Game Configurations in Set

### Background Information
Set is a pattern recognition card game released in 1991[reference] that is beloved by maths students everywhere. The game uses a special deck of cards, each of which has 4 attributes (colour, shape, number of shapes, shading) each of which have 3 values
* colour can be purple, red, or green
* shape can be diamond, squiggle or oval
* number of shapes can be 1, 2 or 3
* shading can be solid, stripe or open

The aim of the game is to identify "sets" amongst the cards on the table which must satisfy the following rule: 
"a SET consists of 3 cards in which each of the cards' features, looked at one-by-one, are the same on each card, or, are different on each card. All of the features must seperately satisfy this rule

In other words: shape must be either the same on all 3 cards, or different on each of the 3 cards; colour must be either the same on all 3 cards or different on all 3 cards, etc

If 2 cards are the same and 1 card is different for any attribute, then it is not a SET" 


[reference https://www.setgame.com/sites/default/files/instructions/SET%20INSTRUCTIONS%20-%20ENGLISH.pdf] 
(insert some images as well)

In the standard game of SET, the dealer deals 12 cards onto the table and all players simultaneously look for sets amongst the cards. If none are found, three additional cards are dealt. When a player see's a set, she calls "SET!" and takes the three cards and the dealer lays three more cards onto the table. The game continues like this and ends when all cards the deck is exhausted and there are no more sets on the table. Whoever has collected the most sets at the end of the game is the winner. 

The game invites many questions that are mathematical in nature. For example, how many different sets are possible in the deck? what's the probability that 12 cards contain no sets? what's the maximum number of cards that can be dealt onto the table before there must be a set present? The question that this report aims to answer is to do with how many cards are left on the table at the end of the game that cannot be formed into sets and how likely it is that all the cards form sets and there is none leftover at the end. 


* * a bit about monte carlo simulation
* generalising the game of set to different dimensions and values.
We can 

* Explain cap sets

  
### Introduction
This report is interested in the probability distribution of different configurations of the "end game" of set. That is, what is the probability that there is a particular number of cards left on the board at the end of the game, none of which make sets with any other cards on the board. For now, we will discuss the conventional game of set in which there are 4 dimensions (colour, shape, number, filling) and three possible values for each dimension. From [reference The Joy of Set], we know that if there are more than 20 cards on the board, there must be a set amongst them. Therefore, at the end of the game, there can be no more than 20 cards present. For obvious reasons, once all cards are dealt on to the table there must be a multiple of three cards present. For reasons that are also obvious, the number of cards left on the board cannot be less than 0. Based on this, the possible number of cards left on the board at the end of the game are: 0, 3, 6, 9, 12, 15, 18. 

It has been shown that the game cannot end with 3 cards on the table. [https://www.setgame.com/sites/default/files/teacherscorner/DEVELOPING%20MATHEMATICAL%20REASONING.pdf]

So, we are left with the following possibilities: 0, 6, 9, 12, 15, 18. 

The probability distribution for the number of cards left on the table in the conventional game of set is well documented [reference the joy of set]. The purpose of this report is to ask the question - is the probability distribution the same in different dimensions of the game?      

#### What I'm interested in finding out
Is the probability distribution for end game configurations independent of dimension and number of values per dimension? 
lets compare
probability distribution for 4 dimensional set with 3 values per dimension to
probability distribution for 3 dimensional set with 3 values per dimension to 
probability distribution for 3 dimensional set with 4 values per dimension to 
probability distribution for 4 dimensional set with 4 values per dimension
### Body
### Future work and references
#### Future work
#### References
1. The Joy of Set
