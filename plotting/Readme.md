# Plotting in Python

## Statistical software package R has sophisticated plotting functions

You can R code very simply.Familiarise yourself with R (just type 'R' in a shell). R includes a number of datasets that it is convenient to use for examples:
```R
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

## Option 1: Call an rscript within python

```python
os.system('Rscript script.R') # this can also contain variables
```

## Rpy2
Rpy2 is a module that allows to include functions of R (a mathematical/statistical programming language) into python. You can use it to draw complex graphics and use mathematical functions that are not included in python, numpy or scipy.
Let's use Rpy2! (from rpy import *), now you can call any R command by either:

```python
# Import Rpy2
import rpy2
print(rpy2.__version__)

# How to load R packages
from rpy2.robjects.packages import importr
# import R's "base" package
base = importr('base')

# import R's "utils" package
utils = importr('utils')
```
**Note** R object names can contain a ”.” (dot) while in Python the dot means “attribute in a namespace”. Because of this, importr is trying to translate ”.” into “_”. 

```python
import rpy2.robjects as robjects

r = robjects.r

x = robjects.IntVector(range(10))
y = r.rnorm(10)

r.X11()

r.layout(r.matrix(robjects.IntVector([1,2,3,2]), nrow=2, ncol=2))
r.plot(r.runif(10), y, xlab="runif", ylab="foo/bar", col="red")
```

- r('pdf(“graphic1.pdf”)')
- r.pdf(“graphics.pdf”)

to assign a variable from python to R
r.assign('variable_inR',variable_in_python)

## Example plot with Rpy2

```python
import math, datetime
import rpy2.robjects.lib.ggplot2 as ggplot2
import rpy2.robjects as ro
from rpy2.robjects.packages import importr
base = importr('base')
datasets = importr('datasets')


mtcars = datasets.data.fetch('mtcars')['mtcars']
pp = ggplot2.ggplot(mtcars) + \
     ggplot2.aes_string(x='wt', y='mpg', col='factor(cyl)') + \
     ggplot2.geom_point() + \
     ggplot2.geom_smooth(ggplot2.aes_string(group = 'cyl'),
                         method = 'lm')
pp.plot()
```

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

### Loading necessary libraries

Preparation: Import the libraries with an alias. Later, you can invoke Pandas with pd, Matplotlib with plt, and Seaborn with sns
```python
# Pandas for managing datasets
import pandas as pd
# Matplotlib for additional customization
from matplotlib import pyplot as plt
%matplotlib inline
# Seaborn for plotting and styling
import seaborn as sns
```

### Read dataset
```python
df = pd.read_csv('Pokemon.csv', index_col=0)
# Display first 5 observations
df.head()
```

### Scatterplots
```python
# Recommended way
sns.lmplot(x='Attack', y='Defense', data=df)
# More fancy
# Scatterplot arguments
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False, # No regression line
           hue='Stage')   # Color by evolution stage
# Some tweaks
# Plot using Seaborn
sns.lmplot(x='Attack', y='Defense', data=df,
           fit_reg=False,
           hue='Stage')
 
# Tweak using Matplotlib
plt.ylim(0, None)
plt.xlim(0, None)
```

### Boxplots

```python
# Boxplot
sns.boxplot(data=df)

# Pre-format DataFrame
stats_df = df.drop(['Total', 'Stage', 'Legendary'], axis=1)
 
# New boxplot using stats_df
sns.boxplot(data=stats_df)
```

### Themes, Violin plots and swarm plots

```python
# Set theme
sns.set_style('whitegrid')
 
# Violin plot
sns.violinplot(x='Type 1', y='Attack', data=df)

pkmn_type_colors = ['#78C850',  # Grass
                    '#F08030',  # Fire
                    '#6890F0',  # Water
                    '#A8B820',  # Bug
                    '#A8A878',  # Normal
                    '#A040A0',  # Poison
                    '#F8D030',  # Electric
                    '#E0C068',  # Ground
                    '#EE99AC',  # Fairy
                    '#C03028',  # Fighting
                    '#F85888',  # Psychic
                    '#B8A038',  # Rock
                    '#705898',  # Ghost
                    '#98D8D8',  # Ice
                    '#7038F8',  # Dragon
                   ]
# Violin plot with Pokemon color palette
sns.violinplot(x='Type 1', y='Attack', data=df,
               palette=pkmn_type_colors) # Set color palette 
# Swarm plot with Pokemon color palette
sns.swarmplot(x='Type 1', y='Attack', data=df,
              palette=pkmn_type_colors)
```

### Overlay plots

```python
# Set figure size with matplotlib
plt.figure(figsize=(10,6))
 
# Create plot
sns.violinplot(x='Type 1',
               y='Attack',
               data=df,
               inner=None, # Remove the bars inside the violins
               palette=pkmn_type_colors)
 
sns.swarmplot(x='Type 1',
              y='Attack',
              data=df,
              color='k', # Make points black
              alpha=0.7) # and slightly transparent
 
# Set title with matplotlib
plt.title('Attack by Type')
```

### Heatmap of correlations, histograms, bar plots

```python
# Calculate correlations
corr = stats_df.corr()
 
# Heatmap
sns.heatmap(corr)

# Distribution Plot (a.k.a. Histogram)
sns.distplot(df.Attack)
# Count Plot (a.k.a. Bar Plot)
sns.countplot(x='Type 1', data=df, palette=pkmn_type_colors)
 
# Rotate x-labels
plt.xticks(rotation=-45)
```

### Factor plot, denisty plot, joint distribution plot

```python
# Factor Plot
g = sns.factorplot(x='Type 1',
                   y='Attack',
                   data=df,
                   hue='Stage',  # Color by stage
                   col='Stage',  # Separate by stage
                   kind='swarm') # Swarmplot
 
# Rotate x-axis labels
g.set_xticklabels(rotation=-45)

# Density Plot
sns.kdeplot(df.Attack, df.Defense)

# Joint Distribution Plot
sns.jointplot(x='Attack', y='Defense', data=df)
```

**Questions**
- Go to http://seaborn.pydata.org/examples/ and plot 3 self chosen examples
