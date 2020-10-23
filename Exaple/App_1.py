'''
Created on 20 ott 2020

@author: andrea
'''
import angel

version = 0.3
 

Folder_Sync_App = '/home/andrea/SynC'
App_Name = 'AngelTest'
add = 1
s = angel.Angel(Folder_Sync_App, App_Name, add)
print('Angel Version: ',s.AngelVersion+' @ APP_1')

while True:
    nn = input('For Read=r, For Write=w:, For Exit=e ')
    if nn == 'r':
        x=s.Read(delete=False)
        #print('Letto dallo slave..>',x)
        if x is not False:
            for z in x:
                print (z)
    elif nn == 'w':
        cc = input('Inserisci stringa--> ')
        s.Write(cc, 0)
    elif nn == 'e':
        break
    #time.sleep(2)