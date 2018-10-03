import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from sense_hat import SenseHat
from time import time, sleep
import os
import sys
import random
from math import floor, ceil

serviceAccountKey = '../../labo2-simodecl-firebase-adminsdk-e8msv-e190f34af0.json'
databaseURL = 'https://labo2-simodecl.firebaseio.com'

try:
    # Fetch the service account key JSON file contents
    firebase_cred = credentials.Certificate(serviceAccountKey)

    # Initalize the app with a service account; granting admin privileges
    firebase_admin.initialize_app(firebase_cred, {
    'databaseURL': databaseURL
    })

    # As an admin, the app has access to read and write all data
    firebase_ref_arcade_characters = db.reference('arcade-characters')
except:
    print('Unable to initialize Firebase: {}'.format(sys.exc_info()[0]))
    sys.exit(1)

# constants
COLOR_RED = (255, 0, 0)
COLOR_BLUE = (0, 0, 255)
COLOR_BLACK = (0, 0, 0)

# get random arcade matrix
def get_random_arcade_matrix(rows, cols):
    pattern = ''
    matrix = []
    print(int(rows)*int(cols))
    for r in range(0, int(rows)):
        temp_str = ''
        for c in range(0, (int(cols)//2)):
            temp_str = temp_str + str(round(random.random()))

        temp_str = temp_str + temp_str[::-1]
        pattern = pattern + temp_str + (8-int(cols)) * '0'
        print(pattern)
    pattern = pattern +  (8-int(rows))* 8 * '0'
    print('Eindpatroon: ' + pattern)
    for p in range(0, 64):
        bit = int(pattern[p])
        color = COLOR_BLUE if bit == 1 else COLOR_BLACK
        matrix.append(color)

    return(matrix)

def get_character_from_db():
    characters = firebase_ref_arcade_characters.get()
    i = 0
    character = []
    #print(characters)
    if characters is not None:
        for key, val in characters.items():
            character.append(val)
          

        while i < len(character):
            #print(character)
            sense_hat.set_pixels(character[i])
            i += 1
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
        get_character_from_db()
            
        
if __name__ == "__main__":
    try:
        main()
    except (KeyboardInterrupt, SystemExit):
        print('Interrupt received! Stopping the application...')
    finally:
        print('Cleaning up the mess...')
        sense_hat.clear()
        sys.exit(0)