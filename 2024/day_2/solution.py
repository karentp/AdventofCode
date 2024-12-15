import pandas as pd

def read_input(filename="input.txt"):
    with open(filename, 'r') as file:
        rows = [list(map(int, line.split())) for line in file]
    data = pd.DataFrame({'Reports': rows})
    return data

def solve_part1():
    df = read_input()
    df['Condition1']=df['Reports'].apply(check_condition_1)
    df['Condition1and2'] = (df['Condition1'] & df['Reports'].apply(check_condition_2))
    df_condition1and2 = df[df['Condition1and2']==True]
    print("Part 1 result:" ,df_condition1and2.shape[0])
    return df

def check_condition_1(report):
    return all(report[i] <= report[i + 1] for i in range(len(report) - 1)) or \
           all(report[i] >= report[i + 1] for i in range(len(report) - 1))
  
def check_condition_2(report):
    return all(1 <= abs(i-j) <=3 for i,j in zip(report, report[1:]))

def check_if_safe(report):
    return check_condition_1(report) and check_condition_2(report)

def check_problemdampener(report):
    for i in range(len(report)):
        modified_report = report[:i] + report[i + 1:]
        if check_condition_1(modified_report) and check_condition_2(modified_report):
            return True 
    return False


def solve_part2(df):
    df['ProblemDampener'] = df['Reports'].apply(check_problemdampener)
    print("Part 2 result:" , df[df['ProblemDampener']].shape[0])
    
 
def main():
    df = solve_part1()
    solve_part2(df)

if __name__ == "__main__":
    main()