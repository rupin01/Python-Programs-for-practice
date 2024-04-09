class DivisibleBySevenGenerator:
    def __init__(self, n):
        self.n = n
    
    def generate_divisible_by_seven(self):
        for i in range(self.n + 1):
            if i % 7 == 0:
                yield i

# Example usage:
n = 50
generator = DivisibleBySevenGenerator(n)
for num in generator.generate_divisible_by_seven():
    print(num)