import time 
from colorama import Fore 
import sys
import os
open_txt_file=open('hack.txt','r')
text=open_txt_file.readlines()
sequence_1=['''
             ______
            |      |
            |______|''','''
                           ___ ___
                          |       |
                          |_______|''']
sequence_2=['''
             ______ _____
            |      |     |
            |______|_____|                           ''','''          
            
                                 ______ ______
                                |      |      |
                                |______|______|''','''
                                
                                         
             ______ _____       
            |      |     |      
            |______|_____|                                           ''','''         
                         
                         
                                 ______ ______
                                |      |      |
                                |______|______|
                                ''']
os_title='''
          ___ __              ___ __   ______________  _______________   ___________ ___    ____________  _______          ________
          \  \  \            /  /  /  /          /  / / /        / / /  |___________|___| / \___________\ \  \    \       /    /  /
           \  \  \          /  /  /  /          /  / / /        / / /      |    |  |     /  /  /________/  \  \    \     /    /  /
            \  \  \        /  /  /  /          /  / / /________/ / /       |    |  |    /  /  /_________    \  \    \   /    /  /
             \  \  \______/  /  /  /          /  / / /_________\ \ \       |    |  |   /  /  /_________/     \  \    \ /    /  /
              \__\_______/__/__/  /          /  / / / _________ \ \ \      |    |  |  /  /  /_________        \  \___/_\__/\  \\
               \_\_______/__/_/  /_________ /__/ /_/_/           \ \_\     |____|__| /__/__/_________/        /__/___/  \__ \__\\
              '''
def loop_over(sequence,delay_time,color):
    for text in sequence:
        sys.stdout.flush()
        time.sleep(delay_time)
        sys.stdout.write(f'{color}{text}')
    else:
        print(f'{Fore.RESET}')

for n in range(20):
 loop_over(sequence=sequence_1,delay_time=0.1,color=Fore.CYAN)
else:
    time.sleep(1)
    for x in range(10):
        loop_over(sequence=sequence_2,delay_time=0.40,color=Fore.GREEN)
    else:
        time.sleep(1)
        os.system("cls")
        time.sleep(1)
        for nim in text:
            sys.stdout.flush()
            time.sleep(0.0001)
            print(f'{Fore.YELLOW} {"".join(nim)}',flush=True)
        else:
            loop_over('Welcome to...\n\t',delay_time=0.01,color=Fore.RESET)
            time.sleep(1)
            for nu in os_title:
                sys.stdout.flush()
                time.sleep(0.001)
                sys.stdout.write(f'{Fore.LIGHTBLUE_EX}{nu}')
            else:
                print(Fore.RESET)