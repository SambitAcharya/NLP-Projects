from frequency_summarize import FrequencySummarizer
from readingtime import readingTime
from rouge import rougeScore

# original news article borrowed from a news website.
content = '''

THE NDA government has told the Supreme Court that the country does not have to be called 'Bharat' instead of 'India'.
Responding to a PIL seeking a declaration that the Republic be called 'Bharat' for official and unofficial purposes by Union and state governments, the Centre claimed "there is no change in circumstances to consider any change in Article 1 of the Constitution of India." Article 1(1) says, "India, that is Bharat, shall be a Union of States." This is the only provision in Constitution on how this country be called for official and unofficial purposes.
Submitting its affidavit recently, the Ministry of Home Affairs (MHA) said issues regarding the country’s name were deliberated upon extensively by the Constituent Assembly during drafting of the Constitution and clauses in Article 1 were adopted unanimously. It further argued that the name ‘Bharat’ did not figure in the original draft of the Constitution and it was during debates that the Constituent Assembly considered names such as Bharat, Bharatbhumi, Bharatvarsh, India that is Bharat, Bharat that is India and Bharat as is known in English language India. It said there was no change in circumstances since the Constituent Assembly debated the issue to warrant a review.
A representation by the PIL petitioner's advocate Ajay G Majithia, the MHA said, had been examined and the plea now deserves to be dismissed.
Petitioner Niranjan Bhatwal, a social activist, had filed a PIL last year but the top court asked him to wait till his representation is decided upon by the government. After the government refused, he filed a fresh PIL and a bench headed by Chief Justice H L Dattu sought reply from Centre and state governments in April.
Majithia had said Article 1.1 must be interpreted keeping in view Constituent Assembly's intention, "which wanted to name the country Bharat". The plea said 'India' was coined during colonial era and the country, historically and in scriptures, is called Bharat. "India was used in Article 1 for reference, in order to repeal Government of India Act, 1935, and Indian Independence Act, 1947," the petition said.

'''

fs = FrequencySummarizer()

# Combining the lines to form a summary.
summary = ''.join(fs.summarize(content,3))

# Summary written by a human for the same article
human_summary = '''

The government has asked the Supreme Court to dismiss a PIL seeking a declaration that India be called 'Bharat' in all official and unofficial communications. The Home Ministry said the country's name was deliberated upon extensively and adopted unanimously while drafting the Constitution.
The court had asked the government to respond to the PIL filed by a social activist.

'''

print
print "     Summary     "
print "-----------------"

print summary

# Estimating the time taken to read the article.
reading_time = readingTime(summary)

# Evaluating how good the summary is by counting the number of common bigrams
# in both the summaries.
rouge_score = rougeScore(summary, human_summary)

print
print "Original Length %s" % (len(content))
print "Summary Length %s" % len(summary)
print
print "%s minute read" %reading_time
print "Rouge Score - %.3f" %rouge_score
