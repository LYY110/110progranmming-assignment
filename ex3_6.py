import time
scale = 50
t = time.clock()
for i in range(scale + 1):
    a = '.' * i
    c = (i / scale) * 100
    t -= time.clock()
    print("\rStarting {:^3.0f}%[{}] Done".format(c,a,-t), end='')
    time.sleep(0.05)
