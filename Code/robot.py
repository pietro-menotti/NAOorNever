# -*- coding: utf-8 -*-
from naoqi import ALProxy
from positions import *
import sys
import os
import time

import winsound  # Built-in Windows module for WAV playback
from threading import Thread

MANDATORY_POSITION = [
    'StandInit',
    'Sit',
    'Wipe_Forehead',
    'Stand',
    'Hello',
    'SitRelax',
    'StandZero',
    'Crouch'
]

def is_simulator(ip):
    return ip == "127.0.0.1" or ip == "localhost"

class Nao:
    def __init__(self, NAO_IP, PORT):
        self.tts = ALProxy("ALTextToSpeech", NAO_IP, PORT)
        self.player = ALProxy("ALAudioPlayer", NAO_IP, PORT)
        self.ip = NAO_IP
        self.port = PORT
        self.sim = is_simulator(NAO_IP)

    def say(self, string):
        return self.tts.say(string)

    def playMusic(self, music_path):
        if self.sim:
            print("Playing music locally with winsound:", music_path)
            def play():
                winsound.PlaySound(music_path, winsound.SND_FILENAME | winsound.SND_ASYNC)
            Thread(target=play).start()
            return None
        else:
            return self.player.post.playFile(music_path)

    def stopMusic(self, song=None):
        if self.sim:
            print("Stopping music")
            winsound.PlaySound(None, winsound.SND_PURGE)
        else:
            self.player.stopAll()

    def applyPosture(self, string):
        switch = {
            'Stand_from_sit': Stand_from_sit,
            'Arms_opening': Arms_opening,
            'Crouch': Crouch,
            'Diagonal_left': Diagonal_left,
            'Diagonal_right': Diagonal_right,
            'Move_backward': Move_backward,
            'Move_forward': Move_forward,
            'Right_arm': Right_arm,
            'Rotation_foot_LLeg': Rotation_foot_LLeg,
            'Rotation_foot_RLeg': Rotation_foot_RLeg,
            'Rotation_handgun_object': Rotation_handgun_object,
            'Sit': Sit,
            'SitRelax': SitRelax,
            'Stand': Stand,
            'StandInit': StandInit,
            'StandZero': StandZero,
            'Union_arms': Union_arms,
            'Hello': Hello,
            'Wipe_Forehead': Wipe_Forehead,
            'AirGuitar': AirGuitar,
            'ComeOn': ComeOn,
            'Dab': Dab,
            'DanceMove': DanceMove,
            'PulpFiction': PulpFiction,
            'TheRobot': TheRobot,
            'Mani_sui_fianchi': Mani_sui_fianchi,
            'Ballo_braccia': Ballo_braccia,
            'Right_sprinkler': Right_sprinkler,
            'Happy_Birthday': Happy_Birthday
        }

        function = switch.get(string, None)

        if function is None:
            print("\n....")
            print("Not Valid Position")
            print("Move to the next")
            print("....\n")
        else:
            function.main(self.ip, self.port)

def main():
    if len(sys.argv) < 3:
        print("Usage: python robot.py <NAO_IP> <PORT>")
        sys.exit(1)

    NAO_IP = sys.argv[1]
    PORT = int(sys.argv[2])

    print('\nIP: ' + str(NAO_IP))
    print('PORT: ' + str(PORT) + '\n')

    music_path = 'NowOrNever.wav'

    start = time.time()
    nao = Nao(NAO_IP, PORT)

    song = nao.playMusic(music_path)

    with open('choreography.txt', 'r') as file:
        choreography = [line.strip() for line in file if line.strip()]

    time.sleep(0.2)

    try:
        for move in choreography:
            if move in MANDATORY_POSITION:
                print('\n' + move.upper() + '\n')
            else:
                print(move)
            nao.applyPosture(move)
    except Exception as e:
        print(e)

    nao.stopMusic(song)
    end = time.time()
    total_time = end - start
    print("The choreography lasted for")
    print(total_time)

if __name__ == '__main__':
    main()

