l = 1
u = 12
 for i in range(l , u+1):
	print(i)
print("January , February , March , April , May , June , July , August , September , October , November , December")
month_name = input("Input the name of month:")
  if month_name == "February":
	print("no. of days 28/29")
elif month_name in ("April","June","September","November"):
	print("no. of days 30")
elif month_name in ("January","March","May","July","August","October","December"):
	print("no. of days 31")
else:
	print("wrong month")

	
	