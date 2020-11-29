# Import necessary modules and else
from microbit import *
import neopixel
import radio
import music
from random import randint
from gesture import *
from ultrasonic import *


# Setup the Neopixel strip on pin0 with a length of 30 pixels
np = neopixel.NeoPixel(pin1, 30)
variable = 400;

# Turn on the radio function to ensure two kits could communicate with each other
radio.on()

# Set the channel and transmitting power
radio.config(channel = 20)
radio.config(power = 7)

# Define the gesture for better conviences
gesture = Gesture()

while True:
    #Iterate over each LED in the strip
    for pixel_id in range(0, len(np)):
        red = 255
        green = 0
        blue = 55

        # By having clear and sleep set as 5, skipping standby mode would be achieved
        np.clear()
        sleep(5)

        # Assign the current LED a purple skipping colour
        np[pixel_id] = (red, green, blue)

        # Read gesture input
        g = gesture.read()

        # Button a pressed acting like a fail safe, so the new message could still be checked when needed
        if g == 'up' or button_a.is_pressed():

            radio.send("dinner")
            lightstrip = 0
            length = range(len(np))
            red = randint(10, 100)
            green = randint(10, 100)
            blue = randint(10, 100)


            for lightstrip in length:
                np[lightstrip] = (red, green, blue)
                display.show(Image.HEART)
                np.show()
                sleep(60)

                # Clear the logo after the LED notification is over
                display.clear()

            #np[pixel_id] = (red, green, blue)



        if g == 'down':

            radio.send("game")

            lightstrip = 0
            length = range(len(np))

            red = randint(200, 200)
            green = randint(200, 200)
            blue = randint(200, 200)
            for lightstrip in length:
                np[lightstrip] = (red, green, blue)
                display.show(Image.HEART_SMALL)
                np.show()
                sleep(60)
                display.clear()

        # When gesture is left, indicating sleeping mode and put the device on to sleep
        if g == "left":

            lightstrip = 0
            length = range(len(np))

            red = 0
            green = 0
            blue = 0
            for lightstrip in length:
                np[lightstrip] = (red, green, blue)
                display.show(Image.ASLEEP)
                np.clear()
                sleep(20000)
                display.clear()

        rf = Rangefinder(pin0)
        dist = rf.distance_cm()

        # Receive possible messages
        incoming_message = radio.receive()

        if dist > 15 and dist < 55:
            # Using radio.send to send a message to another kit when in range of ultraranger sensor
            radio.send("Care")

            lightstrip = 0
            length = range(len(np))
            red = 255
            green = 186
            blue = 195


            for lightstrip in length:
                np[lightstrip] = (red, green, blue)
                display.show(Image.COW)
                np.show()
                sleep(20)

                # Clear the logo after the LED notification is over
                display.clear()

        if dist < 5:
            # Send help to another kit if dist is less than 5
            radio.send("Help")

            lightstrip = 0
            length = range(len(np))
            red = 255
            green = 0
            blue = 33


            for lightstrip in length:

                np[lightstrip] = (red, green, blue)
                display.show(Image.SKULL)
                np.show()
                sleep(20)

                # Clear the logo after the LED notification is over
                display.clear()

        # Check the incoming messages
        if incoming_message == "Care":
            display.scroll("Hope you are doing well !")
            #music.play(music.BLUES)
            lightstrip = 0
            length = range(len(np))

            # Set up a series of colour to be displayed
            red1 = 255
            green1 = 196
            blue1 = 195

            for lightstrip in length:
                np[lightstrip] = (red1, green1, blue1)
                # display.scroll("Hope you doing well")
                display.show(Image.COW)

                np.show()
                sleep(35)
                display.clear()

        if incoming_message == "Help":
            display.scroll("PLEASE HELP")
            #music.play(music.stop)
            lightstrip = 0
            length = range(len(np))



            # Set up a series of colour to be displayed
            red = 255
            green = 0
            blue = 33

            for lightstrip in length:
                np[lightstrip] = (red, green, blue)
                #display.scroll("HELP")
                display.show(Image.SKULL)

                np.show()
                sleep(35)
                display.clear()

        if incoming_message == "dinner":
            display.scroll("Care for a zoom drink tonight ?")
            #music.play(music.stop)
            lightstrip = 0
            length = range(len(np))



            # Set up a series of colour to be displayed
            red = 252
            green = 162
            blue = 234

            for lightstrip in length:
                np[lightstrip] = (red, green, blue)
                #display.scroll("HELP")
                display.show(Image.HEART)

                np.show()
                sleep(35)
                display.clear()

        if incoming_message == "game":
            display.scroll("Care for a game sesh later ?")
            #music.play(music.stop)
            lightstrip = 0
            length = range(len(np))



            # Set up a series of colour to be displayed
            red = 162
            green = 236
            blue = 252

            for lightstrip in length:
                np[lightstrip] = (red, green, blue)
                #display.scroll("HELP")
                display.show(Image.FABULOUS)

                np.show()
                sleep(35)
                display.clear()




        # Display the current pixel data on the Neopixel strip
        np.show()
        sleep(100)






