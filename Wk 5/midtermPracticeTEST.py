>>> from midtermPractice import *

# midtermPractice

[toc]

## Disclaimer

These problems are for practice.  While they are *representative* of midterm problems, they are not intended to fully cover all the material covered. 

## Programming Problems ##

### `numCapitalized` 

Write a function `numCapitalized` that accepts a sentence consisting of words and spaces (no punctuation) and returns the number of words in the sentence that are capitalized.
Note that this is NOT the total number of capitals in the string.  Sample usage:


>>> numCapitalized('This sentence has one such')
1
>>> numCapitalized('This sentence has ONE more ')
2
>>> numCapitalized('ALL THESE ARE')
3
>>> numCapitalized('ALL THESE ARE')==3
True


---

## `gct` 

Implement a function `gct` according to these guidelines:

* The function accepts a single positive integer which represents a number of tablespoons of a liquid.  
* You may assume that this number is always between 0 and 25599 (inclusive of both).  
* The function returns a formatted `str` containing an equivalent number of gallons, cups and tablespoons.  The answer should use as many gallons, then cups as possible.  For example `gct(312)` would return `'01g,03c,08t'` as 312 tablespoons is equivalent to 1 gallon, 3 cups, and 8 tablespoons.
* Each of the output quantities (gallons, cups, tablespoons) should occupy two digits.  
* If the values have less than two digits, they should be padded with leading zeroes.  I.e., 2 cups is represented by `'02c'`.     
* If you look things up, cite them (same goes for all problems)


>>> gct(312)
'01g,03c,08t'
>>> gct(777)
'03g,00c,09t'
>>> gct(25599)
'99g,15c,15t'
>>> gct(25599)=='99g,15c,15t'
True


---

## `priceTShirt` 

Implement a function `priceTShirt` that computes and returns the price of a T-shirt.  

* The function accepts two arguments:  a) the size of the T-shirt, one of `'S','M','L'` and b) a `str` containing a slogan to be written on the shirt.  
* The shirts have a base price of 12 dollars for small shirts, 15 dollars for medium and 18 dollars for large.
* The cost of the slogan depends on the amount of ink used to print the characters:
  * each lower case letter costs 25 cents,
  * each upper case letter costs 30 cents,
  * each punctuation mark, anyone of marks appearing in `.,!'"?:` cost 20 cents,
  * whitespace, either a space or newline character, cost 0 cents (no ink!).
  * you may assume the slogan has no characters other than those mentioned above 


>>> priceTShirt('S',"Vote!")
13.25
>>> priceTShirt('L',"Madam, \nI'm Adam")
21.3
>>> priceTShirt('L',"Taco cat!")
20.0
>>> priceTShirt("M","A man, a plan, a canal: Panama.")
21.15
>>> priceTShirt("M","   \n\n\n   ")==15
True


---

## `alterCase` 

Implement a function `alterCase` that converts a word to "alterCase".  Given a word, using any mix of upper and lower case letters, the function then returns the same word, except that the first letter is upper case, the second is lower case, and then cases of letters alternate throughout the rest of the word.


>>> alterCase('apple')
'ApPlE'
>>> alterCase('ABRACADABRA')
'AbRaCaDaBrA'
>>> alterCase('Mississippi')
'MiSsIsSiPpI'
>>> alterCase('apPLE')
'ApPlE'
>>> alterCase('apPLE')=='ApPlE'
True

---
