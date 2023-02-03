import random
import requests

my_apikey="bc7f4fb01da32e200227651edf763045"

def getjson(place):
    link=f"https://api.openweathermap.org/data/2.5/weather?q={place}&appid={my_apikey}&units=metric"
    request_api=requests.get(link)
    weatherdatajson=request_api.json()
    return weatherdatajson

def temperature(place):
        temperaturejson=getjson(place)
        # print(temperaturejson)
        print(f"\ntemperature at {place} is ",temperaturejson['main']['temp'],"\n")

def weather(place):
    weatherjson=getjson(place)
    print(f"\nTemperature at {place} is ",weatherjson['main']['temp'],"\n")
    print(f"Humidity at {place} is ",weatherjson['main']['humidity'],"\n")
    print(f"Max temperature at {place} is ",weatherjson['main']['temp_max'],"\n")
    print(f"Windspeed at {place} is ",weatherjson['wind']['speed'],"\n")
    print(weatherjson['weather'][0]['description'],"\n")

def pressure(place):
        pressurejson=getjson(place)
        print(f"\nPressure at {place} is ",pressurejson['main']['pressure'],"\n")

def humidity(place):
        humidityjson=getjson(place)
        print(f"humidity at {place} is ",humidityjson['main']['humidity'],"\n")

def visibility(place):
        visibilityjson=getjson(place)
        print(f"visibility at {place} is ",visibilityjson['visibility'],"\n")

def windspeed(place):
        windspeedjson=getjson(place)
        print(f"windspeed at {place} is ",windspeedjson['wind']['speed'],"\n")

def sunrise(place):
        sunrisejson=getjson(place)
        print(f"sunrise at {place} is ",sunrisejson['sys']['sunrise'],"\n")

def sunset(place):
        sunsetjson=getjson(place)
        print(f"sunset at {place} is ",sunsetjson['sys']['sunset'],"\n")



greet=['hi','hello','ola','hello you','hello there','hey bot','hey','good morning','good afternoon','good evening','hiiii']
bot_greet=['hi there','Hello','hey!','Nice to see you ']
randomgreet=random.randint(0,len(bot_greet)-1)
# print(randomgreet)
goodbye=['bye','goodbye','bye bot','goodbye!','see you next time','see you again','thankyou']
bot_goodbye=['Bye!Hope to see you again','Goodbye','see you next time','Thank you! Hope I helped you']
randomgoodbye=random.randint(0,len(bot_goodbye)-1)
temp=['what is the temperature?','what is the temperature','temperature','tell me the weather','hows the weather','whats the max temperature?','temperature near me','what is temperature','what is temperature?']
weat=['what is the weather','what is weather','weather','what is the weather?','what is weather?','what is the climate?','what is the climate']
pres=['what is the pressure','what is pressure','pressure','what is the pressure?','what is pressure?']
humi=['what is the humidity','what is humidity','humidity','what is the humidity?','what is humidity?']
visibi=['what is the visibilty','what is visibility','visibility','what is the visibility?','what is visibility?']
windspe=['what is the windspeed','what is windspeed','windspeed','what is the windspeed?','what is windspeed?']
sunri=['sunrise','what was the time of sunrise','what was the time of sunrise today','what was the time of sunrise?',]
sunse=['sunset','what will be the time of sunset','what will be the time of sunset?']


print("************************")
while(True):
    print("\n\t\t\t\t",end=" ")
    userinput=input("").lower()
    if(userinput in greet):
        print(bot_greet[randomgreet],"\nWelcome to weather bot\n")
    elif(userinput in goodbye):
        print(bot_goodbye[randomgoodbye])
        break
    elif(userinput in temp):
        print("\nWhich place?\n")
        print("\t\t\t\t",end=" ")
        useri=input("")
        temperature(useri)
    elif(userinput in pres):
        print("\nWhich place?\n")
        print("\t\t\t\t",end=" ")
        useri=input("")
        pressure(useri)
    elif(userinput in humi):
        print("\nWhich place?\n")
        print("\t\t\t\t",end=" ")
        useri=input("")
        humidity(useri)
    elif(userinput in visibi):
        print("\nWhich place?\n")
        print("\t\t\t\t",end=" ")
        useri=input("")
        visibility(useri)
    elif(userinput in windspe):
        print("\nWhich place?\n")
        print("\t\t\t\t",end=" ")
        useri=input("")
        windspeed(useri)
    elif(userinput in sunri):
        print("\nWhich place?\n")
        print("\t\t\t\t",end=" ")
        useri=input("")
        sunrise(useri)
    elif(userinput in sunse):
        print("\nWhich place?\n")
        print("\t\t\t\t",end=" ")
        useri=input("")
        sunset(useri)
    elif(userinput in weat):
        print("\nWhich place?\n")
        print("\t\t\t\t",end=" ")
        useri=input("")
        weather(useri)
    else:
        print("I don't understand what you are saying")
print("************************")






















#  my_apikey="499fd4723659b54b68661a7a90693d6d"

    

        # link=f"https://api.openweathermap.org/data/2.5/weather?q={useri}&appid={my_apikey}&units=metric"
# 
        # request_api=requests.get(link)
        # weatherdatajson=request_api.json()
        # print(weatherdatajson)
# 
        # if(weatherdatajson['cod']==404):
            # print(f"Weather for {useri} is not available")
        # else:
            # curr_temp=((weatherdatajson['main']['temp']))
            # curr_weather_desc=((weatherdatajson['weather'][0]['description']))
            # curr_humidity=((weatherdatajson['main']['humidity']))
            # max_temp_today=((weatherdatajson['main']['temp_max']))
            # min_temp_today=((weatherdatajson['main']['temp_min']))
            # windspeed=((weatherdatajson['wind']['speed']))
# 
# 
        # print("--------------------------------------------------------")
        # print(f"Temperature at {useri} is {curr_temp} \n Humidity is {curr_humidity}\n")
        # print(f"current weather description is {curr_weather_desc}")
        # print(f"Today maximum temp at {useri} will be {max_temp_today}")
        # print(f"Today minimum temp at {useri} will be {min_temp_today}")
        # print(f"wind speed at {useri} is {windspeed}")