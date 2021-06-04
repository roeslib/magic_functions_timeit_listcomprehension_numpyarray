import numpy as np

#list comprehension duration
%timeit sum([x for x in range(0, 10_000_000)])

#numpy array duration
%timeit np.arange(0, 10_000_000).sum()

#there are more magic function for Python
#%load - read code into IPython from a local file or URL
#%save - to save snippets to a file
#%run - execute a .py file from IPython
#%precision -  change the default floating-point precision for IPython outputs
#cd - change jdirectories without having to exit IPython first
#%edit - launch an external editor-handy if you need to modify more complex snippets
#%history - list all snippets/commands executed in the current IPython session
