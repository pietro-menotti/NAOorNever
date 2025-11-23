# -*- coding: utf-8 -*-

# We used this file to measure the time of each move, to run the script simply use the line below in the shell opened in the same 
# reponsory using the same premises given to start the choreography

#  python2 measure_single_move.py 127.0.0.1 9559 <MOVE>

from naoqi import ALProxy
from robot import Nao
import sys
import time

def main():
    if len(sys.argv) < 4:
        print("Usage: python2 measure_single_move.py <NAO_IP> <PORT> <MOVE_NAME>")
        sys.exit(1)

    NAO_IP = sys.argv[1]
    PORT = int(sys.argv[2])
    MOVE = sys.argv[3]

    print("")
    print("NAO IP: " + str(NAO_IP))
    print("PORT:   " + str(PORT))
    print("MOVE:   " + str(MOVE))
    print("")

    nao = Nao(NAO_IP, PORT)
    durations = []

    
    start = time.time()
    nao.applyPosture(MOVE)
    end = time.time()

    duration = end - start
    durations.append(duration)
    
    print("Tempo per move '{}': {:f} secondi".format(MOVE, duration))
    
    time.sleep(0.5)

if __name__ == "__main__":
    main()