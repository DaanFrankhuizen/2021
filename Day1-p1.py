from time import sleep

def increased_checker():
    f = open('Day1Input.txt', 'r')
    file_lines =f.readlines()

    day1_list = []

    increased_total = 0

    for l in file_lines:
        day1_list.append(l.replace("\n", ""))

    for i in range(0, len(day1_list)):
        day1_list[i] = int(day1_list[i])
    
    print(day1_list)

    for i in range(0, len(day1_list)-1):
        if day1_list[i] < day1_list[i+1]:
            increased_total += 1
            print(str(day1_list[i]) +  " depth increased")
            print(increased_total)
        elif day1_list[i] > day1_list[i+1]:
            print(str(day1_list[i]) +  " depth decreased")


if __name__ == "__main__":
    increased_checker()
