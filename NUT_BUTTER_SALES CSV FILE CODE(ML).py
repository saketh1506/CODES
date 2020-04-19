#IMPORTING THE TOOLS REQUIRED TO CREATE FILES BY PANDAS N NUMPY
import pandas as pd
import numpy as np

#CREATING THE SALES_AMOUNT ARRAY TO CREATE THE WEEKLY_SALES DATA FRAME
sales_amounts = np.array([ [2,7,1],
                           [9,4,16],
                           [11,14,18],
                           [13,13,16],
                           [15,18,19], 
                           [10,8,12]])
                      
#CREATING WEEKLY_SALES DATA FRAME
weekly_sales = pd.DataFrame(sales_amounts,
                             index=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','PRICES OF EACH ITEM'],
                             columns=['ALMONDS BUTTER','PEANUT BUTTER','CASHEW BUTTER'])                
#CREATING THE PRICES ARRAY
prices = np.array([10,8,12])

#CALCULATING TOTAL_SALES FOR A WEEK WITH TOTAL COST OF EACH ITEM
total_sales = prices.dot(sales_amounts.T)
total_sales[5]=30

#ADDING TOTAL COLUMN AND ITS VALUES TO THE WEEKLY_SALES DATAFRAME
weekly_sales['TOTAL($)'] = total_sales.T
