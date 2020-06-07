# Sales invoice finder program

salesFile = open ("sales_data.csv", "r")

# Capture only vaild input
while True:
    searchBy = input("Search by invoice id (id) or customer last name (lname)? ")
    if searchBy == "id" or searchBy == "lname":
        searchTerm = input("Enter your search term: ")
        break
    else:
        print("ERROR: You must enter either 'id' for invoice id search or 'lname' for customer last name search")                    

# Since there are only two valid choices we only need to check once to determine which element to compare in the sequence
if searchBy == "id":
    index = 0
else:
    index = 2
    
totalRecords = 0
# Loop through the sales file until no record is returned
lineItem = salesFile.readline()
while lineItem:
    # Split the lineItem into a sequence of items to be searched
    item = lineItem.split(",")
    # If the search term is in the line item print the line item and increment the accumulator 
    if searchTerm == item[index]:
        totalRecords = totalRecords + 1
        print (lineItem.strip())
    lineItem = salesFile.readline()

# Print a total when finished searching the file
print ("{0} records found.".format(totalRecords))
salesFile.close()
