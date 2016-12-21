import numpy as np
import matplotlib.pyplot as plt




##Notes##

##Variables
#p_ie= current period dividen from firm/firm profit
#p_ie_2= future period dividen from pir/firm_profit
#r=real interest rate. Rate at which consumers and the government can borrowers and lend. 

#firm demand increases until MPN = w
#labor demand shifts with z or with inital K. High z or K shifts demand to right.

class Output_Market:

    def __init__(self, oma_s, oma_s_2, omb_s, omb_s_2, Ys, Ys_2):
        """
        Set up market parameters.  All parameters are scalars.  See
        http://quant-econ.net/py/python_oop.html for interpretation.

        """
        #oma_d=(pie_d-(1+r))
        #oma_d_2=(pie_d_2-(1+r_2))
        #oma_s=((1+r)-pie_s)
        #oma_s_2=((1+r_2)-pie_s_2)
        
        self.omb_s, self.omb_s_2, self.oma_s, self.oma_s_2, self.Ys, self.Ys_2 = omb_s, omb_s_2, oma_s, oma_s_2, Ys, Ys_2
        #if  oma_d  <  a_s :
         #   raise ValueError('Insufficient demand.')
        #elif oma_d_2 < a_s_2 :
         #   raise ValueError('Insufficient demand on 2.')
        
   # def omrate_p1(self):
    #    "Return equilibrium wage"
     #   return  round((self.oma_d - self.a_s)/(self.omb_d  + self.b_s ), 2)

    def inverse_supply_p1(self,x):
        "Compute inverse output supply curve"
        return ((self.oma_s/self.omb_s ) + (1/self.omb_s ) * x)/100
        
    def inverse_supply_p2(self,x):
        "Compute inverse output supply curve"
        return ((self.oma_s_2 /self.omb_s_2 ) + (1/self.omb_s_2 ) * x)/100
    
    def ys_rate_p1(self):
        "Compute real interest rate at Ys"
        return ((self.oma_s /self.omb_s ) + (1/self.omb_s ) * self.Ys)/100
        
    def ys_rate_p2(self):
        "Compute real interest rate at Ys_2"
        return ((self.oma_s_2 /self.omb_s_2 ) + (1/self.omb_s_2 ) * self.Ys_2)/100


#__init__.py



if __name__ == '__main__':

#Output Market Vars
#    r       = .015
#    r_2     = .015
    oma_s   = 15
    oma_s_2 = 15
    omb_s   = .2
    omb_s_2  = .2
    #wealth_lifetime = 
    #z       =  #an increae will shift output curve to right
    #z_2     =  #an increae will shift output curve to right
    #K       =  #an increae will shift output curve to right
    #K_2     =  #an increae will shift output curve to right
    Ys      = 5.7
    Ys_2    = 5.7
#    Cd_1    =
#    Cd_2    =
#    I_1     =
#    I_2     =
   # G_1     =
   # G_2     =
   # T_1     =
   # T_2     =
#    X_1     =
#    X_2     =
#    M_1     =
#    M_2     =
    
    
    #Calculating the Equlibriums 
    bs_line= oma_s, oma_s_2, omb_s, omb_s_2, Ys, Ys_2
    #print(bs_line)    
    om= Output_Market(*bs_line) 
    
    print("Rate at Ys = ",om.ys_rate_p1())
    print("Rate at Ys_2 = ",om.ys_rate_p2())
    
    
    #print("Equilibrium Wage in Period One = ", om.wage_p1())
    #print("Labor Market in Period One = ", om.quantity_p1())
    #print("Equilibrium Wage in Period Two = ", om.wage_p2())
    #print("Labor Market in Period Two = ", om.quantity_p2())
    
    #print("Interest Rate = ", mm.rate_p1())
    #print("Interest Rate 2 = ", mm.rate_p2())


#Graphing the Model    
    q_max =  Ys * 2
    q_grid = np.linspace(0.0, q_max, 100)
    oms_p1 = om.inverse_supply_p1(q_grid)    
    #omd_p1 = om.inverse_demand_p1(q_grid)
    oms_p2 = om.inverse_supply_p2(q_grid)    
    #omd_p2 = om.inverse_demand_p2(q_grid)
      
    fig, ax = plt.subplots()
    ax.plot(q_grid, oms_p1, lw=2, alpha=0.6, label='Supply Period 1') 
    #ax.plot(q_grid, omd_p1, lw=2, alpha=0.6, label='Demand Period 1')
    ax.plot(q_grid, oms_p2, lw=2, alpha=0.6, label='Supply Period 2') 
    #ax.plot(q_grid, omd_p2, lw=2, alpha=0.6, label='Demand Period 2')
    ax.scatter(Ys, om.ys_rate_p1(), s=200, c='red', marker='x')
    ax.scatter(Ys_2, om.ys_rate_p2(), s=200, c='red', marker='x')
    ax.set_xlabel('Output Quantity', fontsize=14)
    ax.set_xlim(0, q_max)
    ax.set_ylabel('Real Interest Rate', fontsize=14)
    ax.legend(loc='upper right', frameon=False, fontsize=12)
    plt.show()