from api import AirNow_Curr, AirNow_Pred
from fileReader import ExcelReader
from fileWriter import ExcelWriter
import numpy
import time
import datetime

data = numpy.array([['zipcode','Pred High','Current Ozone','Current PM2.5', 'Time Stamp']])

def main():
    global data
    apiKey='' #your API key
    airnow_curr = AirNow_Curr(apiKey)
    airnow_pred = AirNow_Pred(apiKey)

    excelReader = ExcelReader()
    excelReader.loadData('input.xlsx',1,1,3000)    

    for i in range(1, len(excelReader.data)):        

        zipcode = excelReader.data[i]

        val_pm2dot5_pred = ''

        val_Ozone_curr = ''

        val_pm2dot5_curr = ''

        jsonrslt1, resp1 = airnow_curr.makeRequest(zipcode)    

        jsonrslt2, resp2 = airnow_pred.makeRequest(zipcode)

        #Predicted High

        test_flag = 0;
        
        if(len(jsonrslt2)!=0):
            if(len(jsonrslt2[0])!=0):
                if(jsonrslt2[0]['ParameterName'] == 'PM2.5'):
                    test_flag = 1;                 

        if(test_flag == 1):
            #PM2.5(Predicted)
            val_pm2dot5_pred = jsonrslt2[0]['AQI']
        else:
            #PM2.5(Predicted)
            val_pm2dot5_pred = 'N/A'
            


        #Current Values

        rslt_len = len(jsonrslt1)
        found_pm2dot5_flag = -1;
        found_Ozone_flag = -1;

        if(rslt_len!=0):
            for j in range(0,rslt_len):
                if (len(jsonrslt1[j])!=0):
                    if (found_pm2dot5_flag!=-1 and found_Ozone_flag!=-1):
                        pass
                    elif (found_Ozone_flag == -1 and (jsonrslt1[j]['ParameterName'] == 'O3' or jsonrslt1[j]['ParameterName'].upper() == 'OZONE')):
                        found_Ozone_flag = j
                    elif(found_pm2dot5_flag == -1 and jsonrslt1[j]['ParameterName'] == 'PM2.5'):
                        found_pm2dot5_flag = j  
        

        if(found_Ozone_flag == -1):
            #Ozone
            val_Ozone_curr = 'N/A'
        else:
            #Ozone
            val_Ozone_curr = jsonrslt1[found_Ozone_flag]['AQI']

        if(found_pm2dot5_flag == -1):
            #PM2.5
            val_pm2dot5_curr = 'N/A'
        else:
            #PM2.5
            val_pm2dot5_curr = jsonrslt1[found_pm2dot5_flag]['AQI']
                

        data = numpy.vstack((data, numpy.array([[zipcode,val_pm2dot5_pred,val_Ozone_curr,val_pm2dot5_curr,datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")]])))
        print i        
        time.sleep(8) #less than 500 queries/hour
            
    
    excelWriter = ExcelWriter()
    excelWriter.write('output.xlsx',data)    


if __name__ == '__main__':
    try:
        main()
    except:
        excelWriter = ExcelWriter()
        excelWriter.write('output.xlsx',data) 
    
        
