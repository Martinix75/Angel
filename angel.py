'''
Created on 20 ott 2020
@author: Andrea Martin
-------------------------
functions:
- Angel(path, app_name, app_number) init:
    - path --> path of the cloud directory (str)
    - app_name --> program name (str)
    - app_number --> client number (int)
- Write(text) --> text= all in string mode (strings, numbers, lists, ecc)
- Read(read_app_number, delete) --> read_app_number = client number to read, 
  delete=TRUE delete (file FALSE non delete)
- Delete_File(file_name) --> file_name name of the file to delete
'''
from os import makedirs, path, chdir, remove
from pickle import dump, load

class Angel():
    def __init__(self, path, app_name, app_number):
        self.AngelVersion = '0.0.1'
        self.Path = path #variabile con per la path di lavoro
        self.App_Name = app_name #variabile con il nome del programma
        self.App_Number = str(app_number) #variabile per numero identificativo (0=master)
        self.Path_Total = self.Path+'/'+self.App_Name #crea il percorso completo
        self.File_Name = self.App_Name+'_'+self.App_Number+'.pkd' #crea il nome corretto del file
        
        self._Initialize(self.Path_Total)
        
    # ---------------- Funzioni Pubbliche -------------------------------------
    
    def Write(self, text): #funzione pubblica per scrivere il file pickle
        self._Write_File_Obj(self.File_Name, text) #chiama il metodo privato
        
    def Read(self, read_app_number, delete=True): #funzione pubblica per leggere il file pickle
        File_Read = self.App_Name+'_'+str(read_app_number)+'.pkd'
        return self._Read_File_Obj(File_Read, delete) #chiama il metodo privato
    
    def Delete_File(self, file_name): #funzione pubblica per cancellare un file specifico
        remove(file_name) #rimove il file specificato nell dir di lavoro
        
    # ---------------- Funzioni Private ---------------------------------------
    
    def _Initialize(self, pathx):
        #print('Inizializzo....')
        self._Check_Path(pathx) #controlal se ce il percorso altrimenti crealo
        self._Ch_Dir(pathx) #cambia directori di lavoro (in quella del programma asegnato)
    
    def _Write_File_Obj(self, file_name, text, mode='ab', protocol=3): #scrittura file pickle
        self._Check_Path(self.Path_Total) #contolla la ptha se non ce la ricrea (BUG2)
        self._Ch_Dir(self.Path_Total) #punta alla directori corratta di lavoro
        with open(file_name, mode) as File_W: #apri o crea il file mode (ab = append binario)
            dump(text, File_W, protocol)# scrivi con pikle prtocollo3
            #print('scritto--> ', text)
            
    def _Read_File_Obj(self, file_name, delete=True): #lettura file pickle
        if self._FileisPresent(file_name): # se il file esiste allora....
            Date=[] #cra la lista dove inserire le singole voci
            with open(file_name, 'rb') as File_R: #apri il file in lattura binaria
                try: # quando compare eeore esci e va avanti
                    while True:# cicla fino alal comparsa dell errore (fine dati)
                        Date.append(load(File_R)) #aggiungi la voce alla lista
                except(EOFError): #... va avanti.. senza fare nulla
                    pass
            if delete: # se attiva l'opzione delete, cancella il file letto
                self.Delete_File(file_name) # chiam la f(x) di cancellazione
            return Date #torna la lista con i valori
        else:
            return False #correzione (BUG1)
    
    def _FileisPresent(self, file_name):# controlla se il file indicato è presente o meno
        if path.isfile(file_name):
            return True
        else:
            return False
        
    def _Make_Path(self, pathx): #crea il percorso coretto
        if path.exists(pathx) == False: #valuta se esite il percorso indicato se no..
            makedirs(pathx) #crea ricorsivamente le directoy mancanti
            #print(f'Creata {pathx}')
            return False
        else:
            #print(f'Percorso {pathx} Presente!')
            return True
    
    def _Check_Path(self, pathx): #funzione per controllare i percorsi corretti
        return self._Make_Path(pathx)# solo per comodita poi rimanda a make_path tutto
    
    def _Ch_Dir(self, pathx): #cambia la directori di lavoro (per scrivere e leggere correttamente)
        return chdir(pathx)

if __name__ == '__main__':
    print('Work in Local....')
    Pathx = '/home/andrea/SynC'
    Name_App = 'Angel'
    Number_Addres = 0
    test = Angel(Pathx, Name_App, Number_Addres)
    
    