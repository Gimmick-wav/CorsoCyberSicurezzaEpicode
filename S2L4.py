import math
lq, l1r, l2r, lt, ht, b1, b2, htrpz, r, lob = None, None, None, None, None, None, None, None, None, None
while True:
    forma= input("Ciao, scegli una forma geometrica:\n (quadrato), (rettangolo), (triangolo), (trapezio), (cerchio): ") 
    if forma.lower() == "quadrato":
        print("Hai scelto: Quadrato")
        lq=input("Dammi il lato del quadrato: ")
        lq=float(lq)
        break
    elif forma.lower()=="rettangolo":
        print("Hai scelto: Rettangolo")
        l1r=input("Dammi il primo lato del rettangolo: ")
        l1r=float(l1r)
        l2r=input("Dammi il secondo lato del rettangolo: ")
        l2r=float(l2r)
        break
    elif forma.lower()=="triangolo":
        print("Hai scelto: Triangolo")
        lt=input("Dammi il lato del triangolo: ")
        lt=float(lt)
        ht=input("Dammi l'altezza del triangolo: ")
        ht=float(ht)
        break
    elif forma.lower()=="trapezio":
        print("Hai scelto: Trapezio")
        b1=input("Dammi la prima base del Trapezio: ")
        b1=float(b1)
        b2=input("Dammi la seconda base del Trapezio: ")
        b2=float(b2)
        htrpz=input("Dammi l'altezza del Trapezio: ")
        htrpz=float(htrpz)
        lob=float(input("Dammi il lato obliquo: "))
        break
    elif forma.lower()=="cerchio":
        print("Hai scelto: Cerchio")
        r=input("Dammi il raggio del cerchio: ")
        r=float(r)
        break
    else:
        print("\nSei pregato di selezionare una delle forme offerte, scrivendo il nome per intero e senza spazi:)\n")
while True:
    opt=input("Vuoi calcolare l'area o il perimetro?\n A/P: ")
    if opt.lower()=="a":
        print(
            f"L'Area è: {lq*lq if lq is not None else ""}"
            f"{l1r*l2r if l1r is not None and l2r is not None else ""}"
            f"{(lt * ht)/2 if lt is not None and ht is not None else ""}"
            f"{((b1+b2)*htrpz)/2 if b1 is not None and b2 is not None and htrpz is not None else ""}"
            f"{math.pi*r*r if r is not None else ""}"
            )
        break
    elif opt.lower()=="p":
        print(
            f"Il perimetro è {lq*4 if lq is not None else ""}"
            f"{(l1r+l2r)*2 if l1r is not None and l2r is not None else ""}"
            f"{3*lt if lt is not None else ""}"
            f"{(2*lob)+b1+b2 if lob is not None and b1 is not None and b2 is not None else ""}"
            f"{2*math.pi*r if r is not None else""}"
        )  
        break
    else:
        print("Selezione non valida")
        

    