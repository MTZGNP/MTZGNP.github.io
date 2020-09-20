from math import pi

case=""
while case not in ["a","c","r"]:
    print("a: a=πr^2")
    print("c: c=2πr")
    print("r: r=2π/c")
    case=input("enter func. to use: ")
if case =="a":
    while True:
        try:
            print(pi*(int(input("enter radius: "))^2),"m^2")
            break
        except:
            pass
elif case=="c":
    while True:
        try:
            print(pi*2*int(input("enter radius: ")),"m")
            break
        except:
            pass
elif case=="r":
    while True:
        try:
            print(int(input("enter circumference: "))/(2*pi),"m")
            break
        except:
            pass
    
    
