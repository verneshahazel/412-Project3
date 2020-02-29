#imports
import urllib.request

#Download and read the lines of the file using for loop
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "412File")

with open("412File.txt", "r") as File:
    Count=0
    LocationList=[]
    DashList1=[]
    DashList2=[]
    DateList=[]
    TimeZoneList=[]
    GETList=[]
    
    for line in File:
        Line=line.split(" ")
        
        #Here lies my data which I am splitting apart by spaces. I am ignoring all special cases where a string/instance of data could possibly be formatted differently. i.e. a piece of information is missing or added causing the string to be longer or shorter. I will not be using regular expressions. 
        Location=Line[0]
        Dash=Line[1]
        Dash2=Line[2]
        Date=Line[3] #Come back and remove leading " [ "
        TimeZone=Line[4] #Come back and remove ending " ] "
        GET=Line[5]
        
        #append split data to it's respective list
        
        LocationList.append(Location)
        DashList1.append(Dash)
        DashList2.append(Dash2)
        DateList.append(Date)
        TimeZoneList.append(TimeZone)
        GETList.append(GET)
        
        while Count<5: #This while loop is just so that it stops trying to run the whole data set because that's stressing my poor computer out
            print(Location)
            print(Dash)
            print(Dash2)
            print(Date)
            print(TimeZone)
            print(GET)
            Count+=1
    
    print()
    print(f" There were {Count} total requests made in the time period requested in the log.")
