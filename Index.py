import string

fhand = open('Item.txt')
for line in fhand:
    if len(line) < 4 and line[0] != 'e': #or line.startswith('//'): continue
        line = line.rstrip()
        cat = int(line)
        print(cat)
    elif line.startswith('//') or line[0] == 'e': continue
    x = line.find('"')
    y = line.find('"', 80)
    name = line[x+1:y]
    print(name)
    # line = line.translate(str.maketrans('', '', string.punctuation))
    # words = line.split()
    # for word in words:
    #     t = word.find('"')
    #     print(t)
    # if len(words[8]) == 1:
    #     n1 = words[8]
    # if len(words[9]) == 1:
    #     n2 = words[9]
    # if len(words[10]) == 1:
    #     n3 = words[10]
    # if len(words[11]) == 1:
    #     n4 = words[11]
    # if len(words[12]) == 1:
    #     n5 = words[12]
    # if len(words[13]) == 1:
    #     n6 = words[13]
    # name = n1 + n2 + n3 + n4 + n5 + n6
    # id = int(words[0])
    # index = (cat * 512) + id
    # print(index, name)
        