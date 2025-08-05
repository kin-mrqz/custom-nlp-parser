TRAIN_DATA = [
    # Pairing
    ("What wine should I drink with grilled salmon?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("Can you suggest a wine to go with mushroom risotto?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("Which wine pairs best with spicy Thai curry?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("I'm having roast beef tonight; what wine do you recommend?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("What wine goes well with a Caesar salad?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("Suggest a wine to serve with lobster thermidor.", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("Which wine should I pair with spaghetti carbonara?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),

    # Similar
    ("I really liked Châteauneuf-du-Pape. What other wines are similar?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("What wines are like Amarone della Valpolicella?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Can you recommend something similar to a Napa Valley Cabernet?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("I enjoyed a bottle of Priorat recently. What should I try next?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Looking for wines with a similar profile to Rioja Reserva.", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Give me alternatives to Pouilly-Fumé.", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("I liked the minerality of a Chablis — what else should I try?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),

    # Description
    ("What's the flavor profile of a Barolo?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("Can you describe the taste of Gewürztraminer?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("What does a Sancerre typically taste like?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("Tell me about the body and aroma of Syrah.", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("What kind of notes should I expect from a Viognier?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("Is Pinot Noir usually earthy or fruity?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),

    ("What kind of meat goes well with a full-bodied Shiraz?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("Which dessert should I serve with Moscato d’Asti?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("I'm opening a bottle of Grenache — what dinner would complement it?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("Suggest a lunch dish that pairs nicely with Pinot Blanc.", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("What cheese should I have with a Merlot?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("Which foods enhance the flavor of a dry Riesling?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("I'm serving grilled tuna — which wine should I open?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("What wine should I pair with mushroom ravioli?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("Can you recommend a wine that complements spicy Sichuan cuisine?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("What's the ideal wine for grilled halloumi and veggies?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),

    ("I liked a bottle of Mencia — what similar wines do you suggest?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Looking for wines with a similar style to Vouvray.", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Suggest something close to a Rioja Crianza.", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Any recommendations like a good Alsace Riesling?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("What else might I enjoy if I liked a Nero d'Avola?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Wines similar to Brunello di Montalcino?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("I enjoy the richness of Zinfandel. What else compares?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Looking for something that reminds me of Torrontés.", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("What’s a good wine with the same fruitiness as Lambrusco?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("I liked the acidity in Txakoli — got anything else like it?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),

    ("What’s the typical flavor of a Nebbiolo?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("Describe the aroma profile of Torrontés.", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("Does a Viognier tend to be sweet or dry?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("How would you describe the mouthfeel of Barbera?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("Tell me about the acidity and tannins in Tannat.", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("What kind of flavors are found in Orange wines?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("Is Grüner Veltliner typically herbaceous or citrusy?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("Describe the typical body and texture of Chardonnay from Burgundy.", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("What does a young Barolo taste like compared to an aged one?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("Tell me if a dry Muscat has floral notes.", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}})
]


NEW_TRAIN_DATA = [
    # pairing
    ("What wine would you recommend with foie gras served during a tasting menu?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("Which wine pairs well with duck à l’orange and roasted root vegetables?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("I'm making creamy mushroom risotto — what bottle should I open?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("Suggest a wine for grilled octopus with lemon and paprika.", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("Hosting a brunch with smoked salmon bagels — wine ideas?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("What would go well with a black truffle pasta?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),
    ("I'm serving beef Wellington — what wine should I pour?", {"cats": {"pairing": 1.0, "similar": 0.0, "description": 0.0}}),


    # similar
    ("Do you have a wine that is similar to Andre Beaufort Non Dose Potion x Tregalli, Champagne 2020?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Looking for a wine like Clos Rougeard Saumur-Champigny, ideally under $100.", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Can you recommend something close to a Domaine Tempier Bandol Rosé from 2021?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("I want a wine similar in flavor to a 2018 Tignanello, but less expensive.", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Suggest an alternative to Selbach-Oster Zeltinger Sonnenuhr Riesling Spätlese under 30 euros.", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Can you help me find a wine with a similar profile to the 2020 Gaja Barbaresco but from Chile?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("I'm searching for a substitute for a 2015 Château Pichon Baron with a lighter body.", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),
    ("Any suggestions similar to the Billecart-Salmon Brut Rosé Champagne but non-vintage?", {"cats": {"pairing": 0.0, "similar": 1.0, "description": 0.0}}),

    # description
    ("Describe Andre Beaufort Non Dose Potion x Tregalli, Champagne 2020.", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("What’s the taste profile of the 2020 Champagne from Andre Beaufort (Potion x Tregalli)?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("Can you tell me what the André Beaufort Non Dosé Potion x Tregalli tastes like?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("I want to know the characteristics of Champagne Potion x Tregalli 2020.", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("How would you describe the flavor and aroma of the 2020 Non Dosé Potion x Tregalli by André Beaufort?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("Give me a tasting note for Andre Beaufort’s Potion x Tregalli Champagne.", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("What's the nose and palate like for the 2020 Potion x Tregalli?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}}),
    ("What should I expect from the mouthfeel and finish of Potion x Tregalli 2020 Champagne?", {"cats": {"pairing": 0.0, "similar": 0.0, "description": 1.0}})

]