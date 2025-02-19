import unittest
from EmotionDetection.emotion_detection import emotion_detector
class TestEmotionDetection(unittest.TestCase):
    def test_emotion_detector(self):
        inp = "I am glad this happened"
        expected = "joy"
        return self.assertEqual(emotion_detector(inp)['dominant_emotion'], expected)

unittest.main()