# seatsArray = input("input seats arrangement:")
# no_of_passengers = input("input the no of passengers:")

# columns, rows
seatsArray = [[3,2], [4,3], [2,3], [3,4]]

seats_id = []

totalColumns = 0
totalRows = 0

no_of_passengers = 30

aisleSeats = []
windowSeats = []
middleSeats = []

def cal_seats_id(totalColumns, totalRows):
  for (index, eachArray) in enumerate(seatsArray):
    columns = eachArray[0]
    totalColumns = totalColumns + columns
    
    rows = eachArray[-1]
    totalRows = totalRows + rows
  
  for eachRow in range(totalRows):
    for eachColumn in range(totalColumns):
      seats_id.append([eachColumn, eachRow])


cal_seats_id(totalColumns, totalRows)


def find_asile_seats(seatsArray):
  rowCount = 0
  columnCount = 0
  for (index, eachArray) in enumerate(seatsArray):
    global totalColumns
    global totalRows

    columns = eachArray[0]
    rows = eachArray[-1]

    if (index == 0):
      for eachRow in range(rows):
        for eachColumn in range(columns):
          # assign asile seats in the first array
          if ((eachColumn+1) == columns):
            aisleSeats.append([eachColumn, eachRow])

    elif ((index+1) == len(seatsArray)):
      for eachRow in range(rows):
        for eachColumn in range(columns):
          if (eachColumn == 0):
            # aisle seats in the last array
            aisleSeats.append([columnCount, eachRow])

    else:
      for eachRow in range(rows):
        for eachColumn in range(columns):
          if (eachColumn == 0):
            aisleSeats.append([columnCount, eachRow])

          elif ((eachColumn) == (columns-1)):
            tempCol = columnCount + eachColumn
            aisleSeats.append([tempCol, eachRow])

    rowCount = rowCount + rows
    columnCount = columnCount + columns
        

find_asile_seats(seatsArray)

# sort by row to go from left to right while assigning
aisleSeats.sort(key=lambda x : x[1])

def find_window_seats(seatsArray):
  rowCount = 0
  columnCount = 0

  for (index, eachArray) in enumerate(seatsArray):

    columns = eachArray[0]
    rows = eachArray[-1]
    
    if(index == 0):
      for eachRow in range(rows):
        for eachColumn in range(columns):
          if(eachColumn == 0):
            windowSeats.append([columnCount, eachRow])
      
    elif ((index+1) == len(seatsArray)):
      for eachRow in range(rows):
        for eachColumn in range(columns):
          if(eachColumn == (columns-1)):
            tempCol = columnCount + eachColumn
            windowSeats.append([tempCol, eachRow])

    rowCount = rowCount + rows
    columnCount = columnCount + columns

find_window_seats(seatsArray)

# sort by row to go from left to right while assigning
windowSeats.sort(key=lambda x : x[1])

seated_passenger = 0

for eachEle in aisleSeats:
  print("assignable aisle seat for", seated_passenger, "is",eachEle)
  seated_passenger = seated_passenger + 1

print(" ")

for eachEle in windowSeats:
  print("assignable window seat for", seated_passenger, "is", eachEle)
  seated_passenger = seated_passenger + 1

print(" ")

# for seats in seats_id:
#   print(seats)
# print('the aisle seats are', aisleSeats)
# print(totalColumns, "total Cols")
# print(totalRows, "total rows")
# print(seatsArray, no_of_passengers)