class TicTacToe(object):
    def __init__(self):
        """
        inits a 3x3 matrix
        """
        self._row, self._col = 3, 3
        self._board = [['.'] * self._row for _ in range(self._col)]

    def play(self, i, j, user):
        """
        when play gets called, user 1 or user 2 depending on their usage will get marked
        Player 1 uses X while Player 2 uses O
        """
        over = False
        if user==1:
            if self.isValid(i, j):
                self._board[i][j] = 'X'
                if self.iswin(user):
                    print(f"\n\n******* Player {user} won *******\n\n")
                    over = True
                    return over
                self.pprint_board()
            else:
                return 'Marker already placed or the location does not exist'
        elif user==2:
            if self.isValid(i,j):
                self._board[i][j] = 'O'
                if self.iswin(user):
                    print(f"Player {user} won")
                    over=True
                    return over
                self.pprint_board()
            else:
                return 'Marker already placed or the location does not exist'
        print('\n**Board Updated**\n')
        return over

    
    def isValid(self, i, j):
        """
        checks if the move is valid on the board
        1. The move could already been played
        2. The board moves are exhausted
        """
        if self._board[i][j] == '.':
            return True
        return False

    def iswin(self, user):
        """
        Checks winning condition for 
        """
        isWinner = False
        for i in range(len(self._board)):
            vertical_check = []
            if self.win(self._board[i]):
                    isWinner=True
                    return isWinner
            for j in range(len(self._board)):
                vertical_check.append(self._board[j][i])
            if self.win(vertical_check):
                isWinner=True
                return isWinner

        #checking diagonals
        leading_diagonal = [self._board[i][i] for i in range(len(self._board))]
        cross_diagonal = [self._board[i][~i] for i in range(len(self._board))]
        if self.win(leading_diagonal) or self.win(cross_diagonal):
            isWinner=True
            return isWinner
        return isWinner

    def win(self, win_list):
        if '.' not in win_list and len(win_list)==3 and len(set(win_list))==1:
            return True
        return False

    def pprint_board(self):
        print('Board is now: \n')
        print(*(' | '.join(row) for row in self._board), sep='\n')


if __name__ == "__main__":
    board = TicTacToe()
    print("*** Game starting: Player 1 is X and Player 2 is O   ***")
    print("*** Player 1 goes first ***")
    game,counter = False,0
    while not game:
        print("*** Player 1: Enter x,y coordinates ***\n")

        x,y = input().split()
        game_ret = board.play(int(x),int(y), 1)
        if game_ret:
            break
        print("*** Player 2 is placing O now ***\n")
        a,b = input().split()
        game_r=board.play(int(a),int(b), 2)
        if game_r:
            break
