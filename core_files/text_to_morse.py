import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import time
import math 
from core_files.morse_data import MORSE_CODE

pygame.mixer.init(frequency=22050, size=-16, channels=1, buffer=512)

def tone(duration, freq=650, sample_rate=44500):
    samples = int(sample_rate * duration)
    tone=bytearray()
    for i in range(samples):
        value = int(10000 * math.sin(2 * math.pi * freq * i / sample_rate))
        tone += value.to_bytes(2, 'little', signed=True)
    return pygame.mixer.Sound(buffer=tone)

time_unit = 0.12

def play_dot():
    dot_sound=tone(time_unit)
    dot_sound.play()
    time.sleep(time_unit)

def play_dash():
    dash_sound=tone(time_unit*3)
    dash_sound.play()
    time.sleep(time_unit)
    
def transmit(message):
    message=message.upper()
    for char in message:
        time.sleep(time_unit * 7)
        if char == ' ':
            time.sleep(time_unit*10)
        elif char in MORSE_CODE:
            code=MORSE_CODE[char]
            for symbol in code:
                if symbol == ".":
                    play_dot()
                if symbol == "-":
                    play_dash()
                time.sleep(time_unit*2)