# Numpy and Scipy

NumPy and SciPy are open-source add-on modules to Python that provide common mathematical and numerical routines in pre-compiled, fast functions. 

## Arrays

Have a look at [Numpy_Tutorial.pdf](../Numpy_Tutorial.pdf) to familiarise yourself with arrays. Also take a look at: http://www.loria.fr/~rougier/teaching/numpy/numpy.html (solutions to questions marked with an asterisk are hidden on the website)

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

## How to get data into python

### Create data frames from lists

```python
import numpy as np
t = np.linspace(-6, 6, 20)
sin_t = np.sin(t)
cos_t = np.cos(t)
pandas.DataFrame({'t': t, 'sin': sin_t, 'cos': cos_t})
```
### Data frames with pandas module - read in from files

Data: http://www.scipy-lectures.org/_downloads/brain_size.csv

```python
import pandas
data = pandas.read_csv('examples/brain_size.csv', sep=';', na_values=".")
data  
```

### Manipulating data

```python
data.shape    # 40 rows and 8 columns
data.columns # It has columns
print(data['Gender'])
data[data['Gender'] == 'Female']['VIQ'].mean() # simple calculation

# Grouping data
groupby_gender = data.groupby('Gender')
for gender, value in groupby_gender['VIQ']:
    print((gender, value.mean()))
groupby_gender.mean()
```

For a quick view on a large dataframe, use its describe method: pandas.DataFrame.describe().

**Questions**

- What is the mean value for VIQ for the full population?
- How many males/females were included in this study?
- Hint use ‘tab completion’ to find out the methods that can be called, instead of ‘mean’ in the above example.
- What is the average value of MRI counts expressed in log units, for males and females?

## Hypothesis testing

There are numerous statistics and statisctical tests implemented in Scipy. Take a look at https://docs.scipy.org/doc/scipy/reference/stats.html

```python
from scipy import stats

# 1-sample t-test: testing the value of a population mean
stats.ttest_1samp(data['VIQ'], 0) 

# 2-sample t-test: testing for difference across populations
female_viq = data[data['Gender'] == 'Female']['VIQ']
male_viq = data[data['Gender'] == 'Male']['VIQ']
stats.ttest_ind(female_viq, male_viq)

# Paired t-test
stats.ttest_rel(data['FSIQ'], data['PIQ'])

# Wilcoxon signed-rank test
stats.wilcoxon(data['FSIQ'], data['PIQ']) 
```

**Questions**

- Test the difference between weights in males and females.
- Use non parametric statistics to test the difference between VIQ in males and females.

## Statsmodels

http://www.statsmodels.org/stable/example_formulas.html

Create an example data
```python
import numpy as np
x = np.linspace(-5, 5, 20)
np.random.seed(1)
# normal distributed noise
y = -5 + 3*x + 4 * np.random.normal(size=x.shape)
# Create a data frame containing all the relevant variables
data = pandas.DataFrame({'x': x, 'y': y})

```

Run the statistical model

```python
from statsmodels.formula.api import ols
model = ols("y ~ x", data).fit()
print(model.summary()) 
```

**Questions**

- Retrieve the estimated parameters from the model above.
- What does following statistical model test and what is the outcome?
```python
data = pandas.read_csv('examples/brain_size.csv', sep=';', na_values=".")
model = ols("VIQ ~ Gender + 1", data).fit()
print(model.summary())
```

