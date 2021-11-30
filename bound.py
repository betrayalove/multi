from hashlib import md5
from random import choice
import concurrent.futures
import time


with concurrent.futures.ProcessPoolExecutor(max_workers=61) as executor:
    i = 0
    start_time = time.time()
    while i < 2:
        s = "".join([choice("0123456789") for i in range(50)])
        h = md5(s.encode('utf8')).hexdigest()

        if h.endswith("00000"):
            i += 1
            print(s, h)

print("--- %s seconds ---" % (time.time() - start_time))