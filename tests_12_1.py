import unittest
import runner

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        walks = runner.Runner('Лео')
        for i in range(10):
            walks.walk()
        self.assertEqual(walks.distance, 50)

    def test_run(self):
        runs = runner.Runner('Лена')
        for i in range(10):
            runs.run()
        self.assertEqual(runs.distance, 100)

    def test_challenge(self):
        walks = runner.Runner('Леo')
        runs = runner.Runner('Лена')
        for i in range(10):
            runs.run()
            walks.walk()
            self.assertNotEqual(runs.distance, walks.distance)