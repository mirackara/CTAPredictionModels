import pandas
import datetime
import calendar
import numpy as np
import matplotlib.pyplot as plt

'''
Assignment 1.[15 Points] Write a Python function that takes a file name, as a string s, on input and, when called with s = ’CTA-Ridership-L-Station-Entries-Daily-Totals.csv’ 
reads in all data contained in the file. You are strongly #encouraged to use the Pandas module for this task (as #illustrated in lecture notes) but you are free to write #your own CSV file reader, 
if you want. The function you #write to complete Assignment 1 will be used to complete #the subsequent assignments below.
'''

def Assignment1(s):
  #Sorts the data from the csv file into a nicely formated data list
  data = pandas.read_csv(s, names=['station_id','stationname','date','daytype','rides'], skiprows=[0])
  return data

#Grabs the .csv file from PC location. NOTE: I had my csv named as cta.csv. Rename yours to corresponding file.
data = Assignment1('cta.csv')

'''Assignment 2.[15 Points] Write a function that prints to screen the average number of rides, for all months, for the UIC-Halsted (station id = 40350) train station.
 Use the solution from Assignment 1 to access the data.

The output of your function must have the format
January : average number of rides as a float 
February: average number of rides as a float 
December: average number of rides as a float
'''

ridesList = data['rides'].tolist()
datesList = data['date'].tolist()
stationnameList = data['stationname'].tolist()



print("Assignment 2")


def Assignment2():
  
# Variable for the amount of times a month is counted
  counterJan = 0 
  counterFeb = 0
  counterMar = 0
  counterApr= 0 
  counterMay = 0
  counterJune = 0
  counterJuly = 0
  counterAug = 0
  counterSept = 0
  counterOct = 0 
  counterNov = 0
  counterDec = 0

# Variable for the amount of rides
  janRides = 0.0
  febRides = 0.0
  marRides = 0.0
  aprRides = 0.0
  mayRides = 0.0
  juneRides = 0.0
  julyRides = 0.0
  augRides = 0.0
  septRides = 0.0
  octRides = 0.0
  novRides = 0.0
  decRides = 0.0
# In order to get our answer we have to divide rides/counter


  for i in range(len(datesList)):
    if stationnameList[i] == 'UIC-Halsted': #If the station is named 'UIC-Halsted'...
      
      if datesList[i][0] == '0': #If the month is month < 10 ...
        if datesList[i][1] == '1': #If the month is 'x' month...
          janRides += ridesList[i] # Add the rides from the list 
          counterJan+=1 #Increase counter by 1
        elif datesList[i][1] == '2':
          febRides += ridesList[i]
          counterFeb+=1
        elif datesList[i][1] == '3':
          marRides += ridesList[i]
          counterMar+=1
        elif datesList[i][1] == '4':
          aprRides += ridesList[i]
          counterApr+=1
        elif datesList[i][1] == '5':
          mayRides += ridesList[i]
          counterMay+=1
        elif datesList[i][1] == '6':
          juneRides += ridesList[i]
          counterJune+=1
        elif datesList[i][1] == '7':
          julyRides += ridesList[i]
          counterJuly+=1
        elif datesList[i][1] == '8':
          augRides += ridesList[i]
          counterAug+=1
        elif datesList[i][1] == '9':
          septRides += ridesList[i]
          counterSept+=1
      if datesList[i][0] == '1':
        if datesList[i][1] == '0':
          octRides += ridesList[i]
          counterOct+=1
        elif datesList[i][1] == '1':
          novRides += ridesList[i]
          counterNov+=1
        elif datesList[i][1] == '2':
          decRides += ridesList[i]
          counterDec+=1


  print('January: ' , janRides/counterJan)
  print('February: ', febRides/counterFeb)
  print('March: ', marRides/counterMar)
  print('April: ', aprRides/counterApr)
  print('May: ', mayRides/counterMay)
  print('June: ', juneRides/counterJune )
  print('July: ',julyRides/counterJuly )
  print('August: ',augRides/counterAug)
  print('September: ', septRides/counterSept )
  print('October: ',octRides/counterOct)
  print('November: ', novRides/counterNov )
  print('December: ',decRides/counterDec )
  
Assignment2()


print('Assignment 3')


def getWeekday(year, month, day):
    """
    input: integers year, month, day
    output: name of the weekday on that date as a string
    """
    date = datetime.date(year, month, day) 
    return calendar.day_name[date.weekday()]


def Assignment3():

  '''
Assignment 3.[20 Points] Write a function that computes the average number of rides, 
for all days of the week, for the UIC-Halsted (station id = 40350) train station. 
Use the solution from Assignment 1 to access the data. 
Assign the value of 1 for Monday, 2 for Tuesday, ... , and 7 for Sunday. 
Using the polynomial curve fitting capabilities of NumPy, fit the data with a polynomial of degree 6.
predict the number of rides on a Wednesday for the UIC-Halsted train station
estimate which day of the week is the UIC-Halsted trains station most busy
estimate which day of the week is the UIC-Halsted trains station least busy
  '''

# Days of the week
  monday = 1
  tuesday = 2
  wednesday = 3
  thursday = 4
  friday = 5
  saturday = 6
  sunday = 7

# Variable for the day counter
  counterMon = 0.0
  counterTues = 0.0
  counterWed = 0
  counterThurs = 0.0
  counterFriday = 0.0
  counterSat = 0.0
  counterSun = 0.0


# Variable for the amount of rides
  monRides = 0.0
  tuesRides = 0.0
  wedRides = 0.0
  thursRides = 0.0
  friRides = 0.0
  satRides = 0.0
  sunRides = 0.0



  datesSorted = [] #We have to sort the dates as well as convert to ints if we want to check it against the dates
  
  for i in datesList: #Sorts the list
    datesSorted.append(i.split('/'))

  for i in range(len(datesSorted)): #Makes sure all values in the list are ints
      for x in range(len(datesSorted[i])):
          if type(datesSorted[i][x]) != int:
              datesSorted[i][x] = int(datesSorted[i][x])

  for i in range(len(ridesList)):
    if stationnameList[i] == 'UIC-Halsted': #If the station name is UIC-Halsted...
        if getWeekday(datesSorted[i][2], datesSorted[i][0], datesSorted[i][1]) == 'Monday':#If the day is Monday,,,
          monRides += ridesList[i] # Add the rides from the list
          counterMon+= 1 # Increase counter by 1
        elif getWeekday(datesSorted[i][2], datesSorted[i][0], datesSorted[i][1]) == 'Tuesday':
          tuesRides +=ridesList[i]
          counterTues+=1
        elif getWeekday(datesSorted[i][2], datesSorted[i][0], datesSorted[i][1]) == 'Wednesday':
          wedRides +=ridesList[i]
          counterWed+=1
        elif getWeekday(datesSorted[i][2], datesSorted[i][0], datesSorted[i][1]) == 'Thursday':
          thursRides +=ridesList[i]
          counterThurs+=1
        elif getWeekday(datesSorted[i][2], datesSorted[i][0], datesSorted[i][1]) == 'Friday':
          friRides +=ridesList[i]
          counterFriday+=1
        elif getWeekday(datesSorted[i][2], datesSorted[i][0], datesSorted[i][1]) == 'Saturday':
          satRides +=ridesList[i]
          counterSat+=1
        elif getWeekday(datesSorted[i][2], datesSorted[i][0], datesSorted[i][1]) == 'Sunday':
          sunRides +=ridesList[i]
          counterSun+=1
  
  #Variables to add up the average number of rides per day  
  monTotal=monRides/counterMon
  tuesTotal= tuesRides/counterTues
  wedTotal = wedRides/counterWed
  thursTotal= thursRides/counterThurs
  friTotal = friRides/counterFriday
  satTotal = satRides/counterSat
  sunTotal = sunRides/counterSun


  print('Mondays: ', monTotal)
  print('Tuesday: ', tuesTotal)
  print('Wednesday: ', wedTotal)
  print('Thursday: ', thursTotal)
  print('Friday: ', friTotal)
  print('Saturday: ', satTotal)
  print('Sunday: ', sunTotal)

  #List of all weekdays 
  weekdays = [monday,tuesday,wednesday,thursday,friday,saturday,sunday]
  x = weekdays
  y = [monTotal, tuesTotal, wedTotal, thursTotal, friTotal, satTotal, sunTotal]
  f = np.polyfit(x, y, 6)
  F = np.poly1d(f)

  #Plots the graph (X: Weekdays Y: Average Rides per days)
  plt.plot(x, y, 'bo')

  print("Prediction for the number of rides on a Wednesday for the UIC-Halsted train station: " + str(wedTotal))
  print("Estimate for which day of the week is the UIC-Halsted trains station most busy: " + str(max(y)))
  print("Estimate for which day of the week is the UIC-Halsted trains station least busy: " + str(min(y)))
  #Plots data on graph
  plt.plot(x, F(x))



Assignment3()
