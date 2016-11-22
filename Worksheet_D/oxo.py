class OxoBoard:
    def __init__(self):
        #Starts up the Oxoboard list
        self.oxoboard = ([0,0,0], [0,0,0], [0,0,0])

    def get_square(self, x, y):
        return self.oxoboard

    def set_square(self, x, y, mark):
        #Checks if the square is empty, if empty it is filled with a mark and if filled is returned as false
        if self.oxoboard[x][y] == 0:
            self.oxoboard[x][y] = mark
            return True
        else:
            return False


    def is_board_full(self):
        for x in range(3):#Shows as false if empty squares are on the board
            for y in range(3):
                if self.oxoboard[x][y] == 0:
                    return False
        return True#shows true if all squares on the board are filled

    def get_winner(self):
        for i in range(3):
            #Checks for horizontal match
            if self.oxoboard[i][0] == self.oxoboard[i][1] == self.oxoboard[i][2] > 0:
                return self.oxoboard[i][0]
            #Checks for vertical match
            elif self.oxoboard[0][i] == self.oxoboard[1][i] == self.oxoboard[2][i] > 0:
                return self.oxoboard[0][i]
            #checks for diagonal matches
            elif self.oxoboard[0][0] == self.oxoboard[1][1] == self.oxoboard[2][2] > 0:
                return self.oxoboard[0][0]
            elif self.oxoboard[0][2] == self.oxoboard[1][1] == self. oxoboard[2][0] > 0:
                return self.oxoboard [0][2]
        return 0


    def show(self):
        for y in xrange(3):
            if y > 0:
                print "--+---+--"
            for x in xrange(3):
                if x > 0:
                    print '|',

                # Print a space for empty (0), an O for player 1, or an X for player 2
                print " OX"[self.get_square(x, y)],
            print


def input_square():
    """ Prompt the player to enter a square. You should not need to edit this. """
    while True:
        input = raw_input("Enter x,y where x=0,1,2, y=0,1,2: ")
        if input.count(',') != 1:
            print "Input must contain exactly one comma!"
            continue

        x, y = input.split(',')
        try:
            x = int(x)
            y = int(y)
        except ValueError:
            print "Input must be two numbers separated by a comma!"
            continue

        if x < 0 or x > 2 or y < 0 or y > 2:
            print "Input is out of bounds!"
            continue

        return x, y


if __name__ == '__main__':
    oxoboard = OxoBoard()
    current_player = 1
    while True:
        oxoboard.show()
        print "Choose a square, Player", current_player
        x, y = input_square()

        if oxoboard.set_square(x, y, current_player):
            # Move was played successfully, so check for a winner
            winner = oxoboard.get_winner()
            if winner != 0:
                print "Player", winner, "wins!"
                break   # End the game
            elif oxoboard.is_board_full():
                print "It's a draw!"
                break   # End the game
            else:
                # Switch players
                if current_player == 1:
                    current_player = 2
                else:
                    current_player = 1
        else:
            # Move was not played successfully
            print "That square is already filled!"
