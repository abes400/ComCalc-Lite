import PyQt5.QtWidgets as qtw
import PyQt5.QtCore as qtc
import PyQt5.QtGui as qtg
from Functions import error
from os.path import expanduser

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()

        self.rollenabled = 0

        # Define Layout
        self.setWindowTitle("")
        self.vert = qtw.QVBoxLayout()
        self.hor = qtw.QHBoxLayout()
        self.gri = qtw.QGridLayout()
        self.miniver = qtw.QVBoxLayout()

        # Prepare the Layout
        self.vert.addLayout(self.hor)
        self.gri.addLayout(self.miniver, 2, 4)
        self.vert.addLayout(self.gri)
        self.setLayout(self.vert)
        
        self.gri.setVerticalSpacing(3)
        self.gri.setHorizontalSpacing(3)
        self.layout().setContentsMargins(8, 8, 8, 8)

        # Screen object shows entered digit(s) and operation results
        self.screen = qtw.QLineEdit(self, readOnly = True)
        self.screen.setStyleSheet('background-color: #FFFFFF')
        self.screen.setText('')
        self.screen.setFont(qtg.QFont('Avenir', 30))
        self.screen.setAlignment(qtc.Qt.AlignRight)

        #Number Keys
        self.key7 = qtw.QPushButton('\n7\n', clicked = lambda: self.scrapd('7'))
        self.key8 = qtw.QPushButton('\n8\n', clicked = lambda: self.scrapd('8'))
        self.key9 = qtw.QPushButton('\n9\n', clicked = lambda: self.scrapd('9'))
        self.key4 = qtw.QPushButton('\n4\n', clicked = lambda: self.scrapd('4'))
        self.key5 = qtw.QPushButton('\n5\n', clicked = lambda: self.scrapd('5'))
        self.key6 = qtw.QPushButton('\n6\n', clicked = lambda: self.scrapd('6'))
        self.key1 = qtw.QPushButton('\n1\n', clicked = lambda: self.scrapd('1'))
        self.key2 = qtw.QPushButton('\n2\n', clicked = lambda: self.scrapd('2'))
        self.key3 = qtw.QPushButton('\n3\n', clicked = lambda: self.scrapd('3'))
        self.key0 = qtw.QPushButton('\n0\n', clicked = lambda: self.scrapd('0'))
        self.keyD = qtw.QPushButton('\n•\n', clicked = lambda: self.scrapd('.'))

        self.key7.setShortcut('7')
        self.key8.setShortcut('8')
        self.key9.setShortcut('9')
        self.key4.setShortcut('4')
        self.key5.setShortcut('5')
        self.key6.setShortcut('6')
        self.key1.setShortcut('1')
        self.key2.setShortcut('2')
        self.key3.setShortcut('3')
        self.key0.setShortcut('0')
        self.keyD.setShortcut('.')

        #Operational Keys
        self.divKey = qtw.QPushButton('', clicked = lambda: self.scrapd('/'))
        self.mulKey = qtw.QPushButton('', clicked = lambda: self.scrapd('*'))
        self.subKey = qtw.QPushButton('\n－\n', clicked = lambda: self.scrapd('-'))
        self.addKey = qtw.QPushButton('\n＋\n', clicked = lambda: self.scrapd('+'))

        # Shortcuts of the operational keys are defined at Functions.py

        #Extra Keys
        self.clrKey = qtw.QPushButton('\nC\n', clicked=lambda: self.resetcalc())
        self.delKey = qtw.QPushButton('\n⌫\n', clicked=lambda: self.backspace())
        self.equKey = qtw.QPushButton('\n=\n', clicked=lambda: self.equals())

        self.clrKey.setShortcut('C')
        self.equKey.setShortcut('Return')

        # Adding the widgets to the window
        self.hor.addWidget(self.screen)
        self.gri.addWidget(self.key7, 0, 0)
        self.gri.addWidget(self.key8, 0, 1)
        self.gri.addWidget(self.key9, 0, 2)
        self.gri.addWidget(self.key4, 1, 0)
        self.gri.addWidget(self.key5, 1, 1)
        self.gri.addWidget(self.key6, 1, 2)
        self.gri.addWidget(self.key1, 2, 0)
        self.gri.addWidget(self.key2, 2, 1)
        self.gri.addWidget(self.key3, 2, 2)
        self.gri.addWidget(self.key0, 3, 0, 1, 2)
        self.gri.addWidget(self.keyD, 3, 2)
        self.gri.addWidget(self.divKey, 0, 3)
        self.gri.addWidget(self.mulKey, 1, 3)
        self.gri.addWidget(self.subKey, 2, 3)
        self.gri.addWidget(self.addKey, 3, 3)
        self.gri.addWidget(self.clrKey, 1, 4)
        self.gri.addWidget(self.delKey, 0, 4)
        self.gri.addWidget(self.equKey, 3, 4)

        self.show()
    
    # The functions assigned to the buttons are defined below
    
    # Appends the value of the button to the content of the screen
    def scrapd(self, appendedValue):
        self.screen.setText(self.screen.text() + appendedValue)

    # Evaluates the content of the screen
    def equals(self):
        try:
            if self.screen.text()[-1] == '+' or self.screen.text()[-1] == '-':
                result = eval(self.screen.text() + '0.0')
                self.writeToRoll(self.screen.text() + '=' + str(result))
                self.screen.setText(str(result))
            elif self.screen.text()[-1] == '*' or self.screen.text()[-1] == '/':
                result = eval(self.screen.text() + '1.0')
                self.writeToRoll(self.screen.text() + '=' + str(result))
                self.screen.setText(str(result))
            else:
                result = eval(self.screen.text()) + 0.0
                self.writeToRoll(self.screen.text() + '=' +str(result))
                self.screen.setText(str(result))
        except Exception as e:
            self.writeToRoll(self.screen.text() + '=Undefined')
            error(1)
            self.screen.setText('')

    # If enabled from the options, writes the operaton to the abstract file called paper_roll.txt
    def writeToRoll(self, eqn):
        if self.rollenabled:
            self.rollfile = open(expanduser('~') + '/ComCalc/paper_roll.txt', 'a')
            self.rollfile.write(eqn + '\n')
            self.rollfile.close()

    # Removes the last character of the content of the screen
    def backspace(self):
        try:
            if len(self.screen.text() == 1):
                self.screen.setText('')
            else:
                self.screen.setText(self.screen.text().removesuffix(self.screen.text()[-1]))
        except Exception as e:
            self.screen.setText('')
    
    # Resets the calculator to its initial state
    def resetcalc(self):
        self.screen.setText('')

    def __del__(self):
        print('MainWindow Instance Killed')

    def closeEvent(self, event):
        self.deleteLater()

