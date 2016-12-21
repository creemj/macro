# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:34:50 2016

@author: jcreem
"""
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

##Variables

#r=real interest rate. Rate at which consumers and the government can borrowers and lend. 
#Output is produce using production function 
#Y =z *F(K ,N )
#K =capital firm starts with, given
#z=total factor productivity
#d=depreciation, rateat which capital deperciates


#Y_2=z_2*F(K_2,N_2)
#K_2=(1-d)*K +I
#i =1 percent of units taken from p_ie for investment. stays 1 for now
#pie_d= Y -(w *N )-(I *i )  current period dividen from firm/firm profit. Firm produces on unit of cap using 1 unit of output.
                            #this can change. each investment unit decreases orift by 1 unit.

#pie_d_2= Y_2-(w_2*N_2)+((1-d)*K_2) future period dividen from pir/firm_profit

#pie_V = pie_d  + (pie_d_2/(1+r)) present value of profit for the firm. firm wants to max this by choosing N , N_2, I 

#firm demand increases until MPN = w. should also include optimal investment choice
#labor demand shifts with z or with inital K. High z or K shifts demand to right.

#Functional form Y=self.z*((self.K**self.alpha)*(self.N**self.beta))

class Production_Market:
    


    def __init__(self, z , z_2, d, d_2, K, N, N_2, alpha, alpha_2, \
                    beta, beta_2, I, i, w, w_2, T_c, T_c_2):
        """
        Set up market parameters.  All parameters are scalars.  See
        http://quant-econ.net/py/python_oop.html for interpretation.

        """
        K_2=((1-d)*K)+I
        K_o= (1-d_2)*K_2
        

        self.z , self.z_2, self.d, self.d_2, self.K, self.K_2, self.K_o, self.N, self.N_2, self.alpha, self.alpha_2, self.beta, self.beta_2, self.I, self.i, self.w, self.w_2, self.T_c, self.T_c_2 = z , z_2, d, d_2, K , K_2, K_o, N , N_2, alpha , alpha_2, beta , beta_2, I, i, w, w_2, T_c, T_c_2
        
        #if  lma_d  <  a_s :
         #   raise ValueError('Insufficient demand.')
        #elif lma_d_2 < a_s_2 :
         #   raise ValueError('Insufficient demand on 2.')
        
    def production_p1(self):
        "Total Production"
        return  round(self.z*((self.K**self.alpha)*(self.N**self.beta)),4)
        
    def production_p2(self):
        "Total Production"
        return  round(self.z_2*((self.K_2**self.alpha_2)*(self.N_2**self.beta_2)),4)
        
    def capital_p2(self):
        return self.K_2     #((1-self.d )*self.K )+self.I
    
    def capital_out(self):
        return self.K_o     #((1-self.d )*self.K )+self.I
        
    def profit_p1(self):
        return (pm.production_p2()-(self.w*self.N)-self.I-self.T_c)     #pie_d= Ys-(w*N)-I-T_c
        
    def profit_p2(self):
        return (pm.production_p2()-(self.w_2*self.N_2)+self.K_o-self.T_c_2)     #pie_d_2=Ys_2-(w_2*N_2)+K_o-T_c_2

    #def inverse_demand_p1(self,x):
    #    "Compute inverse labor demand curve"
     #   return self.lma_d /self.lmb_d  - (1/self.lmb_d )* x



if __name__ == '__main__':
    #(self, r, r_2, pie_d, pie_d_2, lmb_d, lmb_d_2, pie_s, pie_s_2, b_s, b_s_2)
    #             (ad, bd, az, bz)
    #Market MODEL (15, .5, -2, .5)
    #r       = 2.0
    #r_2     = 2.0
    #r       = mm.rate_p1()
    #r_2     = mm.rate_p2()
 
    z        =1
    z_2      =1
    w        =.05
    w_2      =.05
    d        =.2
    d_2      =.2
    K        =5.0
    #K_2     = Calculated
    #K_o     = (1-d_2)*K_2
    N        =6.66
    N_2      =6.66
    alpha    =.5
    alpha_2  =.5
    beta     =(1-alpha)
    beta_2   =(1-alpha)
    I        =1
    i        =1
    T_c      =0
    T_c_2    =0
    #pie_d    = Ys-(w*N)-I-T_c
    #pie_d_2  = Ys_2-(w_2*N_2)+K_o-T_c_2
 
    
   #bs_line= 0.015, 0,  15, 0 .2, 15, .9

#Calculating the Equlibriums 
    bs_line= z , z_2, d, d_2, K , N , N_2, alpha , alpha_2, \
                    beta , beta_2, I, i, w, w_2, T_c, T_c_2
    #print(bs_line)    
    pm= Production_Market(*bs_line)   

    print("Labor Market in Period One = ", N )
    print("Capital in Period One = ", K )
    print("Total Production in Period One = ", pm.production_p1())
    print("Total Profit in Period One ", pm.profit_p1())
    print("Labor Market in Period Two = ", N_2)
    print("Capital in Period Two = ", pm.capital_p2())
    print("Total Production in Period Two = ", pm.production_p2())
    print("Capital to Liquidate = ", pm.capital_out())
    print("Total Profit in Period Two ", pm.profit_p2())
    
    
    #print(pm.capital_p2())
 
    #print("Interest Rate = ", mm.rate_p1())
    #print("Interest Rate 2 = ", mm.rate_p2())


#Graphing the Model    
    q_max , q_max2   = pm.production_p1() * 3 , pm.production_p2()*3
    #print(q_max,q_max2)
    K_n , K_n2 = np.linspace(0.0, q_max, 100) , np.linspace(0.0, q_max2, 100)
    N_n , N_n2 = np.linspace(0.0, q_max, 100) , np.linspace(0.0, q_max2, 100)
    K_n , N_n = np.meshgrid(K_n, N_n)
    K_n2 , N_n2 = np.meshgrid(K_n2, N_n2)
    xs , xs2  = [K , pm.capital_p2()]
    ys , ys2 = [N , N_2]
    zs , zs2 = [pm.production_p1(), pm.production_p2()]
   
    pd_p1   = z *((K_n**alpha )*(N_n**beta ))
    pd_p2   = z_2*((K_n2**alpha_2)*(N_n2**beta ))
      

    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    
    #plt.plot(K ,pm.production_p1())
    #plt.plot(K_n,pd_p2)
    
    ax.plot_wireframe(K_n, N_n, pd_p1, rstride=100, cstride=100, color='blue', linewidth=1 )#, shade=False, antialiased=True) #, lw=2, alpha=0.6, label='Production 1')
    ax.scatter(xs, ys, zs, s=200, c='red', marker='o', depthshade=False)    
    ax.plot_wireframe(K_n2, N_n2, pd_p2, rstride=10, cstride=10, color='lightblue', linewidth=1)    #, antialiased=True) #, lw=2, alpha=0.6, label='Production 2')    
    ax.scatter(xs2, ys2, zs2, s=200, c='blue', marker='o', depthshade=False)     
    
    
    ax.set_xlabel('Capital Quantity', fontsize=14)
    ax.set_ylabel('Labor Quantity', fontsize=14)
    if q_max >= q_max2:    
        ax.set_xlim(0, q_max)
        ax.set_ylim(0, q_max)
    else:
        ax.set_xlim(0, q_max2)
        ax.set_ylim(0, q_max2)

    ax.set_zlabel('Production', fontsize=14)
    ax.view_init(elev=15, azim=225) #225
    ax.legend(loc='upper center', frameon=False, fontsize=12)
    plt.show()