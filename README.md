# Python tutorial

This tutorial is aimed to get familiar with the programming language Python. The file [learnpython.py](learnpython.py) contains five sections introducing basic principles of the programming language. For each section there are a number of questions, please answer the questions of each section in a separate script. As a little guide to start, please read the instructions for code annotations [How_to_document_code.pdf](How_to_document_code.pdf). 

**Question**

What are the three basic rules for code annotation?

## 1. Primitive Datatypes and Operators

**Questions**

- Which python version is installed on your system (type python in a terminal)
- How do you print a string/numeric?
- What is the effect of using “+” to add strings? What is the difference between “2”+”2” and 2+2
- How can you add a number and a string?
- What is the result of 1 / 2 and why?
- How can you print inverted commas?
- Are following expression True/False and why?

```
    - False==0
    - 2>False
    - True==0
    - True==2
    - “2”==2
    - “2”=='2'
    - “'”=='\''
```
- How do you extract the first letter of a string?
- How do you extract the second digit of a numeric variable?

## 2. Variables and Collections

**Questions**

- How do you assign a variable? How do you print a variable?
- What is the syntax to create
    - a list
    - a tuple
    - a dictionary
    - a set
- How do you check for the existence of an element in
    - a list
    - a tuple
    - a dictionary
    - a set
- How do you create 
    - the union of a list
    - the intersection of a list
- What is the code to swap two variables?
- How do you reverse a list?
- How do you create a list of integers
    - 0.....x
    - 5.....x
    - 5,7,..x
- How do you obtain the last but one element of a list
- Can you apply list commands to strings?

## 3. Control Flow

**Questions**

- How to use the ”for … in” loop to extract every other letter of a string
- Use the “if ... elif … else” function to check if a variable contains letters, numerics or both
- Use the “for … in” loop to calculate faculty
- Use the “while … ” loop to calculate faculty
- Use a suitable loop to check if a number is a prime number
- Code an exception handling for a zero division 
- Assume a string of coding DNA, extract for each letter the codon position (1st,2nd and 3rd) using a loop and the if command

## 4. Functions

**Questions**

- Write a function that returns the GC content of a  string(e.g. a DNA string that contains of the four letters A,C,G,T or a,c,g,t)
- Do you need to return a value in a function?
- What is the “None” object
- Write a recursive function (a function that calls itself) to calculate faculty.
- Can you overload functions (use the same function name with different input parameters) in Python?
- What is the difference between a global and local variable? How can you define a global variable in a local context?

## 5. Modules

**Questions**

- How and where to import a module in a python script?
- Check if following modules are installed on your computer and import them: scipy, numpy, rpy, math
- How can you check what functions and attributes are included in a module?
- Create your own module with two functions and import it to a separate script to run the functions.

## 6. Numpy and Scipy

NumPy and SciPy are open-source add-on modules to Python that provide common mathematical and numerical routines in pre-compiled, fast functions. Have a look at [Numpy_Tutorial.pdf](Numpy_Tutorial.pdf) to familiarise yourself with the two modules.

Also take a look at: http://www.loria.fr/~rougier/teaching/numpy/numpy.html (solutions to questions marked with an asterisk are hidden on the website)

**Questions**

- Import the numpy package under the name np
- Convert a list of numbers (5 elements) to a numpy array
- Convert a numpy array to a list
- Create two numpy arrays of the same length and apply following mathematical operations: +,*,-,/,%
- Create a null vector of size 10 but the fifth value which is 1 *
- Create a vector with values ranging from 10 to 99 *
- Create a 3x3 matrix with values ranging from 0 to 8 *
- Find indices of non-zero elements from [1,2,0,0,4,0] *
- Declare a 10x10x10 array with random values *
- Normalize a 5x5 random matrix (between 0 and 1) *
- Multiply a 5x3 matrix by a 3x2 matrix (real matrix product) *
- Create a random vector of size 1000 and find the mean value *
- Create two numpy arrays and apply following correlation functions: Pearson r, Spearman rho, Kendall tau

## 7. Biopython

Biopython is a set of freely available tools for biological computation. Please look at [Biopython_Intro.pdf](Biopython_Intro.pdf) to answer the following questions.

**Questions**

- What is the fasta format?
- How to open a fasta file with Biopython?
- How to open a fasta file using the open command?
- How can you open (very) large inputfiles?
- How to convert a sequence in a string?
- How to convert a string to a sequence (e.g. DNA, RNA)
- Print the genetic code (standard code and mitochondrial code) using Biopython
- Create following DNA sequence: AAAAGAGAGATGTCCCTACCCTTT
    1) Find the motif “TACC”
    2) Produce the complement
    3) Produce the reverse complement
    4) Transcribe the sequence
    5) Transcribe the reverse complement
    6) Translate the sequence using the Standard code
- What is the difference between Seq and MutableSeq?

## 8. Parsing and text extraction

Take a look at the File [Inparanoid_table.txt](Inparanoid_table.txt). It contains gene identifiers of homolog genes in two genomes (Gene identifiers of species 1 starts with ENSTGUP and species 2 with ENSGALP). Some genes have more than one homolog in the other species (multiple entries). Extract the following information:

**Questions**

- Create two lists, one for each species, containing the first gene identifiers of each line (the so called seed orthologs) 
- Create a dictionary “homologs” with the keys of the seed ortholog of species 1. Each entry should contain the seed ortholog of species 2. e.g. homologs('ENSTGUP00000011593')
>> ENSGALP00000021957

## 9. Rpy (to produce fancy graphs)

** This section will not work with the most recent rpy version. Please try to run the program with R only **

Rpy is a module that allows to include functions of R (a mathematical/statistical programming language) into python. You can use it to draw complex graphics and use mathematical functions that are not included in python, numpy or scipy. You can R code very simply:

- Familiarise yourself with R (just type 'R' in a shell)

R includes a number of datasets that it is convenient to use for examples:
```
# load prepared data trees
data(trees)
# First five columns of dataset tree including labels
trees[1:5,]
# each column
attach(trees)
# a simply operational
mean(Height)
# Plot some two nice graphs
pdf(“graphic1.pdf”)
par(mfrow=c(2,2)) 
hist(Height) 
boxplot(Height) 
hist(Volume) 
boxplot(Volume)
dev.off() 
pdf(“graphic2.pdf”)
par(mfrow=c(1,1))
plot(Height,Volume)
dev.off()
```
Let's use Rpy! (from rpy import *), now you can call any R command by either:
- r('pdf(“graphic1.pdf”)')
- r.pdf(“graphics.pdf”)

to assign a variable from python to R
r.assign('variable_inR',variable_in_python)

**Questions**

- Plot the two graphs from the R tutorial above using rpy.
Look at http://www.harding.edu/fmccown/r/ , you will find simple plots and the corresponding R code. Use rpy to complete the following tasks:
-Plot a simple (plot each in a seprate pdf file)
    a) Line Chart (use at least three colors)
    b) Bar Chart (add a meaningful legend), 
    c) Histogram (use a lognormal distribution)
    d) Pie Chart (add a title) 
    e) Dotchart (use percentage as labels)

## 10. Run external programs

External programs can be called from within python using 
```
os.system('external program')
```
Questions

- run another python script from within python
- create a new file with the “>” pipe command
- run the program “codeml” (in the subfolder paml). It requires an inputfile, which you can copy or explicitly define as argument 
- obtain the likelihood of the output file of codeml (file codeml_output, it's indicated on the line with lnL = ) 
