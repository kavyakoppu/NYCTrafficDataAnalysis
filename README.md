# NYCTrafficDataAnalysis4
Analyze the NYC traffic data using mapper and reducer scripts and yield summary counts for each vehicle involved in an incident, per vehicle type.

## Pre-requisites:  
* Data to be analyzed was collected from the City of New York’s data website, and contains all reports of vehicular incidents in New York City over a period of time.  
* Data is already uploaded in the following location :  
`/user/tatavag/nyc.data`  
* You can also export data into CSV from :  
[https://data.cityofnewyork.us/Public-Safety/NYPD-Motor-VehicleCollisions/h9gi-nx95]  
* Login to Hadoop Server using your credentials from putty  
* Clone this repository into hadoop  
`git clone https://github.uc.edu/koppuka/NYCTrafficDataAnalysis4.git`  
* Move to git project folder path  
`cd NYCTrafficDataAnalysis4`  

## General Hadoop Commands:  
* List directory  
`hadoop fs -ls`  
* Create directory  
`hadoop fs -mkdir <dirname>`  
* Delete directory  
`hadoop fs -rm -r <dirname>`  
* Delete File  
`hadoop fs -rm <dirname>/<filename>`  
* Display content of file  
`hadoop fs -cat <fileNameWithPath>`  
* View first N lines in a file  
` hadoop fs -cat <fileNameWithPath> | head -n N`  
* Get a file from Hadoop Cluster   
`hadoop fs -copyToLocal <sourcepath> <destinationpath>`  
* Put file into HDFS  
`hadoop fs -put <filename> <destination directory on hdfs>`  

## Running Mapper and Reducer Scripts:  
* To run MapReduce and get result in local:  
koppuka@hadoop-gate-0:~/NYCTrafficDataAnalysis4$ `hadoop fs -cat <inputDataPath> | python mapper.py | sort | python reducer.py`  
* To run in hadoop cluster using Hadoop Streaming jar :  
koppuka@hadoop-gate-0:~/NYCTrafficDataAnalysis4$ `hadoop jar /usr/hdp/current/hadoop-mapreduce-client/hadoop-streaming.jar -file mapper.py -mapper mapper.py -file reducer.py -reducer reducer.py -input /user/tatavag/nyc.data -output hadoopstreamingoutput`  
* or you can use different Hadoop streaming jar based on version :
koppuka@hadoop-gate-0:~/NYCTrafficDataAnalysis4$ `hadoop jar /usr/hdp/3.1.0.0-78/hadoop-mapreduce/hadoop-streaming-3.1.1.3.1.0.0-78.jar -file mapper.py -mapper 'python mapper.py' -file reducer.py -reducer 'python reducer.py' -input /user/tatavag/nyc.data -output hadoopstreamingoutput`  
* To view results in output file :  
`hadoop fs -cat hadoopstreamingoutput/*`  

## Useful Links :  
[https://piazza.com/class_profile/get_resource/jqx71md1irpi8/jt6bq54ho6j3mb]  
[http://www.michael-noll.com/tutorials/writing-an-hadoop-mapreduce-program-in-python/]  
[https://hadoop.apache.org/docs/r1.2.1/streaming.html]  
