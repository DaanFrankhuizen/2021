def part2():
    # open the input file
    f = open("Day2Input.txt", "r")
    file_lines = f.readlines()

    print("starting")

    day2_list = []

    # replace the newline
    for l in file_lines:
        day2_list.append(l.replace("\n", ""))

    aim = 0
    depth = 0
    horizontal = 0 
    for i in day2_list:
        if "up" in i:
            heading_up = i.split(" ")
            amount_up = int(heading_up[1])
            aim -= amount_up
        elif "down" in i:
            heading_down = i.split(" ")
            amount_down = int(heading_down[1])
            aim += amount_down
        elif "forward" in i:
            heading_forward = i.split(" ")
            amount_forward = int(heading_forward[1])
            depth += (aim * amount_forward)
            horizontal += amount_forward

            print(depth, horizontal)
            print(depth*horizontal)




if __name__ == "__main__":
    part2()