# -*- coding: utf-8 -*-
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

    # Esegui 15 misurazioni
    # for i in range(15):
    # print("Misurazione {}/15 in corso...".format(i+1))
    
    start = time.time()
    nao.applyPosture(MOVE)
    end = time.time()

    duration = end - start
    durations.append(duration)
    
    print("Tempo per move '{}': {:f} secondi".format(MOVE, duration))
    
    # Piccola pausa tra le misurazioni
    time.sleep(0.5)

    # # Calcola statistiche
    # average_time = sum(durations) / len(durations)
    # min_time = min(durations)
    # max_time = max(durations)

    # print("\n" + "="*50)
    # print("RISULTATI FINALI:")
    # print("Move analizzato: {}".format(MOVE))
    # print("Numero di misurazioni: {}".format(len(durations)))
    # print("Tempo medio: {:f} secondi".format(average_time))
    # print("Tempo minimo: {:f} secondi".format(min_time))
    # print("Tempo massimo: {:f} secondi".format(max_time))
    # print("Variazione: {:f} secondi".format(max_time - min_time))
    # print("="*50)

if __name__ == "__main__":
    main()



# # -*- coding: utf-8 -*-
# from naoqi import ALProxy
# from robot import Nao
# import sys
# import time

# def main():
#     if len(sys.argv) < 4:
#         print("Usage: python2 measure_single_move.py <NAO_IP> <PORT> <MOVE_NAME>")
#         sys.exit(1)

#     NAO_IP = sys.argv[1]
#     PORT = int(sys.argv[2])
#     MOVE = sys.argv[3]

#     print("")
#     print("NAO IP: " + str(NAO_IP))
#     print("PORT:   " + str(PORT))
#     print("MOVE:   " + str(MOVE))
#     print("")

#     nao = Nao(NAO_IP, PORT)

#     start = time.time()
#     nao.applyPosture(MOVE)
#     end = time.time()

#     duration = end - start

#     print("")
#     print("Time for move '" + MOVE + "': %f seconds" % duration)
#     print("")

# if __name__ == "__main__":
#     main()