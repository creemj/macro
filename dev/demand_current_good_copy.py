import numpy as np
import matplotlib.pyplot as plt

##Notes##

##Variables
#p_ie= current period dividen from firm/firm profit
#p_ie_2= future period dividen from pir/firm_profit
#r=real interest rate. Rate at which consumers and the government can borrowers and lend. 

#firm demand increases until MPN = w
#labor demand shifts with z or with inital K. High z or K shifts demand to right.

class Demand_Current_Good:

    def __init__(self, dcga_s, dcga_s_2, dcgb_s, dcgb_s_2, Ys, Ys_2, h , h_2, l, l_2, Cd, Cd_2, I, I_2, G, G_2, T, T_2):
        """
        Set up market parameters.  All parameters are scalars.  See
        http://quant-econ.net/py/python_oop.html for interpretation.

        """
        income  = w*(h-l)
        income_2= w_2*(h_2-l_2)
        #dcga_d=(pie_d-(1+r))
        #dcga_d_2=(pie_d_2-(1+r_2))
        #dcga_s=((1+r)-pie_s)
        #dcga_s_2=((1+r_2)-pie_s_2)
        
        self.dcgb_s, self.dcgb_s_2, self.dcga_s, self.dcga_s_2, self.Ys, self.Ys_2 , self.h , self.h_2, self.l, self.l_2, self.Cd, self.Cd_2, self.I,  self.I_2, self.G, self.G_2, self.T, self.T_2 = dcgb_s, dcgb_s_2, dcga_s, dcga_s_2, Ys, Ys_2, h , h_2, l, l_2, Cd, Cd_2, I, I_2, G, G_2, T, T_2
        #if  dcga_d  <  a_s :
         #   raise ValueError('Insufficient demand.')
        #elif dcga_d_2 < a_s_2 :
         #   raise ValueError('Insufficient demand on 2.')
        
   # def dcgrate_p1(self):
    #    "Return equilibrium wage"
     #   return  round((self.dcga_d - self.a_s)/(self.dcgb_d  + self.b_s ), 2)

    def inverse_demand_current_good_p1(self,x):
        "Compute inverse demand for current goods curve"
        return ((self.Cd+self.I+self.G) * x)/100
        
    def inverse_demand_current_good_p2(self,x):
        "Compute inverse demand for current goods curve"
        return ((self.Cd_2+self.I_2+self.G_2) * x)/100
        
    def ys_rate_p1(self):
        "Comgpute real interest rate at Ys"
        return ((self.dcga_s /self.dcgb_s ) + (1/self.dcgb_s ) * self.Ys)/100




if __name__ == '__main__':

#Output Market Vars
#    r       = .015
#    r_2     = .015
    dcga_s   = 15
    dcga_s_2 = 15
    dcgb_s   = .2
    dcgb_s_2  = .2
    w  = 2.5
    w_2= 2.5
    h = 876.0
    h_2 = 876.0
    l = 668.0
    l_2 = 668.0
    
    #Nedd to add other components of wealth_lifetime#
    #wealth_lifetime = 100
    #######################
    #z       =  #an increae will shift output curve to right
    #z_2     =  #an increae will shift output curve to right
    #K       =  #an increae will shift output curve to right
    #K_2     =  #an increae will shift output curve to right
    Ys      = 5.7
    Ys_2    = 5.7
    Cd      = 1000
    Cd_2    = 1000
    I       = 1000
    I_2     = 1000
    G       = 1000
    G_2     = 1000
    T       = 1000
    T_2     = 1000
#    X_1     =
#    X_2     =
#    M_1     =
#    M_2     =
    
    
    #Calculating the Equlibriums 
    bs_line= dcga_s, dcga_s_2, dcgb_s, dcgb_s_2, Ys, Ys_2, h, h_2, l, l_2, Cd, Cd_2, I, I_2, G, G_2, T, T_2
    #print(bs_line)    
    dcg= Output_Market(*bs_line) 
    
    print("Rate at Ys = ",dcg.ys_rate_p1())
    print("Rate at Ys_2 = ",dcg.ys_rate_p2())
    
    
    #print("Equilibrium Wage in Period One = ", dcg.wage_p1())
    #print("Labor Market in Period One = ", dcg.quantity_p1())
    #print("Equilibrium Wage in Period Two = ", dcg.wage_p2())
    #print("Labor Market in Period Two = ", dcg.quantity_p2())
    
    #print("Interest Rate = ", mm.rate_p1())
    #print("Interest Rate 2 = ", mm.rate_p2())

