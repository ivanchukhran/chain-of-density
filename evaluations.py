import json

import numpy as np
import spacy
import evaluate
import nltk.tokenize
from tqdm import tqdm


def extractive_fragments(prediction_tokens, source_tokens):
    F = []
    i, j = 0, 0
    while i < len(prediction_tokens):
        f = []
        while j < len(source_tokens):
            if prediction_tokens[i] == source_tokens[j]:
                i_hat, j_hat = i, j
                while i_hat < len(prediction_tokens) and j_hat < len(source_tokens) and prediction_tokens[i_hat] == \
                        source_tokens[j_hat]:
                    i_hat += 1
                    j_hat += 1
                if len(f) < (i_hat - i):
                    f = prediction_tokens[i:i_hat]
                j = j_hat
            else:
                j += 1
        i, j = i + max(1, len(f)), 0
        F = F + [f]
    return F


def extractive_density(prediction_tokens, source_tokens):
    tokenized_fragments = extractive_fragments(prediction_tokens, source_tokens)
    return np.sum([len(f) ** 2 for f in tokenized_fragments]) / len(prediction_tokens)


rouge = evaluate.load('rouge')


def fusion(prediction, source, return_alignments=False, threshold=0.0):
    alignments_ = np.zeros((len(prediction), len(source)))
    for i, summary_sentence in enumerate(prediction):
        for j, article_sentence in enumerate(source):
            computed_rouge = rouge.compute(predictions=[summary_sentence], references=[article_sentence])
            alignments_[i, j] = computed_rouge['rougeL']
    average_alignments = (alignments_ > threshold).sum() / len(source)
    return average_alignments, alignments_ if return_alignments else average_alignments


def tokenize(text):
    return [token for token in nltk.word_tokenize(text.lower()) if token.isalnum()]


nlp = spacy.load('en_core_web_sm')


def main():
    with open('summaries.json', 'r') as file:
        summaries = json.load(file)
    for element in tqdm(summaries, leave=False, desc='Evaluating samples'):
        element['n_tokens'] = []
        element['n_entities'] = []
        element['entity_density'] = []
        element['extractive_density'] = []
        element['fusion'] = []
        for gpt_summary in tqdm(element['gpt_summary'], leave=False, desc='Evaluating summaries'):
            summary = gpt_summary['Denser_Summary']
            # With punctuation and stopwords
            entities = nlp(summary).ents
            summary_tokens = nltk.word_tokenize(summary)
            entity_density = len(entities) / len(summary_tokens)

            # Without punctuation
            clean_summary_tokens = tokenize(summary)
            clean_article_tokens = tokenize(element['article'])
            extractive_density_ = extractive_density(clean_summary_tokens, clean_article_tokens)
            fusion_ = fusion(clean_summary_tokens, clean_article_tokens)

            element['n_tokens'].append(len(summary_tokens))
            element['n_entities'].append(len(entities))
            element['entity_density'].append(entity_density)
            element['extractive_density'].append(extractive_density_)
            element['fusion'].append(fusion_)
        break
    with open('summaries.json', 'w') as file:
        json.dump(summaries, file, indent=4)


if __name__ == '__main__':
    main()


