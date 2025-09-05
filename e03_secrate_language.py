import string

salt = ["##ttrr", "678$%09", 56]


def encoder(text):
    sl = f"${salt[0]}"
    for i in range(len(text)):
        sl += text[i] + f"{i+salt[2]}"
    return sl + salt[1]


def decoder(text):
    text = text[len(salt[0]) + 1 : -len(salt[1])]
    dsl = text
    for i in range(len(dsl)):
        dsl = dsl.replace(f"{salt[2]+i}", "")
    return dsl


# msg = "Zahid"


# secrate_msg = encoder(msg)
# print(secrate_msg)
# decode_language = decoder(secrate_msg)
# print(decode_language)


def messager():
    try:
        type = int(input("For Encode ( Press 1 ) For Decode ( Press 2 ) : "))
        if type == 1:
            msg = input("Enter your Message : ")
            print(encoder(msg))
        elif type == 2:
            msg = input("Enter your Message : ")
            print(decoder(msg))
        else:
            raise ("Unexpected input are you dumb ?")
    except Exception as e:
        print("Error : " + e)
    finally:
        msg = ""
        isAgain = input("Do you want use this again ? \n y for yes")
        if isAgain == "y":
            messager()
        else:
            return 1

messager()