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

    print("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n")
    total_reward : float = 0;
    total_step : float = 0;
    reward1 : int = 0;
    reward10 : int = 0;

    # Q表を０で初期化
    for i in range(STATE):
        for j in range(WAY):
            Q[i][j] = 0;

    for time in range(REPEAT):
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
    #     while (not Verflucht.Q.getStateIsGoal()): #終状態であればbreak

    #         #現在の状態を取得
    #         state = Verflucht.Q.getState();
    #         #現在の状態のQ表を配列にする
    #         double[] line = { Q[state, 0], Q[state, 1], Q[state, 2], Q[state, 3] };


    #         do:
    #         {
    #             //ルーレット選択を行う
    #             //action = roulette(line);

    #             //イプシロングリーディ法による選択を行う
    #             action = Epsilon_Greedy(line);

    #             //Console.WriteLine(reward);

    #         } while (maze.getNextState(action) == preState || maze.getNextState(action) == state);
    #         //報酬を観測
    #         //Console.WriteLine("action: " + maze.nextState(action));
    #         reward = maze.doAction(action);
    #         //Q表を更新
    #         Q[state, action] = (1 - ALPHA) * Q[state, action] + ALPHA * (reward + GAMMA * maxQ(state, action, maze));
    #         //Console.WriteLine("Q[" + state + ", " + action + "] = (1 - ALPHA) * " + Q[state, action] + " + ALPHA * (" + reward + " + GAMMA * " + maxQ(state, action, maze) + ") = " + ((1 - ALPHA) * Q[state, action] + ALPHA * (reward + GAMMA * maxQ(state, action, maze))));


    #         //Console.WriteLine("state : " + state + "\taction : " + action + "\treward : " + reward+ "\tstep : " + step);
    #         step++;
    #         //maze.nextState(action);
    #         //Console.Write("getState: ");        Console.WriteLine(maze.getState());
    #         //Console.Write("getPreState: ");     Console.WriteLine(preState);
    #         preState = state;
    #         //state = maze.getState();
    #     }
    #     state = maze.getState();
    #     //Console.WriteLine(getState());
    #     if (getState() == 24)
    #         countReward[0]++;
    #     else if (getState() == 8)
    #         countReward[1]++;
    #     else if (getState() == 16)
    #         countReward[2]++;
    #     else if (getState() == 18)
    #         countReward[3]++;
    #     else
    #         countReward[4]++;

    #     if (reward.Equals(10))
    #         reward10++;
    #     else if (reward.Equals(1))
    #         reward1++;


    #     total_reward += reward;//累計獲得報酬
    #     total_step += step;

    #     kakunoReward[time] = total_reward;
    #     //（３）で用いる
    #     //Console.WriteLine((time + 1) + "\t\t" + total_reward / total_step + "\t\t報酬：" + reward);
    #     reward = 0;

    #     if (time % 5 == 0)
    #     {
    #         kouritu[1][time / 5] = reward10;
    #         kouritu[0][time / 5] = reward1;
    #     }

    #     Console.WriteLine(kouritu[0][time / 5] + "\t" + kouritu[1][time / 5]);

    #     /*if (reward == 1.0)
    #         countReward[0]++;
    #     else if (reward == 5.0)
    #         countReward[1]++;
    #     else
    #         countReward[2]++;*/
    #     //Console.WriteLine(time);
    #     //showQTable();
    # }
    # Console.WriteLine("平均ステップ" + total_step / REPEAT);//
    # Console.WriteLine("平均報酬" + total_reward / REPEAT);
    # //Console.Beep();
    # //System.Media.SystemSounds.Asterisk.Play();




    # //（３）で用いる
    # /*total_reward += reward;//累計獲得報酬
    # total_step += step;
    # kakunoReward[REPEAT - 1] = total_reward;
    # kakunoSteps[REPEAT - 1] = total_step;

    # //Console.WriteLine(5000 + "\t\t" + total_reward / total_step);
    # kouritu[test][REPEAT / 5 - 1] = total_reward / total_step;
    # //Console.WriteLine("ゴールしました。報酬は" + reward + "でした");
    # */
    # showQTable();

'''


            //課題（３）で用いる

            double[] kakunoReward = new double[REPEAT];
            double[] kakunoSteps = new double[REPEAT];
            double[][] kouritu = new double[2][];
            for (int i = 0; i < 2; i++)
                kouritu[i] = new double[REPEAT / 5];

            double[] countReward = { 0, 0, 0, 0, 0 };

            for (int test = 0; test < TEST; test++)
            {
                Console.Write("------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");
                double total_reward = 0;
                double total_step = 0;
                int reward1 = 0;
                int reward10 = 0;

                //Q表を０で初期化
                for (int i = 0; i < STATE; i++)
                    for (int j = 0; j < WAY; j++)
                        Q[i, j] = 0;

                for (int time = 0; time < REPEAT; time++)
                {

                    //状態を初期化
                    maze.initState();
                    step = 0;
                    preState = 0;
                    while (!maze.getStateIsGoal())//終状態であればbreak
                    {

                        //現在の状態を取得
                        state = maze.getState();
                        //現在の状態のQ表を配列にする
                        double[] line = { Q[state, 0], Q[state, 1], Q[state, 2], Q[state, 3] };


                        do
                        {
                            //ルーレット選択を行う
                            //action = roulette(line);

                            //イプシロングリーディ法による選択を行う
                            action = Epsilon_Greedy(line);

                            //Console.WriteLine(reward);

                        } while (maze.getNextState(action) == preState || maze.getNextState(action) == state);
                        //報酬を観測
                        //Console.WriteLine("action: " + maze.nextState(action));
                        reward = maze.doAction(action);
                        //Q表を更新
                        Q[state, action] = (1 - ALPHA) * Q[state, action] + ALPHA * (reward + GAMMA * maxQ(state, action, maze));
                        //Console.WriteLine("Q[" + state + ", " + action + "] = (1 - ALPHA) * " + Q[state, action] + " + ALPHA * (" + reward + " + GAMMA * " + maxQ(state, action, maze) + ") = " + ((1 - ALPHA) * Q[state, action] + ALPHA * (reward + GAMMA * maxQ(state, action, maze))));


                        //Console.WriteLine("state : " + state + "\taction : " + action + "\treward : " + reward+ "\tstep : " + step);
                        step++;
                        //maze.nextState(action);
                        //Console.Write("getState: ");        Console.WriteLine(maze.getState());
                        //Console.Write("getPreState: ");     Console.WriteLine(preState);
                        preState = state;
                        //state = maze.getState();
                    }
                    state = maze.getState();
                    //Console.WriteLine(getState());
                    if (getState() == 24)
                        countReward[0]++;
                    else if (getState() == 8)
                        countReward[1]++;
                    else if (getState() == 16)
                        countReward[2]++;
                    else if (getState() == 18)
                        countReward[3]++;
                    else
                        countReward[4]++;

                    if (reward.Equals(10))
                        reward10++;
                    else if (reward.Equals(1))
                        reward1++;


                    total_reward += reward;//累計獲得報酬
                    total_step += step;

                    kakunoReward[time] = total_reward;
                    //（３）で用いる
                    //Console.WriteLine((time + 1) + "\t\t" + total_reward / total_step + "\t\t報酬：" + reward);
                    reward = 0;

                    if (time % 5 == 0)
                    {
                        kouritu[1][time / 5] = reward10;
                        kouritu[0][time / 5] = reward1;
                    }

                    Console.WriteLine(kouritu[0][time / 5] + "\t" + kouritu[1][time / 5]);

                    /*if (reward == 1.0)
                        countReward[0]++;
                    else if (reward == 5.0)
                        countReward[1]++;
                    else
                        countReward[2]++;*/
                    //Console.WriteLine(time);
                    //showQTable();
                }
                Console.WriteLine("平均ステップ" + total_step / REPEAT);//
                Console.WriteLine("平均報酬" + total_reward / REPEAT);
                //Console.Beep();
                //System.Media.SystemSounds.Asterisk.Play();




                //（３）で用いる
                /*total_reward += reward;//累計獲得報酬
                total_step += step;
                kakunoReward[REPEAT - 1] = total_reward;
                kakunoSteps[REPEAT - 1] = total_step;

                //Console.WriteLine(5000 + "\t\t" + total_reward / total_step);
                kouritu[test][REPEAT / 5 - 1] = total_reward / total_step;
                //Console.WriteLine("ゴールしました。報酬は" + reward + "でした");
                */
                showQTable();
            }
            WriteCsv(kouritu);

            Console.WriteLine("  10 (24) : " + countReward[0]);
            Console.WriteLine("   1 ( 8) : " + countReward[1]);
            Console.WriteLine("   1 (16) : " + countReward[2]);
            Console.WriteLine("   1 (18) : " + countReward[3]);
            //Console.WriteLine("-100 : " + countReward[4]);
            //Console.WriteLine("平均ステップは" + (sumSteps / TEST) + "平均報酬は" + (sumReward / TEST) + "でした");
            Console.Read();
        }















        static int getState()
        {
            return state;
        }

        /// <summary>
        /// Q表を表示するメソッド
        /// </summary>
        static void showQTable()
        {
            Console.WriteLine();
            for (int j = 0; j < STATE; j++)
                Console.Write(j + "\t");
            Console.WriteLine();
            Console.Write("-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n");

            for (int i = 0; i < WAY; i++)
            {
                for (int j = 0; j < STATE; j++)
                {
                    Console.Write($"{Q[j, i]:F3}" + "\t");
                }
                Console.WriteLine();
            }

        }


        static double maxQ(int s, int a, Maze maze)
        {
            double max = 0;
            int sNext = maze.getState();

            for (int i = 0; i < WAY; i++)
                if (max < Q[sNext, i])
                    max = Q[sNext, i];
                   
            return max;
        }

        /// <summary>
        /// ルーレット方式
        /// </summary>
        /// <param name=""></param>
        /// <returns></returns>
        int roulette(double[] q)
        {

            double sum = 0;             //適合度の合計
            double[] range = new double[WAY];   //範囲の境界値を保存する．
            int choice = 0;  //親世代遺伝子の使用するインデックスを格納する

            //適合度の累計及び，累計の境界値を計算する．
            for (int i = 0; i < WAY; i++)
            {
                sum += q[i] + ROULETTE_ALPHA;
                range[i] = sum;
            }

            //選択する位置を決定
            double pointer = rnd.NextDouble() * sum;
            for (int j = 0; j < WAY; j++)
                if (pointer < range[j])
                {
                    choice = j;
                    break;
                }
            return choice;
        }

        int showRoulette(double[] q)
        {
            double sum = 0;             //適合度の合計
            double[] range = new double[WAY];   //範囲の境界値を保存する．
            int choice = 0;  //親世代遺伝子の使用するインデックスを格納する

            /*Console.WriteLine();
            Console.WriteLine(rnd.NextDouble());
            Console.WriteLine();*/

            //適合度の累計及び，累計の境界値を計算する．
            for (int i = 0; i < WAY; i++)
            {
                sum += q[i] + ROULETTE_ALPHA;
                range[i] = sum;
                Console.Write(range[i] + " ");
            }

            //選択する位置を決定
            double pointer = rnd.NextDouble() * sum;
            Console.WriteLine("\n" + pointer);
            for (int j = 0; j < WAY; j++)
                if (pointer < range[j])
                {
                    choice = j;
                    break;
                }
            return choice;
        }


        static int Epsilon_Greedy(double[] q)
        {
            int max = 0;

            for (int i = 1; i < WAY; i++)
                if (q[i] > q[max])
                    max = i;

            double random = rnd.NextDouble();
            if (random > (EPSILON))
                return max;

            random = rnd.NextDouble();
            for (int i = 1; i <= WAY; i++)
                if (random <= ((double)i / (double)WAY))
                    return i - 1;
            return 0;
        }


        private static void WriteCsv(double[][] kouritu)
        {

            try
            {
                // appendをtrueにすると，既存のファイルに追記
                //         falseにすると，ファイルを新規作成する
                var append = false;
                // 出力用のファイルを開く
                using (var sw = new System.IO.StreamWriter(@"PARCENT2.csv", append))
                {
                    sw.WriteLine("{0}, {1}, {2},",
                                 "episode", "1", "10" );
                    for (int i = 0; i < kouritu[0].Length; ++i)
                    {
                        // 
                        //sw.WriteLine("{0}, {1}, {2},{3},", i, "&", kouritu[i], "\\\\\\hline" );
                        sw.WriteLine("{0}, {1}, {2},", i + 1, kouritu[0][i], kouritu[1][i]);
                    }
                }
                Console.WriteLine("正常に終了しました．");
            }
            catch (System.Exception e)
            {
                // ファイルを開くのに失敗したときエラーメッセージを表示
                System.Console.WriteLine(e.Message);
            }
        }

    }









    public class Maze
    {
        static int state;
        static int preState;
        public Maze()
        {
            state = 0;
            preState = 0;
        }

        static int[,] viaRoute =
        {
            /*パターン１
            { 0,  5,  1,  0},//0
            { 1,  6,  2,  0},//1
            { 2,  7,  3,  1},//2
            { 3,  8,  4,  2},//3
            { 4,  9,  4,  3},//4
            { 0, 10,  6,  5},//5
            { 1, 11,  7,  5},//6
            { 2, 12,  8,  6},//7
            { 3, 13,  9,  7},//8
            { 4, 14,  9,  8},//9
            { 5, 15, 11, 10},//10
            { 6, 16, 12, 10},//11
            { 7, 17, 13, 11},//12
            { 8, 18, 14, 12},//13
            { 9, 19, 14, 13},//14
            {10, 20, 16, 15},//15
            {11, 21, 17, 15},//16
            {12, 22, 18, 16},//17
            {13, 23, 19, 17},//18
            {14, 24, 19, 18},//19
            {15, 20, 21, 20},//20
            {16, 21, 22, 20},//21
            {17, 22, 23, 21},//22
            {18, 23, 24, 22},//23
            {19, 24, 24, 23} //24
            */
            //パターン２　
            //理想は16ステップ
            { 0,  5,  0,  0},//0
            { 1,  6,  2,  1},//1
            { 2,  2,  3,  1},//2
            { 3,  3,  4,  2},//3
            { 4,  9,  4,  3},//4
            { 0, 10,  5,  5},//5
            { 1, 11,  6,  6},//6
            { 7,  7,  8,  6},//7
            { 8,  8,  8,  7},//8
            { 4, 14,  9,  9},//9
            { 5, 15, 11, 10},//10
            { 6, 11, 11, 10},//11
            {12, 17, 13, 12},//12
            {13, 13, 14, 12},//13
            { 9, 14, 14, 13},//14
            {10, 20, 15, 15},//15
            {16, 21, 16, 16},//16
            {12, 22, 17, 17},//17
            {18, 18, 19, 18},//18
            {14, 19, 19, 18},//19
            {15, 20, 21, 20},//20
            {16, 21, 21, 20},//21
            {17, 22, 23, 22},//22
            {23, 23, 24, 22},//23
            {24, 24, 24, 24} //24

        };



        //8 16 18
        //                           0    1    2    3    4    5    6    7    8    9   10   11   12   13   14   15   16   17   18   19   20   21   22   23   24
        static double[] reward = {   0,   0,   0,   0,   0,   0,   0,   0,   1,   0,   0,   0,   0,   0,   0,   0,   1,   0,   1,   0,   0,   0,   0,   0,  10 };
 
        public int getState()
        {
            return state;
        }

        public int getPreState()
        {
            return preState;
        }

        public double doAction(int action)
        {
            state = getNextState(action);
            return reward[state];
        }

        public int getNextState(int action)
        {
            //preState = state;
            //state = viaRoute[state, action];
            return viaRoute[state, action];
        }

        public bool getStateIsGoal()
        {
            if (!reward[state].Equals(0))
            {
                //Console.WriteLine(reward[state]);
                return true;
            }
            else
                return false;
        }

        public void initState()
        {
            state = 0;
            preState = 0;
        }
    }
'''