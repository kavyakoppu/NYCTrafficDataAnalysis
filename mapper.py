# Few records of data collected from NYC traffic data website :

# DATE,TIME,BOROUGH,ZIP CODE,LATITUDE,LONGITUDE,LOCATION,ON STREET NAME,CROSS STREET NAME,OFF STREET NAME,NUMBER OF PERSONS INJURED,NUMBER OF PERSONS KILLED,NUMBER OF PEDESTRIANS INJURED,NUMBER OF PEDESTRIANS KILLED,NUMBER OF CYCLIST INJURED,NUMBER OF CYCLIST KILLED,NUMBER OF MOTORIST INJURED,NUMBER OF MOTORIST KILLED,CONTRIBUTING FACTOR VEHICLE 1,CONTRIBUTING FACTOR VEHICLE 2,CONTRIBUTING FACTOR VEHICLE 3,CONTRIBUTING FACTOR VEHICLE 4,CONTRIBUTING FACTOR VEHICLE 5,UNIQUE KEY,VEHICLE TYPE CODE 1,VEHICLE TYPE CODE 2,VEHICLE TYPE CODE 3,VEHICLE TYPE CODE 4,VEHICLE TYPE CODE 5
# 04/07/2019,0:00,BROOKLYN,11221,40.68569,-73.93559,"(40.68569, -73.93559)",LEWIS AVENUE                    ,PUTNAM AVENUE,,0,0,0,0,0,0,0,0,Traffic Control Disregarded,Unspecified,,,,4110071,Sedan,Taxi,,,
# 04/07/2019,0:00,BROOKLYN,11225,40.663124,-73.96244,"(40.663124, -73.96244)",FLATBUSH AVENUE                 ,EMPIRE BOULEVARD,,0,0,0,0,0,0,0,0,Driver Inattention/Distraction,Unspecified,,,,4110921,Sedan,Taxi,,,
# 04/07/2019,0:00,STATEN ISLAND,10312,40.557377,-74.18158,"(40.557377, -74.18158)",,,22        ERIKA LOOP                    ,0,0,0,0,0,0,0,0,Driver Inattention/Distraction,Unspecified,,,,4110530,Sedan,,,,

# We need to analyse the count of vehicle types that are ivolved in incidents - So our data of interest is after 24 columns i.e, last five coloumns (VEHICLE TYPE CODE 1 to 5)

#!/usr/bin/env python
"""mapper.py"""

import sys

# input comes from STDIN (standard input)
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()    
    # split the line into columns
    columns = line.split(',')
    # consider only last five columns of data
    vehicletypecodes = columns[-5:]
    # increase counters
    for vehicletypevalue in vehicletypecodes:
        # skip first row - header
        if('VEHICLE TYPE CODE' in vehicletypevalue) :
            continue
        if (vehicletypevalue != '') :
            # ('VEHICLE TYPE CODE' not in vehicletypevalue) 
            # if vehicletypevalue is not null, write the results to STDOUT; what we output here will be the input for reducer.py
            print '%s\t%s' % (vehicletypevalue, 1)
            # tab-delimited;