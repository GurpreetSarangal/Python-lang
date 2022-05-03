def main():
    file = open('parsing project\\textyesno.txt','r')
    lines = file.readlines()
    file.close
    countYes = 0
    countNo = 0
    for line in lines:
        line = line.strip()
        if(line == 'YES'):
            countYes += 1
    print('count of YES in file is : ',countYes)

main()