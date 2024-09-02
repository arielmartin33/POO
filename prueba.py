class Dog:
    def __matmul__(self, x):
        return f'hello {x}'

dog = Dog()
print(dog @ 500)
