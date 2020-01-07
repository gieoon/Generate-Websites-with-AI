'''
	Assesses generated HTML against target HTML to create a quantified difference.
	The score is wrapper into a score within 1. This is regardless of the length of the text.
	
	Each action is then assessed on its distance/discrepancy from the target.
'''

import os
import numpy as np


'''
	INPUT: raw generated & target HTML
	OUTPUT: score from 0 to 1 on similarity
'''

from sklearn.feature_extraction.text import TfidfVectorizer

def Assess_HTML_SIM(generatedHTML, targetHTML):
	from html_similarity import style_similarity, structural_similarity, similarity
	print("---------------------------")
	print(style_similarity(generatedHTML, targetHTML))
	print("---------------------------")
	print(structural_similarity(generatedHTML, targetHTML))
	print("---------------------------")
	print(similarity(generatedHTML, targetHTML))

# Doesn't work with code blocks...
def Assess_TF_IDF(generatedHTML, targetHTML):
	documents = [generatedHTML, "p"]
	#documents = ["I'd like an apple", "An apple a day keeps the doctor away", "Never compare an apple to an orange", "I prefer scikit-learn to Orange", "The scikit-learn docs are Orange and Blue"]
	#documents = ["The sky is blue.", "The sun is bright today.", "The sun in the sky is bright.", "We can see the shining sun, the bright sun."]
	vect = TfidfVectorizer(min_df=1, stop_words="english")
	print("documents: ", documents)
	tfidf = vect.fit_transform(documents)
	# no need to normalize, since Vectorizer will return normalized tf-idf
	pairwise_similarity = tfidf * tfidf.T
	print(pairwise_similarity)

#pairwise_similarity.toarray()

# Tensorflow Hub Universal Sentence Encoder implementation
def Assess_USE(generatedHTML, targetHTML):
	import tensorflow.compat.v1 as tf
	tf.disable_v2_behavior()
	documents = [generatedHTML, targetHTML]
	import matplotlib.pyplot as plt
	import tensorflow_hub as hub
	print(tf.__version__)
	tf.disable_eager_execution()
	tf_hub_cache_dir = "universal_encoder_cached/"
	os.environ["TFHUB_CACHE_DIR"] = tf_hub_cache_dir

	# URL for First time downloading model
	#MODULE_URL = "https://tfhub.dev/google/universal-sentence-encoder/1?tf-hub-format=compressed"
	#global embed
	MODULE_URL = tf_hub_cache_dir+"/d3941dd08d84aba44358d623640d2604d47ffb74/"
	embed = hub.Module(MODULE_URL)
	similarity_input_placeholder = tf.placeholder(tf.string, shape=(None))
	similarity_message_encodings = embed(similarity_input_placeholder)
	with tf.Session() as session:
		session.run(tf.global_variables_initializer())
		session.run(tf.tables_initializer())
		message_embeddings_ = session.run(similarity_message_encodings, feed_dict={similarity_input_placeholder: documents})

		corr = np.inner(message_embeddings_, message_embeddings_)
		print(corr)
		#heatmap(generatedHTML, generatedHTML, corr)

def heatmap(x_labels, y_labels, values):
    fig, ax = plt.subplots()
    im = ax.imshow(values)

    # We want to show all ticks...
    ax.set_xticks(np.arange(len(x_labels)))
    ax.set_yticks(np.arange(len(y_labels)))
    # ... and label them with the respective list entries
    ax.set_xticklabels(x_labels)
    ax.set_yticklabels(y_labels)

    # Rotate the tick labels and set their alignment.
    plt.setp(ax.get_xticklabels(), rotation=45, ha="right", fontsize=10,
         rotation_mode="anchor")

    # Loop over data dimensions and create text annotations.
    for i in range(len(y_labels)):
        for j in range(len(x_labels)):
            text = ax.text(j, i, "%.2f"%values[i, j], ha="center", va="center", color="w", fontsize=6)
    fig.tight_layout()
    plt.show()