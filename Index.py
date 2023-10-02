# import string
fhand = open('Item.txt')
out = open('ItemIndex.txt', 'w')

for line in fhand:
    if len(line) == 0 or line.startswith('//') or line.startswith('e'): continue    
    elif len(line) <= 3: 
        line = line.rstrip()
        if len(line) == 0: continue
        cat = int(line)
        out.write(str(cat) + '\n')
        
    elif len(line) > 3:
        if len(line) == 0: continue
        line = line.rstrip()
        x = line.find('"')
        y = line.find('"', 80)
        words = line.split()
        print(words[0])
        id = words[0]
        if id.startswith('e') or len(words) == 0: continue
        intid = int(id)
        index = (cat * 512) + intid
        words = line.split('"')
        name = words[1]
        sindex = str(index) + '\t' + name + '\n'
        
        out.write(sindex)
out.close()
        
       