import os
from deck import Deck

from player import Player
from datetime import datetime

class Game:
    '''
    Class chứa các chức năng chính của game

    Game chứa danh sách người chơi, và bộ bài
    '''

    def __init__(self):
        self._playerList = [Player(1,'KA'),Player(2,'VA')]
        self._is_deal = False
        self._is_fliped = False
        self._play_at = datetime.now()
        self._winner = None
        pass
    
    def setup(self):
        '''Khởi tạo trò chơi, nhập số lượng và lưu thông tin người chơi'''
        playerNumber = 0
        while True:
            inputPlayer = input('Nhap so luong nguoi choi:')
            try:
                inputPlayer = int(inputPlayer)
            except ValueError:
                print('So nhap vao khong hop le!')
            if inputPlayer > 1 and inputPlayer < 10:
                playerNumber = inputPlayer
                break
            else:
                print('So nhap vao khong hop le!')
        # os.system('cls' if os.name == 'nt' else 'clear')
        self._playerList = []
        for i in range(1,playerNumber+1):
            pName = input(f'Nhat ten nguoi choi {i}:')
            self._playerList.append(Player(i,pName))

    def guide(self):
        '''Hiển thị menu chức năng/hướng dẫn chơi'''
        
        pass

    def list_players(self):
        '''Hiển thị danh sách người chơi'''
        print('ID\tTen')
        for p in self._playerList:
            print(f'{p._id}\t{p._name}')
        pass

    def add_player(self):
        '''Thêm một người chơi mới'''
        next_seq = len(self._playerList) +1
        nextName = input(f'Nhap ten nguoi choi thu {next_seq}:')
        self._playerList.append(Player(next_seq,nextName))
        print('Them nguoi choi thanh cong')
        pass

    def remove_player(self):
        '''
        Loại một người chơi
        Mỗi người chơi có một ID (có thể lấy theo index trong list)
        '''
        inputPlayer = input('Nhap ID nguoi choi de xoa:')
        try:
            inputPlayer = int(inputPlayer)
        except ValueError:
            print('So nhap vao khong hop le!')
        indexToDel = -1
        for idx, player in enumerate(self._playerList):
            if player._id == inputPlayer:
                indexToDel = idx
        if indexToDel >=0:
            self._playerList.pop(indexToDel)
        else:
            print('Khong tim thay nguoi choi!')
        pass

    def deal_card(self):
        '''Chia bài cho người chơi'''
        self._deck = Deck()
        self._deck.build()
        self._deck.shuffle_card()
        for p in self._playerList:
            p.remove_card()
        
        numberPlayer = len(self._playerList)
        cardNumber = 3
        for i in range(numberPlayer*cardNumber):
            playerIndex = i%numberPlayer
            card = self._deck.deal_card()
            self._playerList[playerIndex].add_card(card)
        print('Da chia xong!')
        self._is_deal = True
        pass

    def flip_card(self):
        '''Lật bài tất cả người chơi, thông báo người chiến thắng'''
        winner = None
        for player in self._playerList:
            player.flip_card()
            if winner == None:
                winner = player
            else:
                if winner.point == player.point:
                    if player.biggest_card > winner.biggest_card:
                        winner = player
                elif player.point > winner.point:
                    winner = player
        print(f'Nguoi chien thang:{winner._name}')
        self._winner = winner._name
        self._is_fliped = True
        # import db
        # db.log(self)
        pass


# game = Game()
# # game.setupTest()
# game.guide()
print(datetime.now())