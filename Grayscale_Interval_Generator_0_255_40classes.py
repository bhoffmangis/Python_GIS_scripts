'''
The purpose of this script is to equally split the 8-bit color range 
of 0 - 255 into 40 6.375 unit interval classes.  After that, an 8-bit 
grayscale image can be imported into ArcGIS Pro and reclassified to 
40 10 unit interval classes (starting at 5).

The results of running the script can then be used in the Reclassify 
tool as follows:

Start       End         New

0           6.3749      5       # 1st class
6.375       12.7499     15
12.75       19.1249     25
...
235.875     242.2499    375
242.25		248.6249    385
248.625		255.0       395     # 40th class

The values used for the New classes can then be used to create a 40 class 
raster color ramp with the specified New values being explicitly tied to 
each color increment in the ramp.  The same colors can then be applied to 
the same classes over multiple reclassified rasters regardless of whether
or not certain class values exist in any or all of the rasters.
'''

INTERVAL = 6.375        # 255 / 40 classes = 6.375

lower = 0
upper = 6.375 - 0.0001
print str(1) + "\t" + str(lower) + "\t\t" + str(upper)
for i in range(1,40):
    lower += INTERVAL
    upper += INTERVAL
    if upper == 254.9999:
        upper = upper + 0.0001
    print str((i + 1)) + "\t" + str(lower) + "\t\t" + str(upper)