# 🍷 Wine & Food NLP with spaCy

This project builds two lightweight NLP models using [spaCy](https://spacy.io) for handling natural language queries related to wine and food. It supports:

- **Intent Classification**: Distinguish between wine or food recommendation queries.
- **Named Entity Recognition (NER)**: Extract key details like wine name, price, and tasting descriptions.

---
<br>

### Text Classification Model (Intent Detection)
Example Inputs:
- “Recommend a red wine under 300 HKD that pairs with grilled lamb.” → recommend_wine
- “What should I cook for dinner to go with a chilled bottle of Sancerre?” → recommend_food


Output Example
- {'recommend_wine': 0.01, 'recommend_food': 0.99}
<br>

---
<br>

### Named Entity Recognition (NER) Model
Extracted Fields:
- wine_name: “Silver Oak 2019”
- price: “$120”
- description_phrase: “vanilla and cherries”

Output Example
- wine_name : 2020 Opus One
- price : $299
- description_phrase : chocolate, spice, and tobacco

---

**Quick Notes**: 
- A problem you will likely encounter when training a NER with multiple labels is the quality of annotations
- Annotation indices (i.e., start index and end index) should match with the start and end indices of the token/s
- For example, "Try Château Margaux for $350." "Château Margaux" has a valid token span from start=4 to end=19. An error would occur if you try to index end=18.
- Remember this when generating training data using LLMs, as they are prone to inaccurate indexing. Use Prodigy to help label your training data
