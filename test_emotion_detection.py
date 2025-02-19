import unittest
from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        inp = "I am glad this happened"
        expected = "joy"
        self.assertEqual(emotion_detector(inp)['dominant_emotion'], expected)

        inp = "I am really mad about this"
        expected = "anger"
        self.assertEqual(emotion_detector(inp)['dominant_emotion'], expected)

        inp = "I feel disgusted just hearing about this"
        expected = "disgust"
        self.assertEqual(emotion_detector(inp)['dominant_emotion'], expected)

        inp = "I am so sad about this"
        expected = "sadness"
        self.assertEqual(emotion_detector(inp)['dominant_emotion'], expected)

        inp = "I am really afraid that this will happen"
        expected = "fears"
        self.assertEqual(emotion_detector(inp)['dominant_emotion'], expected)

unittest.main()