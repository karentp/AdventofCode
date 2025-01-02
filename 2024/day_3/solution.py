import re

def read_input(filename="input.txt"):
    with open(filename, 'r') as file:
        input_text = file.read()
        return input_text

def solve_part1(input_text = read_input()):
    pattern = r'mul\(\d+\,\d+\)'
    filtered_text = ';'.join(re.findall(pattern, input_text))
    valid_ops = ','.join(re.findall(r'\d+', filtered_text))
    nums_for_op = [int(s) for s in valid_ops.split(',')]
    products = [nums_for_op[i] * nums_for_op[i+1] for i in range(0, len(nums_for_op)-1, 2)]

    print("Part 1 result: ", sum(products) )
   
def filter_text_new_rules(text_to_use, pending_text):
    pending_text = pending_text.split("don't()", 1)
    text_to_use.append(pending_text[0]) 
    if len(pending_text) > 1 and pending_text[1]: 
        pending_text = pending_text[1].split("do()", 1) 
        if len(pending_text) > 1:
            filter_text_new_rules(text_to_use, pending_text[1])
        else:
            text_to_use.append(pending_text[0])
    return text_to_use

def solve_part2():
    input_text= read_input()
    text_to_use = ','.join(filter_text_new_rules([],input_text))
    solve_part1(input_text=text_to_use)

def main():
    solve_part1()
    solve_part2()

if __name__ == "__main__":
    main()