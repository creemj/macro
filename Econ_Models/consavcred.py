import numpy as np
import pandas as pd
import csv
import json


## Two Period Model

# r   = 	        #real interest rate. Rate at which consumers and the government can borrowers and lend. Normal interest rate (Rate - Inflation Rate)
# #N   = 	        #number of consumers (aggregate)
# #y   = 	        #consumers real income in current period
# #y_2 = 	        #consumers real income in future period
# t    = 1	    #consumer lump sum taxes in current period
# #t_2 = 	        #consumer lump sum taxes in future period
# s    = 1	    #consumer savings in current period
# #s_2 = 	        #consumer savings in future period
# c    = 1	    #consumption in current period   
# #c_2 = 	        #consumption in future period
# p_2  =  1/(1+r) #relative price of future consumption
# G	 =			#government consumption goods in current period
# G_2	 =			#government consumption goods in future period
# T	 = N*t		#Aggregate taxes collected by government in current period
# T_2	 = N*t_2	#Aggregate taxes collected by gov in furter period.	
# B	 =			# total quantity of bonds issued in current period 
# S_p	 = 			#agg private savings in current period
# S    =S_p + S_g #Natioanl saving equal total private savings plus total government savings
# 
# y   = c + s + t           #c + s = y - t consumer's budget constraint in current period
# y_2 = c_2 + t_2 - (1+r)*s #c_2 = y_2 - t_2 + (1+r)*s  consumer's budget constraint in future period
# 
# ##Lifetime budget constraint **********
# 	#In terms of period 1 consumption
# #c + (c_2/(1+r)) = y + (y_2/(1+r)) - t - (t_2/(1+r))
# bc_life =  c + (c_2/(1+r)) - y - (y_2/(1+r)) + t + (t_2/(1+r)) 
# 
# #Lifetime Wealth *********
# we = y + (y_2/(1+r)) - t - (t_2/(1+r))
# 
# ##GOVERNMENT BUDGET CONSTRAINT
# G = T + B 						#current period
# T_2 = G_2 + (1+r)*B 			#further period government budget constraint 
# #G + G_2/(1+r) = T + T_2/(1+r)	#government present value budget constraint
# gov_life = G + G_2/(1+r) - T - T_2/(1+r) #gov must pay all of its debts by taxing its citizens	***********
# 
# ##Competitive Equilibrium
# 
# S_p = B #Credit market clears when net quantity of private savingd equals to the quantity of debt issued by government
# S_p = Y - C - T #Agg private savings equal private consumption minus income minus taxes
# 					#-Given B = G - T anf S_p = B --credit market clears
# Y - C - T = G - T # therefore
# 
# Y = C + G #Income - Expenditure Identity of Economy**********

#Applied Example

#dtgdp	#Gov Debt to GDP ratio is a measure of the burden of government debt
#B_t = 		#total gov debt in period t
r 	=	.01	#rate of interest
d	=	.03	#Ratio of primary deficit to GDP. (total debt to interest/total debt)
#dYt	=		#Gov primary deficit. value of gov defict after deducting interest payments on gov debt 
#Y_t	=		#Real GDP in period t
#Y_0	=		#GDP at period 0
g	=	.03	#GDP growth rate
t	=	2

# Y_t	=	Y_0(1+g)**t
# B_t1=	(1+r)*B_t+(d*Y_0*(1+g)^(t+1))
#dtgdp	=	d[(((1+r)/(1+g))^t)+(((1+r)/(1+g))^(t-1))+...+1
print (d*(((1+r)/(1+g))**t)+1)
print (d*(((1+r)/(1+g))**t)+(((1+r)/(1+g))**(t-1))+1)
print (120-(d*(((1+r)/(1+g))**t)+(((1+r)/(1+g))**(t-1))+(((1+r)/(1+g))**(t-2))+1))

#if real interest rate r < growth rate of real gdp then
dtgdp_lt = d*((1+g)/(g-r))
print('Long Run Debt to GDP Ratio=',round(dtgdp_lt,3))








##Objectives
#	1 - Choose c and c_2 to make yourself as well off as possible while satisfying bc_life
#	2 - Consumption should be smoother than income overtime but not smooth enough as theory suggests
#	3 - Consumption must fall during recession because income are lower
#			-Therefore, high consumption when output is high and low consumption when output is low.
#	4 - Primary determinant of consumer's current consumption is permanent income. (M. Fredman, 1957)		

#         Notes           #
##Highlights
#	1 Intertemporal decisions and the implications of of government deficits
#		-Dynamic consumption-savings decision
#		-r determines the the relative price of consumption in the future in terms of consumption in the present.
#		-consumption smoothing
#		-Ricardian equivalence theorem
#			-A change in the timing of taxes by the government is neural. In equilibrium, a change in current taxes 
#	    	exactly offset in present-value terms by an equal but opposite change in future taxes, has no real effect
#			on the real interest rate or on consumption of individual consumers
#			-Tax cut is not a free lunch
#	2 Notes on Model
#		-asset that is traded in credit market is currently bonds
#			-all bonds are indistingusiable because consumers dont default
#			-bonds traded directly in credit market	
#			-consumer buying bonds means they are lending
#			-consumer selling bonds means they are borrowing
#
#		-Lifetime Budget Constraint
#			-the present value of lifetime consumption equal present value of lifetime income minus lifetime taxes
#		-The market that N consumers interact with the government is the credit market.
#
#

##Future work
#	1-Work in work leisure decision in each period
#	2-Add assets to model
#	3-add various financial assets to model
#	4-add default on debts and intermediaries in credit markets
#   5-real vs normal interest rate
#   6-different rates for consumers borrow and lend. Rate on loan vs saving rate return-- depicts cost of running bank
#   7-progressive tax structure
#	8-$ for kids
# 	9-Add I = investment and CA = current account
#		- National accounts identitiy = S_p + S_g = I + CA, where S_g = -B
#	10-DSGE Models 