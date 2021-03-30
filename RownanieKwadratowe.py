import math
def check_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()

def delta(a,b,c):
    #oblicz deltę
    return b**2-(4*a*c)


def Pierwiastki(a,b,delta):
    #oblicza pierwiastki
    tab=[]
    if delta==0:
        x=-b/(2*a)
        tab.append(x)
    else:
        x1=round((-b-math.sqrt(delta))/(2*a),2)
        x2=round((-b+math.sqrt(delta))/(2*a),2)
        tab.append(x1)
        tab.append(x2)
    return tab        

wspA=input('Podajwspółczynnik a:\n')
wspB=input('Podajwspółczynnik b:\n')
wspC=input('Podajwspółczynnik c:\n')


while True:
    if not check_int(wspA) or not check_int(wspB) or not check_int(wspC):
        print('podałeś niewłaściwe współczynniki')
        break
    elif int(wspA) == 0:
        print('to nie jest równanie kwadratowe')    
        break
    else:
        if delta(int(wspA),int(wspB),int(wspC))<0:
            print('brak rozwiązań')
            break
        else:
           rozw = Pierwiastki(int(wspA),int(wspB),delta(int(wspA),int(wspB),int(wspC)))
           print(rozw)
           break


