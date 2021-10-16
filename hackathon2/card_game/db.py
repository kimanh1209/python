'''Kết nối CSDL'''
from pymysql import connect, cursors,Error
from card import Card
from player import Player

from game import Game

config = {
    "host": "localhost",
    "user": "root",
    "password": "123456",
    "database": "game_log",
    "cursorclass": cursors.DictCursor
}

def log(game):
    '''
    Ghi thông tin về game vào CSDL và 2 bảng games và logs

    Bảng games gồm tên người chiến thắng

    Bảng logs gồm danh sách người chơi, bộ bài, điểm và lá bài lớn nhất tương ứng với game

    Chú ý, sau khi INSERT vào games, có thể lấy id của game vừa tạo với cursor.lastrowid
    '''

    sql = '''
    INSERT INTO games (play_at, winner)
    VALUES (%s, %s)
    '''
    try:
        with connect(**config) as conn:
            with conn.cursor() as cur:
                data = (game._play_at, game._winner)
                cur.execute(sql, data)
                conn.commit()
                gameId = cur.lastrowid
                for player in game._playerList:
                    sqlLog = 'INSERT INTO logs (game_id, player, cards, point, biggest_card) VALUES (%s, %s, %s, %s, %s)'
                    cards = ''
                    for c in player._cardList:
                        cards+= str(c) +' '
                    cards = cards.strip()
                    logsData = (gameId,player._name,cards,player.point,str(player.biggest_card))
                    cur.execute(sqlLog, logsData)
                conn.commit()
                return cur.lastrowid
    except Error as e:
        print(e)

    pass


def get_last_game():
    '''Lấy thông tin về game gần nhất từ cả 2 bảng games và logs'''
    # sqlLog = 'INSERT INTO logs (game_id, player, cards, point, biggest_card) VALUES (%s, %s, %s, %s, %s)'
    try:
        with connect(**config) as conn:
            with conn.cursor() as cur:
                sqlgame = 'SELECT * FROM game_log.games order by play_at desc limit 1'
                cur.execute(sqlgame)
                result = cur.fetchone()
                game_id = result['game_id']

                sqllogs = 'SELECT * FROM game_log.logs where game_id = %s;'
                cur.execute(sqllogs,(game_id))
                logsResult =  cur.fetchall()

                game = Game()
                game._winner = result['winner']
                game._play_at = result['play_at']
                game._playerList = []
                for idx,log in enumerate(logsResult):
                    player = Player(idx+1,log['player'])
                    cards = log['cards'].split(' ')
                    for c in cards:
                        card = Card(0,0)
                        card.fromString(c)
                        player.add_card(card)
                    game._playerList.append(player)
                return game
                
    except Error as e:
        print(e)
    pass


def history():
    '''
    Lấy thông tin về lịch sử chơi

    Bao gồm tổng số game đã chơi, số game chiến thắng ứng với mỗi người chơi (sử dụng GROUP BY và các hàm tổng hợp)
    '''
    sql  = 'select winner,count(winner) as count from game_log.games group by winner order by count desc'
    try:
        with connect(**config) as conn:
            with conn.cursor() as cur:
                cur.execute(sql)
                return cur.fetchall()
    except Error as e:
        print(e)
# print('9♣'[1])