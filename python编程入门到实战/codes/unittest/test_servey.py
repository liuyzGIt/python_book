import unittest
from survey import AnonymousSurvey

class SurveyTestCase(unittest.TestCase):
    
    def setUp(self):
        question = "what language are you learn:"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Chinese', 'Spanish']
    
    def test_store_single_response(self):
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)
    
    # 简单测试
    def test_store_three_response(self):
        question = "what language are you learn:"
        my_survey = AnonymousSurvey(question)
        responses = ['English', 'Chinese', 'Spanish']
        for response in responses:
            my_survey.store_response(response)
        for response in responses:
            self.assertIn(response, my_survey.responses)
        
unittest.main()
    
