from box import Box

START_URL = {
    "CommercialBankShare": Box({
        "file_locaion" : {
            "W":"../../../../../data/commercialBank/weekly.json",
            "M": "../../../../../data/commercialBank/monthly.json",
            "Y": "../../../../../data/commercialBank/yearly.json"
        },
        "links": [ 
        {"value": 131, "symbol": "NABIL", "name": "Nabil Bank"},
        { "value": 238, "symbol": "NMB", "name": "NMB Bank"},
        {"name": "Prime Commercial Bank Ltd.", "symbol": "PCBL","value": 357 },
        {"name": "Sanima Bank Limited", "symbol": "SANIMA", "value": 171},
        {"name": "Siddhartha Bank Limited", "symbol": "SBL", "value": 145},
        {"name": "Standard Chartered Bank Limited", "symbol": "SCB", "value": 133},
        {"name": "Sunrise Bank Limited", "symbol": "SRBL", "value": 359},
        {"name": "Corporate Development Bank Limited", "symbol": "CORBL", "value" : 450},
        ]})
}
