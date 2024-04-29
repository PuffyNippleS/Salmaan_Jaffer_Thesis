
def checker(pred,eve,):
    if pred >0:
        if eve >0
            return "HA"
    elif

def accuracy(i,j):
    #i = num testeted samples forcasted correctly
    #j =  total test samples
    num = i/j
    formatted_num = "{:.2f}".format(num)
    return formatted_num

    #Threat score
    # Hit alarms  = ha
    #missing alarms  = ma
    #false alarms = fa
def TS(ha,ma,fa):
    num = (ha/(ha+fa+ma))
    formatted_num = "{:.2f}".format(num)
    return formatted_num
def MAR(ma,ha):
    num =(ma/(ma+ha))
    formatted_num = "{:.2f}".format(num)
    return formatted_num
def precision(ha,fa):
    num = (ha/(ha+fa))
    formatted_num = "{:.2f}".format(num)
    return formatted_num
