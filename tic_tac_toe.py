
class TicTacToe():

    def __init__(self):
        self.board = {
            "7":' ', '8':' ', '9':' ',
            '4':' ', '5':' ', '6':' ',
            '3':' ', '2':' ', '1':' '
        }
        self.cross = ('x','x','x')
        self.circle = ('o','o','o')

    def __get_board(self):
        print(self.board['7'] + '|' + self.board['8'] + '|' + self.board['9'])
        print('-+-+-')
        print(self.board['4'] + '|' + self.board['5'] + '|' + self.board['6'])
        print('-+-+-')
        print(self.board['1'] + '|' + self.board['2'] + '|' + self.board['3'])

    def __circle_winner(self):
        _ = False
        if self.circle ==(self.board['7'], self.board['8'], self.board['9']):
            _ = True
        elif self.circle == (self.board['1'], self.board['2'], self.board['3']):
            _ = True
        elif self.circle == (self.board['4'], self.board['5'], self.board['6']):
            _ = True
        elif self.circle == (self.board['7'], self.board['4'], self.board['1']):
            _ = True
        elif self.circle == (self.board['9'], self.board['5'], self.board['1']):
            _ = True
        elif self.circle == (self.board['7'], self.board['5'], self.board['3']):
            _ = True
        
        elif self.circle ==  (self.board['9'], self.board['5'], self.board['1']):
            _ = True
        
        elif self.circle == (self.board['8'], self.board['5'], self.board['2']):
            _ = True
        return _
          
    
    def __cross_winner(self):
        _ = False
        if self.cross == (self.board['7'], self.board['8'], self.board['9']):
            _ = True
        
        elif self.cross == (self.board['1'], self.board['2'], self.board['3']):
            _ = True
        
        elif self.cross == (self.board['4'], self.board['5'], self.board['6']):
            _ = True
        
        elif self.cross == (self.board['7'], self.board['4'], self.board['1']):
            _ = True
        
        elif self.cross == (self.board['9'], self.board['5'], self.board['1']):
            _ = True
        
        elif self.cross == (self.board['7'], self.board['5'], self.board['3']):
            _ = True
        
        elif self.cross == (self.board['9'], self.board['5'], self.board['1']):
            _ = True
        
        elif self.cross == (self.board['8'], self.board['5'], self.board['2']):
            _ = True
        return _
            
    def __check_win(self, count):
        winner = None
        circle = self.__circle_winner()
        cross = self.__cross_winner()
        if circle:
            winner = 'o'
        if cross:
            winner = 'x'
        if count == 9:
            winner = "No body"
        return winner

    def __move(self, key, value):
        self.board[key] = value
        self.count+=1
        
    def __game(self):
        turn = 'x'
        self.count = 0
        winner = None
        while winner is None:
            turn_msg = f"please enter move for player {turn} "
            self.__get_board()
            move = str(input(turn_msg))
            self.__move(move, turn)              
            if turn == 'x':
                turn = 'o'
            else:
                turn = 'x'
            winner = self.__check_win(self.count)
            if winner:
                break
        self.__get_board()
        print(f'winner is -> {winner}')
    def run(self):
        self.__game()

app = TicTacToe()



if __name__ == "__main__":
    print("Beggining of Game")
    app.run()