#sochhie says: need to combinations.txt too
parent1 = "1" #what pal you already have with good passive skills
parent2 = "2" #another pal you already have with good p skills, makes things a lil less accurate
original = "3" #what Pal you want to transfer passive skills to
origin = original
originadd = "="+origin+"'"
position1 = 0
position2 = 0

nottheseones = ["Chikipi","Paladius","Necromus","Frostallion","Jetragon","Selyne","Bellanoir","Bellanoir Libero","Xenovader"]
thefile = open("combinations.txt").read()

recycle = 2
oparent1 = "p1"
oparent2 = "p2"

notthis = "a"
paldict = {} #pal-cycle link
completed = [] #for list of childs
trail = []
badcombos = []

if origin not in nottheseones:
    while oparent1 != parent1 and oparent1 != parent2 and oparent2 != parent1 and oparent2 != parent2:
        while notthis != ']':
            position1 = thefile.find(originadd, position2)
            position2 = (thefile.rfind("'", 0, position1))
            parents = thefile[position2+1:position1]
            trail.append(parents)
            if parents in badcombos: parents = prevparents
            oparent1, oparent2 = parents.split('+')
            if oparent1 in nottheseones and oparent2 in nottheseones or oparent1 == oparent2:
                prevparents = trail.pop()
                if oparent1 != oparent2:
                    oparent2, oparent1 = prevparents.split('+')
                else:
                    while oparent1 == oparent2:
                        prevparents = trail.pop()
                        oparent2, oparent1 = prevparents.split('+')
                if parents not in badcombos: badcombos.append(parents)
            #print(oparent1, oparent2, origin)
            if oparent1 not in paldict:paldict[oparent1] = recycle
            elif oparent2 not in paldict: paldict[oparent2] = recycle
            if oparent1 == parent1 or oparent1 == parent2:
                isfinish = oparent1
                break
            elif oparent2 == parent1 or oparent2 == parent2:
                isfinish = oparent2
                break
            else:
                notthis = thefile[position1+len(origin)+2]
                position2=position1+1


        position1 = 0
        position2 = 0
        testagainst = origin
        completed.append(origin)
        while origin == testagainst:
            if origin in paldict:
                recycle = paldict.get(origin)
            position1 = thefile.find(originadd, position2)
            position2 = (thefile.rfind("'", 0, position1))
            if oparent1 != testagainst and oparent1 not in completed and oparent1 not in nottheseones:
                origin = oparent1
                originadd = "=" + origin + "'"
                print(oparent1, oparent2)
            elif oparent2 != testagainst and oparent2 not in completed and oparent1 not in nottheseones:
                origin = oparent2
                originadd = "=" + origin + "'"
            else:
                position1 = thefile.find(originadd, position2)
                position2 = (thefile.rfind("'", 0, position1))
                parents = thefile[position2+1:position1]
                oparent1, oparent2 = parents.split('+')
        notthis = "a"
        position1 = 0
        position2 = 0
        recycle+=1

    print(isfinish + " is "+str(recycle)+" steps away from "+original)
else: print("NO")
