>>> from final import *

# final - CSC 401- Winter 2021

[toc]

---

## Exam Guidelines: read this section first

### Rules

You **MUST**:

* **work on your own**
* **write your own code**
* **cite** any sources of information (outside of course notes) that you use to solve the problems (include urls in comments in your code)

You **MUST NOT**:

* **collaborate or communicate** with others
* **solicit** advice or **ask or answer questions** on the internet or from any other person or source *except* for the instructor  
* **post or distribute** code, solutions, questions or problem descriptions anywhere or anytime (posting anytime **after** the exam is also a violation)
* **use sources** that were posted on the internet after this project was released, especially if the posting was a **result** of this project being released.  For example: After the project is released, Student A posts problem statement(s) from the project to Chegg, CourseHero, StackOverflow, or other website.  "Solutions" are posted by Student B (or some other party).  Student C finds the posting and uses/references some part of that "solution" in their submission. Then Student A, Student B  and Student C are violating the rules, and will receive a grade of 0.
* **share or discuss** questions, code, solutions or ideas with anyone else 

You **MAY**:

* use course materials (without citation)
* **research** and cite existing material on the internet or python docs as long as (see above) 
  * they existed before this project was released
  * you **cite** your sources   
* ask the instructor questions to clarify the assignment (Discord preferred)

### Grading Notes 

* Run the supplied doctest (same examples as in this document).  However, the instructor may **run a more thorough doctest** during grading that checks additional cases.  For each problem, make sure to consider other cases that may not appear in test but that fit the problem description.
* **Note** that the instructor will use software (for example [Moss](http://theory.stanford.edu/~aiken/moss/)) to **compare** your solutions versus those submitted by other students as well as **search** the internet for any postings related to this project. The comparison compares the structure of your code, not just variable names etc. 

### Directions

1. **download** `finalTEST.py` and any supporting files from d2l to your working folder

2. **create** a Python module `final.py` 

3. **implement** your solutions (functions/classes) in `final.py`

4. **run** the `doctest` to check your solutions and fix errors.  Here is the snippet:

   
   if __name__ == '__main__':
       import doctest
       print( doctest.testfile('finalTEST.py'))
   


5. **submit** your solutions to d2l > submissions > ...

---

## Programming Problems

### `differ` (25  points)

Implement a function `differ` that:

* accepts two words (`str`ings) as arguments.  You may assume that they have the same length (you do not need to check this)
* returns the number of *positions* in the words where the two words have *different* letters.  
* the function should be case-insensitive, i.e., it does not distinguish upper and lower case versions of the same character.


>>> differ('pear','pear')
0
>>> differ('Pear','pEAR')
0
>>> differ( 'restful', 'fluster' )  # all positions have different letters
7
>>> differ('their','there') # differ in the last two positions
2
>>> differ('ACCEPT','except') # differ in first two positions
2
>>> differ("cold","warm") # all different
4
>>> lst = ["cold", "CORD", "Word", "wORM", "warm"] # called a word ladder
>>> [ differ(lst[i],lst[i+1]) for i in range(len(lst)-1)]
[1, 1, 1, 1]


---

### `wordsByStart` (25 points)

Implement a function `wordsByStart` that 

* accepts a sentence (`str`) as an argument
* returns a `dict`ionary so that 
  * each key is a capital letter 
  * the corresponding value is a list of all words in the sentence that begin with that letter (either upper or lower case)  
* only letters that start words in the sentence should be included (no keys with empty lists)
* keys should be added to the dictionary in the order they are encountered in the sentence
* words should occur in the lists in the order they appear in the sentence
* the punctuation characters in `.,;!?:` should be ignored (not included in any word)


>>> wordsByStart("Was it a car or a cat I saw?")
{'W': ['Was'], 'I': ['it', 'I'], 'A': ['a', 'a'], 'C': ['car', 'cat'], 'O': ['or'], 'S': ['saw']}
>>> wordsByStart( "A man, a plan, a canal: Panama." )
{'A': ['A', 'a', 'a'], 'M': ['man'], 'P': ['plan', 'Panama'], 'C': ['canal']}
>>> wordsByStart("Anne, I vote more cars race Rome to Vienna.")
{'A': ['Anne'], 'I': ['I'], 'V': ['vote', 'Vienna'], 'M': ['more'], 'C': ['cars'], 'R': ['race', 'Rome'], 'T': ['to']}
>>> wordsByStart("Are we not drawn onward, we few, drawn onward to new era?")
{'A': ['Are'], 'W': ['we', 'we'], 'N': ['not', 'new'], 'D': ['drawn', 'drawn'], 'O': ['onward', 'onward'], 'F': ['few'], 'T': ['to'], 'E': ['era']}


---

### `Vial`  (25 points)

Implement a class `Vial` that represents a vial containing some number of doses of vaccine.  Internally, each `Vial` object will keep track of the *brand* of the vaccine as well as the number of *remaining doses*.  Implementation details:

#### creating and displaying objects

* the constructor (`__init__`) accepts two *required* arguments
  * brand - a `str`, we will use single characters for brevity (you do *not* need to verify)
  * number of doses available - an `int`
* `__repr__` returns a `str` version of the `Vial` as formatted below, note that single quotes appear around the brand


>>> v = Vial('M',10)
>>> v
Vial('M',10)
>>> v = Vial('J',5)
>>> v
Vial('J',5)


#### dosing

The number of available doses can be manipulated/accessed with two methods:

* `dose` applies a single does if one is available, specifically
  * returns a `str` with the brand of the dose
  * **reduces** the number of available doses by one 
  * if the `Vial` is empty, then returns an empty string, and does *not* reduce the number of doses
* `getDoses` - returns the number of available doses


>>> v = Vial('P',2)
>>> v.getDoses()
2
>>> v.dose()
'P'
>>> v
Vial('P',1)
>>> v.dose()
'P'
>>> v
Vial('P',0)
>>> v.dose()  # no more left :(
''
>>> v
Vial('P',0)
>>> v.getDoses()
0


#### comparisons

Two `Vial` objects are compared by *comparing the number of doses available*, for these comparisons the *brand is ignored*.  There are two comparisons supported:

* `==` - this method *must* be named `__eq__`, it accepts two `Vial` objects and returns `True` if and only if they have the same number of doses available.
* `>` - this method *must* be named `__gt__`, it accepts two `Vial` objects and returns `True` if the first `Vial` has *strictly more* doses than the second `Vial`.   

Hints/Notes: 

* You may not have written `__gt__` before.  Structurally the code is identical to `__eq__`, the only difference is that the Boolean expression inside the method is different, as described above.
* optional (no additional credit): implement `>=`, which must be named `__ge__`.   Note that if you do this, then `<` and `<=` will also work, *without writing any additional code*).   Again, this is *optional*, it is not required and will not be tested.


>>> Vial('J',5) == Vial('M',5)
True
>>> Vial('J',5) == Vial('M',3)
False
>>> Vial('J',5) > Vial('M',3)
True
>>> Vial('J',5) > Vial('M',5)
False


#### bonus!

**Do not write more code, this should work for free!** If you have implemented `==` and `>` correctly as required above, then *without writing more code* you will also be able to take a `max` and sort lists using `sort` or `sorted`:


>>> max( Vial('P',3), Vial('M',6), Vial('J',2) )
Vial('M',6)
>>> sorted( [Vial('P',3), Vial('M',6), Vial('J',2)])
[Vial('J',2), Vial('P',3), Vial('M',6)]


---

### `rollDoubles` (25 points)

Consider a dice game for a *pair of dice* which follows these rules:

* the game ends whenever doubles appear (both dice have the same value)
* start the game by rolling both dice (stop if doubles)
* at every other step (assuming doubles not showing):
  * keep the die with the higher value, and 
  * re-roll the die with the lower value.  

Implement a function `rollDoubles` that simulates the above game and when it ends, returns a `tuple` with two values:

1. the total of the showing pair, and
2. the total number of dice rolled to get to the end of the game 

Examples:

1. Suppose that double 4's are rolled at the start of the game. The game ends. The function returns `(8, 2)` because the sum of the dice values is 8, and 2 dice were rolled.  (note: this is the `random.seed(0)` case below)
2. Suppose that random rolls generate the sequence:  `5, 3, 6, 3, 6, 6, 6, 5, 1, 4, ...`.  .  (note: this is the `random.seed(5)` case below).   The starting roll will be the first two numbers in the sequence, each subsequent roll will replace one of the showing dice with the next number in the sequence
   * the starting roll shows (5,3).  5 is kept, 3 is re-rolled to get 6 
   * (5,6) shows.  6 is kept. 5 is re-rolled to get  3 
   * (3,6) shows.  6 is kept, 3 is re-rolled to get 6
   * (6,6) shows, the game ends!   
   * the function returns `(12, 5)`, 12 is the total value of the double 6's and 5 is the total number of dice rolled, 2 at the start then 3 more rolls to get to double 6's. 

Examples:


>>> import random
>>> random.seed(0)   # generates rolls: 4, 4, ....
>>> rollDoubles()
(8, 2)
>>> random.seed(5)   # generates rolls: 5, 3, 6, 3, 6 ...
>>> rollDoubles()
(12, 5)
>>> [ (i, random.seed(i), rollDoubles()) for i in range(20)]
[(0, None, (8, 2)), (1, None, (12, 19)), (2, None, (2, 2)), (3, None, (10, 3)), (4, None, (12, 25)), (5, None, (12, 5)), (6, None, (12, 11)), (7, None, (12, 27)), (8, None, (12, 14)), (9, None, (12, 17)), (10, None, (10, 5)), (11, None, (10, 5)), (12, None, (12, 5)), (13, None, (6, 2)), (14, None, (12, 4)), (15, None, (12, 10)), (16, None, (8, 3)), (17, None, (12, 8)), (18, None, (12, 9)), (19, None, (12, 33))]

---

[toc]





