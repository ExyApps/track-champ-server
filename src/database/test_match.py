TESTS = {
    'Pista': [
        {'name': 'Corridas', 'model': None}
    ]
}

class TestMatch:
    @staticmethod
    def get_test_structure():
        return {k: [t['name'] for t in v] for k, v in TESTS.items()}
    
    @staticmethod
    def get_test_model(category, test):
        try:
            return TESTS[category][test]
        except IndexError as e:
            raise ValueError('Not supposed to happen')