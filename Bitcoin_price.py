import requests
import json
def BitCoin_price(Currency,value):
    url="https://blockchain.info/ticker"
    fop=" https://blockchain.info/ticker?currency ="+str(Currency)+"&value="+str(value)
    print(fop)
    response=requests.get(fop)
    #print(response,response.text,type(response.text))
    j_response=json.loads(response.text)
    #print(j_response,type(j_response))
    usd_value=str(j_response['USD']["symbol"])+"  "+str(j_response['USD']["last"])
    print("The value in USD is : "+usd_value)
    key="83d32efcf69d48899d6e82006d86489d"
    fop2="http://data.fixer.io/api/convert?access_key="+key+"&from=USD&to=INR&amount="+str(usd_value)
    resp=requests.get(fop2)
    j_resp=json.loads(resp.text)
    #print(j_resp)
    #inr_value=j_resp["rates"]["1"]["INR"]*usd_value
    inr_value="RS. "+str(71.73*j_response['USD']["last"])
    print("THe value in INR is : "+str(inr_value))
BitCoin_price(input("Enter the Currency Code"),input("Enter the value"))
#all tweets from twitter related to a particular key word
#py,P,SQL,Java,HTML,CSS
