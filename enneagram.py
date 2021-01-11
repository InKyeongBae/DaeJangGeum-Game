#애니그램
import random
import time


def enneagram():
    print('='*50)
    print('우리말 겨루기')
    time.sleep(1)
    print('뒤섞인 단어를 옳게 배열하여라.')
    time.sleep(1)
    print('문장의 경우 띄어쓰기도 확실하게 입력하여라.')
    time.sleep(1)
    print('제한시간은 5초다.')
    time.sleep(1)
    print('='*50)
    words = ['노트북 충전기', '아이패드', '내가 조선의 국모다', '을지문덕', '피로그래밍']
    random.shuffle(words)
    count = 0

    for word in words:
        characters = list(word)
        random.shuffle(characters)
        shuffled_word = ''.join(characters)

        start = time.time()
        guess = input('[{}] 이건 원래 무엇이겠느냐: '.format(shuffled_word))

        if guess == word and time.time()-start <= 5:
            time.sleep(1)
            print('정답')
            count += 1
        elif time.time()-start > 5 and guess != word:
            time.sleep(1)
            print('느리면 답이라도 맞추거라')
        elif time.time()-start > 5:
            time.sleep(1)
            print('늦는구나')
        else:
            time.sleep(1)
            print('뭬야?')

        print()
        print()
    print('='*50)
    if count >= 4:
        time.sleep(1)
        print('잘했다. 재료를 건네주마')
        print('')
        time.sleep(1)
        print('  ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗    ██╗██╗███╗   ██╗  ██╗')
        print('  ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║    ██║██║████╗  ██║  ██║')
        print('   ╚████╔╝ ██║   ██║██║   ██║    ██║ █╗ ██║██║██╔██╗ ██║  ██║')
        print('    ╚██╔╝  ██║   ██║██║   ██║    ██║███╗██║██║██║╚██╗██║  ╚═╝')
        print('     ██║   ╚██████╔╝╚██████╔╝    ╚███╔███╔╝██║██║ ╚████║  ██╗')
        print('     ╚═╝    ╚═════╝  ╚═════╝      ╚══╝╚══╝ ╚═╝╚═╝  ╚═══╝  ╚═╝')
        return True
    else:
        time.sleep(1)
        print('자격이 안되는구나')
        time.sleep(1)
        print('돌아가거라')
        time.sleep(1)
        print('')
        print('  ██╗   ██╗ ██████╗ ██╗   ██╗    ██╗      ██████╗ ███████╗███████╗    ██╗')
        print('  ╚██╗ ██╔╝██╔═══██╗██║   ██║    ██║     ██╔═══██╗██╔════╝██╔════╝    ██║')
        print('   ╚████╔╝ ██║   ██║██║   ██║    ██║     ██║   ██║███████╗█████╗      ██║')
        print('    ╚██╔╝  ██║   ██║██║   ██║    ██║     ██║   ██║╚════██║██╔══╝      ╚═╝')
        print('     ██║   ╚██████╔╝╚██████╔╝    ███████╗╚██████╔╝███████║███████╗    ██╗')
        print('     ╚═╝    ╚═════╝  ╚═════╝     ╚══════╝ ╚═════╝ ╚══════╝╚══════╝    ╚═╝')

        return False
