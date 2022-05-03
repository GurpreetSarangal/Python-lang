fo = open("College_Practicle_File_Programs\\text2.txt","r")
lines = fo.readlines()
fo.close()

fo = open("College_Practicle_File_Programs\\text2.txt","w")
lines.reverse()

for line in lines:
    fo.write(line)

fo.close()