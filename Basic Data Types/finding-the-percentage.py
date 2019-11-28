if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    media = 0 
    #print(student_marks[query_name][0])
    for x in range (0,len(student_marks[query_name])):
      media = media + float(student_marks[query_name][x])
    print("%.2f" %(media/3))
    
