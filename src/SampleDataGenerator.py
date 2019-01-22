import random


class SampleDataGenerator:
    """
    class: SampleDataGenerator
    holds class methods used to create sample data

    generateSamples(amount: int, seed=None : int)
    """

    class Constants:
        Solid = "solid"
        Diagonal = "Diagonal"
        Horizontal = "Horizontal"
        Vertical = "Vertical"
        Unknown = "unknown"

    @classmethod
    def capture(cls, value, minValue, maxValue):
        return min(maxValue, max(minValue, value))

    __labels__ = [Constants.Solid, Constants.Diagonal, Constants.Horizontal, Constants.Vertical]

    @classmethod
    def __generateSample__(cls):
        label = SampleDataGenerator.__labels__[int(random.random() * len(SampleDataGenerator.__labels__))]
        base = random.random() * 0.75 + 0.25
        if (label == SampleDataGenerator.Constants.Solid):
            return ([base, SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1)], SampleDataGenerator.Constants.Solid)
        elif (label == SampleDataGenerator.Constants.Diagonal):
            return ([base, SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1)], SampleDataGenerator.Constants.Diagonal)
        elif (label == SampleDataGenerator.Constants.Horizontal):
            return ([base, SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1)], SampleDataGenerator.Constants.Horizontal)
        elif (label == SampleDataGenerator.Constants.Vertical):
            return ([base, SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1)], SampleDataGenerator.Constants.Vertical)

    @classmethod
    def generateSamples(cls, amount, seed=None):
        if not seed == None:
            random.seed = seed
        for i in range(amount):
            yield SampleDataGenerator.__generateSample__()