# Creating simple pipelines of external programs

This section of the course aims to give a simple overview of calling an external program within a python script and grabbing output from a program and storing it, using the ```subprocess``` module.
 
A common use of python when working with big data and complex work flows is to provide a level of automation. Whether that is to run the same process on multiple files without manually running it on each one, or enabling your multi-program pipeline to pass output files from one program to the input of another with running them one by one yourself.
 
There example I will use here will be based on my work on INDELs (again) but the principles are applicable for any pipeline.
 
So first of in our example we want to run the program ```pick a program``` which does x. First off we need to know the programs commandline and have that as a string.

```python
program_cmd = ''
```

We can then call this command from out script using the subprocess module, but we also need to make sure we put an import statement at the top of our script.
 
```python
import subprocess

program_cmd = ''
subprocess.call(program_cmd, shell=True)
```
Our script will now call that program and wait for it to finish.
