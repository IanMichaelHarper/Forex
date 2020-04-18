import quandl as q

codes = ["ISM/NONMAN_PMI", 
        "ISM/NONMAN_NMI", 
        "UMICH/SOC1", 
        # no free BP, but quandl has this data for 200+ countries. Think I need an account
        "FED/M2_M",  # quandl has data here for other countries
        "FED/RIFSPFF_N_M",  # monthly fed funds, quandl has daily rates too (more up to date)        
        "FRED/CPIAUCSL", 
        "FRED/CPIAUCSL", 

for code in codes:
    data = q.get(code)
    data.to_excel(code, index=False)
