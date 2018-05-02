__author__ = 'TrangHa'

import sys
import random
from os import path
# import tictactoeResource
from time import sleep
from logging import basicConfig, getLogger, DEBUG, INFO, CRITICAL
from pickle import dump, load
from PyQt5.QtCore import pyqtSlot, Qt, QSettings, QCoreApplication
from PyQt5 import QtGui, uic, QtCore
from PyQt5.QtWidgets import  QMainWindow, QApplication, QDialog, QFileSystemModel, QDialogButtonBox, QHeaderView, QMessageBox

logFilenameDefault = 'craps.log'

class ticTacToe(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        uic.loadUi("ticTacToe.ui", self)
        self.wins = 0
        self.losses = 0
        self.messageBox = "Let's play!"
        self.board = ["_","_","_",
                      "_", "_", "_",
                      "_", "_", "_"]

        self.sq0Button.clicked.connect(lambda: self.gamePlay(0))
        self.sq1Button.clicked.connect(lambda: self.gamePlay(1))
        self.sq2Button.clicked.connect(lambda: self.gamePlay(2))
        self.sq3Button.clicked.connect(lambda: self.gamePlay(3))
        self.sq4Button.clicked.connect(lambda: self.gamePlay(4))
        self.sq5Button.clicked.connect(lambda: self.gamePlay(5))
        self.sq6Button.clicked.connect(lambda: self.gamePlay(6))
        self.sq7Button.clicked.connect(lambda: self.gamePlay(7))
        self.sq8Button.clicked.connect(lambda: self.gamePlay(8))

        self.messageLabel.setText(str(self.messageBox))

        self.actionPreference.triggered.connect(self.preferenceTriggered)
        self.actionRestart.triggered.connect(self.restartTriggered)
        self.actionQuit.triggered.connect(self.quitTriggered)

        # self.game = TicTacToe()

    def updateUI(self):
        self.lossesLabel.setText(str(self.losses))
        self.winsLabel.setText(str(self.wins))
        self.messageLabel.setText(str(self.messageBox))

    def drawBoard(self):
        print(" {0} | {1} | {2} ".format(self.board[0], self.board[1], self.board[2]))
        print("___|___|___")
        print(" {0} | {1} | {2} ".format(self.board[3], self.board[4], self.board[5]))
        print("___|___|___")
        print(" {0} | {1} | {2} ".format(self.board[6], self.board[7], self.board[8]))
        print("   |   |   ")

    def gamePlay(self):
        winsCount = 0
        lossesCount = 0

        #set winning
        def setWins(char, sqBoard0, sqBoard1, sqBoard2):
            if self.board[sqBoard0] == char and self.board[sqBoard1] == char and self.board[sqBoard2] == char:
                return True

        #check boardgame if there is any winning
        def checkWins(char):
            if setWins(char, 0, 1, 2):
                return True
            elif setWins(char, 3, 4, 5):
                return True
            elif setWins(char, 6, 7, 8):
                return True
            elif setWins(char, 0, 3, 6):
                return True
            elif setWins(char, 1, 4, 7):
                return True
            elif setWins(char, 2, 5, 8):
                return True
            elif setWins(char, 0, 4, 8):
                return True
            elif setWins(char, 2, 4, 6):
                return True

        while True:
            #ask user position to mark
            playerSpot = int(input("Select a spot: "))
            #if sqBoard is empty, run this
            if self.board[playerSpot] == "_":
                self.board[playerSpot] = "X"
                # checkwins
                if checkWins("X") == True:
                    winsCount += 1
                    self.wins += winsCount
                    self.messageBox = "Yass, You win!!!"
                    print(self.messageBox)
                    break
                #calculate computer move
                while True:
                    #random move
                    random.seed()
                    computerPosition = random.randint(0, 8)
                    if self.board[computerPosition] == "_":
                        self.board[computerPosition] = "O"
                        # checkwins
                        if checkWins("O") == True:
                            lossesCount += 1
                            self.losses += lossesCount
                            self.messageBox = "Nooo, You lose!"
                            print(self.messageBox)
                            break
                        break

            else:
                print("This sport is taken!")
        return self.board




    def preferenceTriggered(self):
        print("Setting preferences")
        self.logger.info("Setting preferences")
        preferencesDialog = PreferencesDialog()
        preferencesDialog.show()
        preferencesDialog.exec_()
        self.restoreSettings()
        self.updateUI()

    def restartTriggered(self):
        self.restartGame()
        self.saveGame()
        self.updateUI()

    def quitTriggered(self):
        self.saveGame()

class PreferencesDialog(QDialog, QDialogButtonBox):
    def __init__(self, parent = ticTacToe):
        super(PreferencesDialog, self).__init__()

        uic.loadUi('preferenceWindow.ui', self)
        if self.xMarkButton:
            self.sq1Button.setText("X")
        elif self.oMarkButton:
            self.sq1Button.setText("O")


if __name__ == "__main__":
    QCoreApplication.setOrganizationName("Trang Software");
    QCoreApplication.setOrganizationDomain("trangsoftware.com");
    QCoreApplication.setApplicationName("TicTacToe");
    # appSettings = QSettings()
    # startingFolderName = path.dirname(path.realpath(__file__))
    # if appSettings.contains('logFile'):
    #     logFilename = appSettings.value('logFile', type=str)
    # else:
    #     logFilename = logFilenameDefault
    #     appSettings.setValue('logFile', logFilename)
    # basicConfig(filename = path.join(startingFolderName, logFilename), level=INFO, format='%(asctime)s %(name)-8s %(levelname)-8s %(message)s')
    app = QApplication(sys.argv)
    ticTacToeApp = ticTacToe()
    ticTacToeApp.updateUI()
    ticTacToeApp.show()
    sys.exit(app.exec_())
