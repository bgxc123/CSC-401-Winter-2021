>>> from midterm import *

# midterm - CSC 401- Winter 2021

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
* **post or distribute** code, solutions, questions or problem descriptions anywhere or anytime (posting anytime **after** the midterm is also a violation)
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

1. **download** `midtermTEST.py` and any supporting files from d2l to your working folder

2. **create** a Python module `midterm.py` 

3. **implement** your solutions (functions/classes) in `midterm.py`

4. **run** the `doctest` to check your solutions and fix errors.  Here is the snippet:

   
   if __name__ == '__main__':
       import doctest
       print( doctest.testfile('midtermTEST.py'))
   


5. **submit** your solutions to d2l > submissions > ...

---

## Programming Problems

### `piggyBank`  (25 points)

Implement a function `piggyBank` that represents a piggy bank and determines its value. Details:

* accepts a single argument, a list of coins.
* `'Q','D','N','P'` are the valid values for coins and represent quarter, dime, nickel and penny, respectively.  Each should be valued at their standard US value in whole cents. (Assume they will be supplied in upper case.)
* any other value, for example the the Canadian Quarter `'CQ'`, should be accepted, but should *not* add to the value of the bank
* the value of the bank should be returned in whole cents


>>> piggyBank( ['Q','D','P'] )
36
>>> piggyBank( ['D', 'P', 'P', 'N', 'D', 'D', 'Q'])
62
>>> piggyBank( ['D', 'P', 'P', 'N', 'D', 'D', 'CQ'])
37
>>> piggyBank( ['D', 'X', 'P', 'R', 'D', 'D', 'CQ'])
31
>>> piggyBank( ['D', 'P', 'P', 'N', 'D', 'D', 'CQ'])==37
True


---

### `odds` (25 points)

Write a function `odds` that returns the odd numbers contained in a 2-dimensional list of numbers.  Details:

* accepts a single argument, a 2-dimensional list of positive integers
* returns a (1-dimensional) list containing the odd numbers from the input list.


>>> odds( [[1,2,3],[4,5,6]] )
[1, 3, 5]
>>> odds( [[1,2,3],[4,5,6], [12,14], [13,15]] )
[1, 3, 5, 13, 15]
>>> odds( [[1,2,3],[4,5,6], [3,5], [13,15]] )
[1, 3, 5, 3, 5, 13, 15]
>>> odds( [ [2,4],[4,6,10] ] )
[]
>>> odds( [[1,2,3],[4,5,6], [12,14], [13,15]] )==[1, 3, 5, 13, 15]
True

---

### `findWordOfLength` (25 points)

Write a function `findWordOfLength` that locates the first word in a sentence that has the given length. Details:

* accepts two arguments:
  1. the desired word length
  2. a sentence (`str`) 
* returns the location (index) of the first word in the sentence that has the desired length 
* for this problem, the first word has location/index 0, the second index 1, and so forth ... (Python style counting/indexing)
* the punctuation characters `".,;!?"` should *not* be included in any word's length

* -1 is returned if no word of the desired length is found


>>> findWordOfLength(4,"Able was I ere I saw Elba.")
0
>>> findWordOfLength(1,"Able was I ere I saw Elba.")
2
>>> findWordOfLength(6,"Able was I, ere I saw Elba.")
-1
>>> findWordOfLength(7,"Hey Anna, would you prefer to ride in a kayak or a racecar?")
12
>>> findWordOfLength(8,"Hey Anna, would you prefer to ride in a kayak or a racecar?")
-1
>>> findWordOfLength(4,"What???!!!")
0
>>> findWordOfLength(5,"Hey Anna, would you prefer to ride in a kayak or a racecar?")==2
True


---

### `taller` (25 points)

Write a function `taller` that determines the taller of the heights of two people. Details:

* accepts two height arguments
* each height is a `str` in a set format, e.g., `"6ft2in"` ,  `"4ft11in"`, or `"5ft0in"`.
  * the first number is a *single* digit/character, i.e., `0,1,2..,9`, representing the number of feet
  * followed by `'ft'`
  * the second is a number in `0,1,2,..,11` representing the number of inches (this will be either 1 or 2 characters)
  * followed by `'in'`
  * e.g., `"6ft2in"`  means 6 feet and 2 inches.
* returns the taller of the two input `strs`


>>> taller("6ft2in","4ft11in")
'6ft2in'
>>> taller("5ft2in","5ft11in")
'5ft11in'
>>> taller("6ft2in","4ft11in")
'6ft2in'
>>> taller("5ft2in","4ft11in")
'5ft2in'
>>> taller("4ft2in","4ft11in")
'4ft11in'
>>> taller("5ft9in","5ft11in")
'5ft11in'
>>> taller("5ft9in","5ft11in")=='5ft11in'
True


---

[toc]





