from game import Game
import db

def main():  # khó
    '''Khởi tạo trò chơi, hiển thị menu và thực thi các chức năng tương ứng'''
    game = Game()
    game.setup()
    game.guide()
    while True:
            print(f"""
1.Danh sach nguoi choi
2.Them nguoi choi
3.Xoa nguoi choi
4.Chia bai
5.Lat bai
6.Xem lai game
7.Lich su choi
8.Thoat
            """)
            userInput = input('Nhap:')
            if userInput == '1':
                game.list_players()
            elif userInput == '2':
                game.add_player()
            elif userInput == '3':
                game.remove_player()
            elif userInput == '4':
                game.deal_card()
            elif userInput == '5':
                game.flip_card()
                db.log(game)
            elif userInput == '6':
                game2 = db.get_last_game()
                print(game2._play_at)
                game2.flip_card()
            elif userInput == '7':
                history = db.history()
                totalGame = 0
                for his in history:
                    name = his['winner']
                    count = his['count']
                    countInt = int(count)
                    totalGame += countInt
                    print(f'{name}\t{count}')
                print(f'Tong game:{totalGame}')
            else:
                return
    pass


if __name__ == '__main__':
    main()
