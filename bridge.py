import sympy as sym  
import matplotlib.pyplot as plt
import numpy as np
import math


class SlabDeck():
    def __init__(self):
        pass 

    def start(self):
       #basic span/effective depth is represented has boe
       #slab deck depth is h
       #uniformly distributed load is Ha
       #knife Edge Load K.E.L is Kel
       #concrete cover is c
        d,l,c,D,h,Ha,Hb,Kel = sym.symbols('d,l,c,D,h,Ha,Hb,Kel')
        c=0.06
        #D is the diameer of reinforcement bars
        D=0.032
        l = float(input("Enter your span/effective depth: "))
        h = float(input("Enter your slab depth: "))
        #Cg is concrete grade
        Cg =24
        Hb =float(input("Enter your Hb Load"))
        Kel = float(input("Enter your Knife Edge Load"))
        #d is effective depth
        d = round(h -c - (D/2),3)
        #Swd is self weight of deck slab
        Swd = round(h * Cg,2)
        #Sd is surfacing depth
        Sd = 0.1
        #Sws is Self weight of surfacing
        Sws = round(Sd * Cg,2)
        #Pdl is permanent dead load
        Pdl = round(1.15 * Swd,2)
        #Sid is super imposed dead load
        Sid = round(1.25 * Sws,2)
        #w is total dead load
        w = Pdl + Sid
        #Nm is Nominal moment
        Nm = round(w*l*l/8)
        #Dm is Design moment
        Dm = round(1.1 * Nm)
        #Cw is Carriage way
        Cw=7.3
        #Nwl is Natural width of lane
        Nwl=Cw/2
        w = 30
        #Nnl is the number of nominal lane
        Nnl = 2
        #Wl is the width of lane 
        Wl =w/Nnl

        Kelm= Kel/Nnl

        RA=180

        RB=180

        M = (Wl*l*l)/8 + (Kelm*l)/4

        Lf = 1.5

        DM = M * Lf

        Udm = 1.1 * DM

        Lf = 1.25

        DM = M * Lf

        Udm = 1.1 * DM
        
        R=[RA,RB]
        cordinate_for_area=[]
        Area=[]
        x=[0,0,l/2,l/2,l,l]
        y=[0,RA,(RA-Wl*l/2),(RA-Wl*l/2-Kelm),(RA-Wl*l/2-Kelm-Wl*l/2),(RA-Wl*l/2-Kelm-Wl*l/2+RB)]
        # plt.plot(x, y) 
        # plt.title('Shear force diagram', size=20) 
        # plt.xlabel('x - axis') 
        # # naming the y axis 
        # plt.ylabel('y - axis') 
        # giving a title to my graph 
        # plt.grid()
        # plt.show()
        def Calc(x):
            return (RA*x-((Wl*x*x/2)))

        def Calc1(x4):
            return (RA*(l/2+x4)-(Wl*l/2*(l/4+x4))-(Wl*x4*x4/2)-Kelm*x4)

        x1= np.linspace(0,l/2,20) 
        x2 =np.linspace(l/2,l,20) 
        x3=np.linspace(0,l/2,20) 
        # plt.title('Bending moment diagram', size=20) 
        # plt.xlabel('x - axis') 
        # naming the y axis 
        # plt.ylabel('y - axis') 
        # giving a title to my graph 
        # plt.plot(x2,Calc1(x3))
        # plt.plot(x1,Calc(x1))
        
        # plt.grid()
        # plt.show()
        
        Hbp =10
        Nl=Hb * Hbp
        Nlp = Nl/4
        #taking moment
        CG=(1.8+7.8+9.6)/4

        D1= l/2 -1.8 -(CG -1.8)/2
        Z = 6
        D2=l-D1-1.8-Z-1.8

        RA=(Nlp*(l-D1)+Nlp*(l-D1-1.8)+Nlp*(1.8+D2)+Nlp*D2)/l
        #finding reaction
        RB=Nlp*4 - RA
        #moment at X
        Mx = RA * 8.5 - Nlp * 1.8
        #Standard lane width
        Slw = 3.65
        #maximum moment
        MaxX = round(Mx/Slw,2)
        #
        DMHB = round(1.1*1.3*Mx,2)
        DMHA = round(1.1*1.5*M,2)
        #design moment 1
        DM1= DMHB+DMHA
        DMHB2 = round(1.1*1.1*Mx,2)
        DMHA2 = round(1.1*1.25*M,2)
        #design moment 2
        DM2 = DMHA2+DMHB2

        if DM2 >= DM1:
            DM = DM2
        else:
            DM =DM1

        x=[0,0,D1,D1,(D1+1.8),(D1+1.8),(D1+7.8),(D1+7.8),(D1+9.6),(D1+9.6),(D1+9.6+D2),(D1+9.6+D2)]
        y=[0,RA,RA,(RA-Nlp),(RA-Nlp),(RA-2*Nlp),(RA-2*Nlp),(RA-3*Nlp),(RA-3*Nlp),(RA-4*Nlp),(RA-4*Nlp),(RA-4*Nlp+RB)]
        plt.plot(x, y) 
        plt.title('Shear force diagram', size=20) 
        plt.xlabel('x - axis') 
        # naming the y axis 
        plt.ylabel('y - axis') 
        plt.grid()
        plt.show()

        def Calc2(x):
            return (RA*x)

        def Calc3(x4):
            return (RA*(D1+x4)-(Nlp*x4))
        
        def Calc4(x4):
            return (RA*(D1+1.8+x4)-(Nlp*(1.8+x4))-(Nlp*x4))
        
        def Calc5(x4):
            return (RA*(D1+7.8+x4)-(Nlp*(7.8+x4))-(Nlp*(6+x4))-(Nlp*x4))

        def Calc6(x4):
            return (RA*(D1+9.6+x4)-(Nlp*(9.6+x4))-(Nlp*(7.8+x4))-(Nlp*(1.8+x4))-(Nlp*x4))

        x1= np.linspace(0,D1,20) 
        x21 = np.linspace(0,1.8,20) 
        x2 =np.linspace(D1,D1+1.8,20) 
        x31 = np.linspace(0,6,20)
        x3=np.linspace(D1+1.8,D1+7.8,20) 
        x41 = np.linspace(0,1.8,20)
        x4= np.linspace(D1+7.8,D1+9.6,20) 
        x51 = np.linspace(0,D2,20)
        x5 =np.linspace(D1+9.6,D1+9.6+D2,20) 
        plt.title('Bending moment diagram', size=20) 
        plt.xlabel('x - axis') 
        #naming the y axis 
        plt.ylabel('y - axis') 
        #giving a title to my graph 

        plt.plot(x1,Calc2(x1))
        plt.plot(x2,Calc3(x21))
        plt.plot(x3,Calc4(x31))
        plt.plot(x4,Calc5(x41))
        plt.plot(x5,Calc6(x51))
      
        
        plt.grid()
        plt.show()


        print(MaxX,DMHA2,DMHB2)
        pass



class Abutment():
    def __init__(self):
        pass 

    def start(self):
        #bearing capacity of the soil is represented has bc
        #surcharge load is s
        #coefficient of friction is cf
        #Breaking force  is BF
        #concrete cover is c
        #soil density is sd
        #Dead Load is DL	  
        #Live Load is LL
        #Ka is Active earth pressure 

        bc,s,cf,BF,c,sd,DL,LL = sym.symbols('bc,s,cf,BF,c,sd,DL,LL')
        c=0.06
        h = float(input("Enter the width of the stem: "))
        #D is the diameter of reinforcement bars
        D=0.032
        bc = float(input("Enter the bearing capacity of the soil: "))
        s = float(input("Enter your surcharge load: "))
        #Cg is concrete grade
        Cg =24
        fy = 410
        cf =float(input("Enter your coefficient of friction"))
        c = float(input("Enter your concrete cover"))
        sd = float(input("Enter your soil density"))
        #d is effective depth
        d = round(h -c - (D/2),3)
		#CHECKING FOR SLIDING
        Ka = round((1-math.sin(30)) / (1+math.sin(30)))
        #H is depth of the abutment
        H = float(input("Enter the depth of the abutment"))
        #He is horizontal earth force
        He = round(0.5*H*H*Ka*sd)
		#Hs is horizontal surcharge force
        Hs = round(Ka*s*H)
        #SSF is Sum of sliding force
        SSF = round(He + Hs)
        WA1 = float(input("What is the Wall 1 Area"))
        wall1 = WA1*Cg
        WA2 = float(input("What is the Wall 2 Area"))
        wall2 = WA2*Cg
        BA = float(input("What is the Base Area"))
        Base = BA * Cg
        EA = float(input("What is the Area of the earth"))
        Ve = EA * 2 * 9.81
        SA = float(input("What is the Area of the Surcharge"))
        s = float(input("What is the Surcharge load"))
        Vs = SA * s
        DL = float(input("What is the Dead load"))
        LL= float(input("What is the Live load"))

		#SFR is Sum of Friction Resisting force
        SFR = round(wall1 + wall2 + Base + Ve + DL)

        #FOS is Factor of Safety against SLIDING
        FOS = (0.4*SFR)/SSF
        if FOS > 1.5: 
            print ("ABUTMENT IS SAFE FROM SLIDING")
        else: 
            print ("ABUTMENT IS NOT SAFE FROM SLIDING")

        #CHECKING OF OVERTURNING 
        #Hso = Horizontal Surcharge Overturning Moment
        #LA1 = Lever Arm of the Surcharge
        LA1= float(input("What is the Lever Arm of the surcharge"))
        Hso = Hs * 1.6 * LA1

        #Hse = Horizontal Earth Overturning Moment
        #LA2 = Lever Arm of the Earth 
        LA2= float(input("What is the Lever Arm of the Earth"))
        Hse = He * 1.6 * LA2    
        #TOTAL HORIZONTAL OVERTURNING MOMENT = THOM
        THOM = Hse + Hso

        #Wall overturning resisting moment = W1 
        L1= float(input("What is the Lever Arm of W1"))
        W1 = wall1 * L1

        #Wall overturning resisting moment = W2 
        L2= float(input("What is the Lever Arm of W2"))
        W2 = wall2 * L2

        #BASE overturning resisting moment = Wb 
        L3= float(input("What is the Lever Arm of Wb"))
        Wb = Base * L3

        #EARTH overturning resisting moment = We 
        L4= float(input("What is the Lever Arm of We"))
        We = Ve * L4

		#Dead Load overturning resisting moment = Dm 
        L5= float(input("What is the Lever Arm of Dm"))
        Dm = DL * L5

        #TOTAL VERTICAL OVERTURNING MOMENT = TVOM
        TVOM = Dm + We + Wb + W1 + W2

        #FOS is Factor of Safety against SLIDING
        FOS = (TVOM)/THOM
        if FOS > 2.0:
            print ("ABUTMENT IS SAFE FROM OVERTURNING")
        else: 
            print ("ABUTMENT IS NOT SAFE FROM OVERTURNING")

        #CHECKING FOR BEARING PRESSURE FAILURE
        #Wall moment = W1
        L1= float(input("What is the Lever Arm of W1"))
        W1 = wall1 * L1

        #Wall  moment = W2 
        L2= float(input("What is the Lever Arm of W2"))
        W2 = wall2 * L2

        #BASE moment = Wb 
        L3= float(input("What is the Lever Arm of Wb"))
        Wb = Base * L3

        #EARTH  moment = We 
        L4= float(input("What is the Lever Arm of We"))
        We = Ve * L4

        #Surcharge  moment = Ws 
        L5= float(input("What is the Lever Arm of Ws"))
        Ws = Vs * L5

        #Live Load  moment = Lm
        L6= float(input("What is the Lever Arm of We"))
        Lm = LL * L6

        #Dead Load moment = Dm 
        L7= float(input("What is the Lever Arm of Dm"))
        Dm = DL * L7

        #Hs moment = Hsm 
        L8= float(input("What is the Lever Arm of Hsm"))
        Hsm = Hs * L8

        #He moment = Hem 
        L9= float(input("What is the Lever Arm of Hem"))
        Hem = He * L9

        #TOTAL BEARING MOMENT = TBM

        TBM = (Dm + Lm + Ws + We + Wb + W2 + W1 + Hsm + Hem )

        #BEARING PRESSURE VALUE = BPV
        Baselength = float(input("What is the Base length"))
        BPV = ( (s + LL + SFR)/ Baselength + TBM*TBM/ Baselength) 

        if BPV < bc:
            print ("ABUTMENT IS SAFE FROM BEARING PRESSURE FAILURE")
        else: 
            print ("ABUTMENT IS NOT SAFE FROM BEARING PRESSURE FAILURE")

        #DESIGN OF STEM

        Ka = round((1-math.sin(30)) / (1+math.sin(30)))
        #STM is depth of the stem
        STM = float(input("Enter the depth of the stem"))
        #He is horizontal earth force
        He = round(0.5*STM*STM*Ka*sd)
        #Hs is horizontal surcharge force
        Hs = round(Ka*s*STM)

        M = He + Hs





jeff = Abutment()
print(jeff.start())


