import random
import math

class SampleDataGenerator:
    """
    class: SampleDataGenerator
    holds class methods used to create sample data

    generateSamples(amount: int, seed=None : int)
    """

    class Constants:
        Solid = 0
        Diagonal = 1
        Horizontal = 2
        Vertical = 3
        Unknown = 4

    @classmethod
    def capture(cls, value, minValue, maxValue):
        return min(maxValue, max(minValue, value))

    __labels__ = [Constants.Solid, Constants.Diagonal, Constants.Horizontal, Constants.Vertical, Constants.Unknown]

    @classmethod
    def __generateSample__(cls):
        label = SampleDataGenerator.__labels__[int(random.random() * len(SampleDataGenerator.__labels__))]
        base = random.random() * 0.75 + 0.25
        if label == SampleDataGenerator.Constants.Solid:
            return [[base, SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1)], SampleDataGenerator.Constants.Solid]
        elif label == SampleDataGenerator.Constants.Diagonal:
            tmp = [[base, SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1)], SampleDataGenerator.Constants.Diagonal]
            if random.random() >= 0.5:
                tmp[0] = [*tmp[0][2:], *tmp[0][0:2]]
            return tmp
        elif label == SampleDataGenerator.Constants.Horizontal:
            tmp = [[base, SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1)], SampleDataGenerator.Constants.Horizontal]
            if random.random() >= 0.5:
                tmp[0] = [*tmp[0][2:], *tmp[0][0:2]]
            return tmp
        elif label == SampleDataGenerator.Constants.Vertical:
            tmp = [[base, SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 10 - 0.05) * base,0,1), SampleDataGenerator.capture(base + (random.random() / 3 - 0.5) * base,0,1)], SampleDataGenerator.Constants.Vertical]
            if random.random() >= 0.5:
                tmp[0] = [tmp[0][1], tmp[0][0], tmp[0][3], tmp[0][1]]
            return tmp
        else:
            tmp = ([base, SampleDataGenerator.capture(base + (random.random() / 20 - 0.05) * base, 0, 1),
                     SampleDataGenerator.capture(base + (random.random() / 20 - 0.05) * base, 0, 1),
                     SampleDataGenerator.capture(base + (random.random() / 20 - 0.05) * base, 0, 1)],
                    SampleDataGenerator.Constants.Unknown)
            randindex = math.floor(random.random() * 3 + 0.5)
            if tmp[0][randindex] > 0.5:
                tmp[0][randindex] -= 0.45
            else:
                tmp[0][randindex] += 0.45
            tmp[0][randindex] = SampleDataGenerator.capture(tmp[0][randindex], 0, 1)
            return tmp

    @classmethod
    def generateSamples(cls, amount, seed=None):
        if not seed == None:
            random.seed = seed
        for i in range(amount):
            yield SampleDataGenerator.__generateSample__()