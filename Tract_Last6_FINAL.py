# import arcpy site package
import arcpy

start_time = time.clock()           # time at start of script execution

# set workspace (file path to geodatabase up to and including the geodatabase itself)
arcpy.env.workspace = r'D:\0_DATA\UrbanForests\USFS_UF_DataDiscovery_081121\USFS_UF_DataDiscovery_081121.gdb'

# set feature class that requires processing
table = ['ACS_5Y_B01003_2010_MOD_b', 'ACS_5Y_B01003_2017_MOD_b',
         'ACS_5Y_B15001_2010_MOD_b', 'ACS_5Y_B15001_2017_MOD_b',
         'ACS_5Y_DP04_2010_MOD_b', 'ACS_5Y_DP04_2017_MOD_b',
         'ACS_5Y_DP05_2010_MOD_b', 'ACS_5Y_DP05_2017_MOD_b',
         'ACS_5Y_S1903_2010_MOD_b', 'ACS_5Y_S1903_2017_MOD_b']

# assign to a list the fields that are to be searched and updated
field = ['GEO_ID', 'Tract_Last6']

# Loop through all tables in list
for t in table:
    # Add Tract_Last6 field
    arcpy.AddField_management(t, 'Tract_Last6', 'TEXT', "", "", 10, "", "NULLABLE", "", "")

    # instantiate cursor
    with arcpy.da.UpdateCursor(t, field) as cursor:
        for row in cursor:
            tract_full = row[0]             # assign full GEO_ID value to tract_full variable
            tract_slice = tract_full[-6:]   # extract last 6 characters from GEO_ID field value
            row[1] = tract_slice            # assign extracted 6 characters to Tract_Last6 field
                 
            cursor.updateRow(row)   # update current row and proceed to next row

end_time = time.clock()             # time at end of script execution

# calculate elapsed time in minutes and seconds
elapsed_time = end_time - start_time
minutes = elapsed_time / 60
seconds = elapsed_time % 60

print 'Process completed in ~' + str(int(minutes)) + ' minutes, ' + '%.2f' % (seconds) + ' seconds' # All done!