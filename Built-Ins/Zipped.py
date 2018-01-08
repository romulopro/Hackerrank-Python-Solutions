numStudents, numMedias = map(int, input().split())
media = list(map(float , input().split()))
for _ in range(numMedias - 1):
        media = list(map(sum, zip(media , list(map(float , input().split())))))
media = [x/numMedias for x in media]
print(*media, sep="\n")