TRAIN_DATA = [
    ("What wine goes well with spicy Thai green curry?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Suggest a red wine under 300 HKD that pairs with grilled lamb.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("I have a bottle of Amarone — what foods would pair well with it?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("What should I cook for dinner to go with a chilled bottle of Sancerre?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Suggest a celebratory wine that works with oysters and has high acidity.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("I'm cooking mushroom risotto and want something medium-bodied and earthy to go with it.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Pair a bold Napa Cabernet Sauvignon with sushi.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("What are the best dishes to serve with a 2020 Puligny-Montrachet Chardonnay?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Can you suggest a full-course meal to go with a vintage Champagne?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("What kind of food works well with a sweet Riesling from Mosel?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}})
]

NEW_TRAIN_DATA = [
    # recommend_wine intents
    ("I have this wine Blank Canvas Wines Settlement Vineyard Pinot Noir Marlborough 2020. Find me a wine similar to this.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Can you recommend a wine like the Catena Zapata Malbec Argentino?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Looking for something close to the 2015 Sassicaia — any ideas?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Suggest a red wine that tastes like a Barolo but costs less.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Had a glass of Tavel rosé recently — anything else similar?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Find me a white wine in the same style as Cloudy Bay Sauvignon Blanc.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("I really enjoyed a Tempranillo from Rioja — got a similar one?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("What’s a good alternative to Veuve Clicquot for Champagne?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Give me a wine recommendation that's close to a Napa Cabernet.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Anything like that Brunello I had last month? Rich and earthy.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    
    # recommend_food intents
    ("I had beef bourguignon recently. Can you suggest something similar to cook?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Loved my last mushroom risotto — any related dishes I should try?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Suggest a dish like Thai green curry but less spicy.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Looking for something similar to shrimp scampi for dinner tonight.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Had a great time with lamb tagine — any similar recipes?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Give me food ideas similar to coq au vin.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("I made shakshuka last weekend. What else is in that flavor profile?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Want to try something like chicken tikka masala but vegetarian.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Find me a pasta dish that's similar to carbonara.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Can you recommend a dessert like lemon tart but less tangy?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),

    # Multi-turn queries
    ("Similar to what I had yesterday — a dry red from Bordeaux.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Like the pasta I made last night with mushrooms — got a twist on it?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Remember that Pinot I mentioned? Something in that vein.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("That chicken dish we talked about — got a variant or similar recipe?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Yeah, like the one I paired with Chardonnay last week.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),

    # Indirect phrasing
    ("Reminds me of something I liked — can you help find it?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("That dish had a vibe I liked — know anything in that direction?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Looking for that kind of flavor again.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Wine like that — but maybe a bit fruitier this time.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Food-wise, can we do a remix of what I had with Riesling?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),


    # recommend_wine intents
    ("Describe Andre Beaufort Non Dose Potion x Tregalli, Champagne 2020.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Can you tell me what the 2020 Potion x Tregalli Champagne by Andre Beaufort is like?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("What does a bottle of 2020 Selbach-Oster Zeltinger Sonnenuhr Riesling Spätlese taste like?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("What's the flavor profile of Domaine Huet Vouvray Le Mont Demi-Sec?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("I’m curious about the taste of 2015 Château Rayas Châteauneuf-du-Pape — what can I expect?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("How would you describe the mouthfeel of a vintage Bollinger R.D. Brut?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Is Cloudy Bay Sauvignon Blanc citrusy or more herbal?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("What are the tasting notes for a 2012 Tignanello?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Tell me about the bouquet and finish of Vega Sicilia Unico 2009.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("How aromatic is a 2021 Château d’Esclans Whispering Angel rosé?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    
    # recommend_food intents
    ("Can you describe the flavor of a Thai green curry?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("What's the taste profile of beef bourguignon?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Tell me about the texture and flavor of burrata cheese.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Is a traditional Coq au Vin rich or tangy?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("What makes a Neapolitan pizza distinct in taste?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Describe the spices and flavors in a Moroccan lamb tagine.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("What does a goat cheese tart with caramelized onions taste like?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("How sweet is a traditional Basque cheesecake?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("What's the flavor difference between ramen tonkotsu and shoyu?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Can you explain what a proper risotto alla Milanese tastes like?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}})

]


# Updated 08/05/2025
NEW_TRAIN_DATA = [
    # recommend_wine intents
    ("Can you recommend wine for spicy Indian curry?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Suggest wine for a seafood paella.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Which wine goes well with beef stew?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("I need a wine to pair with roasted duck.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("What wine should I serve with sushi?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Wine recommendation for grilled salmon?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("What wine goes with pork belly?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Wine to drink with a cheese platter?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Recommend wine for lasagna night.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Wine pairing for lamb chops?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Wine that goes with spicy Thai noodles?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Which wine should I pair with veal?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Suggest wine for a vegetarian curry.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Can you recommend wine for roasted vegetables?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("What wine works with spicy barbecue?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Wine to consume with mushroom risotto?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Which wine goes best with chili con carne?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("What wine should I pair with crab cakes?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Wine for a fancy steak dinner?", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),
    ("Recommend me some wine for gnocchi in tomato sauce.", {"cats": {"recommend_wine": 1.0, "recommend_food": 0.0}}),

    # recommend_food intents
    ("What food pairs well with Pinot Noir?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Suggest food for a bottle of Rioja.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Can you recommend food to go with Syrah?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("What dish should I serve with sparkling wine?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Food recommendation for Chardonnay?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("What to eat with a dry Riesling?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Dish for wine: Amarone.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Meal for wine tasting night?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Which food goes with Cabernet Sauvignon?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Suggest food for Merlot.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Can you recommend food to pair with white Burgundy?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("What food works with a bold red wine?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Food to pair with a chilled rosé?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Recommend food with sparkling rosé.", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("What food that goes with Tempranillo?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Which dish pairs well with Sancerre?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Food for serving with Bordeaux?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Food pairing for Barolo night?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("What meal works with Malbec?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}}),
    ("Can you recommend food for a Zinfandel?", {"cats": {"recommend_wine": 0.0, "recommend_food": 1.0}})
]