n = input()

num_boxes = 0
for i in range(n):
    in_text = input()
    r = in_text[0]
    N = in_text[2] #number of sides
    L = in_text[4] #size of base

    diameter = 2*r

    #we're working with a triangular prism
    if N == 3:
        pass
    #we're working with a rectangular prism
    elif N == 4:
        if 13 < L and diameter < L and diameter < 12:
            num_boxes += 1
        elif expression:
            num_boxes += 1