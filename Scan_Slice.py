# import arcpy site package
import arcpy

start_time = time.clock()           # time at start of script execution

# set workspace (file path to geodatabase up to and including the geodatabase itself)
arcpy.env.workspace = r'D:\0_DATA\LALAH\Scan_Slice\Scan_Slice.gdb'

# set feature class that requires processing
fc = 'AllFlightsAOR_mil_library'
# assign to a list the fields that are to be searched and updated
field = ['Scan', 'Scan_Slice']

# instantiate cursor
with arcpy.da.UpdateCursor(fc, field) as cursor:
    for row in cursor:
        scan_full = row[0]
        scan_slice = scan_full[8:-13]
        row[1] = scan_slice
                 
        cursor.updateRow(row)   # update current row and proceed to next row

end_time = time.clock()             # time at end of script execution

# calculate elapsed time in minutes and seconds
elapsed_time = end_time - start_time
minutes = elapsed_time / 60
seconds = elapsed_time % 60

print 'Process completed in ~' + str(int(minutes)) + ' minutes, ' + '%.2f' % (seconds) + ' seconds' # All done!