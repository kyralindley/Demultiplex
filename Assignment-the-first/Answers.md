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




4. Pseudocode [pseudo_code.txt](./pseudo_code.txt)
5. High level functions. For each function, be sure to include:
    1. Description/doc string
    2. Function headers (name and parameters)
    3. Test examples for individual functions
    4. Return statement
