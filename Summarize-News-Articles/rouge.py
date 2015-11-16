def rouge_score(summary, human_summary):

    summary = summary.split()
    human_summary = human_summary.split()

    bigrams_summary = set(' '.join(summary[i:i+2]) for i,v in enumerate(summary) \
    if i!=len(summary)-1)

    bigrams_humansummary = set(' '.join(human_summary[i:i+2]) for i,v in \
    enumerate(human_summary) if i!=len(human_summary)-1)

    common_bigrams = bigrams_summary.intersection(bigrams_humansummary)

    rouge_score = float(len(common_bigrams))/len(bigrams_humansummary)

    return rouge_score

if '__name__' == '__main__':
    rouge_score()
