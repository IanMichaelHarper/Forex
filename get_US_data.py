import quandl as q

codes = ["ISM/MAN_PMI", 
        "ISM/NONMAN_NMI" 
#        "UMICH/SOC1", 
        # no free BP, but quandl has this data for 200+ countries. Think I need an account
#        "FED/M2_M",  # quandl has data here for other countries
#        "FED/RIFSPFF_N_M",  # monthly fed funds, quandl has daily rates too (more up to date)        
#        "FRED/CPIAUCSL", 
#        "FRED/CPIAUCSL",
         "FRED/WPSFD49207",  # PPI finished goods
         "FRED/WPSFD4131",  # PPI finished goods less foods and energy
#        "FRED/PAYEMS",  # Non Farm Payrolls NFP
#        "FRED/FYGDP", # GDP
#        "FRED/GFDEBTN", #  Total Public Debt
#        "FRED/GFDEGDQ188S", # Debt to GDP
#        "FRED/FYFSGDA188S", # Surplus deficit as a % of GDP
#        "FRED/FYOINT", #  Outlays: Interest (interest bill)
#        "FRED/FYONET", #  Outlays: Net 
#        "FRED/FYFR", #  Receipts
#        "FRED/WGS10YR", # 10-year Treasury Bond interest rate
#        "FRED/WALCL", # Fed Balance Sheet
#        "FRED/A191RL1Q225SBEA" # Real GDP % Growth
]

for code in codes:
    data = q.get(code)
    data.to_csv(code.split('/')[1] + ".csv", index=False)
