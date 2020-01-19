class Benchmark:
    def __init__(self, filepath):
        self.path = '../benchmark/' + filepath + '.log'
        self.file = open(self.path, 'w')
        self.scores = []


    def write(self, msg):
        self.file.write(msg + '\n')

    def close(self):
        self.file.close()

    def add(self, score):
        self.scores.append(score)
