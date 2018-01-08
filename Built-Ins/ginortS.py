from operator import itemgetter, attrgetter
print(*sorted(input(), key=lambda char: (char.isdigit() - char.islower(), char in '02468', char)), sep='')