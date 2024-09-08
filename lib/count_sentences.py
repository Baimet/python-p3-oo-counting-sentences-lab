#!/usr/bin/env python3

class MyString:
    def __init__(self, value=""):
        self._value = None
        self.value = value  # This will use the setter validation for value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Replace multiple punctuation marks with a single period for simplicity
        cleaned_value = self.value.replace('!', '.').replace('?', '.')
        # Split by period to separate sentences
        sentences = cleaned_value.split('.')
        # Filter out empty strings that may result from consecutive punctuation marks
        return len([s for s in sentences if s.strip()])

