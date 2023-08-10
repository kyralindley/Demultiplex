#!/bin/bash 
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --cpus-per-task=1                 #optional: number of cpus, default is 1
#SBATCH --mem=8GB                        #optional: amount of memory, default is 4G
#SBATCH --nodes=1                         #optional: number of nodes
#SBATCH --job-name=demultiplex.py                #optional: job name

conda activate base 
f1=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R1_001.fastq.gz
f2=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R2_001.fastq.gz
f3=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R3_001.fastq.gz
f4=/projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz

/usr/bin/time -v ./demultiplex.py -f1 $f1 -f2 $f2 -f3 $f3 -f4 $f4