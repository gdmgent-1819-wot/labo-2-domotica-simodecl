import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from sense_hat import SenseHat
from time import time, sleep
import os
import sys
import random
from math import floor, ceil

serviceAccountKey = '../../labo2-domotica-simodecl-firebase-adminsdk-zm609-4147ea9d6d.json'
databaseURL = 'https://labo2-domotica-simodecl.firebaseio.com'

try:
    # Fetch the service account key JSON file contents
    firebase_cred = credentials.Certificate(serviceAccountKey)

    # Initalize the app with a service account; granting admin privileges
    firebase_admin.initialize_app(firebase_cred, {
    'databaseURL': databaseURL
    })

    # As an admin, the app has access to read and write all data
    firebase_ref_domotica = db.reference()
except:
    print('Unable to initialize Firebase: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

# constants
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_DARKBLUE = (0, 0, 50)
COLOR_GREEN = (0, 255, 0)
COLOR_YELLOW = (255, 255, 0)
COLOR_DARKYELLOW = (50, 50, 0)
COLOR_BLACK = (0, 0, 0)


def get_domotica_from_db():
    domoticaRef = firebase_ref_domotica.get()
    i = 0
    domotica = []
    if domoticaRef is not None:
        for key, val in domoticaRef.items():
            for p in range(0, 64):
                letter = val[p]
                if letter == "g":
                    color = COLOR_GREEN
                elif letter == "r":
                    color = COLOR_RED
                elif letter == "b":
                    color = COLOR_BLUE
                elif letter == "db":
                    color = COLOR_DARKBLUE
                elif letter == "y":
                    color = COLOR_YELLOW
                elif letter == "dy":
                    color = COLOR_DARKYELLOW
                else:
                    color = COLOR_BLACK
                            
                domotica.append(color)
                  
        sense_hat.set_pixels(domotica)
        sleep(1)
           

    else:
        sense_hat.show_message("404")
try:
    # SenseHat
    sense_hat = SenseHat()
    sense_hat.set_imu_config(False, False, False)
except:
    print('Unable to initialize the Sense Hat library: {}'.format(sys.exc_info()[0]))
    sys.exit(1)
    
def main():
    while True:
        get_domotica_from_db()
            
        
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sense_hat.clear()
        sys.exit(0)