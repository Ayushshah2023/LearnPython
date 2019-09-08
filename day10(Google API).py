import requests
import json
#application programming interface(API)
#swiggy uses api to communicate between FB,google,geolocation,payment getaway etc
#client to API has two requests , thus GET(to just get data) and POST(to tell some information to API)
#API has addresss in the form of endpoint
#api sends a response to client using JSON/xml
#figure API then endpoint(URL),Figure out the methods you can use,figure out parameters to send to the api
#city=Raleigh,NC&key=API_KEY are query parameters
def WeatherFore(loc):
    Key=str("95dace7de296455999e47ce82e8cda2e")
    #url=https://api.weatherbit.io/v2.0/current
    fop="https://api.weatherbit.io/v2.0/current?city="+loc+"&key="+Key
    print(fop)
    response=requests.get(fop)#sending a get response to the url
    #if(response.text=="temp"):
        #print(response.text)
    print(response,response.text,type(response.text))
    j_response=json.loads(response.text)
    print(j_response,type(j_response))
    current_temp=j_response['data'][0]["temp"]
    current_feel_temp=j_response['data'][0]["app_temp"]
    print("Current temperature"+str(current_temp))
    print("Current feel-like temperature"+str(current_feel_temp))
WeatherFore(input("Enter the city "))

#FInd the relevant API's
#find the end point of the APITHe parameters it will take
#find the type of response
#Send the request
#recieve the response
#parse the response to get the data that you want
#wap to print real time price of Bit coin in INR and USD
