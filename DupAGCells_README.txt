Although the script functioned properly in identifying the duplicate cells, the process took quite a while to run (nested cursor looping through an outer cursor
for 323,000+ records).  Note that the script ONLY identifies the duplicate records by printing "True" whenever two records are found to have the same
longitude/latitude for a cell's centroid.  I don't recall exactly but it appears that in order to avoid a single record being identified falsely as two 
records with the same centroid coordinates (due to the inner cursor passing through the same record that the outer cursor is being iterated through), there 
is a null check to see if the Count field has a value (IIRC, the duplicates had null values in the Count field).  Whichever row (row_a (outer cursor) or row_b
(inner cursor)) has a null value in the Count field, the field values from the NON-null row are placed into the null row.

Note that this script was a work in progress.  The next step would have been to be able to select the duplicate rows and subsequently delete them from the
feature class.

As it was a much more time efficient process, topology was ultimately used to determine where duplicate cells existed and subsequently deleted...
