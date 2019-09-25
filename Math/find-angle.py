import math
ab= int(input())
bc = int(input())
ac = (ab**2+bc**2)**0.5
metadeac= ac / 2
bm = ((abs(bc**2-metadeac**2))**0.5)
#print(metadeac)
#print(bm)
angulo = (math.atan2(ab,bc))
#print(angulo)
print("%d°" %(round(math.degrees(angulo))))

