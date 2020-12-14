import sys
import time
import os


os.system("python -m pip install plotly -U")
os.system("python -m pip install pandas -U")
os.system("python -m pip install voila -U")


port = 8866
filename = "/folder/voila_app.ipynb"

if __name__ == '__main__':
    #example: voila example.ipynb --port 8888
    try:
        os.system("voila " + filename + " --port " + str(port))
        #os.system("voila " + filename + " --debug" + "--port " + str(port))
    except:
        print("ERROR running voila")
    
    while True:
        time.sleep(0.2) 
        
