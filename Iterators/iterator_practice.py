# Iterators and Generators Practice

class Sentence:
    def __init__(self, sentence):
        self.sentence = sentence
        self.index = 0
        self.words = self.sentence.split()
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration
        
        index = self.index
        self.index += 1
        return self.words[index]


def generator_sentence(sentence):
    current_index = 0
    words = sentence.split()
    while current_index < len(words):
        yield words[current_index]
        current_index += 1


def generator_sentence2(sentence):
    for word in sentence.split():
        yield word


if __name__ == '__main__':

    # Using Custom Class Iterator
    my_sentence = Sentence('This is a test')

    for word in my_sentence:
        print(word)
    
    # Using Generator
    gen_my_sentence = generator_sentence('This is a test')

    for word in gen_my_sentence:
        print(word)

    # Using Generator
    gen2_my_sentence = generator_sentence2('This is a test')

    for word in gen2_my_sentence:
        print(word)
