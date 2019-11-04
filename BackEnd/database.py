def database(my_input):
    from firebase import firebase

    # converting  to upper case
    my_input = my_input.upper()
    # storing the first letter
    first_letter = my_input[0]
    fireurl = ('https://nemo-bot-9ae9c.firebaseio.com/%s/' % first_letter.upper())
    firebase = firebase.FirebaseApplication(fireurl)
    result = firebase.get(my_input, '')
    output=""
    for i in result:
        output+=str(i)
        output+="\n --"+str(result[i])
        output+="\n\n"
    return output
