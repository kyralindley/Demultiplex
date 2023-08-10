#!/usr/bin/env python
# Author: Kyra Lindley klindley@uoregon.edu
#This module is a collection of useful bioinformatics functions
#__version__ = "0.5" 
#this module contains useful bioinformatics tools that I've gained from my time at Knight Campus

DNAbases = set('ATGCNatcgn')
RNAbases = set('AUGCNaucgn')
input_string="ACTG"

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score'''
    return ord(letter)-33

def qual_score(phred_score: str) -> float:
    '''Returns the average phred score of a string of contiguous Phred scores'''
    total=0
    for i in range(len(phred_score)):
        (i,"",phred_score[i]," - ",convert_phred(phred_score[i]))
        total += convert_phred(phred_score[i])
    
    Avg=total/(len(phred_score))
    return Avg

def validate_base_seq():
    '''This function takes a string. Returns True if string is composed
    of only As, Ts (or Us if RNAflag), Gs, Cs. False otherwise. Case
    insensitive.'''
    return set(seq)<=(RNAbases if RNAflag else DNAbases)

def gc_content(DNA):
    '''calculating GC content of DNA sequence, should return a float b/w 0-1'''
    DNA = DNA.upper()
    DNAlength = len(DNA) #total length of genetic code 
    Cs = DNA.count("C")
    Gs = DNA.count("G")
    return ((DNA.count("G")+DNA.count("C"))/(DNAlength))

def oneline_fasta():
    '''This function takes a multi line fasta and converts it into a fasta that has a header line and one sequence line '''
    with open(file, "r")as fh, open(intermediate, "w") as fout:
        print(fh.readline(), end="", file=fout) #this makes it so the print statement wont add a newline character 
        for line in fh:
            line=line.strip('\n')
            if line.startswith('>'): #for every header ex for the first one 
                print(f'\n{line}',file=fout)
            else:
                print(line,end="",file=fout)
        print("",file=fout)

def calc_median(collection):
    '''This will take a sorted list and calculate and return median of a one dimensional list'''
    length = len(collection)
    if length%2 == 1: #if odd
        return collection[length//2]
    else: #if even
        middle_right = length //2
        middle_left= middle_right -1
        return (collection[middle_left]+collection[middle_right])/2 
actg_dict={"A":"T","T":"A","G":"C","C":"G","N":"N"}
def rev_comp(input_string):
    '''this will take a string, reverse it, and then match the reverse compliment to it'''
    new_seq=""
    for base in input_string:
        new_seq += actg_dict[base]
    return(new_seq[::-1])
    
    


if __name__ == "__main__":
    assert validate_base_seq("AATAGAT") == True, "Validate base seq does not work on DNA"
    assert validate_base_seq("AAUAGAU", True) == True, "Validate base seq does not work on RNA"
    assert validate_base_seq("Hi there!") == False, "Validate base seq fails to recognize nonDNA"
    assert validate_base_seq("Hi there!", True) == False, "Validate base seq fails to recognize nonDNA"
    print("Passed DNA and RNA tests")
    assert gc_content("GCGCGC") == 1
    assert gc_content("AATTATA") == 0
    assert gc_content("GCATCGAT") == 0.5
    print("correctly calculated GC content")
    assert convert_phred("I") == 40, "wrong phred score for 'I'"
    assert convert_phred("C") == 34, "wrong phred score for 'C'"
    assert convert_phred("2") == 17, "wrong phred score for '2'"
    assert convert_phred("@") == 31, "wrong phred score for '@'"
    assert convert_phred("$") == 3, "wrong phred score for '$'"
    print("Your convert_phred function is working! Nice job")