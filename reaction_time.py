# -*- coding: utf-8 -*-
"""
Created on Mon Feb  1 10:52:18 2021

@author: alentini1
"""

import random
from time import time, sleep

print ("Welcome to reaction time tester")
print ("When the prompt appears hit emter!")
print ("Get ready")

prompt = random.random() * 5
sleep(prompt)
start_time = time()
print ("Quick, hit enter!")
input()
reaction_time = time() - start_time
print (f"Wow, that was fast. It took {reaction_time:.3f}")