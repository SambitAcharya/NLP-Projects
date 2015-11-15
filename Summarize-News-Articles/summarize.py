from __future__ import division
import re

#This is a summarization algorithm
#implemented by Sambit Acharya

class SummaryTool(object):

    def split_content_to_sentences(self, content):

        '''
        Function to split the given content to sentences.
        '''

        content = content.replace("\n", ". ")
        return content.split(". ")

    def split_content_to_paragraphs(self, content):

        '''
        Function to split content to paragraphs
        '''

        return content.split("\n\n")

    def sentence_intersection(self, sent1, sent2):

        '''
        Function to calculate the intersection between two sentences
        '''

        # split the sentence into words/tokens
        s1 = set(sent1.split(" "))
        s2 = set(sent2.split(" "))

        # If there is not intersection, just return 0
        if (len(s1) + len(s2)) == 0:
            return 0

        # We normalize the result by the average number of words
        return len(s1.intersection(s2)) / ((len(s1) + len(s2)) / 2)

    def get_sentence_ranks(self, content):

        '''
        Function to get the rank of the sentences
        in the paragraph.
        '''

        pass



    def get_best_sentences(self, sentence_dictionary):

        '''
        Function to get the best sentences in the
        paragraph.
        '''

        pass

    def get_summary(self, title, content, sentences_dic):

        '''
        Function to generate the summary.
        '''

        pass
