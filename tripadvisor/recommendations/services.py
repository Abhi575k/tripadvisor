class generateTripRecommendation():
    def __init__(self, start_date, end_date, budget, city):
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.city = city
        self.prompt = self.generatePrompt()
        self.recommendation = self.generateRecommendation()

    def generatePrompt(self):
        prompt = 'You are planning a trip to from to with a budget of $.'
        return prompt
    
    def generateRecommendation(self):
        recommendation = 'You should visit the following places in:'
        return recommendation