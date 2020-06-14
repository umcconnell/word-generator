#!/usr/bin/env python
# coding: utf-8

# # Markov Word Generator

# Generate new words based on words from an input file. Uses markov chains to generate new words.
# Check out [wikipedia](https://en.wikipedia.org/wiki/Markov_chain) for more information.

# In[1]:


from collections import defaultdict
from random import choice


# Specify basic configuration.
# * `END` specifies special end character to mark word-endings.
# * `NGRAM_SIZE` specifies the size of character groupings that are taken into account.
# 
# Tweak the `NGRAM_SIZE` variable to change results. A lower number results in more gibberish, a higher number represents the input wordlist more closely.
# A `NGRAM_SIZE` of `3` will split `hello world` into following ngrams:
# 
# `hel`, `ell`, `llo`, `lo `, `o w`, ` wo`, `wor`, `orl`, `rld`.

# In[2]:


END = "|"
NGRAM_SIZE = 2


# The `markov` dictionary will store all ngrams found in the word list as dict keys. All the characters following a certain ngram will be stored in a list associated with this `ngram`.
# 
# When creating a new word, a random element from the list of possible next characters will be chosen. This leads to words resembling those in the input list, but having slight variations.

# In[3]:


markov = defaultdict(list)
beginnings = list()


# The `ngrams` function will split a word into ngrams and add every ngram and the following character to the `markov` dict.

# In[4]:


def ngrams(line: str) -> None:
    line = list(line)
    line.append(END)
    i = 0

    for i in range(len(line) - NGRAM_SIZE):
        gram = "".join(line[i:i+NGRAM_SIZE])
        following = line[i+NGRAM_SIZE]

        if i == 0:
            beginnings.append(gram)

        markov[gram].append(following)


# The `ngrams_from_file` function will take a path to a word file, read it and pass every line to the `ngrams` function.

# In[5]:


def ngrams_from_file(path: str) -> None:
    with open(path) as f:
        for line in f.readlines():
            ngrams(line.strip())


# The `generate` function will pick a random ngram from the beginnings list. Then it will generate new words, by choosing a random next character from the current ngram. This new next character will then form the next ngram and so on until the `END` character is found.

# In[6]:


def generate(start: str = None) -> str:
    if start is None:
        start = choice(beginnings)

    result = start
    while True:
        gram = result[-NGRAM_SIZE:]
        choices = markov[gram]

        following = choice(choices)

        if following == "|":
            break

        result += following

    return result


# Read the example wordlist

# In[7]:


ngrams_from_file("ai-wordlist")


# Generate 10 random words

# In[10]:


for i in range(10):
    print(generate())

