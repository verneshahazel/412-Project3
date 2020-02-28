  
#imports
import urllib.request

#Download and read the lines of the file using for loop
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "412File")

with open("412File.txt", "r") as File:
    Count=0
    LocationList=[]
    for line in File:
        Line=line.split(" ")
        
        #Here lies my data which I am splitting apart by spaces. I am ignoring all special cases where a string/instance of data could possibly be formatted differently. i.e. a piece of information is missing or added causing the string to be longer or shorter. I will not be using regular expressions. 
        Location=Line[0]
        Dash=Line[1]
        Dash2=Line[2]
        
        
        LocationList.append(Location)
        while Count<5:
            print(Location)
            print(Dash)
            print(Dash2)
            Count+=1
