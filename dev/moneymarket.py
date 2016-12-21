# -*- coding: utf-8 -*-
"""
Created on Sat Sep 17 19:31:03 2016

@author: jcreem
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:34:50 2016

@author: jcreem
"""
import numpy as np
import matplotlib.pyplot as plt

class Money_Market:
    
    #A linear demand curve Nd=a_d−b_d*p
                            #a_d=((1+r)-p_ie)
    #A linear supply curve Ns=a_s+b_s*p
                            #a_s=((1+r)-p_ie)
    def __init__(self, ms, ms_2, mma_d, mma_d_2, mmb_d, mmb_d_2):
        """
        Set up market parameters.  All parameters are scalars.  See
        http://quant-econ.net/py/python_oop.html for interpretation.

        """
        #mma_d=(pie_d-(1+r))
        #mma_d_2=(pie_d_2-(1+r_2))
        #a_s=((1+r)-pie_s)
        #a_s_2=((1+r_2)-pie_s_2)
        
        self.mma_d, self.mma_d_2, self.mmb_d, self.mmb_d_2, self.ms, self.ms_2 =  mma_d , mma_d_2 ,  mmb_d , mmb_d_2, ms, ms_2
        #if  mma_d  <  a_s :
        #    raise ValueError('Insufficient demand.')
        #elif mma_d_2 < a_s_2 :
        #    raise ValueError('Insufficient demand on 2.')
        
    def rate_p1(self):
        "Return equilibrium interest rate"
        return  round((self.mma_d - self.ms)/(self.mmb_d), 3)
        
    def rate_p2(self):
        "Return equilibrium interest rate"
        return  round((self.mma_d_2 - self.ms_2)/(self.mmb_d_2), 3) 
    
    def quantity_p1(self):
        "Compute equilibrium quantity of money"
        return  round(self.mma_d - self.mmb_d  * self.rate_p1(),4)
    
    def quantity_p2(self):
        "Compute equilibrium quantity of money"
        return  round(self.mma_d_2 - self.mmb_d_2  * self.rate_p2(),4)
            
    def inverse_demand_p1(self,x):
        "Compute inverse money demand curve"
        return self.mma_d /self.mmb_d  - (1/self.mmb_d )* x
    
    def inverse_demand_p2(self,x):
        "Compute inverse money demand curve 2"
        return self.mma_d_2 /self.mmb_d_2  - (1/self.mmb_d_2 )* x
    
    #def inverse_supply_p1(self,x):
        #"Compute inverse money supply curve"
        #return -(self.ms/self.b_s ) + (1/self.b_s ) * x
     #   return (self.ms/x)
        
   # def inverse_supply_p2(self):
       # "Compute inverse money supply curve"
        #return -(self.ms_2 /self.b_s_2 ) + (1/self.b_s_2 ) * x
    #    return (self.ms_2)
        
        
#    def labor_supply_surp(self):
 #       "Compute consumer surplus"
  #      # == Compute area under inverse demand function == #
  #      integrand = lambda x: (self.mma_d/self.mmb_d ) - (1/self.mmb_d )* x
  #      area, error = quad(integrand, 0, self.quantity())
  #      return area - self.price() * self.quantity()
    
   # def labor_demand_surp(self):
    #    "Compute producer surplus"
     #   #  == Compute area above inverse supply curve, excluding tax == #
      #  integrand = lambda x: -(self.a_s /self.b_s ) + (1/self.b_s ) * x
      #  area, error = quad(integrand, 0, self.quantity())  
      #  return (self.price() - self.tax) * self.quantity() - area



