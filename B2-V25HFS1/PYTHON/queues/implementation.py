def que():
    q=[]
    while True:
        print("1.enqueue 2.dequeue 3.dis 4.exit")
        ch=int(input())
        match ch:
            case 1:
                q.append(int(input()))
            case 2:
                if len(q)==0:
                    print("queue is empty")
                else:
                    print(q.pop())
            case 3:
                if len(q)==0:
                    print("queue is empty")
                else:
                    print(*q)
            case _:
                break
que()