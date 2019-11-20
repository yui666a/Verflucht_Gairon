import random
import GameSystem




Verflucht = GameSystem
ACTION : int = 4;
STATE : int= Verflucht.getMaxState();
Q = [[0]*ACTION]*STATE
REPEAT : int = 10
MAX_CYCLE : int = 1
Cbid : float = 0.1
rnd = random.random()

def actionSelect():
    s = Verflucht.getState()
    if(s % 2 == 0):
        Verflucht.printState()
        return [1]
    else:
        Verflucht.printState()
        print("タオセルソウデス\n")
        #クリーチャーのリストを取得
        fc = Verflucht.getFieldCreature()
        #武器のリストを取得
        hw = Verflucht.getHandWeapon()
        #ただドローしてるだけ
        #[コマンド選択, [クリーチャーの配列(1体のみ)], [武器の配列(インデックスで複数指定可能)]]
        return [1, [0], [0]]

def actionSelect2():
    s = Verflucht.getState()
    print("おそってくるモンスターの合計値", Verflucht.attackingMonster)
    #武器のリストを取得
    hw = Verflucht.getHandWeapon()
    #ライフで受けてる
    return [-1]


def main():
    # action : int = 0      #行動を表す　WAYによる（0から3)
    # state : int = 0       #状態を表す　STATEによる（0から24)
    preState : int = 0    #
    reward : float = 0    #報酬を表す
    step : float = 0.0
    # sumReward : float = 0.0
    # sumSteps : float = 0.0

    # static double EPSILON = 0.4;//イプシロングリーディ法に用いる
    # static double ROULETTE_ALPHA = 0.1;//ルーレット選択で初めに少し足す値
    # static double ALPHA = 0.2; //学習率
    # static double GAMMA = 0.99; //割引率
    action : int = 0      #行動を表す　WAYによる（0から3)
    state  : int = 0      #状態を表す　STATEによる（0から24)

    for cycle in range(MAX_CYCLE):

        total_reward : float = 0;
        total_step : float = 0;
        reward1 : int = 0;
        reward10 : int = 0;
        bid = [[0] * ACTION] * STATE

        # Q表を０で初期化
        for i in range(STATE):
            for j in range(ACTION):
                Q[i][j] = 0;

        for time in range(REPEAT):
            print(time + 1, "回目----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
            #状態を初期化
            Verflucht.init()
            preState = 0;
            flag = 0
            while(not flag == -1):
                # for i in range(ACTION):
                #     bid[state][i] = Cbid * Q[state][i]

                #通常状態の選択
                flag = Verflucht.chooseCommand(actionSelect())
                if(flag == -1 or flag == 1 or flag == 2):
                    # print("終了します")
                    break
                elif(flag == 3 or flag == 4):
                    Verflucht.printState()
                    #強制戦闘状態の選択
                    Verflucht.afterCheck(actionSelect2())

main()