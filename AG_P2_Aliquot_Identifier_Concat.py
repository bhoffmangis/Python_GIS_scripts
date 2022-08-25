# import arcpy site package
import arcpy

start_time = time.clock()           # time at start of script execution

# set workspace (file path to geodatabase up to and including the geodatabase itself)
arcpy.env.workspace = r'D:\0_DATA\AG_WORK_P2\AG_P2_Concat_FINAL\AG_P2_Concat_FINAL.gdb'

# set feature class that is to be processed
fc = 'AG_P2_UTM10_Aliquots_CLIP_INT'

# ###########################################################################################################
# Add LET_DES (Letter Designation) and ALQ_UID (Aliquot Identifier) fields to table

print "Starting field addition..."

# add fields to table
arcpy.AddField_management(fc, "LET_DES", "TEXT", "", "", 3, "Letter Designation", "NULLABLE", "", "")
arcpy.AddField_management(fc, "ALQ_UID", "TEXT", "", "", 20, "Aliquot Identifier", "NULLABLE", "", "")

print "New fields added!\n"

# ###########################################################################################################
# Update LET_DES (Letter Designation) field with letter value found in native ALQ_DESC (Description) field

print "Starting Letter Designation update..."

# assign to a list the fields that are required for processing
fields = ['BLK_NUM', 'PROT_NUM', 'ALQ_DESC', 'LET_DES', 'ALQ_UID']

# instantiate cursor for field update
with arcpy.da.UpdateCursor(fc, fields) as cursor:

    # update LET_DES field to contain upper case letter designation
    for row in cursor:
        row[3] = row[2].upper()
            
        cursor.updateRow(row)   # update current row and proceed to next row

print "Letter Designation update complete!\n"

# ###########################################################################################################
# Concatenate values of PROT_NUM (OPD number), BLK_NUM (Block Number), and LET_DEC (Letter Designation) fields
# and assign to ALQ_UID (Aliquot Identifier) field

print "Starting Aliquot Identifier concatenation..."

# instantiate cursor for concatenation
with arcpy.da.UpdateCursor(fc, fields) as cursor:

    # concatenate values and assign to ALQ_UID field
    for row in cursor:

        row[4] = row[1] + " " + row[0] + row[3]
            
        cursor.updateRow(row)   # update current row and proceed to next row

print "Aliquot Identifier concatenation complete!\n"

# ###########################################################################################################

end_time = time.clock()             # time at end of script execution

# calculate elapsed time in minutes and seconds
elapsed_time = end_time - start_time
minutes = elapsed_time / 60
seconds = elapsed_time % 60

print 'Process completed in ~' + str(int(minutes)) + ' minutes, ' + '%.2f' % (seconds) + ' seconds' # All done!