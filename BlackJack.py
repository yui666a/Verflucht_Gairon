""" 
BlackJackGame
情報工学特論

参考文献
https://gist.github.com/shiracamus/8c74cf6b97863c4ab56f607889cdfc1f



Copyright:
    Fumi (https://fumisite.net/)

License:
    GNU General Public License version 3.
    (https://www.gnu.org/licenses/gpl-3.0.html)

"""
"""''''''''''''''''''''''''''''''''ルール'''''''''''''''''''''''''''''''''''''''''''''''


'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""

#-*- coding:utf-8 -*-

import random
 
#-------------------------------------------------------
deck = []               #デック
deck_count = 0          #デックのインデント
deck_change_count = 1   #デック交換の回数

card_count = 0          #カウンティング数

money = 10000           #所持金
bet = 100               #ベット数(固定)

SUITS = ('Spade', 'Heart', 'Diamond', 'Club')
RANKS = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')
VALUES = ((1,11), 2, 3, 4, 5, 6, 7, 8, 9, 10)
COUNTS = ( -1, 0, 1)    #ハイローシステム  ランニングカウントは1デックあたりの合計が0なので初期設定IRCは0でよい、今のところ正規化なし

#------------------------------------------------------
def get_value(rank, sum):
    if(rank == 'J' or rank == 'Q' or rank == 'K'):
        return VALUES[9]

    elif(rank == 'A' and sum + 11 <= 21):
        return VALUES[0][1]

    elif(rank == 'A' and sum + 11 > 21):
        return VALUES[0][0]

    else:
        return VALUES[int(rank)-1]

def get_count(rank):    #ハイローシステム
    if(rank == '10' or rank == 'J' or rank == 'Q' or rank == 'K' or rank == 'A'):
        return COUNTS[0]

    elif(rank == '7' or rank == '8' or rank == '9'):
        return COUNTS[1]

    else:
        return COUNTS[2]

def Deck():
    deck = []
    for k in range(6):
        for i in range(4):
            for j in range(13):
                deck.append((SUITS[i], RANKS[j]))

    random.shuffle(deck)
    return deck

def p_result(p, d):
    global money
    global bet
    get_money = 0       #報酬用に変数生成
    if(p.get_rst() == 4):
        print('{0}の負け！'.format(p.name))
    elif(d.get_rst() == 4 and p.cards_total() <= 21):
        print('{0}の勝利！'.format(p.name))
        get_money = 2 * bet
    else:
        if(p.cards_total() > d.cards_total()):
            print('{0}の勝利！'.format(p.name))
            p.set_rst(1)
            get_money = 2 * bet
        elif(p.cards_total() == d.cards_total()):
            print('{0}は引き分け！'.format(p.name))
            p.set_rst(2)
            get_money = bet
        else:
            print('{0}の負け！'.format(p.name))
            p.set_rst(3)

    money += get_money
    print(money)

def o_result(o, d):
    if(o.get_rst() == 4):
        print('{0}の負け！'.format(o.name))
    elif(d.get_rst() == 4 and o.cards_total() <= 21):
        print('{0}の勝利！'.format(o.name))
    else:
        if(o.cards_total() > d.cards_total()):
            print('{0}の勝利！'.format(o.name))
            o.set_rst(1)
        elif(o.cards_total() == d.cards_total()):
            print('{0}は引き分け！'.format(o.name))
            o.set_rst(2)
        else:
            print('{0}の負け！'.format(o.name))
            o.set_rst(3)

#-------------------------------------------------------

class Player:
    def __init__(self, name):
        self.name = name
        self.Cards()
        self.flag = True    #ヒットできるか否か、True：できる。つまりFalseはスタンド、バーストのいずれかが起こった時
        self.rst = 0        #(0:試合中,1:勝ち,2:引き分け,3:負け, 4:バースト)

    def Cards(self):
        self.cards = []

    def cards_hit(self):
        global deck_count
        global deck
        global card_count
        self.cards.append(deck[deck_count])
        card_count += get_count(deck[deck_count][1])
        print('name:{0}, 引いたカード:{1}'.format(self.name, deck[deck_count]))
        value_sum = self.cards_total()
        print('合計:{0}'.format(value_sum))
        if(value_sum > 21):
            self.flag = False
            print('バースト')
            self.rst = 4
        print('カードカウンティング合計:{0}'.format(card_count))
        deck_count += 1 

    def cards_total(self):
        sum = 0
        A_count = 0;
        for a in self.cards:
            if(a[1] == 'A'):
                A_count += 1
                continue
            sum += get_value(a[1], sum)

        #print(sum)
        #print(A_count)
        for i in range(A_count):
            sum += get_value('A', sum)
        return sum

    def get_flag(self):
        return self.flag

    def set_flag(self, flag):
        self.flag = flag

    def get_rst(self):
        return self.rst

    def set_rst(self, num):
        self.rst = num

class Others(Player):
    def Action(self):
        global deck_count
        global deck
        if(self.cards_total() >= 17):
            print('合計:{0}'.format(self.cards_total()))
            self.set_flag(False)
        while(self.flag):
            self.cards_hit()
            if(self.cards_total() >= 17):
                self.set_flag(False)

class Dealer(Others):
    FIRSTCOUNT = 0  #最初に配られるカードのカウンティイングの値を保存するやつ
    FIRSTCARD = ('','')      #最初に配られたカード
    def ini_cards_hit(self):
        global deck_count
        global deck
        global card_count
        self.cards.append(deck[deck_count])
        self.FIRSTCARD = deck[deck_count]
        self.FIRSTCOUNT = get_count(deck[deck_count][1]) 
        deck_count += 1 

    def sec_cards_hit(self):
        global deck_count
        global deck
        global card_count
        self.cards.append(deck[deck_count])
        card_count += get_count(deck[deck_count][1])
        print('name:{0}, 引いたカード:{1}'.format(self.name, deck[deck_count]))
        print('カードカウンティング合計:{0}'.format(card_count))
        deck_count += 1

    def Action(self):
        global deck_count
        global deck
        print('合計:{0}'.format(self.cards_total()))
        if(self.cards_total() >= 17):
            self.set_flag(False)
        while(self.flag):
            self.cards_hit()
            if(self.cards_total() >= 17):
                self.set_flag(False)

    def get_FIRSTCOUNT(self):
        return self.FIRSTCOUNT

    def get_FISTCARD(self):
        return self.FIRSTCARD

#----------------------------------------------------------
def main():
    global deck
    global deck_count
    global deck_change_count
    global money
    global bet 
    global card_count
    deck = Deck()

    while(1):
        print("-------------------------------------------------------------------")

        player = Player('Player')
        other1 = Others('Other1')
        other2 = Others('Other2')
        dealer = Dealer('Dealer')

        if(deck_count > 218):
            deck_count = 0
            deck = Deck()
            print('デック交換')
            deck_change_count+=1

        print("Game Start")
        money -= bet
        player.cards_hit()
        other1.cards_hit()
        other2.cards_hit()
        dealer.ini_cards_hit()
        player.cards_hit()
        other1.cards_hit()
        other2.cards_hit()
        dealer.sec_cards_hit()

        print("Player Turn")
        #プレイヤーの行動記述-------------------------------------------------------------------------------

        while(player.get_flag()):
            print('[call:y, stand:n]:')
            num = input('>>')
            if(num == 'y'):
                player.cards_hit()
            else:
                player.set_flag = False
                break

        #------------------------------------------------------------------------------------------------

        print("Other1 Turn")
        other1.Action()

        print("Other2 Turn")
        other2.Action()

        print("Dealer Turn")
        card_count += dealer.get_FIRSTCOUNT()
        print('ディーラーの最初のカード：{0}'.format(dealer.get_FISTCARD()))
        dealer.Action()

        p_result(player, dealer)
        o_result(other1, dealer)
        o_result(other2, dealer)

        print('現在出た枚数：{0}'.format(deck_count))



if __name__ == '__main__':
    main()
