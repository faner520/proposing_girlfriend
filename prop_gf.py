def future_gf():
    intro = input("Hey! : ")
    build_up = input("Wanted to ask something : ")
    print ("I like you a lot!")
    prop = input("Do you like me as well : ")
    Accept = False
    while not Accept:
        if prop == ('yes'):
            print ("YAY, let's go on a date!")
            Accept = True
        else:
            prop = input("Do you like me as well : ")
            print("SAY YES")

future_gf()