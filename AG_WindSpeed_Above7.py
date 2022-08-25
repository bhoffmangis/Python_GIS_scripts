# import arcpy site package
import arcpy

start_time = time.clock()           # time at start of script execution

# set workspace (file path to geodatabase up to and including the geodatabase itself)
arcpy.env.workspace = r'C:\0_DATA\0_GIS\AG_WORK\AG_WindSpeed_Above7\AG_WindSpeed_Above7.gdb'

# set feature class that contains the average monthly wind speed values per aliquot
fc = 'Aliquots_WestCoast_from_Shore_UTM10_CENTROIDS_WINDSPEED_ABV7'
# assign to a list the fields that contain the average monthly and monthly (5-9pm) wind speed values
fields = ['Jan_Avg', 'Feb_Avg', 'Mar_Avg', 'Apr_Avg', 'May_Avg', 'Jun_Avg',
          'Jul_Avg', 'Aug_Avg', 'Sep_Avg', 'Oct_Avg', 'Nov_Avg', 'Dec_Avg', 'No_Month_Avg_Above_7',
          'Jan_Avg_5_9pm', 'Feb_Avg_5_9pm', 'Mar_Avg_5_9pm', 'Apr_Avg_5_9pm',
          'May_Avg_5_9pm', 'Jun_Avg_5_9pm', 'Jul_Avg_5_9pm', 'Aug_Avg_5_9pm',
          'Sep_Avg_5_9pm', 'Oct_Avg_5_9pm', 'Nov_Avg_5_9pm', 'Dec_Avg_5_9pm', 'No_Month_Avg_5_9_Above_7']

# instantiate cursor
with arcpy.da.UpdateCursor(fc, fields) as cursor:

    for row in cursor:

        count = 0                   # set sum counter to 0 (for No_Month_Avg_Above_7 field)
        i = 0                       # set list index to 0 (for monthly average fields)

        while i < 12:               # loop through 12 monthly average fields
            if row[i] >= 7.0:
                count += 1
            i += 1
            row[12] = count         # assign number of months to No_Month_Avg_Above_7 field

        count = 0                   # set sum counter to 0 (for No_Month_Avg_5_9_Above_7 field)
        i = 13                      # set list index to 13 (for monthly average 5-9pm fields)

        while i < 25:               # loop through 12 monthly average 5-9pm fields
            if row[i] >= 7.0:
                count += 1
            i += 1
            row[25] = count         # assign number of months to No_Month_Avg_5_9_Above_7 field
            
            cursor.updateRow(row)   # update current row and proceed to next row

end_time = time.clock()             # time at end of script execution

# calculate elapsed time in minutes and seconds
elapsed_time = end_time - start_time
minutes = elapsed_time / 60
seconds = elapsed_time % 60

print 'Process completed in ~' + str(int(minutes)) + ' minutes, ' + '%.2f' % (seconds) + ' seconds' # All done!