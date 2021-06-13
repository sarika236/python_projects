while True:
    user_input = str(input("enter the phrase: "))
    text = user_input.split()
    a = " "
    for i in text:
        a = a + str(i[0].upper())
    print(a)