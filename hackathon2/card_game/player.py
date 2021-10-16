from card import Card


class Player:
    '''
    Class đại diện cho mỗi người chơi

    Người chơi chỉ cần lưu tên, và các lá bài người chơi có
    '''

    def __init__(self, id, name):  # dễ
        self._id = id
        self._name = name
        self._cardList = []

    @property
    def point(self):  # trung bình
        '''Tính điểm cho bộ bài'''
        totalPoint = 0
        for card in self._cardList:
            totalPoint += card.get_rank()
        
        p = totalPoint%10
        if p == 0:
            p = 10
        return p

    @property
    def biggest_card(self):
        '''
        Tìm lá bài lớn nhất
        Trong trường hợp điểm bằng nhau, sẽ so sánh lá bài lớn nhất để tìm ra người chiến thắng
        '''
        biggest = self._cardList[0]
        for card in self._cardList:
            if card > biggest:
                biggest = card
        return biggest

    def add_card(self, card: Card):
        '''Thêm một lá bài vào bộ (rút từ bộ bài)'''
        self._cardList.append(card)
        pass

    def remove_card(self):
        '''Reset bộ bài khi chơi game mới'''
        self._cardList = []

    def flip_card(self):
        '''Lật bài, hiển thị các lá bài'''
        # sort card

        cards = ''
        for card in self._cardList:
            cards += str(card) +' '
        print(f'{self._name}\t{cards}\tDiem:{self.point}\tLa lon nhat:{self.biggest_card}')

# c1 = Card(9,0)
# c2 = Card(2,1)
# player = Player(1,'VA')
# player.add_card(c1)
# player.add_card(c2)
# player.flip_card()
