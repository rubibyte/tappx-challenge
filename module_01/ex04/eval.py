class Evaluator:
    def zip_evaluate(coefs: list, words: list):
        if not isinstance(coefs, list) and isinstance(words, list):
            raise TypeError("coeficient and words must be a list")
        elif not all(isinstance(word, str) for word in words):
            raise TypeError("all elements inside words list must be strings")
        elif not all(isinstance(coef, (int, float)) for coef in coefs):
            raise TypeError("all elements inside coeficient list must be \
integers or floats")
        if len(words) != len(coefs):
            return -1
        len_sum = 0
        for coef, word in zip(coefs, words):
            len_sum += len(word) * coef
        return len_sum

    def enumerate_evaluate(coefs: list, words: list):
        if not isinstance(coefs, list) and isinstance(words, list):
            raise TypeError("coeficient and words must be a list")
        elif not all(isinstance(word, str) for word in words):
            raise TypeError("all elements inside words list must be strings")
        elif not all(isinstance(coef, (int, float)) for coef in coefs):
            raise TypeError("all elements inside coeficients list must be \
integers or floats")
        if len(words) != len(coefs):
            return -1
        len_sum = 0
        for i, word in enumerate(words):
            len_sum += len(word) * coefs[i]
        return len_sum
