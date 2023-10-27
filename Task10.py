
import nltk
from nltk.corpus import gutenberg
import fasttext.util
model = fasttext.load_model('cc.en.300.bin')

from gensim.models.fasttext import FastText
import numpy as np
import fasttext
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

blake_poems = gutenberg.raw("blake-poems.txt").encode('utf-8').decode('utf-8')

poem_lines = blake_poems.split('\n')
poem_lines = [line.strip() for line in poem_lines if line.strip()]


line_embeddings = []
matching_scores = []
chapter_boundaries = []

current_chapter = None
for i, line in enumerate(poem_lines):
    if line.isupper():
        if current_chapter is not None:
            chapter_boundaries.append(i - 1)
        current_chapter = line
    words = line.split()
    line_vector = np.mean([model[word] for word in words], axis=0)
    line_embeddings.append(line_vector)
    if i > 0:
        similarity = cosine_similarity([line_embeddings[i - 1]], [line_embeddings[i]])[0][0]
        matching_scores.append(similarity)

chapter_boundaries.append(len(poem_lines) - 1)

# Create a plot to visualize
plt.figure(figsize=(12, 6))
plt.plot(matching_scores, label="Matching Scores")
plt.xlabel("Successive Line Pairs")
plt.ylabel("Cosine Similarity")
plt.title("Coherence Evolution in the Poem")

for boundary in chapter_boundaries:
    plt.axvline(x=boundary, color='r', linestyle='--', label="Chapter Boundary")

plt.legend()
plt.show()
