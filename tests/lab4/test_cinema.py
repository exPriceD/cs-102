import unittest
from src.lab4.task1.cinema import MovieRecommendationSystem
import os

class TestMovieRecommendationSystem(unittest.TestCase):
    def setUp(self):
        self.movies_path = 'tests/lab4/data/movies.txt'
        self.history_path = 'tests/lab4/data/history.txt'

    def test_read_history(self):
        system = MovieRecommendationSystem(self.movies_path, self.history_path)
        self.assertEqual(system.history, [['1', '2', '3'], ['4', '5', '6']])

    def test_read_movies(self):
        system = MovieRecommendationSystem(self.movies_path, self.history_path)
        self.assertEqual(system.movies, {'1': 'Мстители: Финал', '2': 'Хатико', '3': 'Дюна'})

    def test_get_views(self):
        system = MovieRecommendationSystem(self.movies_path, self.history_path)
        system.history = [['1', '2', '3'], ['2', '3', '4'], ['1', '2', '4']]

        views = system.get_views({'1', '2', '3'})
        self.assertEqual(views, {'1': 2, '2': 3, '3': 2})

    def test_get_recommendations(self):
        system = MovieRecommendationSystem(self.movies_path, self.history_path)
        system.movies = {'1': 'Мстители: Финал', '2': 'Хатико', '3': 'Дюна', '4': 'Унесенные призраками'}
        system.history = [['1', '2', '3'], ['2', '3', '4'], ['1', '2', '2']]

        recommendation = system.get_recommendations(['1', '2'])
        self.assertEqual(recommendation, 'Дюна')

        recommendation = system.get_recommendations(['4'])
        self.assertEqual(recommendation, 'No any recommendations')

    def test_get_recommendation_set(self):
        system = MovieRecommendationSystem(self.movies_path, self.history_path)
        system.history = [['1', '2', '3'], ['2', '3', '4'], ['1', '2', '4']]

        recommendation_set = system.get_recommendation_set(['1', '2'])
        self.assertEqual(recommendation_set, {'4', '3'})

        recommendation_set = system.get_recommendation_set(['4'])
        self.assertEqual(recommendation_set, set())


if __name__ == '__main__':
    unittest.main()
