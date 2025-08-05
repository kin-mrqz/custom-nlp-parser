# Training data for NER
TRAIN_DATA = [
    ("Can you recommend a red wine under $40 for a dinner party?",
     {"entities": [
         (20, 23, "wine_type"),          # "red"
         (36, 38, "max_price")           # "$40"
     ]}),

    ("I need a white wine priced above 20 USD for seafood.",
     {"entities": [
         (9, 14, "wine_type"),          # "white"
         (33, 35, "min_price")           # "20 USD"
     ]}),

    ("Looking for Champagne or Prosecco to celebrate a birthday.",
     {"entities": [
         (12, 21, "wine_name"),          # "Champagne"
         (25, 33, "wine_name")           # "Prosecco"
     ]}),

    ("Suggest a wine under $25 that goes well with grilled chicken.",
     {"entities": [
         (22, 24, "max_price")           # "$25"
     ]}),

    ("Is there a full-bodied red under 100 HKD?",
     {"entities": [
         (23, 26, "wine_type"),          # "red"
         (33, 36, "max_price")           # "100 HKD"
     ]}),

    ("I’m in the mood for an oaked Chardonnay.",
     {"entities": [
         (29, 39, "wine_name")           # "oaked Chardonnay"
     ]}),

    ("Any bold Syrah or Malbec options for under $60?",
     {"entities": [
         (9, 14, "wine_name"),           # "Syrah"
         (18, 24, "wine_name"),          # "Malbec"
         (44, 46, "max_price")           # "$60"
     ]}),

    ("Looking for a wine that costs at least 30 USD, preferably red.",
     {"entities": [
         (39, 41, "min_price"),          # "30 USD"
         (58, 61, "wine_type")           # "red"
     ]}),

    ("I’d like a sparkling wine around 50 dollars.",
     {"entities": [
         (11, 20, "wine_type"),          # "sparkling wine"
         (33, 35, "max_price")           # "50 dollars"
     ]}),

    ("Do you have a Pinot Noir or Merlot from California?",
     {"entities": [
         (14, 24, "wine_name"),          # "Pinot Noir"
         (28, 34, "wine_name")           # "Merlot"
     ]}),


    ("I'm looking for a red wine under 300 HKD.",
     {"entities": [
         (18, 21, "wine_type"), 
         (33, 36, "max_price")
    ]}),

    ("Can you recommend a sparkling wine below 500 dollars?",
     {"entities": [
         (20, 29, "wine_type"), 
         (41, 44, "max_price")
    ]}),

    ("Do you have any white wines cheaper than 250?",
     {"entities": [
         (16, 21, "wine_type"), 
         (41, 44, "max_price")
    ]}),

    ("Suggest a wine between 200 and 600 HKD.",
     {"entities": [
         (23, 26, "min_price"), 
         (31, 34, "max_price")
    ]}),

    ("I'd like a bottle of Amarone priced around 800.",
     {"entities": [
         (21, 28, "wine_name"), 
         (43, 46, "max_price")
    ]}),

    ("Looking for a full-bodied red wine priced over 1000.",
     {"entities": [
         (26, 29, "wine_type"), 
         (47, 51, "min_price")
    ]}),

    ("Can I get a nice white wine for about 400 HKD?",
     {"entities": [
         (17, 22, "wine_type"), 
         (38, 41, "max_price")
    ]}),

    ("Need a dry Riesling that costs at most 350.",
     {"entities": [
         (39, 42, "max_price")
    ]}),

    ("Show me wines from 150 to 700.",
     {"entities": [
         (19, 22, "min_price"), 
         (26, 29, "max_price")
    ]}),

    ("Is there a good sparkling option under 1,200?",
     {"entities": [
         (16, 25, "wine_type"), 
         (39, 45, "max_price")
    ]}),

    ("Looking for a Pinot Noir priced between 300 and 800.",
     {"entities": [
         (14, 24, "wine_name"), 
         (40, 43, "min_price"), 
         (48, 51, "max_price")
    ]}),

    ("I'd like a wine that costs more than 600 dollars.",
     {"entities": [
         (37, 40, "min_price")
    ]}),

    ("Can I find something below 200?",
     {"entities": [
         (27, 30, "max_price")
    ]}),

    ("What's a good wine in the 100 – 500 HKD range?",
     {"entities": [
         (26, 29, "min_price"), 
         (32, 35, "max_price")
    ]}),

    ("I want a Burgundy under 900.",
     {"entities": [
         (9, 17, "wine_name"), 
         (24, 27, "max_price")
    ]}),

    ("What sparkling wine goes well with spicy Thai green curry with coconut milk?",
        {"entities": [
        (5, 14, "wine_type"),                    # "wine"
    ]}),

    ("Recommend a red wine under HKD 300 that pairs well with grilled lamb and comes from Spain",
        {"entities": [
        (12, 15, "wine_type"),                 # "red"
        (31, 34, "max_price"),                 # "300"
    ]}),
    
    ("Suggest a celebratory wine under HKD 400 that works with oysters and has high acidity.",
        {"entities": [
        (37, 40, "max_price"),                 # "300"
    ]}),

    ("I'm cooking mushroom risotto and want something above 700 medium-bodied and earthy to go with it.",
        {"entities": [
            (54, 57, "min_price"),                 # "300"

        ]}),

    ("Pair a bold Napa Cabernet Sauvignon between HKD 300 and 500 HKD with sushi.",
     {"entities": [
        (12, 35, "wine_name"),                  # "Napa Cabernet Sauvignon"
        (48, 51, "min_price"),                 # "300"
        (56, 59, "max_price"),                 # "300"
        ]})
]

NEW_TRAIN_DATA = [
    ("I'm looking for a red wine under 300 HKD.",
     {"entities": [
         (18, 21, "wine_type"), 
         (33, 36, "max_price")
    ]}),

    ("Can you recommend a sparkling wine below 500 dollars?",
     {"entities": [
         (20, 29, "wine_type"), 
         (41, 44, "max_price")
    ]}),

    ("Do you have any white wines cheaper than 250?",
     {"entities": [
         (16, 21, "wine_type"), 
         (41, 44, "max_price")
    ]}),

    ("Suggest a wine between 200 and 600 HKD.",
     {"entities": [
         (23, 26, "min_price"), 
         (31, 34, "max_price")
    ]}),

    ("I'd like a bottle of Amarone priced around 800.",
     {"entities": [
         (21, 28, "wine_name"), 
         (43, 46, "max_price")
    ]}),

    ("Looking for a full-bodied red wine priced over 1000.",
     {"entities": [
         (26, 29, "wine_type"), 
         (47, 51, "min_price")
    ]}),

    ("Can I get a nice white wine for about 400 HKD?",
     {"entities": [
         (17, 22, "wine_type"), 
         (38, 41, "max_price")
    ]}),

    ("Need a dry Riesling that costs at most 350.",
     {"entities": [
         (39, 42, "max_price")
    ]}),

    ("Show me wines from 150 to 700.",
     {"entities": [
         (19, 22, "min_price"), 
         (26, 29, "max_price")
    ]}),

    ("Is there a good sparkling option under 1,200?",
     {"entities": [
         (16, 25, "wine_type"), 
         (39, 45, "max_price")
    ]}),

    ("Looking for a Pinot Noir priced between 300 and 800.",
     {"entities": [
         (14, 24, "wine_name"), 
         (40, 43, "min_price"), 
         (48, 51, "max_price")
    ]}),

    ("I'd like a wine that costs more than 600 dollars.",
     {"entities": [
         (37, 40, "min_price")
    ]}),

    ("Can I find something below 200?",
     {"entities": [
         (27, 30, "max_price")
    ]}),

    ("What's a good wine in the 100 – 500 HKD range?",
     {"entities": [
         (26, 29, "min_price"), 
         (32, 35, "max_price")
    ]}),

    ("I want a Burgundy under 900.",
     {"entities": [
         (9, 17, "wine_name"), 
         (24, 27, "max_price")
         ]}),
]
