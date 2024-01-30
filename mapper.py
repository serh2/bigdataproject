#!/usr/bin/env python

import sys
import re

# Fonction pour supprimer les balises HTML
def remove_html_tags(text):
    clean = re.compile('<.*?>')
    return re.sub(clean, '', text)

# Liste de stopwords (à adapter selon vos besoins)
stopwords = set(["the", "and", "or", ...])

for line in sys.stdin:
    # Suppression des balises HTML
    tweet = line.strip().split(',')[1]  # Assumant que la colonne 2 contient les tweets
    tweet = remove_html_tags(tweet)
    
    # Tokenization et suppression des stopwords
    words = tweet.split()
    for word in words:
        word = word.lower()
        if word not in stopwords:
            print(word + "\t1")
