with open('mary.txt', 'w') as outfile:
    string = 'Mary had a little lamb,'
    for each in range(4):
        outfile.write(str(string) + '\n')

with open('mary.txt', 'r') as outfile:
    for line in outfile:
        print(line.strip())

