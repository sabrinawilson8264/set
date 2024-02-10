# set
fun functions and scripts if you have a maths degree and you enjoy playing set a bit too much



### things to think about
for 4-set
1. whats the probability that with 12 cards on the table there is no sets
2. whats the probability that with 15 cards on the table there is no sets
3. whats the minimum number of cards on the board where there must be a set present
4. what is the probability that you deal a "perfect game" i.e. that the shuffled deck forms 27 sets with no remainders (can we work this out with probability, experimentation or linear regression?) does this probability change in higher dimensions? Can we relate the number of dimensions and number of values in a dimension to the probability?
5. If we program a computer to play us in set, what kinds of searching algorithms can we give the computer and will the change in searching speed be perceptible to us in 4-set? How much impedence would we have to put on the computers speed before we could beat the computer? Could we give the computer a dynamic impedence, so that it waits longer for sets that are "harder" to find (in the sense that humans are good at looking for same-ness rather than difference and a set where the value of three attributes are constant and only one attributes has different values between cards is easier for a human to spot than a set where all the values are different on all attributes). 

### background information

We can imagine the cards in Set as a set of points in 4 dimensional space. Each "attribute" in set (colour, filling, shape, number) corresponds to an axis in 4D and each value for that attribute corresponds to a value along that axis. 


d = dimensions
n - number of values in a dimension. 
c = number of cards
s = number of sets

For the conventional game of set that has 4 dimensions and 3 values per dimension, we can relate the variable above thusly: 

$$c = n^d = 3^4 = 81$$

$$s = n^{d-1} = 3^3 = 27$$
That is there is 81 cards which can form up to 27 sets. 

In the game of 3-set (good for beginners) where you keep one dimension at a constant value (good for beginners, I like to pick just the purple cards out of the deck) we would have 

$$c = n^d = 3^3 = 27$$

$$s = n^{d-1} = 3^2 = 9$$
That is there is 27 cards which can form up to 9 sets. 

Also note that the number of cards in a set is determined by n, the number of values in a dimension. This is because, as there is no identical cards, each set of cards much have at least one dimension in which the value is different between cards. 

How many possible sets exist in a deck of d-dimensional set with n values per dimension? 
For each set of n-1 cards, only one card exists that will complete the set. Therefore it is sufficient to calculate how many combinations of n^d items exist. 

$$ {c \choose 2} $$

$$ \frac{c!}{2!(c-2)!} $$

$$ \frac{n^d!}{2(n^d -2)!} $$

For 4-set, 

$$ \frac{3^4!}{2(3^4 -2)!} = \frac{81!}{2\cdot79!} = \frac{81\cdot80\cdot79!}{2\cdot79!} = \frac{81\cdot80}{2} =  3,240 $$

For 3-set

$$ \frac{3^3!}{2(3^3 -2)!} = \frac{27!}{2\cdot25!} = \frac{27\cdot26}{2} = 351 $$


$$ f(3, 3) = 8 $$

$$ f(4, 3) = 20 $$
