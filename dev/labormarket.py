# -*- coding: utf-8 -*-
"""
Created on Mon Sep 12 20:34:50 2016

@author: jcreem
"""
import numpy as np
import matplotlib.pyplot as plt

##Variables
#p_ie= current period dividen from firm/firm profit
#p_ie_2= future period dividen from pir/firm_profit
#r=real interest rate. Rate at which consumers and the government can borrowers and lend. 


class Labor_Market:
    
    #A linear demand curve Nd=a_d−b_d*p
                            #a_d=((1+r)-p_ie)
    #A linear supply curve Ns=a_s+b_s*p
                            #a_s=((1+r)-p_ie)
    def __init__(self, r, r_2, pie_d, pie_d_2, lmb_d, lmb_d_2, pie_s, pie_s_2, b_s, b_s_2):
        """
        Set up market parameters.  All parameters are scalars.  See
        http://quant-econ.net/py/python_oop.html for interpretation.

        """
        lma_d=(pie_d-(1+r))
        lma_d_2=(pie_d_2-(1+r_2))
        a_s=((1+r)-pie_s)
        a_s_2=((1+r_2)-pie_s_2)
        
        self.lma_d, self.lma_d_2, self.lmb_d, self.lmb_d_2, self.a_s, self.a_s_2, self.b_s, self.b_s_2 =  lma_d , lma_d_2 ,  lmb_d , lmb_d_2, a_s, a_s_2 , b_s, b_s_2
        if  lma_d  <  a_s :
            raise ValueError('Insufficient demand.')
        elif lma_d_2 < a_s_2 :
            raise ValueError('Insufficient demand on 2.')
        
    def wage_p1(self):
        "Return equilibrium wage"
        return  round((self.lma_d - self.a_s)/(self.lmb_d  + self.b_s ), 2)
        
    def wage_p2(self):
        "Return equilibrium wage"
        return  round((self.lma_d_2 - self.a_s_2)/(self.lmb_d_2  + self.b_s_2 ), 2) 
    
    def quantity_p1(self):
        "Compute equilibrium quantity of labor"
        return  round(self.lma_d - self.lmb_d  * self.wage_p1(),4)
    
    def quantity_p2(self):
        "Compute equilibrium quantity of labor"
        return  round(self.lma_d_2 - self.lmb_d_2  * self.wage_p2(),4)
            
    def inverse_demand_p1(self,x):
        "Compute inverse labor demand curve"
        return self.lma_d /self.lmb_d  - (1/self.lmb_d )* x
    
    def inverse_demand_p2(self,x):
        "Compute inverse labor demand curve"
        return self.lma_d_2 /self.lmb_d_2  - (1/self.lmb_d_2 )* x
    
    def inverse_supply_p1(self,x):
        "Compute inverse labor supply curve"
        return -(self.a_s/self.b_s ) + (1/self.b_s ) * x
        
    def inverse_supply_p2(self,x):
        "Compute inverse labor supply curve"
        return -(self.a_s_2 /self.b_s_2 ) + (1/self.b_s_2 ) * x
        
#    def labor_supply_surp(self):
 #       "Compute consumer surplus"
  #      # == Compute area under inverse demand function == #
  #      integrand = lambda x: (self.lma_d/self.lmb_d ) - (1/self.lmb_d )* x
  #      area, error = quad(integrand, 0, self.quantity())
  #      return area - self.price() * self.quantity()
    
   # def labor_demand_surp(self):
    #    "Compute producer surplus"
     #   #  == Compute area above inverse supply curve, excluding tax == #
      #  integrand = lambda x: -(self.a_s /self.b_s ) + (1/self.b_s ) * x
      #  area, error = quad(integrand, 0, self.quantity())  
      #  return (self.price() - self.tax) * self.quantity() - area
