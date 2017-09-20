num_lines = int(input())

attr_1 = ['1','2','3']
attr_2 = ['E', 'F', 'S']
attr_3 = ['R', 'P', 'G']
attr_4 = ['O', 'D', 'S']
attrs = [attr_1, attr_2, attr_3, attr_4]

output_str = ""
for i in range(num_lines):
    cards = input()
    card1 = cards[:4]
    card2 = cards[5:]

    output_card = ""
    for index, letter in enumerate(card1):
        index = int(index)
        current_attribute = attrs[index]
        letter2 = card2[index]
        if letter == letter2:
            output_card += letter
        else:
            if letter != current_attribute[0] and letter2 != current_attribute[0]:
                output_card += current_attribute[0]
            elif letter != current_attribute[1] and letter2 != current_attribute[1]:
                output_card += current_attribute[1]
            else:
                output_card += current_attribute[2]

    output_str += 'Group ' + str(i+1) + ": " + output_card + "\n"
f = open("output.txt", "w")
f.write(output_str)
f.close()