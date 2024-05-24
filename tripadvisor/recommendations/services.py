# Description: This file contains the class that generates the trip recommendation based on the user's input.
# The class takes the start date, end date, budget, and city as input and generates a recommendation based on the input.
from .vector_database import VectorDatabase
from .genai import generativeAI


class generateTripRecommendation():
    def __init__(self, start_date, end_date, budget, city):
        self.start_date = start_date
        self.end_date = end_date
        self.budget = budget
        self.city = city
        self.prompt = self.generatePrompt()
        self.recommendation = self.generateRecommendation()
    
    def generateContext(self, query):
        print('Searching vector DB for context...')
        vector_db = VectorDatabase()
        vector_db.createCollection('recommendations')
        similar_text = vector_db.searchQuery('recommendations', query)
        context = ''
        for i in range(len(similar_text)):
            context += f"{i+1}. {similar_text[i]['text']}\n"
        print('Context generated')
        return context

    def generatePrompt(self):
        query = 'I want to visit ' + self.city + ' from ' + self.start_date + ' to ' + self.end_date + ' with a budget of ' + self.budget
        context = self.generateContext(query)
        return f"Here is the information we already have:\n{context}\nAnswer the following question: {query}\n" 
    
    def generateRecommendation(self):
        print('Generating recommendations through generative AI...')
        ai = generativeAI(self.prompt)
        print('Recommendations generated')
        return ai.generateResponse()