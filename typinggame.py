import random
import time


def typing_game():
    words = ['장금이', '조선시대', '경복궁', "중전마마", "투호", "윷놀이", "대장금", "기미상궁"]

    random.shuffle(words)
    start_time = time.time()
    minus = 0
    time.sleep(1)
    print('='*50)
    print('다음 게임은 타자 연습이다.')
    time.sleep(1)
    print('제시된 단어를 똑같이 타이핑하거라. 테스트는 총 5번 진행된다.')
    time.sleep(1)
    print('오타 발생 시 점수가 깎이니 빠르고 정확하게 입력해야한다.')
    time.sleep(1)
    print('그럼 시작!')
    time.sleep(1)
    print('='*50)
    for word in range(5):
        while True:
            user_input = input("%s: " % words[word])
            if (user_input == words[word]):
                break
            else:
                minus += 10
                break

    end_time = time.time()
    time.sleep(2)
    print('='*50)
    print("걸린 시간: %2f초" % (end_time - start_time))
    print("감점: %d" % minus)
    score = (100/(end_time - start_time))-minus
    print("획득 점수: %d" % (score))
    time.sleep(2)
    if score > 10:
        print('='*50)
        print('잘했다. 재료를 건네주마')
        return True
    else:
        print('='*50)
        print('그 실력으로 내 김치를 가져갈 생각을 하다니')
        time.sleep(1)
        return False
