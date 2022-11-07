import sys

class Elephants:
    def __init__(self, filename):

        with open(filename) as f:
            self.n = int(f.readline())
            self.numbers = [x for x in range(self.n)]
            self.weight = [int(x) for x in f.readline().replace("\n", "").split(" ")]
            self.a_places = [int(x) - 1 for x in f.readline().replace("\n", "").split(" ")]
            self.b_places = [int(x) - 1 for x in f.readline().replace("\n", "").split(" ")]
            self.weight_values = dict(
                map(lambda i, j: (i, j), self.numbers, self.weight)
            )
            self.cycles = self.cycle()

    def cycle(self):
        odw = [self.b_places[i] == self.a_places[i] for i in range(self.n)]
        cycles = []
        for i in range(self.n):
            if not odw[i]:
                one_cycle = []
                x = i
                while not odw[x]:
                    odw[x] = True
                    one_cycle.append(x)
                    x = self.b_places.index(self.a_places[x])
                cycles.append(one_cycle)
        return cycles
    
    def calculate(self):
        minimum = float('inf')
        sums = []
        mins = []
        for cycle in self.cycles:
            cycle_sum = 0
            cycle_min = float('inf')
            for element in cycle:
                cycle_sum += self.weight_values[self.a_places[element]]
                cycle_min = min(self.weight_values[self.a_places[element]], cycle_min)
            minimum =  min(minimum, cycle_min)
            sums.append(cycle_sum)
            mins.append(cycle_min)
        
        total = 0
        for i in range(len(self.cycles)):
            total += min(sums[i] + (len(self.cycles[i]) - 2) * mins[i], sums[i] + mins[i] + (len(self.cycles[i]) + 1) * minimum)
        return total
        
solve = print(Elephants(filename=sys.argv[1]).calculate())
