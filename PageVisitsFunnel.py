import codecademylib
import pandas as pd

visits = pd.read_csv('visits.csv',
                     parse_dates=[1])
cart = pd.read_csv('cart.csv',
                   parse_dates=[1])
checkout = pd.read_csv('checkout.csv',
                       parse_dates=[1])
purchase = pd.read_csv('purchase.csv',
                       parse_dates=[1])

# inspection of dataframes
print(visits.head())
print(cart.head())
print(checkout.head())
print(purchase.head())

# Combining visits and cart using left merge
com_visits_cart = pd.merge(visits,cart, how= 'left')
print(len(com_visits_cart))
print(com_visits_cart.head())

# Number of timestamps that are null
null_in_cart_time = com_visits_cart[com_visits_cart['cart_time'].isnull()]
#print(null_in_cart_time.head())
print(len(null_in_cart_time))

#percentage of users who visited cool T-Shirts Inc ended up not placing a t-shirt in their cart.
percent_no_cart = ((float(len(null_in_cart_time)))/(float(len(null_in_cart_time))+float(len(com_visits_cart)))) * 100
print(percent_no_cart)

# Combine Cart and checkout with a left join
com_cart_checkout = pd.merge(cart,checkout, how='left')
print(com_cart_checkout)
null_checkout = com_cart_checkout[com_cart_checkout['checkout_time'].isnull()]
print(len(null_checkout))

# Percentage of users who put items in cart but did not proceed to checkout.
percent_no_checkout= ((float(len(null_checkout))/(float(len(null_checkout)+float(len(com_cart_checkout)))))) * 100
print(percent_no_checkout)

#Merging all four steps of the funnel, using a series of left merges
all_data = visits.merge(cart,how = 'left').merge(checkout, how ='left').merge(purchase, how = 'left')
print(all_data.head())

# Percentage of people who proceeded to checkout but did not purchase a t-shirt
com_checkout_purchase = pd.merge(checkout,purchase, how = 'left')
print com_checkout_purchase 
purchase_null = com_checkout_purchase[com_checkout_purchase['purchase_time'].isnull()]

percent_no_purchase = (float(len(purchase_null)/(float(len(purchase_null)+float(len(com_checkout_purchase)))))) * 100
print(percent_no_purchase)
print('----------------------------------------')

# Which funnel is weakest, i.e has the highest percentage of users not completing it
print(percent_no_cart) # higest
print(percent_no_checkout)
print(percent_no_purchase)

# Calculate the average time from initial visit to final purchase. 
all_data['time_to_purchase'] = \
    all_data.purchase_time - \
    all_data.visit_time

#Examine the results 
print(all_data.time_to_purchase)

#Calculate the average time to purchase using the following code:
print(all_data.time_to_purchase.mean())
