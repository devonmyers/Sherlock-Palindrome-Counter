# Sherlock-Palindrome-Counter

This is Python code for a palindrome counter, that counts palindromes in "The Adventures of Sherlock Holmes" by Arthur Conan Doyle.  A palindrome is a string that has the same order of characters when read forward or backward.  An example of a palindrome is the word "racecar", and an example of a word that is NOT a palindrome would be the word "chocolate".  Note that phrases can also be palindromes, for instance "borrow or rob" is a palindrome.

First, the textual data was read from a text file that has all 12 Holmes short stories from "Adventures" and stored in a list where each list element corresponded to a word in the text.  Next, the data was cleaned by removing special characters such as apostrophes, colons, quotation marks, punctuation, etc.  Afterward, palindromes were counted by using the Python equality comparison operator "==" on each string (word) from the corpus and the reversal of that same string.  Similarly, palindromic phrases were counted by checking palindrome-ness of bigrams, trigrams, and n-grams up to n=5.

If one desired to count palindromes from another body of work, they need only to download the code from the file PalindromeCounter.py, have a text file containing the work to count palindromes from, and changing the name of the text file in the code from 'adventures.txt' to the name of the new text file.
