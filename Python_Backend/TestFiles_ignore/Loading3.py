import itertools
import threading
import time
import sys

total_time = 300
i = 0
def animate():
    i =0
    for c in itertools.cycle(["[■□□□□□□□□□]","[■■□□□□□□□□]", "[■■■□□□□□□□]", "[■■■■□□□□□□]", "[■■■■■□□□□□]", "[■■■■■■□□□□]", "[■■■■■■■□□□]", "[■■■■■■■■□□]", "[■■■■■■■■■□]", "[■■■■■■■■■■]"]):
        #if done:
          #break
        #sys.stdout.write('\rloading' + c)
        sys.stdout.write('\rloading' + c + ' process ' + str(i) + '/' + str(total_time) + ' ' + '{:.2f}'.format(i / total_time * 100) + '%')
        sys.stdout.flush()
        time.sleep(0.5)
        i += 1
        if i == total_time:
            break
    sys.stdout.write('\rDone!     ')

t = threading.Thread(target=animate)
t.start()

time.sleep(total_time)

