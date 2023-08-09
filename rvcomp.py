#!/usr/bin/env python
#might want to comment out the print statements
input_string = "ACTG"
def rev_comp(input_string):
    '''this will take a string, reverse it, and then match the reverse compliment to it'''
#reverse of input string 
    print("this is the input string:", input_string)  
    reversed_string = input_string[::-1]
    print("this is the reverse of the input string:", reversed_string)
#making a dictionary with rv comp of each bp
    actg_dict={"A":"T","T":"A","G":"C","C":"G"}
#make a translation table, this will map character by character based on actg_dict, maps each character (key) to its replacement (value)
    trans_table = str.maketrans(actg_dict)    
#now, translate the reversed sequence (merv) using the trans_table 
    reverse_compliment=reversed_string.translate(trans_table)
    print("the rv comp of:", input_string, "is", reverse_compliment)
    return(rev_comp)


print(rev_comp(input_string))