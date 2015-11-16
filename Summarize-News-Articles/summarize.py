from __future__ import division
import re

#This is a summarization algorithm
#implemented by Sambit Acharya

class SummaryTool(object):

    def split_content_to_sentences(self, content):

        """
        Function to split the given content to sentences.
        """

        content = content.replace("\n", ". ")
        return content.split(". ")

    def split_content_to_paragraphs(self, content):

        """
        Function to split content to paragraphs
        """

        return content.split("\n\n")

    def sentence_intersection(self, sent1, sent2):

        """
        Function to calculate the intersection between two sentences
        """

        # split the sentence into words/tokens
        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))

        # If there is not intersection, just return 0
        if (len(s1) + len(s2)) == 0:
            return 0

        # We normalize the result by the average number of words
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)

    def format_sentence(self, sentence):

        """
        Function to remove all the non-alphabetic characters
        from the sentence.
        """

        sentence = re.sub(r'\W+', '', sentence)
        return sentence

    def get_sentence_ranks(self, content):

        """
        Function to get the rank of the sentences
        in the paragraph.
        """

        # Split the content into sentences
        sentences = self.split_content_to_sentences(content)

        # Calculate the intersection of every two sentences
        n = len(sentences)
        values = [[0 for x in xrange(n)] for x in xrange(n)]
        for i in range(0, n):
            for j in range(0, n):
                values[i][j] = self.sentences_intersection(sentences[i], sentences[j])

        # Build the sentences dictionary
        # The score of a sentences is the sum of all its intersection
        sentences_dic = {}
        for i in range(0, n):
            score = 0
            for j in range(0, n):
                if i == j:
                    continue
                score += values[i][j]
            sentences_dic[self.format_sentence(sentences[i])] = score
        return sentences_dic



    def get_best_sentences(self, sentence_dictionary):

        """
        Function to get the best sentences in the
        paragraph.
        """

        # Split the paragraph into sentences
        sentences = self.split_content_to_sentences(paragraph)

        # Ignore short paragraphs
        if len(sentences) < 2:
            return ""

        # Get the best sentence according to the sentences dictionary
        best_sentence = ""
        max_value = 0
        for s in sentences:
            strip_s = self.format_sentence(s)
            if strip_s:
                if sentences_dic[strip_s] > max_value:
                    max_value = sentences_dic[strip_s]
                    best_sentence = s

        return best_sentence


    def get_summary(self, title, content, sentences_dic):

        """
        Function to generate the summary.
        """

        # Split the content into paragraphs
        paragraphs = self.split_content_to_paragraphs(content)

        # Add the title
        summary = []
        summary.append(title.strip())
        summary.append("")

        # Add the best sentence from each paragraph
        for p in paragraphs:
            sentence = self.get_best_sentence(p, sentences_dic).strip()
            if sentence:
                summary.append(sentence)

        return ("\n").join(summary)
