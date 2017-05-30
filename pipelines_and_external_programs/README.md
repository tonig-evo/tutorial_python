# Creating simple pipelines of external programs

This section of the course aims to give a simple overview of calling an external program within a python script and grabbing output from a program and storing it, 
using the ```subprocess``` module.
 
A common use of python when working with big data and complex work flows is to provide a level of automation. Whether that is to run the same process on 
multiple files without manually running it on each one, or enabling your multi-program pipeline to pass output files from one program to the input of another 
with running them one by one yourself.
 
The example I will use here will be based on my work on INDELs (again) but the principles are applicable for any pipeline.

The task in this tutorial is to extract all INDELs falling within genes on _D. mel_ chromosome 4 and produce a plot of their lengths.

So first off in our example we want to extract INDELs in genes. To do this we are going to use the program called 'Bedtools'. We will give it our VCF file and a 
BED file of coding sequence coordinates and tell the program to output all INDELs that overlap with coding sequence. The command for this is as follows: 
```bedtools intersect -header -a {our_vcf_file} -b {our_bed_file} > {our_output_file}```

```python
# file locations
vcf_file = 'dmel_17flys_chr2R_indels.vcf' 
bed_file = 'dmel_2R_cds.bed'
our_output_vcf = 'dmel_17flys_chr2R_coding_indels.vcf'

# bedtools intersect
bedtools_cmd = 'bedtools intersect -header -a ' + vcf_file + ' -b ' + bed_file + ' > ' + our_output_vcf
```

Now that we have defined all files we need and assigned the command string to a variable we can then call bedtools from our script using the subprocess module, 
but we also need to make sure we import it at the top of our script.
 
```python
import subprocess

# file locations
vcf_file = 'dmel_17flys_chr2R_indels.vcf' 
bed_file = 'dmel_2R_cds.bed'
our_output_vcf = 'dmel_17flys_chr2R_coding_indels.vcf'

# bedtools intersect
bedtools_cmd = 'bedtools intersect -header -a ' + vcf_file + ' -b ' + bed_file + ' > ' + our_output_vcf
subprocess.call(bedtools_cmd, shell=True)
```

Our script will now call the program and wait for it to finish. Once the script has run we can see that a new vcf file has been created in the current directory.

So now we have a subset vcf file with INDELs in coding regions. The next step of our task is to plot the length distribution. However we first need to get the data 
into a more plotable format than VCF!
For this task the script ```get_length_freqs.py``` is provided (you can take a look at it [here](get_length_freqs.py)), this script outputs a csv file with two columns,
length and number of INDELs. The command we will use for this is ```python get_length_freqs.py {input_vcf} {output_csv}```. So if we add this to our code:

```python
import subprocess

# file locations
vcf_file = 'dmel_17flys_chr2R_indels.vcf' 
bed_file = 'dmel_2R_cds.bed'
our_output_vcf = 'dmel_17flys_chr2R_coding_indels.vcf'
length_csv = 'dmel_indel_lengths.csv'

# bedtools intersect
bedtools_cmd = 'bedtools intersect -header -a ' + vcf_file + ' -b ' + bed_file + ' > ' + our_output_vcf
subprocess.call(bedtools_cmd, shell=True)

# length csv creation
script_cmd = 'python get_length_freqs.py ' + our_output_vcf + ' ' + length_csv
subprocess.call(script_cmd, shell=True)
```

Now we have our data in good shape to plot the distribution of INDEL lengths using ggplot. The provided script ```plot_indel_lengths.R``` 
(view it [here](plot_indel_lengths.R)), will plot our data and create a ```.png``` plot in the current directory, it can be run as follows: 
```Rscript plot_indel_lengths.R {in_csv} {plot.png}```. So we can add this step to our pipeline.

```python
import subprocess

# file locations
vcf_file = 'dmel_17flys_chr2R_indels.vcf' 
bed_file = 'dmel_2R_cds.bed'
our_output_vcf = 'dmel_17flys_chr2R_coding_indels.vcf'
length_csv = 'dmel_indel_lengths.csv'
plot_file = 'dmel_indel_length_plot.png'

# bedtools intersect
bedtools_cmd = 'bedtools intersect -header -a ' + vcf_file + ' -b ' + bed_file + ' > ' + our_output_vcf
subprocess.call(bedtools_cmd, shell=True)

# length csv creation
script_cmd = 'python get_length_freqs.py ' + our_output_vcf + ' ' + length_csv
subprocess.call(script_cmd, shell=True)

# plot
plot_cmd = 'Rscript plot_indel_lengths.R ' + length_csv + ' ' + plot_file
subprocess.call(plot_cmd, shell=True)
```

We now have a complete pipeline script that takes a VCF file and pulls out coding INDELs and plots their lengths,
which we can run in one go rather in three separate steps.

## Task 1

Use a for loop to run the above pipeline with each of the following files in turn: 
```dmel_2R_cds.bed```, ```dmel_2R_intron.bed``` and ```dmel_2R_intergenic.bed```

<details>
<summary>Hint</summary>
bed_files = ['dmel_2R_cds.bed', 'dmel_2R_intron.bed', 'dmel_2R_intergenic.bed']
</details>


[Return home](https://github.com/tonig-evo/tutorial_python)