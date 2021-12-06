def increase_check():
    f = open('./Day1Input.txt', 'r')
    file_lines = f.readlines()

    day1_list = []
    
    for l in file_lines:
        day1_list.append(l.replace("\n", ""))

    for i in range(0, len(day1_list)):
        day1_list[i] = int(day1_list[i])



    prev_sum = sum(day1_list[:3])
    num_increases = 0

    # Start from the fourth element
    for i in range(3, len(day1_list)):
        # Sum the numbers from i-2 to i
        new_sum = sum(day1_list[i-2:i+1])
        if new_sum > prev_sum:
            num_increases += 1
        prev_sum = new_sum

    print(num_increases)

    

if __name__ == "__main__":
    increase_check()