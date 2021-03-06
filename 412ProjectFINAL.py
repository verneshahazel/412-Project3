#imports
import urllib.request


#Download and read the lines of the file using for loop
urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "412File")
try:
    with open("412File.txt", "r") as File:
        Count=0
        LocationList=[]
        DashList1=[]
        DashList2=[]
        DateList=[]
        TimeZoneList=[]
        GETList=[]
        FileRequestedList=[]
        StatusCodeList=[]
        
        LocationDict={}
        MonthDict={}
        DayDict={}
        FileRequestedDict={}
        
        for line in File:
            while Count<5:
                Line=line.split(" ")
                Count+=1
                
                #Here lies my data which I am splitting apart by spaces. I am ignoring all special cases where a string/instance of data could possibly be formatted differently. i.e. a piece of information is missing or added causing the string to be longer or shorter. I will not be using regular expressions. 
                Location=Line[0]
                Dash=Line[1]
                Dash2=Line[2]
                Date=Line[3].strip("[") #Come back and remove leading " [ "
                TimeZone=Line[4].strip("]") #Come back and remove ending " ] "
                GET=Line[5]
                FileRequested=Line[6]
                StatusCode=Line[-2] #I kept getting the error "list index out of range" when I tried to say Line[7]
                
        
                #append split data to it's respective list
                
                LocationList.append(Location)
                DashList1.append(Dash)
                DashList2.append(Dash2)
                DateList.append(Date)
                TimeZoneList.append(TimeZone)
                GETList.append(GET)
                FileRequestedList.append(FileRequested)
                StatusCodeList.append(StatusCode)
                
                #while Count<5: #This while loop is just so that it stops trying to run the whole data set because that's stressing my poor computer out
                    #print(Location)
                    #print(Dash)
                    #print(Dash2)
                    #print(Date)
                    #print(TimeZone)
                    #print(GET)
                    #print(FileRequested)
                    #print(StatusCode)
                    #Count+=1
                    
                for item in LocationList:
                    if item in LocationDict:
                        LocationDict[item]+=1
                    else:
                        LocationDict[item]=1
                            
                    #Find how many requests were made per month
                for date in DateList:
                    DateSplit=date.split("/")
                    Day=str(DateSplit[0:1]) #Was getting error "unhashable type: list"
                    Month=DateSplit[1]
                    Year=DateSplit[2]
               
               #Add and count contents in dictionaries     
               
                    if Month in MonthDict:
                        MonthDict[Month]+=1
                    else:
                        MonthDict[Month]=1
                        
                    if Day in DayDict:
                        DayDict[Day]+=1
                    else:
                        DayDict[Day]=1
                        
                #Do the same for files requested
                for file in FileRequestedList:
                    if file in FileRequestedDict:
                        FileRequestedDict[file]+=1
                    else:
                        FileRequestedDict[file]=1
                
                FileRequestedMax=0
                
                for file in FileRequestedDict:
                    if FileRequestedDict[file]>FileRequestedMax:
                        FileRequestedMax=FileRequestedDict[file]
                        MaxFile=file
                    if FileRequestedDict[file]==1:
                        MinFile=file
                        
            
                #Use a for loop to print contents of Dictionaries THIS WORKS!!!!!!!
                
        #for key in MonthDict:
            #print(f"There were {MonthDict[key]} requests made in {key}")
            
        #for key in DayDict:
            #print(f"There were {DayDict[key]} requests made on {key}")
            
        
        CodeCount400=0
        CodeCount300=0
        CodeCount200=0
        for code in StatusCodeList:
            if code=="400":
                CodeCount400+=1
            elif code=="300":
                CodeCount300+=1
            elif code=="200":
                CodeCount200+=1
                
        
        Percent400=(CodeCount400/Count)*100
        Percent300=(CodeCount300/Count)*100
        Percent200=(CodeCount200/Count)*100
        
            
         
         
    ###############DATA OUTPUT TO SCREEN#################        
        print("*******************************************************************************************")
        print(f"There were {Count} total requests made in the time period requested in the log.")
        
        for key in MonthDict:
            print(f"There were {MonthDict[key]} requests made in {key}")
       
        for key in DayDict:
            print(f"There were {DayDict[key]} requests made on {key}")        
        
        print(f"{Percent400}% of requests were not successful.")
        print(f"{Percent300}% of requests were redirected elsewhere.")
        
        print(f"{MaxFile} was the most-requested file.")
        print(f"{MinFile} was the least-requested file.")
        print("*******************************************************************************************")
    
except FileNotFoundError:
    urllib.request.urlretrieve("https://s3.amazonaws.com/tcmg476/http_access_log", "412File")
    print("File is being downloaded. Once the download is complete, save the file as '412File' and run this program again."
