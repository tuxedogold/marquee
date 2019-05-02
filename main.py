from sense_hat import SenseHat
from time import sleep
import requests,json

def get_kanye_quote():
    response = requests.get('http://api.kanye.rest')
    print(response.json())
    data = json.loads(response.text)
    return data.get('quote')

sense = SenseHat()
sense.set_rotation(180)
sense.clear(0,0,0)

amount_vibrations = 100

ton_of_vibrations = [0.1 for i in range(amount_vibrations)]

while(True):
    x,y,z = sense.get_accelerometer_raw().values()
    
    sleep(0.1)

    normal_vibration = sum(ton_of_vibrations)/amount_vibrations
    normal_vibration_variance = 1.1 * normal_vibration
    print(x,normal_vibration)
    if x > normal_vibration_variance: # or y > normal_vibration or z > normal_vibration:
        quote = get_kanye_quote()
        #quote = "lol"
        sense.show_message(quote)
    ton_of_vibrations.pop()
    ton_of_vibrations.insert(-1,x)


