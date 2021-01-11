import random
import time

def users_choice(myArray, user_input):
    if user_input == "w":
        i = 0
        for j in range(0, 4):
            if myArray[i][j] != 0 or myArray[i+1][j] != 0 or myArray[i+2][j] != 0 or myArray[i+3][j] != 0:
                if myArray[i][j] == 0:
                    while myArray[i][j] == 0:
                        myArray[i][j] = myArray[i+1][j]
                        myArray[i+1][j] = myArray[i+2][j]
                        myArray[i+2][j] = myArray[i+3][j]
                        myArray[i+3][j] = 0
                if myArray[i+1][j] == 0 and (myArray[i+2][j] != 0 or myArray[i+3][j] != 0):
                    while myArray[i+1][j] == 0:
                        myArray[i+1][j] = myArray[i+2][j]
                        myArray[i+2][j] = myArray[i+3][j]
                        myArray[i+3][j] = 0
                if myArray[i+2][j] == 0 and (myArray[i+3][j] != 0):
                    while myArray[i+2][j] == 0:
                        myArray[i+2][j] = myArray[i+3][j]
                        myArray[i+3][j] = 0
        i = 0
        for j in range(0, 4):
            if myArray[i][j] == myArray[i+1][j]:
                myArray[i][j] = myArray[i][j]+myArray[i+1][j]
                myArray[i+1][j] = myArray[i+2][j]
                myArray[i+2][j] = myArray[i+3][j]
                myArray[i+3][j] = 0
            if myArray[i+1][j] == myArray[i+2][j]:
                myArray[i+1][j] = myArray[i+1][j]+myArray[i+2][j]
                myArray[i+2][j] = myArray[i+3][j]
                myArray[i+3][j] = 0
            if myArray[i+2][j] == myArray[i+3][j]:
                myArray[i+2][j] = myArray[i+2][j]+myArray[i+3][j]
                myArray[i+3][j] = 0
    elif user_input == "s":
        i = 0
        for j in range(0, 4):
            if myArray[i][j] != 0 or myArray[i+1][j] != 0 or myArray[i+2][j] != 0 or myArray[i+3][j] != 0:
                if myArray[i+3][j] == 0:
                    while myArray[i+3][j] == 0:
                        myArray[i+3][j] = myArray[i+2][j]
                        myArray[i+2][j] = myArray[i+1][j]
                        myArray[i+1][j] = myArray[i][j]
                        myArray[i][j] = 0
                if myArray[i+2][j] == 0 and (myArray[i+1][j] != 0 or myArray[i][j] != 0):
                    while myArray[i+2][j] == 0:
                        myArray[i+2][j] = myArray[i+1][j]
                        myArray[i+1][j] = myArray[i][j]
                        myArray[i][j] = 0
                if myArray[i+1][j] == 0 and myArray[i][j] != 0:
                    while myArray[i+1][j] == 0:
                        myArray[i+1][j] = myArray[i][j]
                        myArray[i][j] = 0
        i = 0
        for j in range(0, 4):
            if myArray[i+3][j] == myArray[i+2][j]:
                myArray[i+3][j] = myArray[i+3][j] + myArray[i+2][j]
                myArray[i+2][j] = myArray[i+1][j]
                myArray[i+1][j] = myArray[i][j]
                myArray[i][j] = 0
            if myArray[i+2][j] == myArray[i+1][j]:
                myArray[i+2][j] = myArray[i+2][j]+myArray[i+1][j]
                myArray[i+1][j] = myArray[i][j]
                myArray[i][j] = 0
            if myArray[i+1][j] == myArray[i][j]:
                myArray[i+1][j] = myArray[i+1][j]+myArray[i][j]
                myArray[i][j] = 0
    elif user_input == "a":
        j = 0
        for i in range(0, 4):
            if myArray[i][j] != 0 or myArray[i][j+1] != 0 or myArray[i][j+2] != 0 or myArray[i][j+3] != 0:
                if myArray[i][j] == 0:
                    while myArray[i][j] == 0:
                        myArray[i][j] = myArray[i][j+1]
                        myArray[i][j+1] = myArray[i][j+2]
                        myArray[i][j+2] = myArray[i][j+3]
                        myArray[i][j+3] = 0
                if myArray[i][j+1] == 0 and (myArray[i][j+2] != 0 or myArray[i][j+3] != 0):
                    while myArray[i][j+1] == 0:
                        myArray[i][j+1] = myArray[i][j+2]
                        myArray[i][j+2] = myArray[i][j+3]
                        myArray[i][j+3] = 0
                if myArray[i][j+2] == 0 and (myArray[i][j+3] != 0):
                    while myArray[i][j+2] == 0:
                        myArray[i][j+2] = myArray[i][j+3]
                        myArray[i][j+3] = 0
        j = 0
        for i in range(0, 4):
            if myArray[i][j] == myArray[i][j+1]:
                myArray[i][j] = myArray[i][j]+myArray[i][j+1]
                myArray[i][j+1] = myArray[i][j+2]
                myArray[i][j+2] = myArray[i][j+3]
                myArray[i][j+3] = 0
            if myArray[i][j+1] == myArray[i][j+2]:
                myArray[i][j+1] = myArray[i][j+1]+myArray[i][j+2]
                myArray[i][j+2] = myArray[i][j+3]
                myArray[i][j+3] = 0
            if myArray[i][j+2] == myArray[i][j+3]:
                myArray[i][j+2] = myArray[i][j+2]+myArray[i][j+3]
                myArray[i][j+3] = 0
    elif user_input == "d":
        j = 0
        for i in range(0, 4):
            if myArray[i][j] != 0 or myArray[i][j+1] != 0 or myArray[i][j+2] != 0 or myArray[i][j+3] != 0:
                if myArray[i][j+3] == 0:
                    while myArray[i][j+3] == 0:
                        myArray[i][j+3] = myArray[i][j+2]
                        myArray[i][j+2] = myArray[i][j+1]
                        myArray[i][j+1] = myArray[i][j]
                        myArray[i][j] = 0
                if myArray[i][j+2] == 0 and (myArray[i][j+1] != 0 or myArray[i][j] != 0):
                    while myArray[i][j+2] == 0:
                        myArray[i][j+2] = myArray[i][j+1]
                        myArray[i][j+1] = myArray[i][j]
                        myArray[i][j] = 0
                if myArray[i][j+1] == 0 and myArray[i][j] != 0:
                    while myArray[i][j+1] == 0:
                        myArray[i][j+1] = myArray[i][j]
                        myArray[i][j] = 0
        j = 0
        for i in range(0, 4):
            if myArray[i][j+3] == myArray[i][j+2]:
                myArray[i][j+3] = myArray[i][j+3] + myArray[i][j+2]
                myArray[i][j+2] = myArray[i][j+1]
                myArray[i][j+1] = myArray[i][j]
                myArray[i][j] = 0
            if myArray[i][j+2] == myArray[i][j+1]:
                myArray[i][j+2] = myArray[i][j+2]+myArray[i][j+1]
                myArray[i][j+1] = myArray[i][j]
                myArray[i][j] = 0
            if myArray[i][j+1] == myArray[i][j]:
                myArray[i][j+1] = myArray[i][j+1]+myArray[i][j]
                myArray[i][j] = 0


def do2048():
    quest_num = 0
    myArray = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    inducerlist = [0, 1, 2, 3]
    myArray[random.choice(inducerlist)][random.choice(inducerlist)] = 2
    print("="*50)
    print()
    time.sleep(1); print("진정한 장금이로 거듭나고 싶은가? 2048게임을 시작해보자꾸나!")
    time.sleep(1); print("2048게임은 w,s,a,d를 입력하여 블럭들을 상,하,좌,우로 이동시키는 게임이다")
    time.sleep(1); print("상하좌우로 블럭들이 이동할 때 이동하는 방향에 같은 숫자의 블럭이 있으면 블럭이 합쳐진다!")
    time.sleep(1); print("이 게임을 중도 포기하고 싶으면 quit을 입력하라!이런 의지박약한 자식같으니라고!!")
    time.sleep(1); print("더 이상 블럭이 움직일 수 없어도 너는 좋은 재료를 얻지 못하니 주의하거라")
    time.sleep(1); print("128블럭을 만들면 너는 2048게임 미션을 성공한 것으로 간주하겠다! 이제 도전하자꾸나!")
    time.sleep(1); print()
    print("="*50)

    while True:
        print(myArray[0][0], "\t", myArray[0][1], "\t",
              myArray[0][2], "\t", myArray[0][3], "\n")
        print(myArray[1][0], "\t", myArray[1][1], "\t",
              myArray[1][2], "\t", myArray[1][3], "\n")
        print(myArray[2][0], "\t", myArray[2][1], "\t",
              myArray[2][2], "\t", myArray[2][3], "\n")
        print(myArray[3][0], "\t", myArray[3][1], "\t",
              myArray[3][2], "\t", myArray[3][3], "\n")
        print('w for upward direction, s for downwards, a for left ,and d for Right')
        print('Type "quit" if you want to give up the game.')
        user_input = input()

        while(user_input != "w" and user_input != "a" and user_input != "s" and user_input != "d" and user_input != "quit"):
            print("Input Again!")
            print('w for upward direction, s for downwards, a for left ,and d for Right')
            print('Type "quit" if you want to give up the game.')
            user_input = input()
        if user_input == 'quit':
            print("="*50)
            print("Mission Fail")
            print('')
            print(
                '  ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗    ██╗')
            print(
                '  ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝    ██║')
            print(
                '   ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗      ██║')
            print(
                '    ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝      ╚═╝')
            print(
                '     ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗    ██╗')
            print(
                '     ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝')
            print("square 2048 Game over")
            print("="*50)
            return False

        users_choice(myArray, user_input)
        listfori = []
        listforj = []
        count = 0
        for i in range(0, 4):
            for j in range(0, 4):
                if myArray[i][j] == 0:
                    count += 1
                    listfori.append(i)
                    listforj.append(j)
                elif myArray[i][j] == 128:
                    quest_num = 1
                    print("="*50)
                    print("You make 128!!Quest Complete!!")
                    print(
                        '  ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗  ██╗')
                    print(
                        '  ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║  ██║')
                    print(
                        '   ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║  ██║')
                    print(
                        '    ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║  ╚═╝')
                    print(
                        '     ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║  ██╗')
                    print(
                        '     ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝  ╚═╝')
        print()
        print('='*50)
        print()
        if count > 0:
            if quest_num == 1:
                return True
            if count > 1:
                randomindex = listfori.index(random.choice(listfori))
                myArray[listfori[randomindex]][listforj[randomindex]] = 2
            else:
                myArray[listfori[0]][listforj[0]] = 2
        else:
            print("="*50)
            print("Mission Fail")
            print('')
            print(
                '  ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗    ██╗')
            print(
                '  ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝    ██║')
            print(
                '   ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗      ██║')
            print(
                '    ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝      ╚═╝')
            print(
                '     ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗    ██╗')
            print(
                '     ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝')
            print("square 2048 Game over")
            print("="*50)
            return False
