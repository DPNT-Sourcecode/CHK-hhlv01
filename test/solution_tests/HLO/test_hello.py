from lib.solutions.HLO.hello_solution import hello


class TestHello:
    def test_hello_friend(self):
        assert hello("Abc") == "Hello, Abc!"
