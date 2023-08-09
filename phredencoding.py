#!/usr/bin/env python
import argparse
import matplotlib.pyplot as plt
import gzip
def get_args():
    parser= argparse.ArgumentParser()
    parser.add_argument("-f", "--filename", help="Input filename", required=True)
    parser.add_argument("-o", "--output", help="Output filename", required=False)
#    parser.add_argument("-r", "--readlength", help="Read Length ", required=True)
    return parser.parse_args()
 
args = get_args()
f=args.filename
o=args.output
#r=args.readlength

def init_list(lst: list, value: float=0.0) -> list:
    '''This function takes an empty list and will populate it with
    the value passed in "value". If no value is passed, initializes list
    with r values of 0.0.'''
    for zeros in range(8):
        lst.append(value)
    return lst

my_list: list = []
my_list = init_list(my_list)

def convert_phred(letter: str) -> int:
    '''Converts a single character into a phred score'''
    return ord(letter)-33
my_list: list = []
my_list = init_list(my_list)

def populate_list(file: str) -> tuple[list, int]: #list should be the array, the counter is the int
    """this will call init_list to populate my empty list 'alist', opens the fastq files, and converts the quality score, returns a counter and a array""" 
    alist=[]
    alist=init_list(alist) #populates list
    with gzip.open(file,"rt") as tfile:
        i=0
        for line in tfile:
            i+=1
            sum=0
            if i%4==0:
                line=line.strip('\n')
                for index,letter in enumerate(line):
                    phredtest=convert_phred(letter)
                    alist[index]+=phredtest
        return(alist,i) 
my_list, num_lines = populate_list(f)

for i,sumoflist in enumerate(my_list):
    mean=sumoflist/(num_lines/4)
    my_list[i]=mean
  #  print(f'{i}\t{mean}')

plt.plot(range(8),my_list) #x axis, y axis
plt.xlabel('Number of Base Pairs')
plt.ylabel('Mean Quality Score')
plt.title('Mean Quality Score of the Base Pairs')
plt.savefig(f'{o}.png')