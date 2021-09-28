'Timer measured to countdown'

import time
print('This is timer')
seconds = int(input('Please input seconds to countdown: '))

sec = 0
mins = 0

while True:
  sec += 1
  print(f'Minutes {mins} Seconds {sec}')
  time.sleep(1)
  if sec == 60:
    sec = 0
    mins += 1
  if mins * 60 + sec == seconds:
    print('It is time')
    break