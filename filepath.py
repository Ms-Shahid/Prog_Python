import os 
import socket 

print(os)
print(socket)


import sys

x =1
print(sys.getsizeof(x))


import speedtest

st = speedtest.Speedtest()

print(f'Download speed: {st.download()}')
print(f'upload speed: {st.upload()}')