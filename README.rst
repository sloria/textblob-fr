===========
textblob-fr
===========

.. image:: https://badge.fury.io/py/textblob-fr.png
    :target: http://badge.fury.io/py/textblob-fr
    :alt: Latest version

.. image:: https://travis-ci.org/sloria/textblob-fr.png?branch=master
    :target: https://travis-ci.org/sloria/textblob-fr
    :alt: Travis-CI

French language support for `TextBlob`_.

Features
--------

* Part-of-speech tagging (``PatternTagger``)
* Sentiment analysis (``PatternAnalyzer``)
* Supports Python 2 and 3

Installing/Upgrading
--------------------

If you have `pip <http://www.pip-installer.org/>`_ installed (you should), run ::

    $ pip install -U textblob
    $ pip install -U textblob-fr

Usage
-----
.. code-block:: python

    >>> from textblob import TextBlob
    >>> from textblob_fr import PatternTagger, PatternAnalyzer
    >>> text = u"Quelle belle matinée"
    >>> blob = TextBlob(text, pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    >>> blob.tags
    [(u'Quelle', u'DT'), (u'belle', u'JJ'), (u'matin\xe9e', u'NN')]
    >>> blob.sentiment
    (0.8, 0.8)

Alternatively, you can use the ``Blobber`` class to avoid having to repeatedly pass the models into the ``TextBlob`` constructor.

.. code-block:: python

    >>> from textblob import Blobber
    >>> from textblob_fr import PatternTagger, PatternAnalyzer
    >>> tb = Blobber(pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
    >>> blob1 = tb(u"Quelle belle matinée")
    >>> blob1.sentiment
    (0.8, 0.8)
    >>> blob2 = tb(u"C'est une voiture terribles.")
    >>> blob2.sentiment
    (-0.7, 0.6)
    >>> blob1.analyzer is blob2.analyzer
    True

Requirements
------------

- Python >= 2.6 or >= 3.3

TODO
----

- Tokenization
- Parsing
- NLTK tagging?

License
-------

MIT licensed. See the bundled `LICENSE <https://github.com/sloria/textblob-fr/blob/master/LICENSE>`_ file for more details.

.. _TextBlob: https://textblob.readthedocs.org/
