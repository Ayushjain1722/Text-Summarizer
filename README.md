# Text-Summarizer
A webapp that summarizes the given text and returns the result.

## Steps involved:

1. Import libraries
2. Pre-processing the document
3. Convert all words to lower case and removing stopWords
4. Feature Extraction
  A. Sentence Features:

  Cue-Phrases like example, therefore, important, according to, etc.
  Numerical Data like dates, transactions, year, age, etc.
  Sentence Length like too long or too short sentence are of little worth
  Sentene Position like starting and ending sentences are of more importance
  
  B. Word Features:
  
  Word Frequency
  Upper Case
  Proper Noun
  Heading Match
5. Compiling all features to get the summary.
