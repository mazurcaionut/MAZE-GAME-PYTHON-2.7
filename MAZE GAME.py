from Tkinter import *
import tkMessageBox

f=Tk()
f.title("Labirint")
f.geometry("600x600")

cadru=Frame(f,bg="white")
cadru.grid()

plansa=Canvas(f,width=400,height=810,bg="white")
plansa.grid()

'''plansa1=Canvas(f,width=400,height=800,bg="white")
plansa1.grid()
'''

                

def desen():

        plansa.create_line(0,1,400,1,tag="1",fill="black",width=3)
        plansa.create_line(1,0,1,275,tag="1",fill="black",width=3)
        plansa.create_line(1,302,1,398,tag="1",fill="black",width=3)
        plansa.create_line(1,398,398,398,tag="1",fill="black",width=3)
        plansa.create_line(398,1,398,398,tag="1",fill="black",width=3)
        plansa.create_rectangle(301, 2,301 , 2,tag="1",fill="black",width=3)
        plansa.create_rectangle(2, 272,30 , 272,tag="1",fill="black",width=3)
        plansa.create_rectangle(33, 350,31 , 273,tag="1",fill="black",width=3)
        plansa.create_rectangle(2, 376,59 , 376,tag="1",fill="black",width=3)
        plansa.create_rectangle(59, 376,61 , 318,tag="1",fill="black",width=3)
        plansa.create_rectangle(33, 295,82 , 293,tag="1",fill="black",width=3)
        plansa.create_rectangle(81, 272, 83 , 317,tag="1",fill="black",width=3)
        plansa.create_rectangle(84, 344,84 , 396,tag="1",fill="black",width=3)
        plansa.create_rectangle(134, 272 ,81 , 270,tag="1",fill="black",width=3)
        plansa.create_rectangle(135, 271 ,136 , 315,tag="1",fill="black",width=3)
        plansa.create_rectangle(83, 318,108 , 318,tag="1",fill="black",width=3)
        plansa.create_rectangle(108, 318,108 , 298,tag="1",fill="black",width=3)
        plansa.create_rectangle(137, 395,137,369,tag="1",fill="black",width=3)
        plansa.create_rectangle(137,369,111,369,tag="1",fill="black",width=3)
        plansa.create_rectangle(87,345,160,345,tag="1",fill="black",width=3)
        plansa.create_rectangle(162,346,161,370,tag="1",fill="black",width=3)
        plansa.create_rectangle(163,368,188,368,tag="1",fill="black",width=3)
        plansa.create_rectangle(162,344,160,314,tag="1",fill="black",width=3)
        plansa.create_rectangle(161,314,187,315,tag="1",fill="black",width=3)
        plansa.create_rectangle(188,314,190,339,tag="1",fill="black",width=3)
        plansa.create_rectangle(187,338,211,338,tag="1",fill="black",width=3)
        plansa.create_rectangle(211,338,213,395,tag="1",fill="black",width=3)
        plansa.create_rectangle(212,368,267,368,tag="1",fill="black",width=3)
        plansa.create_rectangle(239,339,293,339,tag="1",fill="black",width=3)
        plansa.create_rectangle(294,339,295,395,tag="1",fill="black",width=3)
        plansa.create_rectangle(290,340,322,341,tag="1",fill="black",width=3)
        plansa.create_rectangle(322,373,347,373,tag="1",fill="black",width=3)
        plansa.create_rectangle(347,373,348,343,tag="1",fill="black",width=3)
        plansa.create_rectangle(348,343,369,343,tag="1",fill="black",width=3)
        plansa.create_rectangle(370,367,369,396,tag="1",fill="black",width=3)
        plansa.create_rectangle(324,340,318,291,tag="1",fill="black",width=3)
        plansa.create_rectangle(323,314,346,313,tag="1",fill="black",width=3)
        plansa.create_rectangle(372,341,369,290,tag="1",fill="black",width=3)
        plansa.create_rectangle(347,289,395,289,tag="1",fill="black",width=3)
        plansa.create_rectangle(347,288,347,262,tag="1",fill="black",width=3)
        plansa.create_rectangle(347,261,291,260,tag="1",fill="black",width=3)
        plansa.create_rectangle(292,259,293,310,tag="1",fill="black",width=3)
        plansa.create_rectangle(291,285,237,289,tag="1",fill="black",width=3)
        plansa.create_rectangle(268,288,269,309,tag="1",fill="black",width=3)
        plansa.create_rectangle(270,309,214,309,tag="1",fill="black",width=3)
        plansa.create_rectangle(213,310,212,286,tag="1",fill="black",width=3)
        plansa.create_rectangle(189,84,190,321,tag="1",fill="black",width=3)
        plansa.create_rectangle(237,285,235,260,tag="1",fill="black",width=3)
        plansa.create_rectangle(235,259,212,258,tag="1",fill="black",width=3)
        plansa.create_rectangle(232,258,261,258,tag="1",fill="black",width=3)
        plansa.create_rectangle(212,258,212,230,tag="1",fill="black",width=3)
        plansa.create_rectangle(212,230,258,230,tag="1",fill="black",width=3)
        plansa.create_rectangle(257,230,257,206,tag="1",fill="black",width=3)
        plansa.create_rectangle(190,201,227,201,tag="1",fill="black",width=3)
        plansa.create_rectangle(209,201,209,175,tag="1",fill="black",width=3)
        plansa.create_rectangle(231,173,278,173,tag="1",fill="black",width=3)
        plansa.create_rectangle(277,172,277,256,tag="1",fill="black",width=3)
        plansa.create_rectangle(294,259,294,196,tag="1",fill="black",width=3)
        plansa.create_rectangle(258,207,258,197,tag="1",fill="black",width=3)
        plansa.create_rectangle(274,172,316,172,tag="1",fill="black",width=3)
        plansa.create_rectangle(318,172,319,234,tag="1",fill="black",width=3)
        plansa.create_rectangle(320,232,366,232,tag="1",fill="black",width=3)
        plansa.create_rectangle(370,203,370,260,tag="1",fill="black",width=3)
        plansa.create_rectangle(370,173,395,173,tag="1",fill="black",width=3)
        plansa.create_rectangle(343,38,343,199,tag="1",fill="black",width=3)
        plansa.create_rectangle(190,149,319,149,tag="1",fill="black",width=3)
        plansa.create_rectangle(320,148,319,171,tag="1",fill="black",width=3)
        plansa.create_rectangle(344,147,368,147,tag="1",fill="black",width=3)
        plansa.create_rectangle(369,148,368,122,tag="1",fill="black",width=3)
        plansa.create_rectangle(344,36,371,38,tag="1",fill="black",width=3)
        plansa.create_rectangle(370,37,370,17,tag="1",fill="black",width=3)
        plansa.create_rectangle(340,2,342,14,tag="1",fill="black",width=3)
        plansa.create_rectangle(341,121,321,122,tag="1",fill="black",width=3)
        plansa.create_rectangle(321,120,319,101,tag="1",fill="black",width=3)
        plansa.create_rectangle(395,102,372,102,tag="1",fill="black",width=3)
        plansa.create_rectangle(372,102,372,79,tag="1",fill="black",width=3)
        plansa.create_rectangle(374,55,396,55,tag="1",fill="black",width=3)
        plansa.create_rectangle(293,148,291,121,tag="1",fill="black",width=3)
        plansa.create_rectangle(318,99,273,97,tag="1",fill="black",width=3)
        plansa.create_rectangle(272,96,272,118,tag="1",fill="black",width=3)
        plansa.create_rectangle(189,81,233,83,tag="1",fill="black",width=3)
        plansa.create_rectangle(213,80,215,114,tag="1",fill="black",width=3)
        plansa.create_rectangle(214,113,232,114,tag="1",fill="black",width=3)
        plansa.create_rectangle(247,102,275,102,tag="1",fill="black",width=3)
        plansa.create_rectangle(272,101,270,81,tag="1",fill="black",width=3)
        plansa.create_rectangle(271,79,317,79,tag="1",fill="black",width=3)
        plansa.create_rectangle(229,80,245,79,tag="1",fill="black",width=3)
        plansa.create_rectangle(342,76,342,76,tag="1",fill="black",width=3)
        plansa.create_rectangle(307,77,306,58,tag="1",fill="black",width=3)
        plansa.create_rectangle(342,59,330,57,tag="1",fill="black",width=3)
        plansa.create_rectangle(325,3,327,57,tag="1",fill="black",width=3)
        plansa.create_rectangle(325,30,309,30,tag="1",fill="black",width=3)
        plansa.create_rectangle(305,57,285,57,tag="1",fill="black",width=3)
        plansa.create_rectangle(284,57,281,17,tag="1",fill="black",width=3)
        plansa.create_rectangle(283,17,303,15,tag="1",fill="black",width=3)
        plansa.create_rectangle(183,1,184,25,tag="1",fill="black",width=3)
        plansa.create_rectangle(183,22,246,21,tag="1",fill="black",width=3)
        plansa.create_rectangle(246,79,246,59,tag="1",fill="black",width=3)
        plansa.create_rectangle(246,59,256,56,tag="1",fill="black",width=3)
        plansa.create_rectangle(284,38,214,39,tag="1",fill="black",width=3)
        plansa.create_rectangle(214,37,214,55,tag="1",fill="black",width=3)
        plansa.create_rectangle(159,286,157,232,tag="1",fill="black",width=3)
        plansa.create_rectangle(159,232,34,234,tag="1",fill="black",width=3)
        plansa.create_rectangle(60,233,59,253,tag="1",fill="black",width=3)
        plansa.create_rectangle(34,230,32,170,tag="1",fill="black",width=3)
        plansa.create_rectangle(33,170,82,170,tag="1",fill="black",width=3)
        plansa.create_rectangle(60,171,60,197,tag="1",fill="black",width=3)
        plansa.create_rectangle(85,232,85,204,tag="1",fill="black",width=3)
        plansa.create_rectangle(84,204,110,204,tag="1",fill="black",width=3)
        plansa.create_rectangle(4,145,51,143,tag="1",fill="black",width=3)
        plansa.create_rectangle(83,170,81,143,tag="1",fill="black",width=3)
        plansa.create_rectangle(82,144,105,144,tag="1",fill="black",width=3)
        plansa.create_rectangle(109,203,107,145,tag="1",fill="black",width=3)
        plansa.create_rectangle(136,234,136,207,tag="1",fill="black",width=3)
        plansa.create_rectangle(138,207,159,206,tag="1",fill="black",width=3)
        plansa.create_rectangle(159,207,159,101,tag="1",fill="black",width=3)
        plansa.create_rectangle(109,170,135,168,tag="1",fill="black",width=3)
        plansa.create_rectangle(135,169,134,39,tag="1",fill="black",width=3)
        plansa.create_rectangle(191,82,135,82,tag="1",fill="black",width=3)
        plansa.create_rectangle(135,38,183,40,tag="1",fill="black",width=3)
        plansa.create_rectangle(158,38,158,21,tag="1",fill="black",width=3)
        plansa.create_rectangle(158,59,215,58,tag="1",fill="black",width=3)
        plansa.create_rectangle(133,112,54,111,tag="1",fill="black",width=3)
        plansa.create_rectangle(25,142,25,111,tag="1",fill="black",width=3)
        plansa.create_rectangle(55,108,55,57,tag="1",fill="black",width=3)
        plansa.create_rectangle(27,81,75,81,tag="1",fill="black",width=3)
        plansa.create_rectangle(56,56,29,56,tag="1",fill="black",width=3)
        plansa.create_rectangle(4,93,20,93,tag="1",fill="black",width=3)
        plansa.create_rectangle(133,3,133,15,tag="1",fill="black",width=3)
        plansa.create_rectangle(86,96,103,96,tag="1",fill="black",width=3)
        plansa.create_rectangle(103,97,104,55,tag="1",fill="black",width=3)
        plansa.create_rectangle(104,55,83,54,tag="1",fill="black",width=3)
        plansa.create_rectangle(83,54,85,18,tag="1",fill="black",width=3)
        plansa.create_rectangle(85,18,105,18,tag="1",fill="black",width=3)
        plansa.create_rectangle(138,40,110,37,tag="1",fill="black",width=3)
        plansa.create_rectangle(29,56,29,32,tag="1",fill="black",width=3)
        plansa.create_rectangle(83,32,59,32,tag="1",fill="black",width=3)
        plansa.create_rectangle(2,18,59,18,tag="1",fill="black",width=3)
        plansa.create_rectangle(60,18,60,33,tag="1",fill="black",width=3)
        plansa.create_rectangle(375,4,395,22,fill="yellow",tag="patrat galben")
        plansa.create_rectangle(373,376,395,394,fill="green",tag="patrat verde")
        plansa.create_rectangle(3,3,22,15,fill="blue",tag="patrat albastru")
        plansa.create_oval(14,285,19,289,fill="blue",tag="nava")
def gata():
        tkMessageBox.showwarning("Ai pierdut!","Ai atins peretii. Jocul s-a terminat.")
        f.destroy()
def coliziune():
        C=plansa.coords("nava")
        L=plansa.find_overlapping(C[0],C[1],C[2],C[3])
        if 1 in L:
                gata()
        if 2 in L:
                gata()
        if 3 in L:
                gata()
        if 4 in L:
                gata()
        if 5 in L:
                gata()
        if 6 in L:
                gata()
        if 7 in L:
                gata()
        if 8 in L:
                gata()
        if 9 in L:
                gata()
        if 10 in L:
                gata()
        if 11 in L:
                gata()
        if 12 in L:
                gata()
        if 13 in L:
                gata()
        if 14 in L:
                gata()
        if 15 in L:
                gata()
        if 16 in L:
                gata()
        if 17 in L:
                gata()
        if 18 in L:
                gata()
        if 19 in L:
                gata()
        if 20 in L:
                gata()
        if 21 in L:
                gata()
        if 22 in L:
                gata()
        if 23 in L:
                gata()
        if 24 in L:
                gata()
        if 25 in L:
                gata()
        if 26 in L:
                gata()
        if 27 in L:
                gata()
        if 28 in L:
                gata()
        if 29 in L:
                gata()
        if 30 in L:
                gata()
        if 31 in L:
                gata()
        if 32 in L:
                gata()
        if 33 in L:
                gata()
        if 34 in L:
                gata()
        if 35 in L:
                gata()
        if 36 in L:
                gata()
        if 37 in L:
                gata()
        if 38 in L:
                gata()
        if 39 in L:
                gata()
        if 40 in L:
                gata()
        if 41 in L:
                gata()
        if 42 in L:
                gata()
        if 43 in L:
                gata()
        if 44 in L:
                gata()
        if 45 in L:
                gata()
        if 46 in L:
                gata()
        if 47 in L:
                gata()
        if 48 in L:
                gata()
        if 49 in L:
                gata()
        if 50 in L:
                gata()
        if 51 in L:
                gata()
        if 52 in L:
                gata()
        if 53 in L:
                gata()
        if 54 in L:
                gata()
        if 55 in L:
                gata()
        if 56 in L:
                gata()
        if 57 in L:
                gata()
        if 58 in L:
                gata()
        if 59 in L:
                gata()
        if 60 in L:
                gata()
        if 61 in L:
                gata()
        if 62 in L:
                gata()
        if 63 in L:
                gata()
        if 64 in L:
                gata()
        if 65 in L:
                gata()
        if 66 in L:
                gata()
        if 67 in L:
                gata()
        if 68 in L:
                gata()
        if 69 in L:
                gata()
        if 70 in L:
                gata()
        if 71 in L:
                gata()
        if 72 in L:
                gata()
        if 73 in L:
                gata()
        if 74 in L:
                gata()
        if 75 in L:
                gata()
        if 76 in L:
                gata()
        if 77 in L:
                gata()
        if 78 in L:
                gata()
        if 79 in L:
                gata()
        if 80 in L:
                gata()
        if 81 in L:
                gata()
        if 82 in L:
                gata()
        if 83 in L:
                gata()
        if 84 in L:
                gata()
        if 85 in L:
                gata()
        if 86 in L:
                gata()
        if 87 in L:
                gata()
        if 88 in L:
                gata()
        if 89 in L:
                gata()
        if 90 in L:
                gata()
        if 91 in L:
                gata()
        if 92 in L:
                gata()
        if 93 in L:
                gata()
        if 94 in L:
                gata()
        if 95 in L:
                gata()
        if 96 in L:
                gata()
        if 97 in L:
                gata()
        if 98 in L:
                gata()
        if 99 in L:
                gata()
        if 100 in L:
                gata()
        if 101 in L:
                gata()
        if 102 in L:
                gata()
        if 103 in L:
                gata()
        if 104 in L:
                gata()
        if 105 in L:
                gata()
        if 106 in L:
                gata()
        if 107 in L:
                gata()
        if 108 in L:
                gata()
        if 109 in L:
                gata()
        if 110 in L:
                gata()
        if 111 in L:
                gata()
        if 112 in L:
                gata()
        if 113 in L:
                gata()
        if 114 in L:
                gata()
        if 115 in L:
                gata()
        if 116 in L:
                gata()
        if 117 in L:
                gata()
        if 118 in L:
                gata()
        if 119 in L:
                gata()
        if 120 in L:
                gata()
        if 121 in L:
                gata()
        if 122 in L:
                gata()
        if 123 in L:
                gata()
        if 124 in L:
                gata()
        if 125 in L:
                gata()
        if 126 in L:
                gata()
        if 127 in L:
                gata()
        if 128 in L:
                gata()
        if 129 in L:
                gata()
        if 130 in L:
                gata()
        if 131 in L:
                gata()
        if 132 in L:
                gata()
        if 133 in L:
                gata()
        if 134 in L:
                gata()
        if 135 in L:
                gata()
        if 136 in L:
                gata()
        if 137 in L:
                gata()
        if 138 in L:
                gata()
        if 142 in L:
                tkMessageBox.showwarning("Mai cauta!", "Nu ai gasit patratul castigator!")
        if 141 in L:
                tkMessageBox.showwarning("Felicitari !", "Ai castigat !")
        if 140 in L:
                tkMessageBox.showwarning("Mai cauta!", "Nu ai gasit patratul castigator!")
                
                
        
def sus():
        plansa.move("nava",0,-2)
        coliziune()
        
def jos():
        plansa.move("nava",0,2)
        coliziune()
def dreapta():
        plansa.move("nava",2,0)
        coliziune()
def stanga():
        plansa.move("nava",-2,0)
        coliziune()
#
def apas(tasta):
        if tasta.keysym == 'Up':
                sus()
                        
        elif tasta.keysym == 'Down':
                jos()
                        
        elif tasta.keysym == 'Left':
                stanga()
                        
        elif tasta.keysym == 'Right':
                dreapta()
                
f.bind('<Key>',apas)
        
reguliLbl=Label(cadru,text="CAPCANA LABIRINTULUI",font=1)
reguliLbl.grid()

reguli1Lbl=Label(cadru,text="INSTRUCTIUNI:",font=1)
reguli1Lbl.grid()

reguli2Lbl=Label(cadru,text="1)NU TRECETI PRIN PERETI.",font=1)
reguli2Lbl.grid()

reguli3Lbl=Label(cadru,text="2)DACA INCALCATI PRIMA REGULA JOCUL SE VA INCHIDE.",font=1)
reguli3Lbl.grid()

reguli4Lbl=Label(cadru,text="3)DOAR UNUL DINTRE CELE 3 PATRATE DIN JOC ESTE CORECT.",font=1)
reguli4Lbl.grid()

buton = Button(cadru,text="INCEPE JOCUL",command=desen)
buton.grid()

f.mainloop()
