'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
   counter = 0 # variable to hold the # of times the value "th" is present
   if len(word) < 2: # list is empty or only contains 1 element and will not contain "th"
       return 0
   if word[0:2] == 'th': # if the value of the two elements = 'th' -- need to go one larger; the last element isn't inclusive
       counter += 1 # increment the counter
   return counter + count_th(word[1:]) # recurse through the list(word) for each element (adds calls the the stack until the end of the string is reached) 