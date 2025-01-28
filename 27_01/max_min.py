def get_input():
    num=int(input("enter the range: "))
    numbers=[int(input(f"enter the value for {i+1}: ")) for i in range(num)]
    return num,numbers
    
def display(num,numbers):
    print(f"maximum number: {numbers[0]}")
    print(f"minimum number: {numbers[num-1]}")

num,numbers=get_input()
numbers.sort(reverse=True)
display(num,numbers)