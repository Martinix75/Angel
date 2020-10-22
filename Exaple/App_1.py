'''
Created on 20 ott 2020

@author: andrea
'''
import angel

version = 0.2
 

Folder_Sync_App = '/home/andrea/SynC'
App_Name = 'AngelTest'
add = 0
s = angel.Angel(Folder_Sync_App, App_Name, add)
print('Angel Version: ',s.AngelVersion@APP_1)

while True:
    nn = input('For Read=r, For Write=w: ')
    if nn == 'r':
        x=s.Read(read_app_number=1, delete=True)
        #print('Letto dallo slave..>',x)
        if x is not False:
            for z in x:
                print (z)
    elif nn == 'w':
        cc = input('Inserisci stringa--> ')
        s.Write(cc)
    #time.sleep(2)