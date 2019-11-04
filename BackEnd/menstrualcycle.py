

def func(result):
    output = ""
    for i in result:
        output += str(i)
        output += "\n" + str(result[i])
        output += "\n\n"
    return  output

def menstrualcycle():
    from firebase import firebase
    firebase = firebase.FirebaseApplication('https://menstrual-cycle-9e1af.firebaseio.com/MENSTRUALCYCLE/')
    result = firebase.get('PHASES','PHASE1',)
    x = func(result)
    output=""
    output+=('PHASE1'+'\n'+x)

    result = firebase.get('PHASES','PHASE2',)
    y = func(result)    
    output+=('PHASE2'+'\n'+y)

    result = firebase.get('PHASES','PHASE3',)
    z = func(result)
    output+=('PHASE3'+'\n'+z)
    return output
