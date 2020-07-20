from SafeInput import InpList
def encode(message,pw):
    return "".join([chr(ord(char)+ord(pw[i%len(pw)])) for i,char in enumerate(message)])
def decode(message,pw):
    return "".join([chr(ord(char)-ord(pw[i%len(pw)])) for i,char in enumerate(message)])


#ÚÛÐÛÓ×ÈåÍÌ
while True:
    if InpList("(D)ecode or (E)ncode: ",["D","E"]) == "E":
        print("Enter your message and press ^C or ^Z to submit:\n")
        contents = []
        while True:
            try:
                line = input("=>")+"\n"
            except KeyboardInterrupt:
                break
            contents.append(line)
        print(encode("".join(contents),input("\nenter password : ")))
    else:
        print(decode(input("enter message : "),input("enter password : ")))

#ïÜáÞÛÛÍÙÖÊÈ¦ÍÌ
