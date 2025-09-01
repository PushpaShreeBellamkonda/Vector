while True:
    print("1.Add student 2.Display 3.Search 4.Sort 5.Delete 6.Edit 7.Exit")
    ch=int(input())
    match ch:
        case 1:
            f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/std-details.txt","a")
            f.write("\n"+input("enter student data: "))
            f.close()
        case 2:
            f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/std-details.txt","r")
            print(f.read())
            f.close()
        case 3:
            print("1.By ID 2.By name 3.By department 4.By Marks")
            x=int(input())
            match x:
                case 1:
                    sid=input("enter sid: ")
                    f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/std-details.txt","r")
                    l=f.readlines()
                    f.close()
                    for std in l:
                        if std[:3]==sid:
                            print(std)
                            break
                    else:
                        print(-1)
                case 2:
                    name=input("enter name: ")
                    f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/std-details.txt","r")
                    l=f.readlines()
                    f.close()
                    flag=True
                    for std in l:
                        if std.split()[1]==name:
                            print(std)
                            flag=False
                    if flag:
                        print(-1)

                case 3:
                    dept=input("enter department: ")
                    f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/std-details.txt","r")
                    l=f.readlines()
                    f.close()
                    flag=True
                    for std in l:
                        if std.split()[2]==dept:
                            print(std)
                            flag=False
                    if flag:
                        print(-1)
                case 4:
                    marks=input("enter marks: ")
                    f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/std-details.txt","r")
                    l=f.readlines()
                    f.close()
                    flag=True
                    for std in l:
                        if std.split()[3]>=marks:
                            print(std)
                            flag=False
                    if flag:
                        print(-1)
        case 4:
            f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/std-details.txt","r")
            l=f.readlines()
            f.close()
            for i in range(len(l)):
                l[i]=l[i].strip().split()
                l[i][-1]=int(l[i][-1])
            l=sorted(l,key=lambda x:(x[2],x[3]),reverse=True)
            for row in l:
                print(*row)
        case 5:
            f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/std-details.txt","r")
            l=f.readlines()
            f.close()
            f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/std-details.txt","w")
            sid=input("enter sid: ")
            for i in range(len(l)):
                if l[i][:3]==sid:
                    l.pop(i)
                    if i==len(l):
                        l[i-1]=l[i-1].strip()
                    break
            else:
                print(-1)
            f.writelines(l)
            f.close()
        case 6:
            sid=input("enter sid to edit: ")
            f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/std-details.txt","r")
            l=f.readlines()
            f.close()
            for i in range(len(l)):
                if l[i][:3]==sid:
                    data=input("enter updated student record")
                    l[i]=data+"\n"
                    break
            else:
                print(-1)
            l[-1]=l[-1].strip()            
            f=open("/Users/vector/Desktop/Vector/B2-V25HFS1/PYTHON/files/std-details.txt","w")
            f.writelines(l)
            f.close()
        case _:
            break


                    