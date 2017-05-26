# Creating simple pipelines of external programs

This section of the course aims to give a simple overview of calling an external program within a python script and grabbing output from a program and storing it, using the ```subprocess``` module.
 
A common use of python when working with big data and complex work flows is to provide a level of automation. Whether that is to run the same process on multiple files without manually running it on each one, or enabling your multi-program pipeline to pass output files from one program to the input of another with running them one by one yourself.
 
There example I will use here will be based on my work on INDELs (again) but the principles are applicable for any pipeline.
 
So first of in our example we want to run the a modified version of the script we just wrote ```extract_indels_over_10bp.py```, which has only had the file paths changed. Firstly off we need to know the programs commandline and have that as a string. Normally, as this is a Python script, we would just import it. But for the sake of demonstration, we will call the script like we would call any script.

```python
script_cmd = 'python extract_indels_over_10bp.py'
```

We can then call this command from out script using the subprocess module, but we also need to make sure we put an import statement at the top of our script.
 
```python
import subprocess

script_cmd = 'python extract_indels_over_10bp.py'
subprocess.call(script_cmd, shell=True)
```
Our script will now call that program and wait for it to finish. Once the script has run we can see that a bed file has been created in the current directory.

Next off we are going to run a program we haven't written ourselves, bedtools. We are going to use bedtools to take the overlap between our vcf file and out bed file and output a new vcf file with the overlapping variants. The command line for this is: ```bedtools intersect -header -a {our_vcf_file} -b {our_bed_file} > {our_output_file}```.

```python
import subprocess

# file locations
vcf_file = 'dmel_17flys_chr4_indels.vcf' 
bed_file = 'dmel_indels_over_10bp.bed'

# extract indel positions
script_cmd = 'python extract_indels_over_10bp.py'
subprocess.call(script_cmd, shell=True)

# perform a bedtools intersect
our_output_vcf = 'dmel_17flys_chr4_indels_over10bp.vcf'
bedtools_cmd = 'bedtools intersect -header -a ' + vcf_file + ' -b ' + bed_file + ' > ' + our_output_vcf
subprocess.call(bedtools_cmd, shell=True)
```

So now we have a subset vcf file with INDELs over 10bp. Say we want to plot the distribution of INDEL lengths using ggplot. First we probably want to get the data into a convenient format for plotting, particularly as reading in large data files in R can be a bit of faff. For this there is the simple script ```get_length_freqs.py``` which outputs in a csv format with two columns, length and number of INDELs. So the command we will use for this is ```python get_length_freqs.py > dmel_indel_lengths.csv```. We can the read this summarised data into R and plot a it with ggplot such as with the following script:

```R
library(ggplot2)

length_data <- read.csv('dmel_indel_lengths.csv', header=FALSE)

ggplot(length_data, aes(x=V1, y=V2))+
    geom_bar(stat='identity', position='dodge', fill='steel blue') +
    xlab('Indel Length (bp)') + ylab('Number of INDELs') +
    theme_bw()
    
ggsave('indel_length_plot.png', height=6, width=9)
```
