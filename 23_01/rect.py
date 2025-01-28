def get_input():
    lenn=int(input("enter length: "))
    widd=int(input("enter width: "))
    return(lenn, widd)

def calc_area(x,y):
    area=x*y
    return area

def disp(arr):
    print(f"area of rectangle: {arr}")

(length,width)=get_input()
arr=calc_area(length,width)
disp(arr)