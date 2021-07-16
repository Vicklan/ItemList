def calcInclusivePrice(exclusivePrice,taxRate):
     inclusiveprice = exclusivePrice + (exclusivePrice*taxRate)
     return (inclusiveprice)

items = [
     {
         "Name": "Sugar",
         "exclusivePrice":85,
         "TaxRate":0.16,
         "description":"Kabras Sugar",
         "inclusivePrice":0
         
     },
     {
         "Name": "Bread",
         "exclusivePrice":47,
         "TaxRate":0.18,
         "description":"Supa Loaf" ,
         "inclusivePrice":0
     },
     {
         "Name": "Milk",
         "exclusivePrice":46,
         "TaxRate":0.12,
         "description":"KCC",
         "inclusivePrice":0
     },
     {
         "Name": "Salt",
         "exclusivePrice":19,
         "TaxRate":0.1,
         "description":"KenSalt",
         "inclusivePrice":0
     },
 ]

for item in items:
   inclusive = (calcInclusivePrice(item["exclusivePrice"],item["TaxRate"]))
   item["inclusivePrice"] = inclusive
   print(item["Name"] ,item["description"],item["inclusivePrice"])
    

     

