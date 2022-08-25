# import arcpy site package
import arcpy

start_time = time.clock()           # time at start of script execution

# set workspace (file path to geodatabase up to and including the geodatabase itself)
arcpy.env.workspace = r'C:\0_DATA\0_GIS\AG_WORK\AG_UTM10.gdb'

# set feature class that contains the erroneous UTM zone identifier
fc = 'Aliquots_WestCoast_from_Shore_UTM10'
# assign to a list the fields that contain the UTM zone identifier
fields = ['Index', 'Protractio']

# instantiate cursor
with arcpy.da.UpdateCursor(fc, fields) as cursor:

    rows_updated = 0    # set counter for the number of rows updated

    for row in cursor:

        index_field = row[0]
        protraction_field = row[1]        

        # if the protraction field has a zone value of "09"...       
        if protraction_field[2] == '0' and protraction_field[3] == '9':

            # ...replace the zone value in the index field to "10"            
            index_field = index_field.replace(index_field[2], '1', 1)
            index_field = index_field.replace(index_field[3], '0', 1)
            row[0] = index_field

            # ...replace the zone value in the protraction field to "10"            
            protraction_field = protraction_field.replace(protraction_field[2], '1', 1)
            protraction_field = protraction_field.replace(protraction_field[3], '0', 1)
            row[1] = protraction_field
            
            cursor.updateRow(row)   # update current row and proceed to next row

            rows_updated += 1            

end_time = time.clock()             # time at end of script execution

# calculate elapsed time in minutes and seconds
elapsed_time = end_time - start_time
minutes = elapsed_time / 60
seconds = elapsed_time % 60

print 'Process completed in ~' + str(int(minutes)) + ' minutes, ' + '%.2f' % (seconds) + ' seconds' # All done!
print str(rows_updated) + ' rows updated'