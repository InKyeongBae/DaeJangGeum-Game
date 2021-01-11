import time


def digit_baseball():
    print()
    print()
    print()
    print()
    print()
    print('='*50)
    time.sleep(1)
    print('체력장 두 번째 종목은 야구다')
    time.sleep(1)
    print('숫자 야구도 야구다')
    time.sleep(1)
    print('내가 생각하는 네 자리 정수를 맞추어 보거라.')
    time.sleep(1)
    print('기회는 10번이다.')
    ans = list('9481')
    num_try = 0

    while True:
        strike = 0
        ball = 0
        time.sleep(1)
        print('네 자리 정수를 입력하여라. 각 자리 숫자는 모두 달라야한다.')
        my = input('=====> ')
        try:
            input_test = (len(list(str(int(my)))) == 4 and (len(set(my)) == 4))
            if input_test and set:
                my = list(my)
                for idx, digit in enumerate(my):
                    if digit in ans:
                        if ans[idx] == digit:
                            strike += 1
                        else:
                            ball += 1

                if strike+ball == 0:
                    print('OUT')
                else:
                    time.sleep(1)
                    print(f'{strike} strike {ball} ball')

                if num_try > 8:
                    time.sleep(1)
                    print()
                    print('많이 부족하구나.')
                    time.sleep(1)
                    print('돌아가거라.')
                    time.sleep(1)
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

                    return False
                if ans == my:
                    time.sleep(1)
                    print('정답이다. 장하구나.')
                    time.sleep(1)
                    print('')
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
                    return True
                num_try += 1
                time.sleep(0.5)
                print(f'현재 시도 횟수는 {num_try}이다.')
                print()

            else:
                print()
                print('각 자릿수가 다른 네 자리 정수를 옳게 입력한 것이 맞느냐?')
        except:
            print()
            print('네 자리 정수를 입력한 것이 맞느냐?')
