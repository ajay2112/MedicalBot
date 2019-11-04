def pregnancy(data):
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://preganency.firebaseio.com/PREGANENCY/')
    my = int(data)
    if (my >= 1) and (my <= 13) :
        result = firebase.get('FIRST TRIMESTER (WEEKS 1 TO 13)',None)
        x = func(result)
        x=('FIRST TRIMESTER:'+'\n'+x)
        return x


    if (my > 13) and (my <= 26) :
        result = firebase.get('SECOND TRIMESTER (WEEKS 13 TO 26)',None)
        y = func(result)
        y=('SECOND TRIMESTER'+'\n'+y)
        return y

    if (my > 26) and (my <= 40) :
        result = firebase.get('THIRD TRIMESTER (WEEKS 27 TO 40)',None)
        z = func(result)
        z=('THIRD TRIMESTER'+'\n'+z)
        return z

def func(result):
    output = ""
    for i in result:
        output += str(i)
        output += "\n" + str(result[i])
        output += "\n\n"
    return  output

