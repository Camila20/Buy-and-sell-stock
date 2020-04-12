# Best Time to Buy and Sell Stocks IV

def buy_sell(A):
    n=len(A)
    ind=0
    profit=[]
    for i in range (n-1):
        for j in range (i,n-1): #Diferecnia entre cada elemento i en diferencia de j
            d=A[j+1]-A[i]
            if d>ind: # Si la ganacia es positiva
                profit.append(d) # Agregarlo a la lista profit
    return max(profit) # Devolver el mayor elemento de la lista profit (máximo beneficio)

print (buy_sell([1,2]))
print (buy_sell([1,4,5,2,4]))
