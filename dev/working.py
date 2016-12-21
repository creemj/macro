import numpy as np
import matplotlib.pyplot as plt

from moneymarket import Money_Market as money
from labormarket import Labor_Market as labor

#__init__.py

if __name__ == '__main__':

#Labor Market Vars
#    r       = .015
#    r_2     = .015
    r       = mm.rate_p1()
    r_2     = mm.rate_p2()

    pie_d   = 15
    pie_d_2 = 15
    lmb_d   = .2
    lmb_d_2 = .2
    pie_s   = 15
    pie_s_2 = 15
    b_s     = .7
    b_s_2   = .7
   #bs_line= 0.015, 0,  15, 0 .2, 15, .9
 
#Momey Market Vars
    ms       = 18.60
    ms_2     = 18.60
    mma_d      = 20
    mma_d_2    = 20
    mmb_d      = .7
    mmb_d_2    = .7

   #bs_line= 0.015, 0,  15, 0 .2, 15, .9

#Calculating the Labor Market Equlibriums 
    lmbs_line= r, r_2, pie_d, pie_d_2, lmb_d, lmb_d_2, pie_s, pie_s_2, b_s, b_s_2
    #print(bs_line)    
    lm=labor(*lmbs_line)  
    

#Calculating the Money Market Equlibriums 
    mmbs_line= ms, ms_2, mma_d, mma_d_2, mmb_d, mmb_d_2, 
    #print(bs_line)    
    mm=money(*mmbs_line)

#Printing Labor Market Data
    print("Equilibrium Wage in Period One = ", lm.wage_p1())
    print("Labor Market in Period One = ", lm.quantity_p1())
    print("Equilibrium Wage in Period Two = ", lm.wage_p2())
    print("Labor Market in Period Two = ", lm.quantity_p2())
    
    print("Interest Rate = ", mm.rate_p1())
    print("Interest Rate 2 = ", mm.rate_p2())


#Graphing the Labor Market Model    
    lmq_max =  lm.quantity_p1() * 2
    lmq_grid = np.linspace(0.0, lmq_max, 100)
    lms_p1 = lm.inverse_supply_p1(lmq_grid)    
    lmd_p1 = lm.inverse_demand_p1(lmq_grid)
    lms_p2 = lm.inverse_supply_p2(lmq_grid)    
    lmd_p2 = lm.inverse_demand_p2(lmq_grid)
      
    lmfig, lmax = plt.subplots()
    lmax.plot(lmq_grid, lms_p1, lw=2, alpha=0.6, label='Supply Period 1') 
    lmax.plot(lmq_grid, lmd_p1, lw=2, alpha=0.6, label='Demand Period 1')
    lmax.plot(lmq_grid, lms_p2, lw=2, alpha=0.6, label='Supply Period 2') 
    lmax.plot(lmq_grid, lmd_p2, lw=2, alpha=0.6, label='Demand Period 2')
    lmax.set_xlabel('Labor Market Quantity', fontsize=14)
    lmax.set_xlim(0, lmq_max)
    lmax.set_ylabel('Wage', fontsize=14)
    lmax.legend(loc='upper right', frameon=False, fontsize=12)
    plt.show()

#Printing Money Market Data
    print("Equilibrium Interest Rate in Period One = ", mm.rate_p1())
    print("Money Supply in Period One = ", mm.quantity_p1())
    print("Equilibrium Interest Rate in Period Two = ", mm.rate_p2())
    print("Money Supply in Period Two = ", mm.quantity_p2())

#Graphing the Money Market Model    
    mmq_max =  mm.quantity_p1() * 2
    mmq_grid = np.linspace(0.0, mmq_max, 100)
    lms_p1 = ms     
    lmd_p1 = mm.inverse_demand_p1(mmq_grid)
    lms_p2 = ms_2
    lmd_p2 = mm.inverse_demand_p2(mmq_grid)
    mmfig, mmax = plt.subplots()

    mmax.axvline(x=lms_p1 , lw=2, alpha=0.6, color= 'b', label='Supply Period 1')
    mmax.plot(mmq_grid, lmd_p1, lw=2, alpha=0.6, color= 'g', label='Demand Period 1')
    mmax.axvline(x=lms_p2, lw=2, alpha=0.6, color = 'r', label='Supply Period 2')
    mmax.plot(mmq_grid, lmd_p2, lw=2, alpha=0.6, color= 'aqua', label='Demand Period 2')
    mmax.set_xlabel('Money Supply Quantity', fontsize=14)
    mmax.set_xlim(0, mmq_max)
    mmax.set_ylabel('Interest Rate', fontsize=14)
    mmax.legend(loc='upper right', frameon=False, fontsize=12)
    plt.show()
