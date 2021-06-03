from box import Box

START_URL = {
    "CommercialBankShare": Box({
        "file_location" : {
            "W":"../../../../../data/commercialBank/weekly.json",
            "M": "../../../../../data/commercialBank/monthly.json",
            "Y": "../../../../../data/commercialBank/yearly.json",
            "Q": "../../../../../data/commercialBank/quaterly.json",
            "D": "../../../../../data/commercialBank/daily.json"
        },
        "links": [ 
            {"name": "Agriculture Development Bank Limited", "symbol": "ADBL", "value": 397},
            {"name": "Bank of Kathmandu Ltd", "symbol": "BOKL", "value": 138},
            {"name": "Century Commercial Bank Ltd", "symbol": "CCBL", "value": 605},
            {"name": "Citizen Bank International Limited", "symbol": "CZBIL", "value": 348},
            {"name": "Civil Bank Ltd", "symbol":"CBL", "value": 532},
            {"name":"Everest Bank Limited", "symbol": "EBL", "value": 137},
            {"name": "Global IME Bank Limited", "symbol": "GBIME", "value": 341},
            {"name": "Himalayan Bank Limited", "symbol": "HBL", "value": 134}, 
            {"name": "Kumari Bank Limited", "symbol": "KBL", "value": 142},
            {"name": "Laxmi Bank Limited", "symbol": "LBL", "value": 141},
            {"name": "Machhapuchhre Bank Limited", "symbol": "MBL", "value": 140},
            {"name": "Mega Bank Nepal Ltd", "symbol": "MEGA", "value": 562},
            {"name": "Nabil Bank Limited", "symbol": "NABIL", "value": 131},
            {"name": "Nepal Bangladesh Bank Limited", "symbol": "NBB", "value": 136},
            {"name": "Nepal Bank Limited", "symbol": "NBL", "value": 517},
            {"name": "Nepal Credit And Commercial Bank Limited", "symbol": "NCCB", "value": 144},
            {"name": "Nepal Investment Bank Limited", "symbol": "NIB", "value": 132},
            {"name": "Nepal SBI Bank Limited", "symbol": "SBI", "value": 135},
            {"name": "NIC Asia Bank Ltd", "symbol": "NICA", "value": 139},
            {"name": "NMB Bank Limited", "symbol": "NMB", "value": 238},
            {"name": "Prabhu Bank Limited", "symbol": "PRVU", "value": 255},
            {"name": "Prime Commercial Bank Ltd", "symbol": "PCBL", "value": 357},
            {"name": "Sanima Bank Limited", "symbol": "SANIMA", "value":171},
            {"name": "Siddhartha Bank Limited", "symbol": "SBL", "value": 145}, 
            {"name": "Standard Chartered Bank Limited", "symbol": "SCB", "value":133},
            {"name": "Sunrise Bank Limited", "symbol": "SRBL", "value": 359}
        ]}),
    "DevelopmentBank": Box({
        "file_location":{
            "W":"../../../../../data/developmentBank/weekly.json",
            "M": "../../../../../data/developmentBank/monthly.json",
            "Y": "../../../../../data/developmentBank/yearly.json",
            "Q": "../../../../../data/developmentBank/quaterly.json",
            "D": "../../../../../data/developmentBank/daily.json"
        },
        "links": [
            {"name": "Corporate Development Bank Limited", "symbol": "CORBL", "value": 450},
            {"name": "Deva Bikas Bank Limited", "symbol": "DBBL", "value": 311},
            {"name": "Excel Development Bank Ltd", "symbol": "EDBL", "value": 274},
            {"name": "Gandaki Bikas Bank Limited", "symbol": "GDBL", "value": 420},
            {"name": "Garima Bikas Bank Limited", "symbol": "GBBL", "value": 417},
            {"name": "Green Development Bank Ltd", "symbol": "GRDBL", "value": 2744},
            {"name": "Jyoti Bikas Bank Limited", "symbol": "JBBL", "value": 418},
            {"name": "Kamana Sewa Bikas Bank Limited", "symbol": "KSBBL", "value": 459}, 
            {"name": "Kanchan Development Bank Limited", "symbol": "KADBL", "value": 505},
            {"name": "Karnali Development Bank Limited", "symbol": "KRBL", "value": 428},
            {"name": "Lumbini Bikas Bank Ltd", "symbol": "LBBL", "value": 358},
            {"name": "Mahalaxmi Bikas Bank Ltd", "symbol": "MLBL", "value": 401},
            {"name": "Miteri Development Bank Limited", "symbol": "MDB", "value": 371},
            {"name": "Muktinath Bikas Bank Ltd", "symbol": "MNBBL", "value": 474},
            {"name": "Narayani Development Bank Limited", "symbol": "NABBC", "value": 172},
            {"name": "Nepal Community Development Bank Ltd", "symbol": "NCDB", "value": 598},
            {"name": "Sahara Bikas Bank Ltd", "symbol": "SHBL", "value": 625},
            {"name": "Sahayogi Bikas Bank Limited", "symbol": "SBBLJ", "value": 174},
            {"name": "Saptakoshi Development Bank Ltd", "symbol": "SAPDBL","value": 2860},
            {"name": "Shangrila Development Bank Ltd", "symbol": "SADBL","value": 472},
            {"name": "Shine Resunga Development Bank Ltd", "symbol": "SHINE", "value": 473},
            {"name": "Sindhu Bikash Bank Ltd", "symbol": "SINDU", "value": 561},
            {"name": "Tinau Mission Development Bank Limited", "symbol": "TMDBL", "value": 2855}
        ]}),
    "FinancialBankShare": Box({
        "file_location" : {
            "W":"../../../../../data/financialCompanies/weekly.json",
            "M": "../../../../../data/financialCompanies/monthly.json",
            "Y": "../../../../../data/financialCompanies/yearly.json",
            "Q": "../../../../../data/financialCompanies/quaterly.json",
            "D": "../../../../../data/financialCompanies/daily.json"
        },
        "links": [ 
            {"name": "Best Finance Company Ltd", "symbol": "BFC", "value": 227},
            {"name": "Capital Merchant Bank & Finance Co. Ltd", "symbol": "CMB", "value": 259},
            {"name": "Central Finance Co. Ltd", "symbol": "CFCL", "value": 245},
            {"name": "City Express Finance Co. Limited", "symbol": "CEFL", "value": 296},
            {"name": "Crystal Finance Ltd", "symbol": "CFL", "value": 361},
            {"name": "Goodwill Finance Co. Ltd", "symbol": "GFCL", "value": 232},
            {"name": "Guheshowori Merchant Bank & Finance Co. Ltd", "symbol": "GMFIL","value": 263},
            {"name": "Gurkhas Finance Ltd", "symbol": "GUFL", "value": 204},
            {"name": "ICFC Finance Limited", "symbol": "ICFC", "value": 273},
            {"name": "Janaki Finance Ltd", "symbol": "JFL", "value": 250},
            {"name": "Lalitpur Finance Ltd.", "symbol": "LFC", "value": 231},
            {"name": "Manjushree Finance Ltd", "symbol": "MFIL", "value": 516},
            {"name": "Multipurpose Finance Company Limited", "symbol": "MPFL", "value": 471},
            {"name": "Nepal Finance Ltd.", "symbol": "NFS", "value": 194},
            {"name": "Nepal Share Markets Ltd.", "symbol": "NSM", "value": 200},
            {"name": "Pokhara Finance Ltd", "symbol": "PFL", "value": 236},
            {"name": "ProgressiveFinance Limited", "symbol": "PROFL", "value": 338},
            {"name": "Reliance Finance Ltd.", "symbol": "RLFL", "value": 587},
            {"name": "Samriddhi Finance Company Limited", "symbol": "SFCL", "value":256},
            {"name": "Shree Investment Finance Co. Ltd.", "symbol": "SIFC", "value": 244},
            {"name": "Shrijana Finance (Bittaya Sanstha)", "symbol": "SFFIL", "value": 261},
            {"name": "Synergy Finance Ltd.", "symbol": "SYFL", "value": 249},
            {"name": "United Finance Ltd.", "symbol": "UFL", "value": 242}
        ]}),
    "MicroFinance": Box({
        "file_location": {
            "W":"../../../../../data/microfinance/weekly.json",
            "M": "../../../../../data/microfinance/monthly.json",
            "Y": "../../../../../data/microfinance/yearly.json",
            "Q": "../../../../../data/microfinance/quaterly.json",
            "D": "../../../../../data/microfinance/daily.json"
        },
        "links": [
            {"name": "Adhikhola Laghubitta Bittiya Sanstha Limited", "symbol": "AKBSL", "value": 2845},
            {"name": "Arambha Microfinance Bittiya Sanstha Ltd", "symbol": "AMFI", "value": 2777},
            {"name": "Asha Laghubitta Bittiya Sanstha Ltd", "symbol": "ALBSL", "value": 2807},
            {"name": "Chhimek Laghubitta Bittiya Sanstha Limited", "symbol": "CBBL", "value": 164},
            {"name": "Deprosc Laghubitta Bittiya Sanstha Limited", "symbol": "DDBL", "value": 166},
            {"name": "First Micro Finance Laghubitta Bittiya Sanstha Ltd.", "symbol": "FMDBL", "value": 490},
            {"name": "Kalika Laghubitta Bittiya Sanstha Limited", "symbol":"KMCDB", "value":593},
            {"name": "Nerude Laghubita Bikas Bank Limited", "symbol": "NLBBL", "value": 396},
            {"name": "Nirdhan Utthan Laghubitta Bittiya Sanstha Limited", "symbol": "NUBL", "value": 163},
            {"name": "RMDC Laghubitta Bittiya Sanstha Limited", "symbol": "RMDC", "value": 575},
            {"name": "Sana Kisan Bikas Laghubitta Bittiya sanstha Limited", "symbol": "SKBBL", "value": 574},
            {"name": "Swarojgar Laghubitta Bittiya Sanstha Ltd.", "symbol": "SLBBL", "value": 545},
            {"name": "Summit Laghubitta Bittiya Sanstha Ltd.", "symbol": "SMFDB", "value": 502},
            {"name": "Swabalamban Laghubitta Bittiya Sanstha Limited", "symbol": "SWBBL", "value":268},
            {"name": "Mithila Laghubitta Bittiya Sanstha Ltd.", "symbol": "MLBBL", "value":601},
            {"name": "Laxmi Laghubitta Bittiya Sanstha Ltd.", "symbol": "LLBS", "value": 618},
            {"name": "Mirmire Laghubitta Bittiya Sanstha Ltd.", "symbol": "MMFDB", "value": 682},
            {"name": "Janautthan Samudayic Laghubitta Bikas Bank Ltd.", "symbol": "JSLBB", "value": 695},
            {"name": "Womi Microfinance Bittiya Sanstha Ltd.", "symbol": "WOMI", "value": 706},
            {"name": "Vijaya laghubitta Bittiya Sanstha Ltd.", "symbol": "VLBS", "value": 687 },
            {"name": "RSDC Laghubitta Bittiya Sanstha Ltd.", "symbol": "RSDC", "value": 2748},
            {"name": "NMB Laghubitta Bittiya Sanstha Ltd.", "symbol": "NMBMF", "value": 704},
            {"name": "Meromicrofinance Laghubitta Bittiya Sanstha Ltd.", "symbol": "MERO", "value": 1741},
            {"name": "National Microfinance Laghubitta Bittiya Sanstha Ltd.", "symbol": "NMFBS", "value": 2746},
            {"name": "Suryodaya Laghubitta Bittiya Sanstha Ltd.", "symbol": "SLBS", "value": 2750},
            {"name": "Ganapati Microfinance Bittiya Sanstha Ltd", "symbol": "GMFBS", "value": 2815},
            {"name": "Civil Laghubitta Bittiya Sanstha Ltd.", "symbol": "CLBSL", "value": 693},
            {"name": "Infinity Laghubitta Bittiya Sanstha Limited", "symbol": "ILBS", "value": 2832},
            {"name": "Forward Microfinance Laghubitta Bittiya Sanstha Ltd", "symbol": "FOWAD", "value": 2758},
            {"name": "Samata Gharelu Laghubitta Bittiya Sanstha Limited", "symbol": "SMATA", "value": 2761},
            {"name": "Mahuli Laghubitta Bittiya Sanstha Ltd.", "symbol": "MSLB", "value": 2768},
            {"name": "Global IME Laghubitta Bittiya Sanstha Ltd.", "symbol": "GILB", "value": 705},
            {"name": "Support Microfinance Bittiya Sanstha Ltd.", "symbol": "SMB", "value": 2771},
            {"name": "Grameen Bikas Laghubitta Bittiya Sanstha Ltd.", "symbol": "GBLBS", "value": 583},
            {"name": "Mahila Laghubitta Bittiya Sanstha Limited", "symbol": "MLBSL", "value": 2925},
            {"name": "Gurans Laghubitta Bittiya Sanstha Limited", "symbol": "GLBSL", "value": 2826},
            {"name": "NIC Asia Laghubitta Biitiya Sanstha Limited", "symbol": "NICLBSL", "value": 2887},
            {"name": "Samudayik Laghubitta Bittiya Sanstha Limited", "symbol": "SLBSL", "value": 2804},
            {"name": "Sadhana Laghubitta Bittiya Sanstha Limited", "symbol": "SDLBSL", "value": 2896},
            {"name": "Swabhimaan Laghubitta Bittiya Sanstha Ltd", "symbol": "SMFBS", "value": 2829},
            {"name": "SABAIKO LAGHUBITTA BITTIYA SANSTHA LIMITED", "symbol": "SABSL", "value": 2843},
            {"name": "Aarambha Chautari Laghubitta Bittiya Sanstha Limited", "symbol": "ACLBSL", "value": 2790},
            {"name": "Unnati Sahakarya Laghubitta Bittiya Sanstha Limited", "symbol": "USLB", "value": 2774},
            {"name": "Sarathi Nepal Laghubitta Bittiya Sanstha Limited", "symbol": "SNLB", "value": 592},
            {"name": "Kisan Lagubitta Bittiya Sanstha Limited", "symbol": "KLBSL", "value": 694},
            {"name": "Meromicrofinance Laghubitta Bittiya Sanstha Limited Promoter Share", "symbol": "MEROPO", "value": 1742}
        ]
    }),
    "Hotel": Box({
        "file_location":{
            "W":"../../../../../data/hotel/weekly.json",
            "M": "../../../../../data/hotel/monthly.json",
            "Y": "../../../../../data/hotel/yearly.json",
            "Q": "../../../../../data/hotel/quaterly.json",
            "D": "../../../../../data/hotel/daily.json"
        },
        "links": [
            {"name": "Oriental Hotels Limited", "symbol": "OHL", "value": 149},
            {"name": "Soaltee Hotel Limited", "symbol": "SHL", "value": 147},
            {"name": "Taragaon Regency Hotel Limited", "symbol": "TRH", "value": 148},
            {"name": "Chandragiri Hills Limited", "symbol": "CGH", "value": 2917}
        ]
    }),
    "HydroPower": Box({
        "file_location": {
            "W":"../../../../../data/hydropower/weekly.json",
            "M": "../../../../../data/hydropower/monthly.json",
            "Y": "../../../../../data/hydropower/yearly.json",
            "Q": "../../../../../data/hydropower/quaterly.json",
            "D": "../../../../../data/hydropower/daily.json"
        },
        "links": [
            {"name": "Arun Valley Hydropower Development Co. Ltd.", "symbol": "AHPC", "value": 360 },
            {"name": "Butwal Power Company Limited", "symbol": "BPCL", "value": 153},
            {"name": "Chilime Hydropower Company Limited", "symbol": "CHCL", "value": 154},
            {"name": "National Hydro Power Company Limited", "symbol": "NHPC", "value": 152},
            {"name": "Sanima Mai Hydropower Ltd.", "symbol": "SHPC", "value": 591},
            {"name": "Ridi Hydropower Development Company Ltd.", "symbol": "RHPC", "value": 610},
            {"name": "Himalaya Urja Bikas Company Limited", "symbol": "HURJA", "value": 2824},
            {"name": "Arun Kabeli Power Ltd.", "symbol": "AKPL", "value": 2757 },
            {"name": "Barun Hydropower Co. Ltd.", "symbol": "BARUN", "value": 686},
            {"name": "Api Power Company Ltd.", "symbol": "API", "value": 697},
            {"name": "Ngadi Group Power Ltd.", "symbol": "NGPL", "value": 2743},
            {"name": "SANJEN JALAVIDHYUT COMPANY LIMITED", "symbol": "SJCL", "value": 2842},
            {"name": "RASUWAGADHI HYDROPOWER COMPANY LIMITED", "symbol": "RHPL", "value": 2841},
            {"name": "United Modi Hydropower Ltd.", "symbol": "UMHL", "value": 2760},
            {"name": "Dibyashwori Hydropower Ltd.", "symbol": "DHPL", "value": 2754}
        ]
    }),
    "LifeInsurance": Box({
        "file_location": {
            "W":"../../../../../data/lifeinsurance/weekly.json",
            "M": "../../../../../data/lifeinsurance/monthly.json",
            "Y": "../../../../../data/lifeinsurance/yearly.json",
            "Q": "../../../../../data/lifeinsurance/quaterly.json",
            "D": "../../../../../data/lifeinsurance/daily.json"
        },
        "links": [
            {"name": "Asian Life Insurance Co. Limited", "symbol": "ALICL", "value": 385},
            {"name": "Gurans Life Insurance Company Ltd.", "symbol": "GLICL", "value": 447},
            {"name": "Life Insurance Co. Nepal", "symbol": "LICN", "value": 188},
            {"name": "Nepal Life Insurance Co. Ltd.", "symbol": "NLIC", "value": 187},
            {"name": "National Life Insurance Co. Ltd.", "symbol": "NLICL", "value": 178},
            {"name": "Prime Life Insurance Company Limited", "symbol": "PLIC", "value": 393},
            {"name": "Surya Life Insurance Company Limited", "symbol": "SLICL", "value": 403},
            {"name": "Jyoti Life Insurance Company Limited", "symbol": "JLI", "value": 2929},
            {"name": "Reliance Life Insurance Company Limited", "symbol": "RLI", "value": 2900},
            {"name": "Prabhu Life Insurance Limited", "symbol": "PLI", "value": 2915},
        ]
    }),
    "NonLifeInsurance": Box({
        "file_location": {
            "W":"../../../../../data/nonlifeinstitution/weekly.json",
            "M": "../../../../../data/nonlifeinstitution/monthly.json",
            "Y": "../../../../../data/nonlifeinstitution/yearly.json",
            "Q": "../../../../../data/nonlifeinstitution/quaterly.json",
            "D": "../../../../../data/nonlifeinstitution/daily.json"
        },
        "links": [
            {"name": "Everest Insurance Co. Ltd.", "symbol": "EIC", "value": 181},
            {"name": "Himalayan General Insurance Co. Ltd", "symbol": "HGI", "value": 179},
            {"name": "Lumbini General Insurance Co. Ltd.", "symbol": "LGIL", "value": 190},
            {"name": "Nepal Insurance Co. Ltd.", "symbol": "NICL", "value": 176},
            {"name": "Neco Insurance Co. Ltd.", "symbol": "NIL", "value": 183},
            {"name": "NLG Insurance Company Ltd.", "symbol": "NLG", "value": 559},
            {"name": "Premier Insurance Co. Ltd.", "symbol": "PIC", "value": 182 },
            {"name": "Prudential Insurance Co. Ltd.", "symbol": "PICL", "value": 189},
            {"name": "Sagarmatha Insurance Co. Ltd.", "symbol": "SIC", "value":185 },
            {"name": "Shikhar Insurance Co. Ltd.", "symbol": "SICL", "value": 192},
            {"name": "Siddhartha Insurance Ltd.", "symbol": "SIL", "value": 280},
            {"name": "United Insurance Co. (Nepal) Ltd.", "symbol": "UIC", "value": 180 },
            {"name": "Prabhu Insurance Ltd.", "symbol": "PRIN", "value": 184},
            {"name": "Rastriya Beema Company Limited", "symbol": "RBCL", "value": 177},
            {"name": "IME General Insurance Ltd.", "symbol": "IGI", "value": 186},
            {"name": "AJOD Insurance Limited", "symbol": "AIL", "value":2893 },
            {"name": "Sanima General Insurance Company Limited", "symbol": "SGI", "value":2908 },
            {"name": "General Insurance Company Limited", "symbol": "GIC", "value": 2905}
        ]
    }),
    "Trading": Box({
        "file_location": {
            "W":"../../../../../data/trading/weekly.json",
            "M": "../../../../../data/trading/monthly.json",
            "Y": "../../../../../data/trading/yearly.json",
            "Q": "../../../../../data/trading/quaterly.json",
            "D": "../../../../../data/trading/daily.json"
        },
        "links": [
            {"name": "Bishal Bazar Company Limited", "symbol": "BBC", "value": 156},
            {"name": "Salt Trading Corporation", "symbol": "STC", "value": 155}
        ]
    }),
    "Manufacturing": Box({
        "file_location": {
            "W":"../../../../../data/manufacturing/weekly.json",
            "M": "../../../../../data/manufacturing/monthly.json",
            "Y": "../../../../../data/manufacturing/yearly.json",
            "Q": "../../../../../data/manufacturing/quaterly.json",
            "D": "../../../../../data/manufacturing/daily.json"
        },
        "links": [
            {"name": "Bottlers Nepal (Balaju) Limited", "symbol": "BNL", "value": 195},
            {"name": "Bottlers Nepal (Terai) Limited", "symbol": "BNT", "value": 213},
            {"name": "Himalayan Distillery Limited", "symbol": "HDL", "value": 235},
            {"name": "Nepal Lube Oil Limited", "symbol": "NLO", "value": 198 },
            {"name": "Shree Raghupati Jute Mills Limited", "symbol": "RJM", "value": 203},
            {"name": "Unilever Nepal Limited", "symbol": "UNL", "value": 219},
            {"name": "SHIVAM CEMENTS LTD", "symbol": "SHIVM", "value": 2809},
        ]
    })

}

