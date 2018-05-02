__author__ = 'TrangHa'

class Square(object):
    def __init__(self):
        self.content = -1

    def isEmpty(self):
        if self.content < 0:
            return True
        else:
            return False

    def getMark(self):
        return self.content

    def setMark(self, playerNumber):
        self.content = playerNumber

class TicTacToe(object):
    def __init__(self, size = 3):
        self.size = size
        self.won = False
        self.winner = -1
        self.currentPlayer = 1
        self.gameBoard = []
        self.nextBlockList = []
    def setWon(self, winnerNumber):
        self.won = True
        self.setWinner(winnerNumber)

    def getWinner(self):
        return self.winner

    def setWinner(self, playerNumber):
        self.winner = playerNumber

    def getCurrentPlayer(self):
        return self.currentPlayer

    def getOppossingPlayer(self):
        opossingPlayer = self.currentPlayer
        opossingPlayer = (opossingPlayer + 1) % 2
        return opossingPlayer

    def setCurrentPlayer(self, playerNumber):
        self.currentPlayer = playerNumber

    def toggleCurrentPlayer(self):
        if self.currentPlayer == 1:
            self.currentPlayer = 2
        else:
            self.currentPlayer = 1

    def getBlockList(self):
        return self.nextBlockList

    def setBlockList(self, list):
        self.nextBlockList = list

    def mark(self, row, column):
        if self.gameBoard[(row - 1) * self.size + (column - 1)].isEmpty():
            self.gameBoard[(row - 1) * self.size + (column - 1)].setMark(self.getCurrentPlayer())




