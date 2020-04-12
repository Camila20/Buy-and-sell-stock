# Best time to buy and sell stocks II
#Find the maximum profit

def buy_sell(A):
    n=len(A)
    profit=0
    for i in range (n-1):   
        d=A[i+1]-A[i]   # Diferencia entre el siguiente y el actual stock
        if d>profit:
            profit=d    # Ganancia mayor
    return profit

print (buy_sell([5,2,10]))
