# Best Time to Buy and Sell Stocks III

def buy_sell(A):
    n=len(A)
    ind=0
    profit=[]
    for i in range (n-1):
        d=A[i+1]-A[i]
        if d>ind:
            profit.append(d)    # Se crea una lista con los beneficios de venta
    n=len(profit)
    for j in range (n-1):
        d=profit[j]+profit[j+1] # Se suma dos elementos consecutivos
        if d>ind:
            ind=d # Se encuentra la mayor suma
    return ind

print (buy_sell([1,2,1,2]))
print (buy_sell([7,2,4,8,7]))
