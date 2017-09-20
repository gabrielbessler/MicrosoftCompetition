in_text = input()
num_slots = ""
index = 0
for i in in_text:
    index += 1
    if i == ":":
        break
    num_slots += i
num_slots = int(num_slots)
remove_empty = bool(in_text[index:])

f = open('input.txt', 'r')
lines = f.readlines()
print(len(lines))
current_nesting = 0
current_list = -1
total_data = []
count_output_nodes = 0
initial_nodes = 0
count_output_slots = 0
count_input_slots = 0

L = []
for line in lines:
    line = line.strip()
    if line == "":
        count_input_slots += 1
        if remove_empty:
            L.append('')
    else:
        if line[0] == "[":
            current_nesting += 1
        elif line[0] == "]":
            if current_nesting == 2:
                total_data.append(L)
                L = []
                initial_nodes += 1
            current_nesting -= 1
        else:
            L.append(line)

output_string = "[\n[\n"
count = 0
for i in total_data:
    for j in i:
        count += 1
        if count <= num_slots:
            if i == "":
                count_output_slots += 1
            output_string += j + "\n"
        else:
            count = 0
            output_string += "]\n[\n" + j + "\n"
            count_output_nodes += 1
            count += 1

while count < num_slots + 2:
    count += 1
    output_string += "" + "\n"
    count_output_slots += 1

count_output_slots -= 2
output_string = output_string[:-2]
output_string += "]\n]"

print(count_output_slots)

output_str = str(count_output_nodes+1) + "\n" + str(count_output_nodes - initial_nodes +1) + "\n" + str(count_output_slots) + "\n" + str(count_output_slots + count_input_slots) + "\n" + str(output_string) + "\n"


f = open("output.txt", "w")
f.write(output_str)
f.close()
