import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import*
import icons
import angel

class Comand_Led(QMainWindow):
    def __init__(self, parent =None):
        super (Comand_Led, self).__init__(parent)
        self.VersionTestAngel = '0.3'
        self.Central_Widget = QWidget()
        self.setWindowIcon(QIcon(':/Panoratux.png'))
        self.setGeometry(160,140,370,200)
        self.setWindowTitle(f'Test for Angel Ver: {self.VersionTestAngel}')
        self.Timer = QTimer(self)
        
        self.Label_1 = QLabel('Comand Recived From')
        self.Line_1 = QLineEdit()
        self.Line_1.setMaximumHeight(40)
        self.Led_Blu = QLabel()
        self.Led_Blu.setPixmap(self.Make_Led('Led_Spento'))
        self.Led_Red = QLabel()
        self.Led_Red.setPixmap(self.Make_Led('Led_Spento'))
        self.Led_Green = QLabel()
        self.Led_Green.setPixmap(self.Make_Led('Led_Spento'))
        
        Tab_1 = QHBoxLayout()
        Tab_1.addWidget(self.Label_1)
        Tab_1.addWidget(self.Line_1)
        
        Tab_2 = QHBoxLayout()
        Tab_2.addWidget(self.Led_Red)
        Tab_2.addStretch()
        Tab_2.addWidget(self.Led_Blu)
        Tab_2.addStretch()
        Tab_2.addWidget(self.Led_Green)
        
        Tab_3 = QGridLayout(self.Central_Widget)
        Tab_3.addLayout(Tab_1,0,0)
        Tab_3.addLayout(Tab_2,1,0)
        
        self.setCentralWidget(self.Central_Widget)
        self.Timer.start(500)
        self.Timer.timeout.connect(self.Protocol)
    
    def AngelRead(self): #function for read data via cloud by Angle
        path = '/home/andrea/SynC'
        app_name = 'AngelTest'
        app_number = 0
        anx = angel.Angel(path, app_name, app_number)
        c= anx.Read(delete=True)
        if c is not False:
            return c

    def Protocol(self):
        Date = self.AngelRead()
        try:
            for number in range(len(Date)):
                print('--> ',Date,number)
                N_app, Parametro, Value_1 = Date[number][0], Date[number][1], Date[number][2]
                if Parametro == 'label':
                    print('--------- Label ---------')
                    self.Line_1.setText(f'{N_app}: {Value_1}')
                elif Parametro == 'led':
                    print('---------- Led ----------')
                    self.Line_1.setText(f'{N_app} ha Richiesto {Value_1}')
                    if Value_1 == 'red':
                        self.Led_Red.setPixmap(self.Make_Led('Led_Rosso.png'))
                    elif Value_1 == 'blue':
                        self.Led_Blu.setPixmap(self.Make_Led('Led_Blu.png'))
                    elif Value_1 == 'green':
                        self.Led_Green.setPixmap(self.Make_Led('Led_Verde.png'))
                    elif Value_1 == 'off':
                        self.Led_Red.setPixmap(self.Make_Led('Led_Spento.png'))
                        self.Led_Blu.setPixmap(self.Make_Led('Led_Spento.png'))
                        self.Led_Green.setPixmap(self.Make_Led('Led_Spento.png'))

        except(TypeError):
            pass
        except(ValueError):
            self.Line_1.setText('Valori Errati!!')
            
    def Write_Label(self, text):
        self.Line_1.setText(text[0])
        
    def Make_Led(self, ColorLed, Dim=35):# crea i vari led e li ridimensione
        ImgX = QPixmap(':/{}'.format(ColorLed))
        Scaled_Imgx = ImgX.scaled(Dim, Dim, Qt.KeepAspectRatio,
                                  Qt.SmoothTransformation)
        return Scaled_Imgx
    def MakeAction(self, Text, Icon=None, Tip=None, Short=None, Disable=False,
                   ChecK=False, Sel=False):
        ActionX = QAction(Text, self)
        if Icon is not None:
            ActionX.setIcon(QIcon(':/{}'.format(Icon)))
        if Tip is not None:
            ActionX.setToolTip(Tip)
        if Short is not None:
            ActionX.setShortcut(Short)
        if Disable is True:
            ActionX.setDisabled(True)
        if ChecK is True:
            ActionX.setCheckable(True)
        if Sel is True:
            ActionX.setChecked(True)
        return ActionX
        

if __name__ == '__main__':
    App = QApplication(sys.argv)
    Form = Comand_Led()
    Form.show()
    App.exec_()