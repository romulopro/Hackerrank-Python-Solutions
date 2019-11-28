from datetime import datetime
for x in range(0, int(input())):
    t1=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    t2=datetime.strptime(input(),'%a %d %b %Y %H:%M:%S %z')
    print (int(abs((t2-t1).total_seconds())))
