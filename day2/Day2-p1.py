# split the given input list into the correct lists
def part1():
    # open the input file
    f = open("Day2Input.txt", "r")
    file_lines = f.readlines()

    # initialize the lists
    day2_list = []
    horpos_list = []
    verpos_up_list = []
    verpos_down_list = []

    # replace the newline
    for l in file_lines:
        day2_list.append(l.replace("\n", ""))

    # iterate over the listitems
    for i in day2_list:
        # check if forward is in the listitem and add the integer to a list
        if "forward" in i:
            horpos = i.split(" ")
            horpos_list.append(int(horpos[1]))
            print("forward " + str(horpos[1]))
        # check if up is in the listitem and add the integer to a list
        elif "up" in i:
            verpos = i.split(" ")
            verpos_up_list.append(int(verpos[1]))
            print("up " + str(verpos[1]))
        # check if down is in the listitem and add the integer to a list
        elif "down" in i:
            verpos = i.split(" ")
            verpos_down_list.append(int(verpos[1]))
            print("down " + str(verpos[1]))

    # add all the items in the lists
    total_horpos = sum(horpos_list)
    total_verpos = sum(verpos_down_list) - sum(verpos_up_list)

    total_sum = total_horpos * total_verpos

    print(total_sum) 

if __name__ == "__main__":
    part1()