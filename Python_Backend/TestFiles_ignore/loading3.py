import itertools
import threading
import time
import sys

total_time = 196
i = 0
def animate():
    i =0
    for c in itertools.cycle(["[■ □ □ □ □ □ □ □ □ □]","[■ ■ □ □ □ □ □ □ □ □]", "[■ ■ ■ □ □ □ □ □ □ □]", "[■ ■ ■ ■ □ □ □ □ □ □]", "[■ ■ ■ ■ ■ □ □ □ □ □]", "[■ ■ ■ ■ ■ ■ □ □ □ □]", "[■ ■ ■ ■ ■ ■ ■ □ □ □]", "[■ ■ ■ ■ ■ ■ ■ ■ □ □]", "[■ ■ ■ ■ ■ ■ ■ ■ ■ □]", "[■ ■ ■ ■ ■ ■ ■ ■ ■ ■]"]):
        sys.stdout.write('\rĐang khởi tạo phần mềm' + c + '; Tiến độ quá trình khởi tạo: ' + str(i) + '/' + str(total_time) + ' ' + '{:.2f}'.format(i / total_time * 100) + '%')
        sys.stdout.flush()
        time.sleep(0.5)
        i += 1
        if i == total_time:
            break
    sys.stdout.write('\rDone!     ')

print("\n\n\n\n\n\n\n               ")
t = threading.Thread(target=animate)
t.start()

time.sleep(total_time)
