
def bonAppetit(bill, k, b):
    # Write your code here
    bill.remove(bill[k])
    b_actual = sum(bill)//2
    if b_actual == b:
        return "Bon Appetit"
    else:
        return b - b_actual


print(bonAppetit([3,10,2,9],1,7))