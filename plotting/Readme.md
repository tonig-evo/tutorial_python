# Plotting in Python

## Use rpy2 to plot (R within python)

Rpy2 is a module that allows to include functions of R (a mathematical/statistical programming language) into python. You can use it to draw complex graphics and use mathematical functions that are not included in python, numpy or scipy. You can R code very simply:

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
- Plot a simple (plot each in a seprate pdf file)
    1. Line Chart (use at least three colors)
    2. Bar Chart (add a meaningful legend), 
    3. Histogram (use a lognormal distribution)
    4. Pie Chart (add a title) 
    5. Dotchart (use percentage as labels)

## Use seaplot to plot

Seaborn provides a high-level interface to Matplotlib (a plotting environment for Python), a powerful but sometimes unwieldy Python visualization library.

Data: https://elitedatascience.com/wp-content/uploads/2017/04/Pokemon.csv

Preparation: Import the libraries with an alias. Later, you can invoke Pandas with pd, Matplotlib with plt, and Seaborn with sns
```
# Pandas for managing datasets
import pandas as pd
# Matplotlib for additional customization
from matplotlib import pyplot as plt
%matplotlib inline
# Seaborn for plotting and styling
import seaborn as sns
```


