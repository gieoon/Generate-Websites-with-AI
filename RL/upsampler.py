'''
Upsampler is a seq2seq model that takes a downsampled input and generates and upsampled output
This is recursively called everytime a human-in-the-loop interaction is made.
'''

import os, sys

from keras.models import Model
from keras.layers import Input, LSTM, GRU, Dense, Embedding
from keras.preprocessing.text import Tokenizer
from keras.preprocessing.sequence import pad_sequences
from keras.utils import to_categorical
import numpy as np
import matplotlib.pyplot as plt

BATCH_SIZE = 64
EPOCHS = 20
LSTM_NODES = 256
NUM_SENTENCES = 1
MAX_SENTENCE_LENGTH = 200
MAX_NUM_WORDS = 20000
EMBEDDING_SIZE = 100

input_sentences = []
output_sentences = []
output_sentences_inputs = []

count = 0
for line in open(r'',encoding='utf-8'):
	count += 1
	
	if count > NUM_SENTENCES:
		break
	
	input_sentence, output = line.rstrip().split(',')
	
	output_sentence = output + ' <eos>'
	output_sentence_input = '<sos> ' + output
	
	input_sentences.append(input_sentence)
	output_sentences.append(output_sentence)
	output_sentences_inputs.append(output_sentences_input)
	
print("num samples input:", len(input_sentences))
print("num samples output:", len(output_sentences))
print("num samples output input:", len(output_sentences_inputs))

input_tokenizer = Tokenizer(num_words=MAX_NUM_WORDS)
input_tokenizer.fit_on_texts(input_sentences)
input_integer_seq = input_tokenizer.texts_to_sequences(input_sentences)

word2idx_inputs = input_tokenizer.word_index
print('Total unique words in the input: %s' % len(word2idx_inputs))

max_input_len = max(len(sen) for sen in input_integer_seq)
print("Length of longest sentence in input: %g" % max_input_len)

output_tokenizer = Tokenizernum_words=MAX_NUMWORDS,filters='')
output_tokenizer.fit_on_texts(output_sentences + output_sentences_inputs)
output_integer_seq = output_tokenizer.texts_to_sequences(output_sentences)
output_input_integer_seq = output_tokenizer.texts_to_sequences(output_sentences_inputs)

word2idx_outputs = output_tokenizer.word_index
print('Total unique words in the output: %s' % len(word2idx_outputs))

num_words_output = len(word2idx_outputs) + 1
max_out_len = max(len(sen) for sen in output_integeter_seq)
print("Length of longest sentence in the output: %g" % max_out_len)

encoder_input_sequences = pad_sequences(input_integer_seq, maxlen=max_input_len)
print("encoder_input_sequences.shape: ", encoder_input_sequences.shape)

decoder_input_sequences = pad_sequences(output_input_integer_seq, maxlen=max_out_len, padding='post')
print("decoder_input_sequences.shape:", decoder_input_sequences.shape)

# GloVe word embeddings
from numpy import array, asarray, zeros

embeddings_dictionary = dict()

glove_file or word2vec embeddings

decoder_targets_one_hot = np.zeros((len(input_sentences),max_out_len,num_words_output),dtype='float32')

