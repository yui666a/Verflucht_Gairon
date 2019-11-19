"""
Verflucht!のゲームシステム

int型の入力のみで動作します．
クリーチャーや武器の選択もリストのインデックスで選択してください．
また，複数の武器を洗濯する時は，インデックスの値の間をスペースで区切ってください
"""
#-*- coding:utf-8 -*-
import random


# classes here
class Card :
    """
    カードの情報を保持するクラス.

    Attributes
    ----------
    num : int
        カードの強さ(1~40)
    isCreature : bool
        カードが「武器」か「クリーチャー」か判定する
        true : creature
        false: weapon
    """
    def __init__(self, num, isCreature):
        self.num : int = num
        self.isCreature : bool = isCreature

    def __lt__(self, other):
        """
        今は小さい順にソートしている．
        """
        # self < other
        return self.num < other.num


# global variable
startingLife = 3
MAISU : int = 80
life : int = startingLife
deck =  [Card] * MAISU
fieldCreature = []
handWeapon = []
aCard : Card = Card(-1, True)


# def here
def init():
    """
    カードを初期化し，山札をランダムな順番に並べる
    また，fieldCreatureやhandWeaponも初期化し，
    lifeを初期値に戻す
    """
    for i in range(MAISU):
        if(i % 2 == 0):
            deck[i] = Card(1 + int(i/2), True)
        else:
            deck[i] = Card(1 + int(i/2), False)
    random.shuffle(deck)
    fieldCreature.clear()
    handWeapon.clear()
    life = startingLife

def draw():
    """
    カードを一枚引く

    Parameters
    ----------

    Returns
    -------
    drawnCard : Card
        引いたカード
    """
    global fieldCreature, handWeapon, deck
    drawnCard = deck[0]
    deck = deck[1:]
    if(drawnCard.isCreature == True):
        fieldCreature.append(drawnCard)
        fieldCreature.sort()
        print("{0}\t{1}".format(drawnCard.num, "Creature"))
    else:
        handWeapon.append(drawnCard)
        handWeapon.sort()
        print("{0}\t{1}".format(drawnCard.num, "Weapon"))
    return drawnCard

def creaturesBack(creatures : [int]):
    """
    バトルし，倒せなかったクリーチャーを山札に戻す

    Parameters
    ----------
    creatures : Card(list)

    Returns
    -------

    Raises
    ------
    引数がない場合
    リストで返されてない場合

    Notes
    -----
    連番により連結したクリーチャーに対応するため，パラメータはリストでよろしく!
    """
    global fieldCreature, deck
    clist : Card= []
    for i in range(creatures.__len__()):
        clist.append(fieldCreature[creatures[i]])
    fieldCreature = [i for j, i in enumerate(fieldCreature) if j not in creatures]
    deck.extend(clist)
    random.shuffle(deck)

def slay(creatures : [int], weapons : [int]):
    """
    場のクリーチャーを退治する
    退治した場合，武器と場のクリーチャーは削除する.
    できなかった場合は，何もせずにFalseを返す.

    Parameters
    ----------
    creatures : int(list) <-- index
    weapons   : int(list) <-- index
    creatures : int(list) <-- 数値(強さ)
    weapons   : int(list) <-- 数値(強さ)

    Returns
    -------
    isSlain : bool
        退治できたかどうかを示す．
        True  : 退治できた．
        False : 退治できなかった.(もしこっちだったらエラー!!)

    Raises
    ------
    引数に過不足がある場合
    リストで返されてない場合

    Notes
    -----
    パラメータはリストでよろしく!
    """

    global fieldCreature, handWeapon
    sumCreatures : int = 0
    sumWeapons : int = 0

    try:
        # TODO : カードがあるかチェックしたい
        # 武器とクリーチャー，それぞれの合計値を算出する
        for i in range(creatures.__len__()):
            sumCreatures += fieldCreature[creatures[i]].num
        for i in range(weapons.__len__()):
            sumWeapons += handWeapon[weapons[i]].num

        # 武器の合計値がクリーチャー合計値より低かった場合(失敗)
        if(sumWeapons < sumCreatures):
            print("x クリーチャーを退治できませんでした")
            return False

        # 武器の合計値がクリーチャー合計値より高かった場合(成功)
        print("○ クリーチャーを退治できました")
        fieldCreature = [i for j, i in enumerate(fieldCreature) if j not in creatures]
        handWeapon = [i for j, i in enumerate(handWeapon) if j not in weapons]
        return True
    except IndexError:
        print("範囲内のインデックスで選択してください")
        print("handWeapon : ", end="")
        printHandWeapon()
        print("fieldCreature : ", end="")
        printFieldCreature()
        return False

def subLife():
    global life
    print("life: {0} -> {1}".format(life, life - 1))
    life -= 1;

def printDeck():
    """
    山札の順番と枚数を出力する(テスト用　使用厳禁)
    """
    global deck
    for i in deck:
        if(i.isCreature == True):
            print("{0}\t{1}".format(i.num, "Creature"))
        else:
            print("{0}\t{1}".format(i.num, "Weapon"))
    print("山札残り枚数: {0}".format(deck.__len__()))

def printACard():
    """
    カード情報を出力する
    """
    global aCard
    try:
        print("{0}\t{1}".format(aCard.num, aCard.isCreature))
    except UnboundLocalError:
        print("まだカードをひいていません")

def printFieldCreature():
    """
    場のクリーチャーを表示
    """
    for i in fieldCreature:
        print("{0} ".format(i.num), end=' ')
    print()

def printHandWeapon():
    """
    手札の武器を表示
    """
    for i in handWeapon:
        print("{0} ".format(i.num), end=' ')
    print()

def printState():
    """
    手札，場のクリーチャー，ライフの数，山札残り枚数を表示
    """
    print("handWeapon : ", end="")
    printHandWeapon()
    print("fieldCreature : ", end="")
    printFieldCreature()
    print("life: {0}".format(life))
    print("山札残り枚数: {0}".format(deck.__len__()))

def fieldCheck():
    if(deck.__len__() == 0):
        print("山札の枚数が0になりました．おめでとうございます!!")
        clear()
        return False
    #連番になった時の動作
    l = isConsecutive()
    if(not l == []):
        print("場のクリーチャーが連番になりました．強制バトルを開始します")
        forcedBattleConsecutive(l)
    if(fieldCreature.__len__() >= 6):
        print("場のクリーチャーが6体になりました．強制バトルを開始します")
        forcedBattle6()
    if(life == 0):
        print("\nGAME OVER")
        gameOver()
        return False
    return True

def clear():
    """
    クリア時のスコア計算を行う
    """
    global fieldCreature
    for i in range(life):
        fieldCreature = fieldCreature[1:]
    sum = 0;
    for i in fieldCreature:
        sum += i.num
    print("スコア: {0}".format(820 - sum))

def gameOver():
    global fieldCreature, deck
    sum = 0;
    for i in fieldCreature:
        sum += i.num
    for i in deck:
        if(i.isCreature == True):
            sum += i.num
    print("スコア: {0}".format(820 - sum - 100))

def forcedBattle6():
    global life, fieldCreature
    flag = False
    while(not flag):
        # c = []
        # c.append(fieldCreature[-1])
        print("\nバトルするクリーチャー: {0}".format(fieldCreature[-1].num))
        print("手持ちの武器: ", end="")
        printHandWeapon()
        if(handWeapon.__len__() == 0):
            print("手持ちの武器がないため，ライフで受けます.")
            subLife()
            creaturesBack([fieldCreature.__len__() - 1])
            return True
        else:
            print("複数の武器を使用する場合は，スペースで区切って入力してくだい．\nライフで受ける場合は，'-1'と入力してくだい")
            # print("handWeapon index: ", end="")
            w = list(map(int, input("handWeapon index: ").split()))
            if(w == [-1]):
                subLife()
                creaturesBack([fieldCreature.__len__() - 1])
                return True
            else:
                flag = slay([fieldCreature.__len__() - 1], w)

def isConsecutive():
    global fieldCreature
    consecutiveCreatures = []
    for i in range(fieldCreature.__len__()):
        try:
            if(fieldCreature[i - 1].num == fieldCreature[i].num - 1):
                consecutiveCreatures.append(i - 1)
                consecutiveCreatures.append(i)
            if(fieldCreature[i + 1].num == fieldCreature[i].num + 1):
                consecutiveCreatures.append(i)
                consecutiveCreatures.append(i + 1)
        except IndexError:
            pass
            # print("IndexError")
    return list(set(consecutiveCreatures)) #重複を削除

def forcedBattleConsecutive(creatures):
    global life, fieldCreature
    flag = False

    s = "\nバトルするクリーチャー: "
    sum = 0
    for i in creatures:
        sum += fieldCreature[i].num
        s += str(fieldCreature[i].num) + ' '
    s += '(合計 ' + str(sum) + ')'

    clist : int = []
    for i in creatures:
        clist.append(i)
    while(not flag):
        print(s)

        print("手持ちの武器: ", end="")
        printHandWeapon()
        if(handWeapon.__len__() == 0):
            print("手持ちの武器がないため，ライフで受けます.")
            subLife()
            creaturesBack(clist)
            return True
        else:
            print("複数の武器を使用する場合は，スペースで区切って入力してくだい．\nライフで受ける場合は，'-1'と入力してくだい")
            # print("handWeapon index: ", end="")
            w = list(map(int, input("handWeapon index: ").split()))
            if(w == [-1]):
                subLife()
                creaturesBack(clist)
                return True
            else:
                flag = slay(creatures, w)
                if(not flag):
                    print("倒せませんでした")

def help():
    print(" 0 : help \t\t(コマンドリストを表示)")
    print(" 1 : draw \t\t(カードを一枚引く)")
    print(" 2 : slay \t\t(クリーチャーを倒す)")
    print(" 3 : printState \t(現在の状態を出力する)")
    print(" 4 : fieldCheck \t(使用禁止 デバッグ用)")
    print(" 5 : printACard \t(使用禁止 デバッグ用)")
    print(" 6 : printDeck \t\t(使用禁止 デバッグ用)")
    print("-1 : exit \t\t(ゲームを終了する)")

def chooseCommand():
    """
    入力を受け付け，コマンドを実行する
    '-1'と入力された時のみ False を返す.
    """

    # print("\nCommand:", end=' ')
    try:
        n = int(input("\nCommand:　"))
    except ValueError:
        print("<数字を入力してください>")
        return True

    if(n == 0):
        help()
    elif(n == 1):
        c = draw()
    elif(n == 2):
        printFieldCreature()
        # print("fieldCreature index: ", end="")
        c = list(map(int, input("fieldCreature index: ").split()))
        if(c.__len__() > 1):
            print("一度に退治できるクリーチャーは１体のみです．")
            return True
        # print("handWeapon index: ", end="")
        printHandWeapon()
        print("複数の武器を使用する場合は，スペースで区切って入力してくだい．")
        w = list(map(int, input("handWeapon index: ").split()))
        slay(c, w)
    elif(n == 3):
        printState()
    elif(n == 4):
        fieldCheck()
    elif(n == 5):
        printACard()
    elif(n == 6):
        printDeck()
    elif(n == -1):
        return False
    else:
        print("コマンドが間違っています")
    return True

def main():
    help()
    print("\nAre you ready?  Let's get started!!")
    init()
    flag = True
    while(flag):
        flag = chooseCommand()
        if(not flag):
            print("終了します")
            break
        flag = fieldCheck()

main()
