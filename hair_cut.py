def hair_cut(hairstyles, prices, last_week):
  total_price = sum(prices)
  average_price = total_price / len(prices)
  
  new_prices = [price - 5 for price in prices]
  
  total_revenue = sum([prices[i] * last_week[i] for i in range(len(hairstyles))])
  average_daily_revenue = total_revenue / 7  # Calculate average daily revenue
  
  cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]
  
  return (
      f"Average Haircut Price: {average_price:.2f}\n"
      f"Average Daily Revenue: {average_daily_revenue:.2f}\n"
      f"Total Revenue: {total_revenue}\n"
      f"Prices reduced by 5: {new_prices}\n"
      f"All cuts under 30: {cuts_under_30}"
  )

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

print(hair_cut(hairstyles, prices, last_week))