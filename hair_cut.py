def hair_cut(hairstyles, prices, last_week):
  total_price = 0 
  
  for price in prices:
    total_price += price
  
  average_price = total_price / len(prices)
  
  new_prices = [price - 5 for price in prices]  
  total_revenue = 0 
  for i in range(len(hairstyles)):
    total_revenue += (prices[i] * last_week[i])
  
  average_daily_revenue = total_revenue / 7
  cuts_under_30 = [hairstyles[i] for i in range(len(hairstyles)) if prices[i] < 30]
  return ("Average Haircut Price: " + str(average_price) +
        "\nAverage Daily Revenue: " + str(average_daily_revenue) +
        "\nTotal Revenue: " + str(total_revenue) +
        "\nPrices reduced by 5: " + str(new_prices) +
        "\nAll cuts under 30: " + str(cuts_under_30))

hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

prices = [30, 25, 40, 20, 20, 35, 50, 35]

last_week = [2, 3, 5, 8, 4, 4, 6, 2]

hair_cut(hairstyles, prices, last_week)