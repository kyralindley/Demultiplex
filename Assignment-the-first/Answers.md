# Assignment the First

## Part 1
1. Be sure to upload your Python script. Provide a link to it here:

| File name | label | Read length | Phred encoding |
|---|---|---|---|
| 1294_S1_L008_R1_001.fastq.gz | Biological Read | 101 | Phred+33 |
| 1294_S1_L008_R2_001.fastq.gz | Index | 8 | Phred+33 |
| 1294_S1_L008_R3_001.fastq.gz | Index | 8 | Phred+33 |
| 1294_S1_L008_R4_001.fastq.gz | Biological Read | 101 | Phred+33 |

2. Per-base NT distribution
    1. Use markdown to insert your 4 histograms here.
    2. **YOUR ANSWER HERE**
    3. **YOUR ANSWER HERE**
    
## Part 2
1. Define the problem: Having four files from a sequencer that we have to demultiplex. Once demultiplex, we need to categorize into the following categories: dual matched, unknown, index hopped.
2. Describe output: The output will be fastq with modified headers w/ indexes (48 files of dual matched index (24 index, and its pair-end reads) 2 unknown files(one for each biological read), 2 index hopped(one for each biological read)). 
3. Upload your [4 input FASTQ files](../TEST-input_FASTQ) and your [>=6 expected output FASTQ files](../TEST-output_FASTQ).
4 input FASTQ files
    R1_Test.fq
    R2_Test.fq
    R3_Test.fq
    R4_Test.fq
6 expected output FASTQ 




4. Pseudocode [pseudo_code.txt](../pseudo_code.txt)
   Pseudo code for demultiplexing

Define a function that reverse compliments barcdodes
    Make it into a dictionary,I will call it compliment_dictionary 
        The key is one letter of genetic code
        The value is its corresponding base pair 
        Ex.... {A:T,T:A, G:C, C:G} 
    Then i will reverse the order of the sequence, then make the changes to the code 


I will the open all four files and read them, in a while true loop i will do these four things, ordering from least computationally intesnse to most computationally
    with open (all 4 files, "r") as f1,f2,f3,f4:
        while true
            *extract sequence line & header (f1,f4)
            header=line
            sequence=line
            *do same on file 3, but call our reverse compliment function on the sequence line of these 
                *if N is present in sequence line or not in list of index: send to unknown
                *elif:
                    add the index-index to both fw and rv if fw_barcode=rv_barcode: send to dual matched 

                *elif: 
                    fw!=rv AND index in list: send to index hopped 
6. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement
