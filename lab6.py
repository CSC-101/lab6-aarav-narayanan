import data
from typing import Optional

# Write your functions for each part in the space below.

# Part 0

# Finds the index of the smallest value in the list, if there are values,
#     starting from the provided index (if in bounds).
# input: a list of integers
# input: a starting index
# returns: index of smallest value as an int or None if no value is found
def index_smallest_from(books:list[data.Book], start:int) -> Optional[int]:
    if start >= len(books) or start < 0:
        return None
    mindex = start
    for idx in range(start + 1, len(books)):
        if books[idx].title < books[mindex].title:
            mindex = idx
    return mindex


# Sorts, in place, the elements of a list using the selection sort algorithm.
# input: a list of integers
# returns: nothing is returned; the list is sorted in place
#    <This function modifies/mutates the input list. Though a traditional
#     approach, cloning the list sorting the clone is potentially less
#     surprising. Or even using a different sorting algorithm.>
def selection_sort(books:list[data.Book]) -> list[data.Book]:
    for idx in range(len(books) - 1):
        mindex = index_smallest_from(books, idx)
        books[idx],books[mindex] = books[mindex],books[idx]
    return books

# Part 1
#Purpose ius to give a list within the book class and sort them out in alphabetical order
#Inpt is the list of book Ex.  [data.Book(["Author1"],"Title2"),data.Book(["Author1"],"Title1")]
#Output is the new sorted list that is within the Book class [data.Book(["Author1"],"Title1"),data.Book(["Author1"],"Title2")
def selection_sort_nooks(books:list[data.Book])-> list[data.Book]:
        return selection_sort(books) #Calls out the function to sort the list
#Part 2
#Purpose is to swap out the lowercase with uppercase and vice verse within a string
#Input is  the string of letters "whyWHYwhy"
#Output the is the changed string Ex. "WHYwhyWHY"
def swap_case(letters:str)->str:
    lst_conversion=list(letters) #Splits the string into a list so that each can be checked individually
    new_lst=[] #Empty list start out
    for i in lst_conversion: #For loop to check each index in the list
        if i.islower(): #If the letter is lower case than change it to upper and it will be appened to new_lst
            new_lst.append(i.upper())
        elif i.isupper(): #If the letter is upper case than change it to lower and it will be appened to new_lst
            new_lst.append(i.lower())
        else: #To cancel out any special character so they won't be affected
            new_lst.append(i)
    new_str="".join(new_lst)  #Join function to create the string again.
    return str(new_str)

# Part 3
#Purpose is to have a string of letters and swap out one with another one
#Input is the string "marvelamazing" and the letter old will be a and the new letter will be x
#Out put is the new string with the old and new letters swapped "mxrvelxmxzing"
def str_translate(string:str,old:str,new:str)->str:
    lst=list(string) #COnvert it into a list to check each individually
    for i in range(len(lst)): #FOr loop to check each iteration and swap them out
        if lst[i]==old: #to see if each iteration on the list equals to the oild letter and if so change that component to the new letter
            lst[i]=new
    return "".join(lst) #Convert the list back to a string
# Part 4
#Purpose of this is to take a string and map each word to a dictionary to show a word count
#Input is the string "Words are words amazing"
#Output would be the dictionary {"words":2, "are":1, "amazing":1}
def histogram(string:str):
    string=string.lower #Convert it all into lower case so that there won't be repeats of the same word
    string_lst=string.split() #Convert it into a list
    words={} #Empty dictionary
    for i in string_lst: #for loop for each index on the list
        if i not in words:  #If they are on the dictionary then add them into the dictionary
            words[i]=1
        else: #If they are then add the count by 1
            words[i]+=1
    return words