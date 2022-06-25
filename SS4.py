import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from SS4 import ss4buy
    ss4buy()
elif bit == '32bit':
    from SS432 import ss4buy
    ss4buy
