import random
import GameSystem


Verflucht = GameSystem
WAY : int = 4;
STATE : int= Verflucht.getMaxState();
Q = [[0]*WAY]*STATE
REPEAT : int = 2
MAX_CYCLE : int = 1
rnd = random.random()

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
# static int action;     //行動を表す　WAYによる（0から3)
# static int state;      //状態を表す　STATEによる（0から24)

for cycle in range(MAX_CYCLE):

    # print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    total_reward : float = 0;
    total_step : float = 0;
    reward1 : int = 0;
    reward10 : int = 0;

    # Q表を０で初期化
    for i in range(STATE):
        for j in range(WAY):
            Q[i][j] = 0;

    for time in range(REPEAT):
        print(time, "回目----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
        #状態を初期化
        Verflucht.init()
        preState = 0;
        flag = True
        while(flag):
            flag = Verflucht.chooseCommand(int(input("\nCommand:　")))
            if(not flag):
                print("終了します")
                break
            flag = Verflucht.fieldCheck()

   