# -*- coding: utf-8 -*-
"""French sentiment analysis implementations.
"""
from __future__ import absolute_import
from text.base import BaseSentimentAnalyzer, CONTINUOUS, DISCRETE
from textblob_fr.fr import sentiment as pattern_sentiment


class PatternAnalyzer(BaseSentimentAnalyzer):

    '''Sentiment analyzer that uses the same implementation as the
    pattern library. Returns results as a tuple of the form:

    ``(polarity, subjectivity)``
    '''

    kind = CONTINUOUS

    def analyze(self, text):
        """Return the sentiment as a tuple of the form:
        ``(polarity, subjectivity)``
        """
        return pattern_sentiment(text)
