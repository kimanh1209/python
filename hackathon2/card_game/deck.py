from card import Card
import random

class Deck:
    '''
    Class đại diện cho bộ bài, bao gồm 36 lá
    '''

    def build(self):
        '''Tạo bộ bài'''
        cardList = []
        for rank in range(2,10):
            for suit in range(0,4):
                card = Card(rank,suit)
                cardList.append(card)
        self._cardList = cardList

    def shuffle_card(self):
        '''Trộn bài'''
        random.shuffle(self._cardList)
        pass

    def deal_card(self):
        '''Rút một lá bài từ bộ bài'''
        if self._cardList == None and len(self._cardList) == 0:
            return None
        card = self._cardList.pop(0)
        return card

# deck = Deck()
# deck.build()
# print(len(deck._cardList))
# deck.shuffle_card()
# print(deck.deal_card())
# print(len(deck._cardList))
