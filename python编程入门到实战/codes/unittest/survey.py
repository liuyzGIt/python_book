class AnonymousSurvey:
    def __init__(self, question):
        self.question = question
        self.responses = []
        
    def show_question(self):
        print(self.question)
        
    def store_response(self, new_response):
        self.responses.append(new_response)
    
    def show_results(self):
        print('Survey results:')
        for response in self.responses:
            print('-' + response)



def func():
    question = 'what language did you learn？'
    my_survey = AnonymousSurvey(question)

    my_survey.show_question()
    print('Enter "q" at any time to quit. \n')

    while True:
        response = input('language:')
        if response == 'q':
            break
        my_survey.store_response(response)
        
    print('\n thank you!')
    my_survey.show_results()
