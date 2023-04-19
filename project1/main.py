calculation_days=24
units="hours"

def total_units(variable):
    if variable>0:
                  return(f"{variable} days are {variable*calculation_days} {units}")
    elif variable==0:
        print("dont enter null")
    else:
        return("value error for entry")

value=input("assholw give input\n")

if value.isdigit():
   n_val=int(value)
   net_value=total_units(n_val)
   print(net_value)
else:
    print("error input for number")


