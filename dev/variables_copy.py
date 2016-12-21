

#Main list of Variable in the Model

Labor market
 Inputs
 #Labor Supply Variables
  #y        =  w(h-l)+pie_s           #Real income, P1
  #y_2      =  w_2(h_2-l_2)+pie_s_2   #Real income, P2
  r       = 2.0                      #Real Interest Rate, P1, MRSc,c_2=1+r
  r_2     = 2.0                      #Real Interest Rate, P2
  T       = 5                        #Total Tax Burden, P1
  T_2     = 5                        #Total Tax Burden, P2
  pie_s   = 15                       #Dividend/Wealth Supply, P1
  pie_s_2 = 15                       #Dividend/Wealth Supply, P2
  lmb_s     = .7                     #Linear Model Parameter for Labor Supply, b(slope), P1***
  lmb_s_2   = .7                     #Linear Model Parameter for Labor Supply, b(slope), P2***
  lma_s=((1+r)-wealth_lifetime)      #Linear Model Parameter for Labor Supply, a(intercept), P1 (lma_s=((1+r)-pie_s+T))
  lma_s_2=((1+r_2)-wealth_lifetime)  #Linear Model Parameter for Labor Supply, a(intercept), P2 (lma_s_2=((1+r_2)-pie_s_2+T_2))
  l        =                         #leisure, P1
  l_2      =                         #leisure, P2
  h        = 24                      #Total hours, P1
  h_2      = 24                      #Total hours, P2
  #c       =                         #Consumption, P1
  #c_2     =                         #Consumption, P2
  #sp      =                         #Savings, Can be negative(borrowing in P1), P1
  wealth_lifetime =                  #Lifetime weath
            =((w*(h-l)+pie_s)+((w_2*(h_2-l_2)+pie_s_2)/(1+r))-T-(T_2/(1+r)))
  #budget_const_future=              #Future Budget Constraint
              #c_2=w_2*(h-l_2)+pie_s_2-T_2+(1+r)*Sp
  #budget_constr_life=               #Lifetime Budget COnstraint   
              #c+(c_2/(1+r))=w(h-l)+pie_s-T+((w_2*(h_2-l_2)+pie_s_2-T_2)/(1+r))
            
 #Labor Demand Variables   
  pie_d   = 15                       #Profit for Firm, P1
  pie_d_2 = 15                       #Profit for Firm, P2
  lmb_d   = .2                       #Linear Model Parameter for Labor Demand, b(slope), P1***
  lmb_d_2 = .2                       #Linear Model Parameter for Labor Demand, b(slope), P2***
  lma_d=(K+z-(1+r))                  #Linear Model Parameter for Labor Demand, a(intercept), P1
  lma_d_2=(K_2+z_2-(1+r_2))          #Linear Model Parameter for Labor Demand, a(intercept), P2
  z       = .2                       #Total Factor Productivity, P1
  z_2     = .2                       #Total Factor Productivity, P2
  K       = 10                       #Capital, P1
  K_2     = 10                       #Capital, P2
  #K_2=((1-d)*K)+I
  #d     =.2                       #Rate of Asset Depreciation, P1
  #d_2     =.2                       #Rate of Asset Depreciation, P2
  #I       =1                        #Firm Investment, P1
  #i       =1                        #Proportion of Investment used to make Output, Constant Returns to Scale****

 Outputs
  #w   =                             #Real Wage, P1, (MRSl,c)
  #w_2 =                             #Real Wage, P2, (MRSl_2,c_2)
  #N   =                             #Labor Market, P1
  #N_2   =                           #Labor Market, P2

Production Market
 Inputs
  z       =1                         #Total Factor Productivity, P1
  z_2     =1                         #Total Factor Productivity, P2
  d       =.2                        #Rate of Asset Depreciation, P1
  d_2     =.2                        #Rate of Asset Depreciation, P2
  K     =5                           #Capital, P1
  K_2=((1-d)*K)+I                    #Capital, P2
  K_o     = (1-d_2)*K_2              #Capital left over at end of P2, sold in liquidation sale
  N       =6.66                      #labor, P1
  N_2     =6.66                      #labor, P2
  alpha   =.5                        #Cobb-Douglas Parameter Alpha, P1
  alpha_2 =.5                        #Cobb-Douglas Parameter Alpha, P2
  beta    =(1-alpha)                 #Cobb-Douglas Parameter Beta, P1
  beta_2  =(1-alpha_2)               #Cobb-Douglas Parameter Beta, P1
  I       =1                         #Firm Investment, P1
  i       =1                         #Proportion of Investment used to make Output, Constant Returns to Scale****, Can produce one unit of capital using one unit of output
  pie_d   = Ys-(w*N)-I               #Profit for Firm, P1
  pie_d_2 = Ys_2-(w_2*N_2)+(1-d)*K_2 #Profit for Firm, P2   
  V       =pie_d+(pie_d/(1+r))       #Present value of profits for firm
  #w      =                          #Marginal Product of Labor, MPN
  #T_c     =                          #Corporate Taxes, P1
  #T_c     =                          #Corporate Taxes, P2
 Outputs
  Ys   =                             #Output/Production Supply Quantity, P1
     #=z*((K**alpha)*(N**beta))
  Ys_2 =                             #Output/Production Supply Quantity, P2
     #=z_2*((K_2**alpha_2)*(N_2**beta_2))
  

 
Money Market
 Inputs
  #pie_d   = 25                      #Profit for Firm, P1
  #pie_d_2 = 14                      #Profit for Firm, P1
  ms       = 18.60                   #Money Supply from Central Bank, P1
  ms_2     = 18.75                   #Money Supply from Central Bank, P1
  mma_d      = 20                    #Linear Model Parameter for Money Demand, a(intercept), P1
  mma_d_2    = 20                    #Linear Model Parameter for Money Demand, a(intercept), P2
  mmb_d      = .7                    #Linear Model Parameter for Money Demand, b(slope), P1
  mmb_d_2    = .7                    #Linear Model Parameter for Money Demand, b(slope), P2
  
 Outputs
  #r       = 0.015                   #Real Interest Rate, P1
  #r_2     = 0.05                    #Real Interest Rate, P1

Demand Current Good
 #Inputs
  #w   =                             #Real Wage, P1, (MRSl,c)
  #w_2 =                             #Real Wage, P2, (MRSl_2,c_2)
  l        =                         #leisure, P1
  l_2      =                         #leisure, P2
  h        = 24                      #Total hours, P1
  h_2      = 24                      #Total hours, P2
  #Cd      =                         #Aggregate Comsumption Demand by concumer, P1
  #Cd_2    =                         #Aggregate Comsumption Demand by consumer, P2
  #I       =                         #Aggregate Investment Demand by firm, P1
  #I_2     =                         #Aggregate Investment Demand by firm, P2
  G       =                          #Aggregate Government Spending, P1
  G_2     =                          #Aggregate Government Spending, P2
  #T       =                         #Aggregate Tax, P1
  #T_2     =                         #Aggregate Tax, P2
  #X       =                         #Aggregate Exports, P1
  #X_2     =                         #Aggregate Exports, P2
  #M       =                         #Aggregate Import, P1
  #M_2     =                         #Aggregate Import, P2
  
Output Market
  #r       = .015                    #Real Interest Rate, P1
  #r_2     = .015                    #Real Interest Rate, P2
  oma_s    = 15                      #Linear Model Parameter for Output Market, a(intercept), P1
  oma_s_2   = 15                     #Linear Model Parameter for Output Market, a(intercept), P2
  omb_s    = .2                      #Linear Model Parameter for Output Market, b(slope), P1
  omb_s_2   = .2                     #Linear Model Parameter for Output Market, b(slope), P2
  wealth_lifetime =                  #Lifetime weath
  z       =                          #Total Factor Productivity, P1
  z_2     =                          #Total Factor Productivity, P2
  K       =                          #Capital, P1
  K_2     =                          #Capital, P2
  Ys       = 20                      #Output Quantity from Production Market, P1
  Ys_2     = 25                      #Output Quantity from Production Market, P2
  #Cd      =                         #Aggregate Comsumption Demand by concumer, P1
  #Cd_2    =                         #Aggregate Comsumption Demand by consumer, P2
  #I       =                         #Aggregate Investment Demand by firm, P1
  #I_2     =                         #Aggregate Investment Demand by firm, P2
  G       =                          #Aggregate Government Spending, P1
  G_2     =                          #Aggregate Government Spending, P2
  #T       =                         #Aggregate Tax, P1
  #T_2     =                         #Aggregate Tax, P2
  #X       =                         #Aggregate Exports, P1
  #X_2     =                         #Aggregate Exports, P2
  #M       =                         #Aggregate Import, P1
  #M_2     =                         #Aggregate Import, P2
  Yd       =                         #Output demand, P1
      = Cd(r) + I(r) + G #+(X-M)
  Yd_2     =                         #Output demand, P2
      = Cd_2(r) + I_2(r) + G_2 #+(X_2-M_2)
  
  
Government
 Inputs
  #G       =                         #Government Spending, P1
  #G _2    =                         #Government Spending, P2
  #T       =                         #Tax, P1
  #T_2     =                         #Tax, P2
  #r       = .015                    #Real Interest Rate, P1
  #r_2     = .015                    #Real Interest Rate, P2
  #budget_constr_gov=                #Government Budget Constraint
        #G+(G/(1+r))=T+(T_2/(1+r))















