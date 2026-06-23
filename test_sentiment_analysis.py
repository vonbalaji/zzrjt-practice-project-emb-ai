from SentimentAnalysis.sentiment_analysis import sentiment_analyzer 
import unittest
import json
class TestSentimentAnalyzer(unittest.TestCase): 
    def test_sentiment_analyzer(self): 
        # Test case for positive sentiment 
        result_1 = json.loads(sentiment_analyzer('I love working with Python') )
        print(result_1)
        print(result_1['documentSentiment']['label'])
        self.assertEqual(result_1['documentSentiment']['label'], 'SENT_POSITIVE') 
        # Test case for negative sentiment 
        result_2 = json.loads(sentiment_analyzer('I hate working with Python') )
        self.assertEqual(result_2['documentSentiment']['label'], 'SENT_NEGATIVE') 
        # Test case for neutral sentiment 
        result_3 = json.loads(sentiment_analyzer('I am neutral on Python'))
        self.assertEqual(result_3['documentSentiment']['label'], 'SENT_NEUTRAL')
unittest.main()