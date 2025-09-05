class prod:
    def __init__(s,name,des,price,rating):
        s.name=name
        s.des=des
        s.price=price
        s.rating=rating
    def disp(s):
        print(s.name,s.des,s.price,s.rating)
p1=prod("mbl","it works",30000,5)
p2=prod("mouse","it works",3000,5)
p1.disp()
p2.disp()