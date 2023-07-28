#!/bin/bash 
#SBATCH --account=bgmp                    #REQUIRED: which account to use
#SBATCH --partition=compute               #REQUIRED: which partition to use
#SBATCH --cpus-per-task=1                 #optional: number of cpus, default is 1
#SBATCH --mem=16GB                        #optional: amount of memory, default is 4G
#SBATCH --nodes=1                         #optional: number of nodes
#SBATCH --job-name=phredencoding.py                #optional: job name


conda activate bgmp

/usr/bin/time -v ./phredencoding.py -f /projects/bgmp/shared/2017_sequencing/1294_S1_L008_R4_001.fastq.gz -o R4_hist