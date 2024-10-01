

![StockSnap_ZMINJHNLV1](https://github.com/talha469/ProjectNLP2023/assets/59912447/47117a45-eaad-4260-9ac1-59f2e68e9003)


# Poetry Analysis Using NLP
GitHub repository for the semester project of NLP

## Instructions for Running the Code
1. Clone the repository
   ```bash
     git clone https://github.com/talha469/ProjectNLP2023.git
   ```
2. Install all required libraries and models by running the following command:
   ```bash
      pip install -r requirements.txt
    ```
3. Run the code in the respective task folder to perform specific tasks (organized by task number). Each folder contains the relevant script for the analysis you wish to execute.

# Poetry Analysis Using NLP

This project explores the use of Natural Language Processing (NLP) techniques to analyze various aspects of poetry, including styles, rhymes, emotions, and linguistic patterns, by leveraging a corpus from the Gutenberg e-book collection.

## Project Overview

This project applies NLP algorithms to poetry data to uncover patterns, similarities, and emotions within the text. Our goal is to automate the analysis of poetic structures and understand the nuanced relationships between linguistic elements. We utilized a variety of well-established NLP libraries and tools such as `NLTK`, `FastText`, `Gensim`, and `SentiWordNet`, along with Python-based tools like `Matplotlib`, `Seaborn`, and `Pandas` for data visualization and manipulation.

### Key Features:
- **Text Preprocessing**: Tokenization, stopword removal, stemming, and frequency distribution analysis.
- **Similarity Analysis**: Computation of Jaccard and Resnik similarity measures to assess commonality between words and topics.
- **Sentiment Analysis**: Using `SentiWordNet` to evaluate positive and negative sentiments in poetry.
- **Lexical Diversity**: Analysis of the richness and variety of vocabulary in poems using the Type-Token Ratio (TTR).
- **Named Entity Recognition (NER)**: Extracting and analyzing named entities such as people, places, and organizations within the poems.
- **Phonetic and Syllable Analysis**: Phonetic similarity measurement using the `Jellyfish` library, and syllable counting using the `Pyphen` library.
- **Statistical Analysis**: Computation of mean, standard deviation, and kurtosis to evaluate various statistical attributes of poems.
- **Topic Modeling**: Application of Latent Dirichlet Allocation (LDA) to uncover underlying topics within the poems.

## Methodology

The following steps were performed in the analysis:

1. **Preprocessing**: The text data was tokenized, cleaned by removing stopwords, and normalized using stemming. Word frequencies were calculated, and the top 100 words from the poems were identified.
   
2. **Similarity Analysis**: We calculated the Jaccard and Resnik similarities between sets of words from the poems, providing insights into how similar the language and themes of different poems or chapters are.
   
3. **Sentiment and Pronoun Analysis**: Sentiment analysis was performed using `SentiWordNet` to gauge the emotional tone of each poem. Pronoun usage and its distribution were also examined to provide insights into narrative perspectives.
   
4. **Lexical Diversity**: Lexical diversity was measured using the Type-Token Ratio (TTR) and parts of speech tagging to analyze the richness and variation of vocabulary in the poems.
   
5. **Phonetic and Syllable Analysis**: We explored phonetic similarities between words using the `Jellyfish` library and performed syllable counting for the top 100 most frequent words in each poem.
   
6. **Named Entity Recognition**: NER was applied to identify key persons, locations, and organizations mentioned in the poems, providing further context to the text.
   
7. **Statistical Analysis**: Statistical measures such as mean, standard deviation, and kurtosis were computed on word repetition, sentence lengths, and chapter boundaries, helping to identify patterns in the text.
   
8. **Topic Modeling**: Latent Dirichlet Allocation (LDA) was used to model and visualize the topics found within the poems, revealing thematic coherence across chapters and lines.

## Libraries Used
- [NLTK](https://www.nltk.org/): Natural Language Toolkit for text processing.
- [Gensim](https://radimrehurek.com/gensim/): Topic modeling and document similarity.
- [FastText](https://fasttext.cc/): Word embeddings and text representation.
- [Matplotlib](https://matplotlib.org/): Visualization library for graphs and plots.
- [Seaborn](https://seaborn.pydata.org/): Statistical data visualization.
- [Pandas](https://pandas.pydata.org/): Data manipulation and analysis.
- [SentiWordNet](https://sentiwordnet.isti.cnr.it/): Lexical resource for sentiment analysis.
- [Spacy](https://spacy.io/): Named Entity Recognition and linguistic features.
- [Pyphen](https://pyphen.org/): Syllable counting in words.
- [Jellyfish](https://github.com/jamesturk/jellyfish): Phonetic similarity computation.

## Results

The project provides several key insights into the analysis of poetic structures:
- **Word Frequency**: Identification of the top 100 most frequent words across poems.
- **Sentiment Distribution**: Histogram analysis of positive and negative sentiments within poems.
- **Phonetic Similarity**: Measurement of phonetic similarities between word pairs using edit distance algorithms.
- **Lexical Diversity**: Visualization of lexical richness and how it varies across different parts of the poem.
- **Named Entity Distribution**: A breakdown of named entities found within the poems.

## Future Work

Future extensions of this project may include:
- Improving the chapter division logic by incorporating deep learning models.
- Creating a general end-to-end solution for poetry analysis in industry, enabling more detailed sentiment, thematic, and structural analysis.
- Developing a user-friendly website or application to analyze any text based on the methods discussed in this project.

## References

A comprehensive list of references and scholarly works used in this project can be found in the `references/` folder.

## Authors
- Muhammad Ahmed (2304796)
- Muhammad Talha Arshad (2304797)
- Saim (2307271)

[GitHub Repository](https://github.com/talha469/ProjectNLP2023)
