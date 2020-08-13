import numpy as np
import os, sys

rootdir = '/Users/Mattia/Desktop/SWE_VDA/SWE_GOLD'
print(os.listdir(rootdir))
listfile = []

for root, dirs, files in os.walk(rootdir):
    for name in files:
        if name.endswith(("SWE_sca.asc")):
            listfile.append(root + '/' + name)

print(listfile)

header ="""\
ncols   177
nrows    114
XLLCORNER 329181.84817857
YLLCORNER 5036669.44714769
CELLSIZE 500
NODATA_VALUE 9999"""

n=0
for i in listfile:
    grid2 = np.loadtxt(listfile[n+1], skiprows=6)
    grid1 = np.loadtxt(listfile[n], skiprows=6)
    sub_results = grid2n-grid1n
    np.savetxt(listfile[n+1][36:46] +'.asc', sub_results, header=header, fmt="%1.2f", comments='')
    n += 1

#https: // pythontic.com / numpy / ndarray / subtract
#http://geospatialpython.com/2013/12/python-and-elevation-data-ascii-grid.html
#https://docs.scipy.org/doc/numpy/reference/generated/numpy.ndarray.html



