class Calculator:
    def solve_me_first(self, a, b):
        number_types = (int, float, complex)

        if isinstance(a, number_types) and isinstance(b, number_types):
            return a + b
        else:
            raise ValueError
