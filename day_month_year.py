# number of days -> ..year, ..months, ..days

# Giving total days
total_days = 999

# calculate the number of years
years = total_days // 365

# calculate the remaining number of days (- years)
days_remaining = total_days - (years * 365)

# calculate the number of months
months = days_remaining // 30

# calculate the remaining days (-months)
days = days_remaining - (months * 30)

# printing the results
print(f"{years} έτη, {months} μήνες, {days} ημέρες")
