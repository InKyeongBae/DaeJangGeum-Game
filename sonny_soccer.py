import time
import sys
from time import sleep


def field():
    print(
        '##########################################\n''\n''프\n''리\n킥   o                                                                                     [T골대T]')
    print('덤\n''벼\n''\n##########################################')
    a = int(input("정답은 150 이하 숫자, kick!:"))
    #try exception


def oo():

    sys.stdout.write('o')
    sys.stdout.flush()


def ceremony():
    print('   ___    _____  _____  ___     _   _ ')
    print('  (  _`\ (  _  )(  _  )(___)   ( ) ( ) ')
    print('  | ( (_)| ( ) || (_) | | |    | | | |')
    print('  | |___ | | | ||  _  | | |    | | | |')
    print('  | (_, )| (_) || | | | | |___ [_] [_]')
    print('  (____/\'(_____)(_) (_) (_____)(_) (_)')


def shoot(a):
    for i in range(a):
        if a <= 30:
            sleep(0.05)
            oo()
        if 30 < a <= 60:
            sleep(0.025)
            oo()
        if 60 < a <= 100:
            sleep(0.005)
            oo()
    print('\n\n\n')


def result(a):
    sleep(1.5)
    if a <= 30:
        print('안되겠다. 지금부터 줄넘기 100회 실시!')
        return False
    if 30 < a <= 60:
        print('정신차려! 프리미어의 세계는 동네축구 수준과는 차원이 다르다구!')
        return False
    if 60 < a <= 93 or a > 97:
        print('축구는 마음으로 하는것, 심기를 가다듬고 골대를 노려봐!')
        return False
    if 150<a :
        print('이건 프리킥이지 골킥이 아니다. 정신차려!')
        return False

    if 94 <= a <= 97:
        ceremony()
        return True
    print('\n\n')


# sonny
def sonny():
    print('dddddddddddddddddddddddddddddol: , .                  ..    ......\', ; : looodddodooooooooooooooooooooooo')
    time.sleep(0.05)
    print('dddddddddddddddddddddddooolc; , \'..             .            ..    ....\'; lodddddoddooooooooooooooooooo')
    time.sleep(0.05)
    print('dddddddddddddddddddddo: \'.......                             .          .,coddddoddddddoooooooooooooo')
    time.sleep(0.05)
    print('ddddddddddddddddddddo: ....  ...                                          .; ldddddddddddddddddddooooo')
    time.sleep(0.05)
    print('ddddddddddddddddddddl, ....  ..                .., lddddddddddddddddddddddo')
    time.sleep(0.05)
    print('ddddddddddddddddddddo; .....           .....  ..., odddddddddddddddddddddd')
    time.sleep(0.05)
    print('dddddddddddddddddddddo; ....  ...\';:clcccc;\'....                             .; oddddddddddddddddddddd')
    time.sleep(0.05)
    print('ddddddddddddddddddddddl: \'. .;loodxkkOOOOOkxdoc;\'.                            .cddddddddddddddddddddd')
    time.sleep(0.05)
    print('xddddddddddddddddddddddl,..lxxxxxxkOO00000OOkdo:\'.; odddddddddddddddddddd')
    time.sleep(0.05)
    print('xxdddddddddddddddddddddl..,kOxxxxkkOO00000OOkdl:\'.    .                       \'odddddddddddddddddddd')
    time.sleep(0.05)
    print('xxxxdddddddddddddddddddl\'.cOkxxxxkkOOOOOOOkkdolc; .......                      \'ldddddddddddddddddddd')
    time.sleep(0.05)
    print('xxxxxddddddddddddddxddxd,.l0OkxkkkOOOOOOOOOkkxddoc:;\'...                     ., odddddddddddddddddddd')
    time.sleep(0.05)
    print('xxxxxxxdddddddddddddddxd;.d0kkkkOOOOOOOOOOOOkkkxdoooc;,\'........            .., odddddddddddddddddddd')
    time.sleep(0.05)
    print('xxxxxxxxxddddddddddddddx:,ldccc:cldxkOOOOOkxdoc;,,;;,,,,,\'\'\'\'\'...           ..:ddddddddddddddddddddd')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxddddxc,locccccccldxxxxdocc::;;;;;,\'\'\'\'\', , \',\'\'..         ..\'lddddddddddddddddddddd')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxcckOkkOOkdooooooolc::codxxxdlc:,,,,,,,,,\'..         .: dddddddddddddddddddddd')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxokK0kxddolloooddoc::coddddoolc:;;,,;;,,,,\'.       ..\':oddddddddddddddddddddd')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxddOOdlcc;..,lddxko::co:;c,...\'\'\',,;;;;;;;,\'.   .....\'\'.:ddddddddddddddddddddd')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxkO0Okkxdolcldkxkxo::oollolc:::,,;:ccc::;;;,.. ..\'\'\'.\'\'.,oxddddddddddddddddddd')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxO00Okkkxxdxxkkxxdc;;ldxddoolllloddoolc::::;\'...,,...\'\'\';oxddddddxddddddxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxk00O0000000Okxxkkdc;;:lxOO000000kxxdolcccclc,..;;\'....,,:dxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxkKKO00KK00OkxxkOkoc;;;cdO000000Okxdolc:ccodo:,;:;\'....,;lxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxkKK00000Oxoodxk0koc:,,;lkOO00OOkxdolcc:cldxl;;::,....\';cdxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxx0KOkkxoc,;oOOkkxl:;;:;;cdxkkkxdollc:::coxxl;::;\'.\'\'\';ldxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxkOkdoc,\',lddllcc;,\'\'\'\'..;llllllc:::;;:coxxdc::,,,;:ldxxxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxdl:,\':oxxdlc;,........,;:::::;;;;;;;:ldxkxc,;codxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxdoc:;coxxxxxdc;,....\'\',;;;:::;,,,,;;;codxxllodxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxdoll:,;;;;:cc:;,\'..\'.....,c::;,,,,,;cloddodxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxddolc:\'\'coolcc,\'......;cllc:;,,,;;:clldooxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxddoodxdodk00Oko:;,,;:cccc::;,,;;;::ccloloxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxddddxkOxlloolc;,,,;;::::;;;,,;;;:::clllloxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxdddxkkdc;;,,,,,,;:::;;;;;,,,;;;:::clccldxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkOkxdlcccccccc::;;;;;,,,;;;;::::::codxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkOOkkxxxxxdolc:;;;;;,,,;;;;:::;;;;codxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxkkkkkxxxxdolc:;;;;;;;;;;;;;;,,,,,;cldxdxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')
    time.sleep(0.05)
    print('xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxdooooolc:;;;;;;;;::::;;,,\'\'\'\',,;:lddodxxxxxxxxxxxxxxxxxxxxxxxxxxxxx\n''\n''\n''')
    #sonny
    sleep(1)
    print('조선의 축구왕 손흥민! 적당한 숫자를 입력하여 골대에 불꽃슛을 넣어라!')
    print(
        '그의 슛강도는?:\n\n''##########################################\n''\n''프\n''리\n킥   o                                                                                     [T골대T]')
    print('덤\n''벼\n''\n##########################################')
    try_count = 0

    while True:
        a = int(input("kick!:"))
        print('\n')
        sleep(1)
        sys.stdout.write('보여주마 나의 불꽃슛!\n')
        print("||".rjust(95))
        print("||".rjust(95))
        print("\/".rjust(95))
        sleep(1)
        shoot(a)
        if result(a):
            print()
            print('도전 성공')
            return True
        else:
            try_count += 1
            if try_count == 3:
                print()
                print('도전 실패')
                return False
