# import arcpy and os site packages
import arcpy
import os

start_time = time.clock()           # time at start of script execution

# set initial workspaces (file path to geodatabase up to and including the geodatabase itself)
arcpy.env.workspace = r'C:\0_DATA\0_GIS\NREL_2017_Python_TEST\NREL_HourlyWind_Pacific_2017_01_06.gdb'
output_gdb = r'C:\0_DATA\0_GIS\NREL_2017_Python_TEST\NREL_2017_UTM10_TEST_1.gdb'

# ###########################################################################################################
# ###########################################################################################################

# project source data to NAD83 / UTM Zone 10N

# set source feature classes
src_fc = ['annual_pacific',
          'jan_pacific','feb_pacific', 'mar_pacific', 'apr_pacific',
          'may_pacific','jun_pacific', 'jul_pacific', 'aug_pacific',
          'sep_pacific','oct_pacific', 'nov_pacific', 'dec_pacific']

# set coordinate system to project to
pcs = arcpy.SpatialReference('NAD 1983 UTM Zone 10N')

# project all source feature classes
for fc in src_fc:
    # set output GDB path and output fc name
    out_fc = os.path.join(output_gdb, fc + '_UTM10').replace('/', '\\')
    # execute projection
    arcpy.Project_management(fc, out_fc, pcs)
    
# ###########################################################################################################
# ###########################################################################################################

# Add new fields to newly projected feature classes

# set initial workspaces (file path to geodatabase up to and including the geodatabase itself)
arcpy.env.workspace = r'C:\0_DATA\0_GIS\NREL_2017_Python_TEST\NREL_2017_UTM10_TEST_1.gdb'

# set projected feature classes that are to be processed
prj_fc_all = ['annual_pacific_UTM10',
              'jan_pacific_UTM10', 'feb_pacific_UTM10', 'mar_pacific_UTM10',
              'apr_pacific_UTM10', 'may_pacific_UTM10', 'jun_pacific_UTM10',
              'jul_pacific_UTM10', 'aug_pacific_UTM10', 'sep_pacific_UTM10',
              'oct_pacific_UTM10', 'nov_pacific_UTM10', 'dec_pacific_UTM10']

# ###########################################################################################################

# Loop through each feature class and add ALQ_UID (Aliquot Identifier) field and...
# Loop through each feature class and perform aliquot identifier concatenation
for fc in prj_fc_all:

    print "Starting ALQ_UID field addition for " + fc + ".\n"

    # add ALQ_UID field to table
    arcpy.AddField_management(fc, "ALQ_UID", "TEXT", "", "", 20, "Aliquot Identifier", "NULLABLE", "", "")

    print "ALQ_UID field added for " + fc + "!\n"

    # ###########################################################################################################
    # Concatenate values of prot and num fields and assign to ALQ_UID field

    print "Starting Aliquot Identifier concatenation for " + fc + ".\n"

    # assign to a list the fields that are required for processing
    fields = ['prot', 'num', 'ALQ_UID']

    # instantiate cursor for concatenation
    with arcpy.da.UpdateCursor(fc, fields) as cursor:

        # concatenate values and assign to ALQ_UID field
        for row in cursor:

            # strip white space from current prot and num values
            row[0] = row[0].strip()
            row[1] = row[1].strip()
                        
            row[2] = row[0] + " " + row[1]
                
            cursor.updateRow(row)   # update current row and proceed to next row

    print "Aliquot identifier concatenation completed for " + fc + "!\n"

# ###########################################################################################################
# ###########################################################################################################

# initialize iterator for month append option (mon list below in else block)
mon_index = 0

# Loop through each feature class and add Avg and Avg_5_9pm fields to their tables (monthly and annual)
for fc in prj_fc_all:

    # ###########################################################################################################
    # Add Avg and Avg_5_9pm fields to table    

    print "Starting Avg & Avg_5_9pm field addition for " + fc + ".\n"    

    # ###########################################################################################################

    # add Annual_Avg & Annual_Avg_5_9pm fields
    if fc[:6] == 'annual':

        # assign Annual_Avg & Annual_Avg_5_9pm fields to variable
        avg_field = "Annual_Avg"
        avg_field_5_9 = "Annual_Avg_5_9pm"

    # ###########################################################################################################

    # add Monthly_Avg & Monthly_Avg_5_9pm fields
    else:    
        # set <mon> append options for Monthly_Avg & Monthly_Avg_5_9pm fields
        mon = ['_Jan', '_Feb', '_Mar', '_Apr', '_May', '_Jun',
               '_Jul', '_Aug', '_Sep', '_Oct', '_Nov', '_Dec']

        # append month to Monthly_Avg & Monthly_Avg_5_9pm fields and assign to variable
        avg_field = "Monthly_Avg" + mon[mon_index]
        avg_field_5_9 = "Monthly_Avg_5_9pm" + mon[mon_index]

        # increment iterator to advance to next month in list
        mon_index += 1

    # ###########################################################################################################        

    arcpy.AddField_management(fc, avg_field, "FLOAT", "", "", "", "", "", "")
    arcpy.AddField_management(fc, avg_field_5_9, "FLOAT", "", "", "", "", "", "")

    print "Avg & Avg_5_9pm field addition completed for " + fc + "!\n"        

    # ###########################################################################################################        

    field_list = arcpy.ListFields(fc)   # create a list of all fields in the FC (to search for WS fields)
    field_array = []                    # create an array that will contain the WS fields    

    # add all WS fields to an array
    for field in field_list:
        if field.name[:3] == "WS_":
            field_array.append(field.name)          # field_array[0] through field.array[23]
    field_array.append(avg_field)                   # field_array[24]
    field_array.append(avg_field_5_9)               # field_array[25]

    # ###########################################################################################################
    # Calculate values for Avg and Avg_5_9pm fields

    print "Starting Avg & Avg_5_9pm field calculation for " + fc + ".\n"

    with arcpy.da.UpdateCursor(fc, field_array) as cursor:
        for row in cursor:

            # monthly average calculation
            i = 0                       # set field iterator to zero (to coincide with 12:00am start value)
            hourly_sum = 0.0                            # set starting sum value for fields to zero
            while i < 24:
                hourly_sum += row[i]
                i += 1
            row_avg = hourly_sum / 24.0                 # get the average of the monthly values
            row[24] = row_avg                           # set monthly average field value

            # monthly average 5-9pm calculation
            i = 17                       # set field iterator to seventeen (to coincide with 5:00pm start value)
            hourly_sum_5_9pm = 0.0                      # set starting sum value for 5-9pm fields to zero
            while i < 22:
                hourly_sum_5_9pm += row[i]
                i += 1
            row_avg_5_9pm = hourly_sum_5_9pm / 5.0      # get the average of the monthly 5-9pm values
            row[25] = row_avg_5_9pm                     # set monthly 5-9pm average field value

            cursor.updateRow(row)       # update current row and proceed to next row            

    print "Monthly_Avg & Monthly_Avg_5_9pm field calculation completed for " + fc + "!\n"

# ###########################################################################################################
# ###########################################################################################################

# delete extraneous fields from feature classes

for fc in prj_fc_all:

    print "Starting extraneous field deletion for " + fc + ".\n"

    field_list = arcpy.ListFields(fc)
    for field in field_list:
        if (field.name[:3] == "WK_" or field.name[:3] == "WC_" or field.name[:3] == "WS_"
            or field.name[:] == "iwtk" or field.name[:] == "prot" or field.name[:] == "num"
            or field.name[:] == "ialiq" or field.name[:] == "lon" or field.name[:] == "lat"):
            # delete the extraneous field
            arcpy.DeleteField_management(fc, field.name)         

    print "Extraneous field deletion completed for " + fc + "!\n"

# ###########################################################################################################
# ###########################################################################################################

end_time = time.clock()             # time at end of script execution

# calculate elapsed time in hours, minutes, and seconds
elapsed_time = end_time - start_time
hours = elapsed_time / 3600
minutes = elapsed_time % 3600
minutes = minutes / 60
seconds = minutes % 60

print str(int(hours)) + ' hours, ' + str(int(minutes)) + ' minutes, ' + '%.2f' % (seconds) + ' seconds.' # All done!
