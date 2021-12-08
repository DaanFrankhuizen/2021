from time import sleep

# really couldn't wrap my head arround this one, credits to https://github.com/xmbgulmus
def part1():
    counterArray=[0,0,0,0,0,0,0,0,0,0,0,0]
    counter=0

    file = open('Day3Input.txt', 'r')
    line = file.readline()
    while line:
        splitLine = [char for char in line.strip("\n")]
        for (indx,bit) in enumerate(splitLine):
            counterArray[indx]+=int(bit)
        counter+=1
        line = file.readline()
    file.close()

    gamma=""
    delta=""

    for i in range(12):
        if(counterArray[i] > (counter/2)):
            gamma+="1"
            delta+="0"
        else:
            gamma+="0"
            delta+="1"

    
    print(int(gamma,2)* int(delta,2))

if __name__ == "__main__":
    part1()