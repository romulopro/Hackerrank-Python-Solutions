from collections import namedtuple
numAlunos = int(input())
campos = input().split()
somaMedias = 0 
for x in range(0,numAlunos):
        students = namedtuple('student',campos)
        coluna1, coluna2, coluna3, coluna4 = input().split()
        student = students(coluna1, coluna2, coluna3, coluna4)
        somaMedias += int(student.MARKS)
print("%.2f" %(somaMedias/numAlunos))
