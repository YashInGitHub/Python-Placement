import random

def demonstrate_random_module():
    print("Random module demonstration: ")

    #random.random() = returns a random float in the range of [0.0, 1.0)
    print("\nrandom.random() = ", random.random())

    #random.uniform(a, b) = returns a random float in the range [a, b]
    print("\nrandom.uniform(1, 10) = ", random.uniform(1, 10))

    #random.randint(a, b) = returns a random integer in the range [a, b]
    print("\nrandom.randint(1, 10) = ", random.randint(1, 10))

    #random.randrange(start, stop, step) = return randomly selected element from a range start, stop and step
    print("\nrandom.randrange(1, 10, 2) = ", random.randrange(1, 10, 2))

    #random.choice(seq) = returns a randommly selected element from a non-empty list
    my_list = [1, 2, 3, 4, 5]
    print("\nrandom.choice([1, 2, 3, 4, 5]) = ", random.choice(my_list))

    #random.choices(seq, weights = None, k = 1) = returns a list of k randomly selected elements from the non=empty list
    print("\nrandom.choices([1, 2, 3, 4, 5], k = 3) = ", random.choice(my_list), 3)

    #random.sample(seq, k) = returns a list of k unique randomly selected elements
    print("\nrandom.sample([1, 2, 3, 4, 5], k=3) = ", random.sample(my_list, 3))

    #random.shuffle(x) = shuffles the sequence x in place
    print("\nrandom.shuffle([1, 2, 3, 4 ,5]) = ", random.shuffle(my_list))

    #random.seed(a = None) = initializes the random number generator
    print("\nrandom.seed(10) and random.random() = ", random.seed(10), random.random())

    #random.getrandbits(k) = returns an integer with k random random bits
    print("\nrandom.getrandbits(5) = ", random.getrandbits(5))

    #random.gauss(mu, sigma) = returns a random float from the gaussian table
    print("\nrandom.gauss(0, 1) = ", random.gauss(0, 1))

if __name__ == "__main__":
    demonstrate_random_module()
