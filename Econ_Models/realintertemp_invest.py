import numpy as np
import pandas as pd
import csv
import json


## Real Intertemporal Model with Investment

r   = 	        #real interest rate. Rate at which consumers and the government can borrowers and lend. 
				#Normal interest rate (Rate - Inflation Rate). Opportunity cost of investing in firm
N   = 	        #Current labor supply
N_2	=			#Future period Labor supply
w	=			#wage rate
h	=			#hour devoted to work/liesure
l	=			#current leisure hours
l_2	=			#future leisure hours
#y   = 	        #consumers real income in current period
#y_2 = 	        #consumers real income in future period
T    = 	    	#consumer lump sum taxes in current period
T_2 = 	        #consumer lump sum taxes in future period
p_ie	=		#current period dividen from firm/firm profit
p_ie_2	=		#future period dividen from pir/firm_profit
S_P    = 	    #consumer savings in current period
# s_2 = 	    #consumer savings in future period
C   = 1	    	#consumption in current period   
C_2 = 	        #consumption in future period
K	=			#Current period capital
K_2	=			#Future period capital
z	=			#Current Total factor productivity
z_2	=			#Future Total factor productivity
Y	=			#Total current output
Y_2	=			#Total future output
d	=			#Rater of capital depreciation
I	=			#Quantity of current investment
V	=			#Present value of profits for the firm 
Y_d	=			#Total current demand for goods
G	=			#Total Government SPending in current period
G_b	=		#Inrease in government spending in current period
G_2	=			#Government spending in future period





#The Rep Consumer#

#consumer lifetime budget constraint

C=w*(h-l)+p_ie-T
C_2

#C+C_2/(1+r)=w*(h-l)+p_ie-T+((w_2*(h-l_2))+p_ie_2-T_2)/(1+r)

##Notes##
#1) Consumer must choose C, C_2, l, l_2 to maximize both period with respect to budget constraint

#2)MRS_Cl = w. When optimize marg rate of sub of liesure for consumption is equal to wage rate. and MES_CC2 = 1+r
	#and MRS_C2l2 = w_2
#3) As r increase N increase. opportunity cost of not working increases
#4)	As total wealth increase N decreases due to income effect.
#5) Marginal Propensity to Consume Amount that current consumption increases when there 
	#is a unit increase in aggregate demand

#The Rep Firm

Y=z*F(K,N)
Y_2=z_2*F(K_2,N_2)
K_2=((1-d)*K)+I	#Future capital equal depreciated current capital plus Investment in current period


##Profits##

p_ie=Y-(w*N)-I
p_ie_2=Y_2-(w_2*N_2)-((1-d)*K_2)
V=p_ie+(p_ie_2/(1+r)) 

##Investment Decision##
MP_K2-d=r #Marginal product of capital after depreciation

##Government##
G+G_2/(1+r)=T+T_2/(1+r)

##Current Labor Market and Output supply curve##

##Curent goods market and output demand curve##
Y_d=C_d(r)+I_d(r)+G #Current consumption and current investment negatively based on real rate of interest


##Change in Gov spending and multipliers##
Y_d=C_d(r)+I_d(r)+G
Y_d2=C_d2(r)+I_d2(r)+G_b #Shift from Y_d to Y_d2 is by (1-MPC)(G_b-G) units so
C_d2(r)-C_d(r)=-MPC(G_b-G)	#therefore
MPC=(Y_d2-Y_d-(1-MPC)(G_b-g))/(Y_d2-Y_d) ==> (Y_d2-Y_d)=(G_b-G) 

(Y_d2-Y_d)/(G_b-G)=1 #Partial Expenditure Multiplier




MPC=1 			#MPC is the marginal propensity to consume
-MPC*(G_b-G) 	#Change in demand for consumption goods. G_b-G is the increase in gov spending but can also be thought
				#of as the decrease in lifetime wealth
				#Two effects are occurring here. Direct effect (G_b-G) and an indirect effect (MPC*G)-MPC*G_b)


##Notes##
#1) Any increase in government spending in current period needs to be offset by taxes in the furture period and therefore 
	#it chages consumers lifetime wealth.
#2) Richardian equivalance would say that it wouldn't matter if extra spending occured via more taxes in current period
	#or borrowed gov debt 
#3) Total change in demnad for goods is the direct effect of a change in gov spending plus the indirect effect on 
	#consumption	(1-MPC)(G_b-G)==>MPS(G_b-G)
#4) MPC+MPS=1 therefore multiplier is 1/(1-MPC) ==> 1/MPS



##Full Model
#exogenous variables [z,w,r,G,T]
#endogenouse variables [C,Y,p_ie,N,K,I] 





#Note#
#1) Current profits are forgone by firm when it invests/acquiring capital in the current period.
	#Firm uses current output to invest in capital
#2)	Capital left over after future period is (1-d)*K_2. Firm can sell off capital at end of second period
	#on second hand market.
#3) goal is to maximize profits over the current and future periods
#4) Firm hires labor until current marginal product equals real wage, MP_N=w
#5) Labor demand curve shifts with z or wit initial capital stock K.
#6) One unit of additional I in current period implies MP_K2+1-d units of p_ie_2.
#7) MP_K2-d=r, firm invests until the net marginal product of capital equals real interest rate. 
	#If marginal cost of investment MC(I)=1 and marginal benefit of investment MB(I)=(MP_K2+1-d)/(1+r).
	#opportunity cost of investing in more capital is the real interest rate or rate of return of 
	#other assets in the economy.
#8) Investment behavior is about the responce of the firm to behavior to perceived marginal rates of return on investment
#9)	As z and K increase production function to shift up, labor demand to shift right, and putput supply to shift right. 
	#This is because there will be a greater marginal product of labor
#10) increase in G or G_2 shifts labor supply to right and shifts output supply to the right
	












