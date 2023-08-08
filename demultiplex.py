#!/usr/bin/env python
import argparse 
import bioinfo
def get_args():
    parser= argparse.ArgumentParser()
    parser.add_argument("-f1", "--filename1", help="Input filename1", required=True)
    parser.add_argument("-f2", "--filename2", help="Input filename2", required=True)
    parser.add_argument("-f3", "--filename3", help="Input filename3", required=True)
    parser.add_argument("-f4", "--filename4", help="Input filename4", required=True)
    return parser.parse_args()
 
args = get_args()
f1=args.filename1
f2=args.filename2
f3=args.filename3
f4=args.filename4

#dictionary of {index sequence:occurence}
known_dict={"GTAGCGTA":0,"AACAGCGA":0,"CTCTGGAT":0,"CACTTCAC":0,"CGATCGAT":0,"GATCAAGG":0,"TAGCCATG":0,"CGGTAATC":0,"TACCGGAT":0,"CTAGCTCA":0,"GCTACTCT":0,"ACGATCAG":0,"TATGGCAC":0,"TGTTCCGT":0,"GTCCTAAG":0,"TCGACAAG":0,"TCTTCGAC":0,"ATCATGCG":0,"ATCGTGGT":0,"TCGAGAGT":0,"TCGGATTC":0,"GATCTTGC":0,"AGAGTCCA":0,"AGGATAGC":0}

#a dictionary of {index code: occurrence count}, all values initially 0.
# known_count_dict={}
# for key in known_dict.keys():
#     known_count_dict[key]=0

#create an empty dictionary to add mismatch pairs 
possibleindexpairs_dict={}

#instances to show how many each condition occured
instances_dict={"matched":0,"hopped":0,"unknown":0}
unknown_file1=open("unknown_R1.fq","w")
unknown_file4=open("unknown_R2.fq","w")
matched_file1=open("matched_R1.fq","w")
matched_file4=open("matched_R2.fq","w")
hopped_file1=open("hopped_R1.fq","w")
hopped_file4=open("hopped_R2.fq","w")
def readfour(fh):
    '''make function to read four lines in a file and returns lines as a tuple'''
    header=fh.readline().strip()     
    seq=fh.readline().strip()
    plus=fh.readline().strip() 
    quality=fh.readline().strip()
    return [header,seq,plus,quality]

def append_header(index1,index2,header):
    '''this takes two indexes and a header that is indicatl on read one and read four
    and returns an appeneded header with the indexes, index1-index2'''
    new_header=header +" "+ index1 + "-" + index2
    return new_header

with open(f1,"r") as fh1, open(f2,"r") as fh2, open(f3,"r") as fh3, open(f4,"r") as fh4:
    while True:
        record_r1 = readfour(fh1)
        #breaking when four empty strings 
        if record_r1 == ["","","",""]:
            break
        record_r2 = readfour(fh2)
        record_r3 = readfour(fh3)
        record_r4 = readfour(fh4)
        #create rv comp of r3
        reverse_index_comp=bioinfo.rev_comp(record_r3[1])
        #appending headers
        record_r1[0]=append_header(record_r2[1],reverse_index_comp,record_r1[0])
        record_r4[0]=append_header(record_r2[1],reverse_index_comp,record_r4[0])
        #print(record_r1[0])
        #record_r1[0]=new_header
        #record_r4[0]=new_header
        index2=record_r2[1]
        
        new_key=(index2+'-'+reverse_index_comp)
        #idk why its called index 2 its index 1
        #make a decision 
        if 'N' in index2 or 'N' in reverse_index_comp:
            instances_dict["unknown"]+=1
            unknown_file1.write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            unknown_file4.write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
        elif index2 not in known_dict or reverse_index_comp not in known_dict:
            instances_dict["unknown"]+=1
            unknown_file1.write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            unknown_file4.write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
        elif index2 in known_dict and index2==reverse_index_comp:
            known_dict[index2]+=1
            instances_dict["matched"]+=1
            matched_file1.write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            matched_file4.write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
            if new_key in possibleindexpairs_dict:
                possibleindexpairs_dict[new_key]+=1
            else:
                possibleindexpairs_dict[new_key]=1
        elif index2 in known_dict and reverse_index_comp in known_dict and index2!=reverse_index_comp:
            instances_dict["hopped"]+=1
            hopped_file1.write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            hopped_file4.write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
            if new_key in possibleindexpairs_dict:
                possibleindexpairs_dict[new_key]+=1
            else:
                possibleindexpairs_dict[new_key]=1
unknown_file1.close()
unknown_file4.close()
matched_file1.close()
matched_file4.close()
hopped_file1.close()
hopped_file4.close()
print(possibleindexpairs_dict)
#print("Instances_dict:",instances_dict)