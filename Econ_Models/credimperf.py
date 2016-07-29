import numpy as np
import pandas as pd
import csv
import json

r_1	=		#real interest rate to lend
r_2	=		#real interest rate to borrow
N_1	=		#number of old age consumers (aggregate)
N_2	=		#number of young age consumers (aggregate)
n	=		#population growth rate 
y	=		#consumers real income in current period
y_2	=		#consumers real income in future period
t	=		#consumer lump sum taxes in current period
t_2	=		#consumer lump sum taxes in future period
s	=		#consumer savings in current period
s_2	=		#consumer savings in future period
c	=		#consumption in current period 
c_2	=		#consumption in future period
H	=		#quantity of an asset
p	=		#price of asset in future
b	=		#benefit to old people


bugd_2_lend = c_2-y_2+t_2-s(1+r_1) #where s >= 0

bugd_2_lend = c_2-y_2+t_2-s(1+r_2) #where s <= 0


#Credit market imperfections NOTES#
#1) Endowment point on graphs indicate that consumer is not a lender or borrower

#2)	The government essentially gives the consumer a low interest loan with the tax cut

#3)	Consumer increases the amount he consumes in current period by the amount of the 
	#tax cut because the government borrows at the lender's rate r_1
	
#4)	To the extent credit marketds are imperfect, ie r_2 > r_1 there is a benefit to have government debt.

#5)	If credit markets matter, people that are helped most by tax cuts are the ones that are 
	#affected by credit imperfections most. The poor. So fiscal policy can be used in welfare redistribution

#Asymetric Information#
L	=		#Quanity of loans
a	=		#percent of good loans


profit	=	L*(a(1+r_2)-(1+r_1))

#In equilibrium profit = 0. Therefore

r_2	=	((1+r_1)/a)-1 

#Asymetric Information NOTES#

#1) If a = 1 the r_1=r_2 and there are no credit market imperfections

#2)	In case of #1 this would resort back to a perfect credit model and possibly Ricardian.

#3) In case of rising defaults amoung borrowers good borrowers face higher interest rates 
	#and must reduce current consumption


we	=	y-t-(y_2-t_2-(p*h))/(1+r_1)

c	=	y-t+((p*H)/(1+r_1))



#Limited Commitment NOTES#

#1) To prevent commitment issues. Borrowers can post collateral. But then get collateral
	#constrained a reduction in the value of that collateral can reduce consumption. 

#Pay as You Go Social Security (PAYG)#
N_2	=	(1+n)N_1	#1

N_1*b	=	N_2*t	#2	#benifits to the old come from taxing the young

#combine 1 and 2

t=b/(1+n)

we =y+y_2/(1+r)+(b*(n-r))/((1+n)*(1+r))

#Notes#
#1)	IF n > r then consumers are better off. Better off if population growth rate is larger 
	#than real interest rate. Other wise the old in the initial generation with forever 
	#be better off

#2)	There is a private market failure that government can exploit. Gov can provide 
	#intergenerational transfers. So young can trade current consumption for fututer
	#and old can trade current consumption for past.
	
#3)	Rate of return in pay as you go system is dependent on population growth. Population
	#growth determines the tax burden. The smaller the tax burden is for each young
	# the higher the ratio of b/t. This ratio is rate of return.
	
#4) If n > r then rate of return in social security > rate of return private credit 
	#market


#Fully Funded Social Security (FF)#


#Notes#

#1)Going to a fully funded privatized SS might work if the gov can commit to not helping 
	#people who choose not to save the money. If they perceive government intervention
	#many will not save the money.
	
#2) Fully funded is subject to political influence. This large amount of money will be 
	#lobbied for by many groups. Another issue with fully funded is the moral hazard argument.
	
#3)Nations with a lot of old people to young could benefit from transition from PAYG to FF 
	#by deficit spending to cover the cost of the FF program. Then the younger generation 
	#will cover that cost with higher future taxes with the savings from current taxes 
	#that go to FF system.

#4) Social security helps with a credit market failure. Unborn cannot trade with the currently alive.


























