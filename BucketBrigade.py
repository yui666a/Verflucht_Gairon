import random
import itertools
import GameSystem
import csv
import decimal

decimal.getcontext().prec = 3
Verflucht = GameSystem
ACTION : int = 5;
STATE : int= Verflucht.getMaxState();
Q = [[0 for i in range(ACTION)] for j in range(STATE)]
bid = [[0 for i in range(ACTION)] for j in range(STATE)]
REPEAT : int = 1000000
MAX_CYCLE : int = 1
Cbid : float = 0.01
rnd = random.random()
preState = 0
action = 0
preAction = 0
state = 0
EPSILON = 0.4 #イプシロングリーディ法に用いる
choice = [0, 1, 2, 3, 4]
# filename = 'calc1.csv'
# filelog = 'log.txt'
# f = open(filename, 'w')
# f2 = open(filelog, 'w')

def attackBetter3(creature, weapon):
    global choice
    wList = []
    for i in range(1, len(weapon) + 1):
        wList.extend(list(itertools.combinations(weapon, i)))
    # print("wlist", wList)
    sumList = []
    for i in wList:
        sumList.append(sum(i))
    if(sumList == []):
        # print("なにもないって\n")
        return [[-1], [-1]]
    for c in reversed(creature):
        # print("c", c)
        for sub in range(117):
            for w in range(len(sumList)):
                # print("sumList[w]:",sumList[w], "  C: ", c )
                if(sumList[w] >= c and sumList[w] - c <= sub):
                    # print()
                    # print("weapon: ",weapon)
                    # print("creatu: ",creature)
                    # print(sumList[w], " - ", c, " <= ", sub)
                    # print([[creature.index(c)], [weapon.index(wList[w][0]), weapon.index(wList[w][1])]])
                    # return [[creature.index(c)], [weapon.index(wList[w][0]), weapon.index(wList[w][1])]]
                    weaponList = []
                    for i in range(len(wList[w])):
                        weaponList.append(weapon.index(wList[w][i]))
                    # print(weaponList)
                    # print("weapon  : ",weapon)
                    # print([[sumCreature], [weapon.index(wList[w][0]), weapon.index(wList[w][1])]])
                    return [[creature.index(c)], weaponList]
    # print("そんなことある？アタック3でだめだった")
    # print("state: ", Verflucht.getState())
    # print("weapon  : ",weapon)
    # print("creature: ",Verflucht.getFieldCreature())

    return [[-1], [-1]]
    # actionSelect(bid)
    
    # for c in reversed(range(0, creature.__len__())):
    #     if(creature[c] in weapon):

def attackBetter2(creature, weapon):
    global choice
    wList = list(itertools.combinations(weapon,2))
    # print(wList)
    sumList = []
    for i in wList:
        sumList.append(sum(i))
    for c in reversed(creature):
        for sub in range(3):
            for w in range(len(sumList)):
                if(sumList[w] >= c and sumList[w] - c <= sub):
                    # print("weapon: ",weapon)
                    # print("creatu: ",creature)
                    # print(sumList[w], " - ", c, " <= ", sub)
                    # print([[creature.index(c)], [weapon.index(wList[w][0]), weapon.index(wList[w][1])]])
                    return [[creature.index(c)], [weapon.index(wList[w][0]), weapon.index(wList[w][1])]]
    # print("アタック２でだめだった")
    choice.remove(3)
    # actionSelect(bid)
    return [[-1], [-1]]
    # return attackBetter3(creature, weapon)
    # for c in reversed(range(0, creature.__len__())):
    #     if(creature[c] in weapon):

def attackBetter1(creature, weapon):
    global choice
    for c in reversed(creature):
        for sub in range(3):
            for w in weapon:
                if(w >= c and w - c <= sub):
                    return [[creature.index(c)], [weapon.index(w)]]
    # print("だめだった")
    # print("weapon: ",weapon)
    # print("creatu: ",creature)
    choice.remove(2)
    # actionSelect(bid)
    return [[-1], [-1]]
    # return attackBetter2(creature, weapon)
    # for c in reversed(range(0, creature.__len__())):
    #     if(creature[c] in weapon):

def attackBest(creature, weapon):
    # print("creatures", creature)
    # w = []
    # index = 0
    global choice, bid
    for c in reversed(range(0, creature.__len__())):
        if(creature[c] in weapon):
            return[[c],[weapon.index(creature[c])]]
    choice.remove(1)
    return [[-1], [-1]]
    # return attackBetter1(creature, weapon)
    # actionSelect(bid)

def afterAttackBetter3(sumCreature, weapon):
    global choice
    # print(choice)
    wList = []
    for i in range(1, len(weapon) + 1):
        wList.extend(list(itertools.combinations(weapon, i)))
    # print(wList)
    sumList = []
    for i in wList:
        sumList.append(sum(i))
    # print("ここで詰まってます")
    # print(type(sumList[0]))
    # print(sumCreature)
    for sub in range(117):
        for w in range(len(sumList)):
            # f2.write("sumList[w]: {0} >= sumCreature: {1} \tsub: {2}\n".format(sumList[w], sum(sumCreature), sumList[w] - sum(sumCreature)))
            if(sumList[w] >= sum(sumCreature) and sumList[w] - sum(sumCreature) <= sub):
                # print("weapon: ",weapon)
                # print("creatu: ",creature)
                # print(sumList[w], " - ", c, " <= ", sub)
                # print([[creature.index(c)], [weapon.index(wList[w][0]), weapon.index(wList[w][1])]])
                weaponList = []
                for i in range(len(wList[w])):
                    weaponList.append(weapon.index(wList[w][i]))
                # print(weaponList)
                # print("weapon  : ",weapon)
                # print([[sumCreature], [weapon.index(wList[w][0]), weapon.index(wList[w][1])]])
                return [sumCreature, weaponList]
    # print("そんなことある？アフターアタック3でだめだった")
    # if(sum(weapon) <= sumCreature):
    #     print("足りないな\n")
    # print("state: ", Verflucht.getState())
    # print("weapon  : ",weapon)
    # print("creature: ",sumCreature)
    choice.remove(4)
    # actionSelect2(bid)
    return [[-2], [-2]]

def afterAttackBetter2(sumCreature, weapon):
    global choice
    wList = list(itertools.combinations(weapon,2))
    # print(wList)
    sumList = []
    for i in wList:
        sumList.append(sum(i))
    for sub in range(117):
        for w in range(len(sumList)):
            if(sumList[w] >= sum(sumCreature) and sumList[w] - sum(sumCreature) <= sub):
                # print("weapon: ",weapon)
                # print("creatu: ",creature)
                # print(sumList[w], " - ", c, " <= ", sub)
                # print([[creature.index(c)], [weapon.index(wList[w][0]), weapon.index(wList[w][1])]])
                return [sumCreature, [weapon.index(wList[w][0]), weapon.index(wList[w][1])]]
    # print("アタック２でだめだった")
    choice.remove(3)
    # actionSelect2(bid)
    return [[-2], [-2]]
    # return afterAttackBetter3(sumCreature, weapon)
    # for c in reversed(range(0, creature.__len__())):
    #     if(creature[c] in weapon):

def afterAttackBetter1(sumCreature, weapon):
    global choice
    for sub in range(117):
        for w in weapon:
            if(w >= sum(sumCreature) and w - sum(sumCreature) <= sub):
                # print("better1, ", [sumCreature, [weapon.index(w)]])
                return [sumCreature, [weapon.index(w)]]
    choice.remove(2)
    # actionSelect2(bid)
    return [[-2], [-2]]
    # return afterAttackBetter2(sumCreature, weapon)

def afterAttackBest(creature, weapon):
    global choice
    # print("choice: ", choice)
    s = sum(creature)
    # for c in reversed(range(0, creature.__len__())):
    if(s in weapon):
        return[[creature],[weapon.index(s)]]
    choice.remove(1)
    # actionSelect2(bid)
    return [[-2], [-2]]
    # return afterAttackBetter1(s, weapon)

def epsilon_greedy(bi):
    """
    イプシロンの確率で最善手を行う

    それ以外の確率でどれかを行う
    """
    global choice
    # print("epsi choice: ", choice)
    # global action, preAction
    # preAction = action
    tmp = 0
    highest = -10000
    for i in range(bi[state].__len__()):
        if((i in choice) and bi[state][i] >= highest):
            highest = bi[state][i]
            tmp = i
    if(random.random() < EPSILON):
        return tmp
    else:
        # return random.randint(0, ACTION - 1)
        # print("epsilon, ", choice)
        ans = random.choice(choice)
        # print("ans: ", ans)
        # print(choice)
        return ans

def actionSelect(bid):
    global action
    s = Verflucht.getState()
    if(s % 2 == 0):
        # Verflucht.printState()
        return [1, [0], [0]]
    else:
        select = epsilon_greedy(bid)
        if(select == 0):
            action = 0
            return [1, [0], [0]]
        else:
            #クリーチャーのリストを取得
            fc = Verflucht.getFieldCreature()
            #武器のリストを取得
            hw = Verflucht.getHandWeapon()
            best = []
            # print(select)
            if(select == 1):
                # print("attackBest")
                best = attackBest(fc, hw)
            elif(select == 2):
                # print("attackBetter1")
                best = attackBetter1(fc, hw)
            elif(select == 3):
                # print("attackBetter2")
                best = attackBetter2(fc, hw)
            elif(select == 4):
                # print("attackBetter3")
                best = attackBetter3(fc, hw)
            # print("best: ", best)
            action = select
            # if(best == None):
            #     actionSelect(bid)
            # print(best)
            return [2, best[0], best[1]]

        # Verflucht.printState()
        # print("タオセルソウデス\n")
        # #クリーチャーのリストを取得
        # fc = Verflucht.getFieldCreature()
        # #武器のリストを取得
        # hw = Verflucht.getHandWeapon()
        #ただドローしてるだけ
        #[コマンド選択, [クリーチャーの配列(1体のみ)], [武器の配列(インデックスで複数指定可能)]]
        # return [1, [0], [0]]

def actionSelect2(bid):
    global action
    # global f2
    s = Verflucht.getState()
    select = epsilon_greedy(bid)

    # if(s % 2 == 1):
        # f2.write("打つ手あり({0})\n".format(select))
        # f2.write("{0}\t{1}\t{2}\t{3}\t{4}\n".format(bid[s][0], bid[s][1], bid[s][2], bid[s][3], bid[s][4]))
    if(select == 0):
        action = 0
        return [-1]
    else:
        # print("おそってくるモンスターの合計値", Verflucht.attackingMonster)
        #武器のリストを取得
        hw = Verflucht.getHandWeapon()
        #ライフで受けてる
        # print("type", type(Verflucht.attackingMonster))
        # print("sumC: ", Verflucht.attackingMonster)
        if(select == 1):
            ans = afterAttackBest(Verflucht.attackingMonster, hw)
        elif(select == 2):
            ans = afterAttackBetter1(Verflucht.attackingMonster, hw)
        elif(select == 3):
            ans = afterAttackBetter2(Verflucht.attackingMonster, hw)
        elif(select == 4):
            ans = afterAttackBetter3(Verflucht.attackingMonster, hw)
        action = select
        # print("select2: ", select)
        # print("se2 ans: ", ans)
        return ans[1]
        # print("ans: ", ans)
        # print("ans[1]: ", ans[1])
        # print("ans[0][0]", ans[0][0])
        # print("ans[0][0]", ans[0][0])
        # a = Verflucht.getHandWeapon
        # print("weapon: ",Verflucht.getHandWeapon())
        # print("creatu: ",Verflucht.getFieldCreature)
        
        # print("ans: ", ans)
        if(ans[0][0] == 0 and ans[1][0] == 0):
            print("ライフで受けるしかないそうだ")
            return [-1]
        else:
            print("いけんじゃね")
            return ans[1]

def main():
    global action, preAction, state, preState, choice
    # action : int = 0      #行動を表す　WAYによる（0から3)
    # state : int = 0       #状態を表す　STATEによる（0から24)
    # preState : int = 0    #
    reward : float = 0    #報酬を表す
    step : float = 0.0
    clear = 0
    gameover = 0
    # sumReward : float = 0.0
    # sumSteps : float = 0.0

    # static double EPSILON = 0.4;//イプシロングリーディ法に用いる
    # static double ROULETTE_ALPHA = 0.1;//ルーレット選択で初めに少し足す値
    # static double ALPHA = 0.2; //学習率
    # static double GAMMA = 0.99; //割引率
    # action : int = 0      #行動を表す　WAYによる（0から3)
    # state  : int = 0      #状態を表す　STATEによる（0から24)

    
    # open('calc.csv', 'w') as f:
    # writer = csv.writer(f)
        # writer.writerow([0, 1, 2])
        # writer.writerow(['a', 'b', 'c'])

    for cycle in range(MAX_CYCLE):

        # total_reward : float = 0;
        # total_step : float = 0;
        # reward1 : int = 0;
        # reward10 : int = 0;
        bid = [[0 for i in range(ACTION)] for j in range(STATE)]

        # Q表を０で初期化
        for i in range(STATE):
            for j in range(ACTION):
                Q[i][j] = 0;
        # for i in Q:
        #     print(i)

        for time in range(REPEAT):
            bid = [[0 for i in range(ACTION)] for j in range(STATE)]
            # print(time + 1, "回目", end="  ")
            state = 0
            preState = 0
            print(time + 1)
            # f2.write("{0}回目\n".format(time+1))
            # print("----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            #状態を初期化
            Verflucht.init()
            # preState = 0
            # state = 0
            # action = 0
            # preAction = 0
            flag = 0
            # for i in range(ACTION):
            #         bid[state][i] = Cbid * Q[state][i]
            # flag = Verflucht.chooseCommand(actionSelect(bid))
            # r = Verflucht.getReward()
            # preState = state
            # state = Verflucht.getState()
            # flag = Verflucht.chooseCommand(actionSelect(bid))
            while(not (flag == -1 or flag == 1 or flag == 2)):
                choice = [0, 1, 2, 3, 4]
                while(True):
                    # print("main choice: ", choice)
                    ans = actionSelect(bid)
                    # print("ans11: ", ans)
                    if(not ans[1] == [-1]):
                        # f2.write("1   state:{0}\taction:{1}\t".format(state,action))
                        flag = Verflucht.chooseCommand(ans)
                        break

                # print("flag: ", flag)
                r = Verflucht.getReward()
                # f2.write("reward: {0}\n".format(r))
                for i in range(ACTION):
                    bid[state][i] = Cbid * Q[state][i]
                #通常状態の選択
                # flag = Verflucht.chooseCommand(actionSelect(bid))
                # preState = state
                # print(type(Q[preState][preAction]))
                # print(type(r))
                # print("Q[{0}][{1}] += {2} + {3} - {4}\t({5})".format(preState, preAction, r, bid[state][action], bid[preState][preAction], Q[preState][preAction]))
                Q[preState][preAction] += r + bid[state][action] - bid[preState][preAction]
                preAction = action
                preState = state
                state = Verflucht.getState()
                if(flag == -1 or flag == 1 or flag == 2):
                    # print("終了します")
                    break
                elif(flag == 3 or flag == 4):
                    # Verflucht.printState()
                    #強制戦闘状態の選択
                    choice = [0, 1, 2, 3, 4]
                    while(True):
                        # print(choice)
                        ans = actionSelect2(bid)
                        # print("ans: ", ans)
                        if(not ans[0] == -2):
                            # print("ans", ans)
                            # f2.write(" 2  state:{0}\taction:{1}\t".format(state,action))
                            flag = Verflucht.afterCheck(ans)
                            if(flag == 0):
                                break
                    Verflucht.attackingMonster.clear()
                    r = Verflucht.getReward()
                    # f2.write("reward: {0}\n".format(r))
                    for i in range(ACTION):
                        bid[state][i] = Cbid * Q[state][i]
                    # print("{0} += {1} + {2} - {3}".format(Q[preState][preAction], r, bid[state][action], bid[preState][preAction]))
                    # print("Q[{0}][{1}] += {2} + {3} - {4}\t({5})".format(preState, preAction, r, bid[state][action], bid[preState][preAction], Q[preState][preAction]))
                    Q[preState][preAction] += r + bid[state][action] - bid[preState][preAction]
                    preAction = action
                    preState = state
                    state = Verflucht.getState()
                    # flag = Verflucht.chooseCommand(actionSelect(bid))
            r = Verflucht.getReward()
            if(flag == 1):
                clear += 1
                # f2.write("    clear   :{0}\n".format(r))
            elif(flag == 2):
                gameover += 1
                # f2.write("    gameOver:{0}\n".format(r))
            # s = "{0}, {1}".format(time, Verflucht.score)
            preAction = action
            preState = state
            state = Verflucht.getState()
            for i in range(ACTION):
                bid[state][i] = Cbid * Q[state][i]
            Q[preState][preAction] += r + bid[state][action] - bid[preState][preAction]
            # if(flag == 1):
                # print("Q[{0}][{1}] += {2} + {3} - {4}\t({5})".format(preState, preAction, r, bid[state][action], bid[preState][preAction], Q[preState][preAction]))
            # f.write("{0}, {1}\n".format(time, Verflucht.score))
    # f.write("\n\n")
    for i in range(len(Q)):
        # f.write("T{0}, ".format(i))
        for j in range(len(Q[i])):
            print('{:15.2f}'.format(Q[i][j]), end="\t\t")
            # f.write("{0},".format(Q[i][j]))
        print()
        # f.write("\n")
    print("clear   : ", clear)
    print("gameover: ", gameover)
    # f.close()
    # f2.close()

main()