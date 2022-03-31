fo = open("College_Practicle_File_Programs\\text2.txt","w")

fo.write("Happiness is not absence of problems; \n")
fo.write("It's the ability to deal with them.\n")

lines = ["When life gives you lemons make lemonade.\n",
        "Life is a race, If you don't run fast...\n",
        "You will be like a broken Undaa"
        ]
fo.writelines(lines)
fo.close()