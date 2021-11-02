
from  convertMillis import convertMillis
import csv



class get_timestamp():
    def __init__(self,timestamp,count,boundingbox):
        self.timestamp = timestamp
        self.count = count
        self.boundingbox = boundingbox    
    def timestamp_(self):
        timestamp_format = convertMillis.convertMillis(self.timestamp)
        with open('timestamp.csv', 'a+', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow([timestamp_format,self.count,self.boundingbox])            
            print(f' _______________________________________________ 總人數{self.count}   {self.boundingbox}')