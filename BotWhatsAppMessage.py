import pywhatkit
import random

messageZap = ['Hello', 'Hello World'] # Enter the messages you want to send in randomness.
num = '+55' # Enter the number you want to send the message.

pywhatkit.sendwhatmsg(num, random.choice(messageZap), 6, random.randint(0, 36))
# If you want to send specific messages, just remove the "random.choice", I also recommend using remove the vector and using just string.
# With "random.randint" it's basically the same thing, it's the minutes, just remove and insert the minutes of your choice.