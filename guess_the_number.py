import random

ans=random.randint(100,999)
max_count=10

print('三桁の数字を一つ選んだよ．ヒントを頼りに',max_count,'回以内に当てよう！')

for i in range(1,max_count+1):
    print(i,'回目、いくつ?')
    num=int(input())

    if num==ans:
        print('正解!!')
        break

    elif i==max_count:
        pass

    elif num > ans:
        print('もっと小さい!')
    else:
        print('もっと大きい!')

else:

    print('正解は',ans,'でした！')
