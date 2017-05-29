# Python tutorial

This tutorial is aimed to get familiar with the programming language Python. 

## 0. Setup

First off got to following link: <https://myapps.shef.ac.uk/sgd/> and enter your iceberg login details. Then click the "Iceberg Applications" menu on the left and select "interactive job", a terminal window should appear.

You now need to clone this github repository and make it your working directory as follows:

```
git clone https://github.com/tonig-evo/tutorial_python.git
cd tutorial_python
```

You will then need to load a python environment setup for this course: 

```
module load apps/python/conda
conda env create -f aps_course.yml
source activate aps_course
```

todo still needs modules adding

Once this is done you can return to "Iceberg Applications" menu and click on "gedit" which will open the text editor that you will use to write your scripts.

## 1. Python fundamentals

The file [learnpython.py](learnpython.py) contains five sections introducing basic principles of the programming language. For each section there are a number of questions, please answer the questions of each section in a separate script. As a little guide to start, please read the instructions for code annotations [How_to_document_code.pdf](How_to_document_code.pdf). 

## 1a. Primitive Datatypes and Operators

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

## 1b. Variables and Collections

**Questions**

- How do you assign a variable? How do you print a variable?
- What is the syntax to create
    - a list
    - a dictionary
- How do you check for the existence of an element in
    - a list
    - a dictionary
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

## 2. Control Flow

**Questions**

- How to use the ”for … in” loop to extract every other letter of a string
- Use the “if ... elif … else” function to check if a variable contains letters, numerics or both
- Use the “for … in” loop to calculate faculty
- Use a suitable loop to check if a number is a prime number (https://en.wikipedia.org/wiki/Prime_number)
- Assume a string of coding DNA, extract for each letter the codon position (1st,2nd and 3rd) using a loop and the if command


## 3. Modules

**Questions**

- How and where to import a module in a python script?
- Check if following modules are installed on your computer and import them: scipy, numpy, rpy2, math
- How can you check what functions and attributes are included in a module?
- Create your own module with two functions and import it to a separate script to run the functions.

## 4. Parsing and manipulating a text file

todo add some intro 

Follow the link below for this step of the workshop:

[working with text files](working_with_text_files/README.md)

## 5. Pipelines and external programs

todo add some intro

Follow the link below for this step of the workshop:

[Pipelines and external programs](pipelines_and_external_programs/README.md)


# OPTIONAL TUTORIALS

## 6. Numpy and Scipy

NumPy and SciPy are open-source add-on modules to Python that provide common mathematical and numerical routines in pre-compiled, fast functions. These include a wide variety of statistical tests and mathematical distributions, as well as fast matrix calculations.

[Introduction to numpy and scipy](scipy_numpy/Readme.md)


## 7. Biopython

Biopython is a set of freely available tools for biological computation, especially sequence handling. Biopython is a collection of modules for computational molecular biology, which allows performing most of the basic (and in many cases also advanced) tasks required in a bioinformatics project.

[Introduction to Biopython](biopython/Readme.md)

## 8. Plotting with seaborn or ggplot2 (through R)

Data visualisation is an important aspect of scientific work. Two powerful approaches are introduced here

1. Plot in python with R functions
2. Plot with seaborn

[Introduction to Plotting](plotting/Readme.md)


## 9. Egglib

EggLib is a C++/Python library and program package for evolutionary genetics and genomics. Main features are sequence data management, sequence polymorphism analysis, and coalescent simulations. EggLib is a flexible Python module with a performant underlying C++ library and allows fast and intuitive development of Python programs and scripts.

[Introduction to Egglib](egglib/Readme.md)



