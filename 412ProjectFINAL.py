  
#imports
import urllib.request

#Download and read the lines of the file using for loop
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "412File")

with open("412File.txt", "r") as File:
    Count=0
    for line in File:
        Line=line.split(" ")
        Location=Line[0]
        while Count<5:
            print(Location)
            Count+=1
