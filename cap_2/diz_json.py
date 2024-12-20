import json

d = { "PONumber" : 2608,
     "ShippingInstructions" : {"name" : "John Silver",
                               "Address" : { "street" : "426 Light Street",
                                            "city" : "South SAn Francisco",
                                            "state" : "CA",
                                            "zipCode" : 99237,
                                            "country" : "United States of  America"},
                               "Phone" : [{"type" : "Office", "number" : "809-123-9309"},
                                          {"type" : "Mobile", "number" : "417-123-4567"}
                                          ]
                               }
    
}

with open("po.json", "w") as outfile:
    json.dump(d,outfile)
