countrydb = {}


while True:
  print("1. Insert")
  print("2. Display all countries")
  print("3. Display all capitals")
  print("4. Get capital")
  print("5. Delete")

  dsa = int(input("Please enter your choice : "))
  if dsa == 1:
    country = input("Please enter a country : ").upper()
    capital = input("Please enter a capital : ").upper()

    countrydb[country] = capital

  elif dsa ==2:
   print(list(countrydb.keys()))

  elif dsa ==3:
    print(list(countrydb.values()))

  elif dsa==4:
    country = input("Please enter a country : ").upper()
    print(countrydb.get(country))    

  elif dsa ==5:
    country = input("Please enter a country : ").upper()
    del countrydb[country]

  else:
    break

    
    
