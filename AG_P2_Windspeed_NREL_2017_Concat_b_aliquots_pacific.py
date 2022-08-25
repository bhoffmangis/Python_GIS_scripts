# import arcpy site package
import arcpy

start_time = time.clock()           # time at start of script execution

# set workspace (file path to geodatabase up to and including the geodatabase itself)
arcpy.env.workspace = r'D:\0_DATA\AG_WORK_P2\AG_P2_Windspeed_NREL_2017\AG_P2_Windspeed_NREL_2017.gdb'

# set feature classes that are to be processed
feature_classes = ['aliquots_pacific_UTM10']


# ###########################################################################################################

# Loop through each feature class and perform field add and aliquot identifier concatenation

for fc in feature_classes:

    # ###########################################################################################################
    # Add ALQ_UID (Aliquot Identifier) field to table

    print "Starting field addition for " + fc

    # add field to table
    arcpy.AddField_management(fc, "ALQ_UID", "TEXT", "", "", 20, "Aliquot Identifier", "NULLABLE", "", "")

    print "New field added for " + fc + "!\n"

    # ###########################################################################################################
    # Concatenate values of PROT_NUMBE and BLOCK_NUMB fields and assign to ALQ_UID (Aliquot Identifier) field

    print "Starting Aliquot Identifier concatenation for " + fc

    # assign to a list the fields that are required for processing
    fields = ['PROT_NUMBE', 'BLOCK_NUMB', 'ALQ_UID']


    # instantiate cursor for concatenation
    with arcpy.da.UpdateCursor(fc, fields) as cursor:

        # concatenate values and assign to ALQ_UID field
        for row in cursor:

            # strip white space from current PROT_NUMBE and BLOCK_NUMB values
            row[0] = row[0].strip()  # no leading white space evident in this field
            row[1] = row[1].strip()
                        
            row[2] = row[0] + " " + row[1]
                
            cursor.updateRow(row)   # update current row and proceed to next row

    print "Aliquot Identifier concatenation completed for " + fc + "!\n"

# ###########################################################################################################

end_time = time.clock()             # time at end of script execution

# calculate elapsed time in minutes and seconds
elapsed_time = end_time - start_time
minutes = elapsed_time / 60
seconds = elapsed_time % 60

print 'Process completed in ~' + str(int(minutes)) + ' minutes, ' + '%.2f' % (seconds) + ' seconds' # All done!