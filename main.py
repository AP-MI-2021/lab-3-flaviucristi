def numarprim(x):
    """
    Determina daca un numar este prim
    :param x: numer intreg
    :return: daca numarul este prim sau nu
    """
    if x<2:
        return False
    else:
        for i in range(2,x//2+1):
            if x%i==0:
                return False

    return True

def sumnr(list):
    """
    Determina suma numerelor
    :param list: numere intregi
    :return: suma numerelor
    """
    s=0
    for i in list:
        s=s+int(i)
    return s

def get_longest_sum_is_prime(list):
    """
    Determina cea mai lunga secventa in care suma numerelor este numar prim
    :param list: numere intregi
    :return:secventa maxima in care suma numerelor este numar prim
    """
    subsec=[]
    for i in range(len(list)):
        for j in range(i,len(list)):
            if numarprim(sumnr(list[i:j+1]))==True and len(list[i:j+1])>len(subsec):
                subsec=list[i:j+1]

    return subsec



def nrcifre(n):
    """
    Determina numarul de cifre
    :param n: numar intreg
    :return: numarul de cifre
    """
    c=int(n)

    t=0
    while c>0:
        t=t+1
        c=c//10
    return t

def numarcifredesc(list):
    """
    Determina daca numarul de cifre ale numerelor se afla in ordine descrescatoare
    :param list: numere intregi
    :return: daca numarul de cifre ale numerelor se afla in ordine descrescatoare
    """
    for i in range(len(list)-1):
        if nrcifre(list[i])< nrcifre(list[i+1]):
            return False
    return True

def get_longest_digit_count_desc(list):
    """
    Determina cea mai lunga secventa in care numarul de cifre este in ordine descrescatoare
    :param list: numere intregi
    :return:secventa maxima in care nuarul de cifre este in ordine descrescatoare
    """
    secmax=[]
    for i in range(len(list)):
        for j in range(i,len(list)):
            if numarcifredesc(list[i:j+1])==True and len(list[i:j+1])>len(secmax):
                secmax=list[i:j+1]

    return secmax



def test_get_longest_sum_is_prime():
    assert (get_longest_sum_is_prime(["4","2","1","3"])==["4","2","1"])
    assert (get_longest_sum_is_prime(["1","2"])==["1","2"])
    assert (get_longest_sum_is_prime(["1","2","3","4","5","6"])==["1","2"])

def test_get_longest_digit_count_desc():
    assert (get_longest_digit_count_desc(["1234","123","1","1234"])==["1234","123","1"])
    assert (get_longest_digit_count_desc(["1234","12"])==["1234","12"])
    assert (get_longest_digit_count_desc(["1234","1","123","12","1","123412"])==["123","12","1"])


def citire():
    list = []
    n = int(input("Dati nr. de elemente: "))
    for i in range(n):
        list.append(int(input("Dati elemente: ")))

    return list



def main():
    while True:

        print(test_get_longest_sum_is_prime())
        print(test_get_longest_digit_count_desc())


        print("1.Cititi numerele: ")
        print("x.Iesire")


        optiune = input("Dati optiune: ")
        if optiune=="1":
            list = []
            list=citire()

            print("1.Determinati cea mai lunga secventa in care suma numerelor este numar prim.")
            print("2.Determinati cea mai lunga secventa in care numarul de cifre este in ordine descrescatoare.")

            optiune2=input("Dati optiune: ")
            if optiune2=="1":
                print(get_longest_sum_is_prime(list))
            elif optiune2=="2":
                print(get_longest_digit_count_desc(list))

        elif optiune=="x":
            break
        else:
            print("Optiune gresita! Rincearca")



if __name__ == '__main__':
    main()


