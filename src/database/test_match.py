from src.database.wrapper.tests import create_race_result

TESTS = {
    'Pista': [
        {'name': 'Corridas', 'model_function': create_race_result}
    ]
}

class TestMatch:
    @staticmethod
    def get_test_structure():
        return {k: [t['name'] for t in v] for k, v in TESTS.items()}
    
    @staticmethod
    def get_test_model(category, test):
        try:
            category_tests = TESTS[category]
            for t in category_tests:
                if t['name'] == test:
                    return t['model_function']
                
            raise ValueError('Not supposed to happen')
        
        except IndexError as e:
            raise ValueError('Not supposed to happen')