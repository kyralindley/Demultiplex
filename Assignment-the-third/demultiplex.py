#!/usr/bin/env python
import argparse 
import bioinfo
import gzip 
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
#dictionary for naming convention of matched pairs {index:(R1.fq,R2.fq)}
file_naming_dict={}
file="/projects/bgmp/shared/2017_sequencing/indexes.txt"
#populate the dictonary with {index:(R1.fq,R2.fq)} from the indexes.txt on talapas
with open(file, "r") as fh:
    fh.readline()
    for line in fh:
        index=line.strip().split("\t")[4]
        for item in index:
            R1_M=open("output/"+index+"_R1.fq","w")
            R2_M=open("output/"+index+"_R2.fq","w")
            file_naming_dict[index]=(R1_M,R2_M)
#naming 
unknown_file1=open("output/"+"unknown_R1.fq","w")
unknown_file4=open("output/"+"unknown_R2.fq","w")

hopped_file1=open("output/"+"hopped_R1.fq","w")
hopped_file4=open("output/"+"hopped_R2.fq","w")
#dictonary containng {matched indexes:occurence}
matched_dict_count={}
#dictonary containng {hopped indexes:occurence}
hopped_dict_count={}
#instances to show how many each condition occured
instances_dict={"matched":0,"hopped":0,"unknown":0}

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
#total read, will increment everytime it takes a new read 
total=0
with gzip.open(f1,"rt") as fh1, gzip.open(f2,"rt") as fh2, gzip.open(f3,"rt") as fh3, gzip.open(f4,"rt") as fh4:
    while True:
        record_r1 = readfour(fh1)
        #breaking when four empty strings (end of file)
        if record_r1 == ["","","",""]:
            break
        record_r2 = readfour(fh2)
        record_r3 = readfour(fh3)
        record_r4 = readfour(fh4)
        total+=1
        #create rv comp of R3_001.fastq.gz index
        reverse_index_comp=bioinfo.rev_comp(record_r3[1])
        #appending headers to contain the index pairs, calling append_header function 
        record_r1[0]=append_header(record_r2[1],reverse_index_comp,record_r1[0])
        record_r4[0]=append_header(record_r2[1],reverse_index_comp,record_r4[0])
        index=record_r2[1]
        new_key=(index+'-'+reverse_index_comp)
        #make a decision 
        if 'N' in index or 'N' in reverse_index_comp:
            instances_dict["unknown"]+=1
            unknown_file1.write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            unknown_file4.write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
        elif index not in known_dict or reverse_index_comp not in known_dict:
            instances_dict["unknown"]+=1
            unknown_file1.write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            unknown_file4.write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
        elif index in known_dict and index==reverse_index_comp:
            known_dict[index]+=1
            instances_dict["matched"]+=1
            #R1 is in position 0 of the file_naming_dict value;R2.fq is the 1 position in the file_naming_dict
            file_naming_dict[index][0].write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            file_naming_dict[index][1].write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
            if new_key in matched_dict_count:
                matched_dict_count[new_key]+=1
            else:
                matched_dict_count[new_key]=1
            
        elif index in known_dict and reverse_index_comp in known_dict and index!=reverse_index_comp:
            instances_dict["hopped"]+=1
            hopped_file1.write(record_r1[0]+'\n'+record_r1[1]+'\n'+record_r1[2]+'\n'+record_r1[3]+'\n')
            hopped_file4.write(record_r4[0]+'\n'+record_r4[1]+'\n'+record_r4[2]+'\n'+record_r4[3]+'\n')
            if new_key in hopped_dict_count:
                hopped_dict_count[new_key]+=1
            else:
                hopped_dict_count[new_key]=1
            
unknown_file1.close()
unknown_file4.close()
hopped_file1.close()
hopped_file4.close()

#Finally, output the matched and hopped dictionary 
print("matched dictionary")
print(f'index\tvalue\tpercentage of matched')
for index in matched_dict_count:
    print(f'{index}\t{matched_dict_count[index]}\t{(matched_dict_count[index]/total)*100}%')
print("hopped dictionary")
print(f'index\tvalue\tpercentage of hopped')
for index in hopped_dict_count:
    print(f'{index}\t{hopped_dict_count[index]}\t{(hopped_dict_count[index]/total)*100}%')