from api import AirNow_Curr, AirNow_Pred


def main():
    apiKey='' ## here insert your api key
    airnow_curr = AirNow_Curr(apiKey)
    airnow_pred = AirNow_Pred(apiKey)

    zipcode = '10001'

    jsonrslt1, resp1 = airnow_curr.makeRequest(zipcode)    

    jsonrslt2, resp2 = airnow_pred.makeRequest(zipcode)


    #Status 1
    print resp1

    if(len(jsonrslt1)!=0):        
        #Ozone
        print jsonrslt1[0]['AQI']

        #PM2.5
        print jsonrslt1[1]['AQI']
    else:
        #Ozone
        print 'N/A'

        #PM2.5
        print 'N/A'
        

    #Status 2
    print resp2

    if(len(jsonrslt2)!=0): 
        #PM2.5(Predicted)
        print jsonrslt2[0]['AQI']
    else:
        #PM2.5(Predicted)
        print 'N/A'


if __name__ == '__main__':
    main()
