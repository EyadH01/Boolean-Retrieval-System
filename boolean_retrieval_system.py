Created on Thu May 23 21:51:53 2024

@author: Eyad Harb
"""

from collections import defaultdict
from math import log


def tokenize(text):
 """
 Preprocesses text by removing stop words, stemming, and converting to lowercase.

 Args:
  text: The text to preprocess.

 Returns:
  A list of preprocessed tokens.
 """
 stop_words = set([ # Add common stop words here (e.g., "the", "a", "is")
  "the", "a", "is", "of", "and", "to", "in", "on", "for", "with", "as", "by"
 ])
 # Use a stemming library (e.g., NLTK) for stemming
 from nltk.stem import PorterStemmer # Import stemming library
 stemmer = PorterStemmer()
 return [stemmer.stem(word.lower()) for word in text.split() if word not in stop_words]


def calculate_tf_idf(documents):
 """
 Calculates TF-IDF scores for each term in each document.

 Args:
  documents: A dictionary where keys are doc_ids and values are document texts.

 Returns:
  A dictionary where keys are terms and values are dictionaries with doc_id as key and TF-IDF score as value.
 """
 tf_idf = defaultdict(dict)
 total_documents = len(documents)
 for doc_id, text in documents.items():
  word_count = {}
  for word in tokenize(text):
   word_count[word] = word_count.get(word, 0) + 1
  for word, count in word_count.items():
   tf = count / sum(word_count.values()) # Term Frequency
   # Avoid division by zero by adding 1 to the denominator
   idf = log(total_documents / (1 + sum(doc.get(word, 0) for doc in documents.values()))) # Inverse Document Frequency
   tf_idf[word][doc_id] = tf * idf
 return tf_idf


def search(query, documents, tf_idf):
 """
 Ranks documents based on their TF-IDF similarity to the query.

 Args:
  query: The user query.
  documents: A dictionary where keys are doc_ids and values are document texts.
  tf_idf: A dictionary containing TF-IDF scores for each term.

 Returns:
  A list of doc_ids ranked by their similarity to the query.
 """
 query_terms = tokenize(query)
 query_tfidf = {term: tf_idf.get(term, {}).get(doc_id, 0) for doc_id in documents for term in query_terms}
 doc_scores = {doc_id: sum(score for term, score in query_tfidf.items() if doc_id in tf_idf.get(term, {})) for doc_id in documents}
 return sorted(doc_scores, key=doc_scores.get, reverse=True)


# Example usage
documents = {
 1: "Artificial intelligence is a branch of computer science",
 2: "Machine learning is a subfield of artificial intelligence",
 3: "Natural language processing is a technique for computers to understand human language",
}

tf_idf = calculate_tf_idf(documents)
query = "machine learning natural language processing"
ranked_documents = search(query, documents, tf_idf)

print("Ranked documents based on TF-IDF:")
for doc_id in ranked_documents:
 print(f" - Document {doc_id}: {documents[doc_id]}")
