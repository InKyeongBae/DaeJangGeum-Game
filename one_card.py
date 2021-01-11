import random
import time


def one_card():
    time.sleep(1)
    print('='*50)
    print('마지막 게임은 바로 1:1 원카드')
    time.sleep(1)
    print('게임에 대한 설명은 생략한다.')
    time.sleep(1)
    print('설마 원카드 규칙도 모르는건 아니겠지')
    time.sleep(1)
    print('그럼 너부터 시작해보거라.')
    time.sleep(1)
    # card 생성
    nums = []
    shapes = '♥♣♠◆'
    for i in range(2, 11):
        nums.append(str(i))
    for c in 'JQKA':
        nums.append(c)

    # deck 생성
    deck = []
    for num in nums:
        for shape in shapes:
            deck.append((shape, num))
    deck.append(('Joker', 'Black'))
    deck.append(('Joker', 'Color'))
    random.shuffle(deck)

    # card 분배
    player = []
    computer = []
    for i in range(7):
        player.append(deck.pop())
        computer.append(deck.pop())

    # 바닥에 카드 놓기
    put = []
    put.append(deck.pop())

    # attack_num
    attack_num = 0
    # is_attack
    is_attack = 0

    # game start
    while True:
        if len(computer) == 0:
            break
        # player turn
        print('##########################################################')
        print('player 차례입니다.')
        print('보유 카드 목록: ', player)
        print('놓여진 카드: ', put[-1])

        # 낼 수 있는 카드 찾기
        player_available = []
        for card in player:
            if (put[-1][1] == 'A' and is_attack == 1):
                if (card[1] == 'A' or card[0] == 'Joker'):
                    player_available.append(card)
            elif (put[-1][1] == '2' and is_attack == 1):
                if (card[1] == '2' or card[1] == 'A' or card[0] == 'Joker'):
                    player_available.append(card)
            elif (put[-1][0] == 'Joker' and is_attack == 1):
                if (card[0] == 'Joker'):
                    player_available.append(card)
            elif(is_attack == 0 and put[-1][0] == 'Joker'):
                player_available.append(card)
            elif (is_attack == 0 and put[-1][0] != 'Joker'):
                if(card[0] == put[-1][0] or card[1] == put[-1][1] or card[0] == 'Joker'):
                    player_available.append(card)

        if len(player_available) == 0:
            if attack_num > 0:

                # check deck empty list
                if len(deck) < attack_num:
                    print('1.카드를 다시 섞습니다.')
                    deck.extend(put[:-1])
                    random.shuffle(deck)
                    for i in range(attack_num):
                        player.append(deck.pop())
                else:
                    for i in range(attack_num):
                        player.append(deck.pop())
                print(f'player가 {attack_num}장 만큼 가져옵니다.')
                attack_num = 0
                is_attack = 0
            else:
                # check deck empty list
                if not deck:
                    print('2.카드를 다시 섞습니다.')
                    deck.extend(put[:-1])
                    random.shuffle(deck)
                    print('player가 낼 수 있는 카드가 없으므로 카드를 한 장 가져옵니다.')
                    player.append(deck.pop())
                else:
                    print('player가 낼 수 있는 카드가 없으므로 카드를 한 장 가져옵니다.')
                    player.append(deck.pop())
        else:
            print('낼 수 있는 카드: ', player_available)
            i = int(input('몇 번째 카드를 내시겠습니까?:(종료:0을 입력하세요) '))
            if i == 0:
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
                print('')
                return False
                break
            if(i > len(player_available)):
                print("선택 할 수 없는 카드입니다! 다시 선택해주세요!")
                i = int(input('몇 번째 카드를 내시겠습니까?:(종료:0을 입력하세요) '))
                if i == 0:
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
                    print('')
                    return False
                    break

            i -= 1
            player_select = player_available[i]
            player.remove(player_select)
            put.append(player_select)

            # 공격 카드 경우
            if (player_select[1] == '2'):
                attack_num += 2
                is_attack = 1
            elif (player_select[1] == 'A'):
                attack_num += 3
                is_attack = 1
            elif (player_select[0] == 'Joker'):
                attack_num += 5
                is_attack = 1
            # J 또는 Q 경우
            elif (player_select[1] == 'J' or player_select[1] == 'K'):
                continue

        if len(player) == 0:
            print('')
            print('  ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗  ██╗')
            print('  ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║  ██║')
            print('   ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║  ██║')
            print('    ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║  ╚═╝')
            print('     ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║  ██╗')
            print('     ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝  ╚═╝')
            print('')
            return True
            break

        while True:
            # computer turn
            print('##########################################################')
            print('computer 차례입니다.')
            computer_available = []
            for card in computer:
                if (put[-1][1] == 'A' and is_attack == 1):
                    if (card[1] == 'A' or card[0] == 'Joker'):
                        computer_available.append(card)
                elif (put[-1][1] == '2' and is_attack == 1):
                    if (card[1] == '2' or card[1] == 'A' or card[0] == 'Joker'):
                        computer_available.append(card)
                elif (put[-1][0] == 'Joker' and is_attack == 1):
                    if (card[0] == 'Joker'):
                        computer_available.append(card)
                elif (is_attack == 0 and put[-1][0] == 'Joker'):
                    computer_available.append(card)
                elif (is_attack == 0 and put[-1][0] != 'Joker'):
                    if (card[0] == put[-1][0] or card[1] == put[-1][1] or card[0] == 'Joker'):
                        computer_available.append(card)

            if len(computer_available) == 0:

                if attack_num > 0:

                    # check deck empty list
                    if len(deck) < attack_num:
                        print('3.카드를 다시 섞습니다.')
                        deck.extend(put[:-1])
                        random.shuffle(deck)
                        for i in range(attack_num):
                            computer.append(deck.pop())
                    else:
                        for i in range(attack_num):
                            computer.append(deck.pop())
                    print(f'컴퓨터가 {attack_num}만큼 가져갑니다.')
                    attack_num = 0
                    is_attack = 0
                else:
                    # check deck empty list
                    if not deck:
                        print('4.카드를 다시 섞습니다.')
                        deck.extend(put[:-1])
                        random.shuffle(deck)
                        print('컴퓨터가 낼 수 있는 카드가 없으므로 카드를 한 장 가져갑니다.')
                        computer.append(deck.pop())
                    else:
                        print('컴퓨터가 낼 수 있는 카드가 없으므로 카드를 한 장 가져갑니다.')
                        computer.append(deck.pop())

            else:
                computer_select = random.choice(computer_available)
                computer.remove(computer_select)
                put.append(computer_select)
                print(f'컴퓨터가 {computer_select}를 냈습니다.')

                # 공격 카드 경우
                if (computer_select[1] == '2'):
                    attack_num += 2
                    is_attack = 1
                elif (computer_select[1] == 'A'):
                    attack_num += 3
                    is_attack = 1
                elif (computer_select[0] == 'Joker'):
                    attack_num += 5
                    is_attack = 1
                # J 또는 Q 경우
                elif (computer_select[1] == 'J' or computer_select[1] == 'K'):
                    continue

            if len(computer) == 0:
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
                print('')
                return False
                break
            break


    
