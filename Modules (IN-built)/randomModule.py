import random

print("=" * 65)
print("         PYTHON RANDOM MODULE - COMPLETE FUNCTION GUIDE")
print("=" * 65)

# ==============================================================================
# 1. INTEGER GENERATION FUNCTIONS
# ==============================================================================
print("\n--- 1. INTEGER GENERATION ---")

# randint(a, b)
# Returns a random integer N such that a <= N <= b (inclusive of both endpoints).
val_randint = random.randint(1, 10)
print(f"random.randint(1, 10) -> {val_randint}")

# randrange(start, stop, step)
# Returns a randomly selected element from range(start, stop, step).
# Note: Upper limit (stop) is EXCLUDED.
val_randrange = random.randrange(0, 100, 10)
print(f"random.randrange(0, 100, 10) -> {val_randrange}")

# getrandbits(k)
# Returns a Python integer with k random bits.
val_getrandbits = random.getrandbits(8)  # 8 bits -> integer range [0, 255]
print(f"random.getrandbits(8) -> {val_getrandbits}")


# ==============================================================================
# 2. FLOATING-POINT GENERATION FUNCTIONS
# ==============================================================================
print("\n--- 2. FLOATING-POINT GENERATION ---")

# random()
# Returns a random floating-point number in the range [0.0, 1.0).
val_random = random.random()
print(f"random.random() -> {val_random}")

# uniform(a, b)
# Returns a random floating-point number N such that a <= N <= b (or b <= N <= a).
val_uniform = random.uniform(1.5, 9.5)
print(f"random.uniform(1.5, 9.5) -> {val_uniform}")

# triangular(low, high, mode)
# Returns a random float from a triangular distribution bounded by low and high,
# with the given mode (peak of the distribution, defaults to midpoint).
val_triangular = random.triangular(10, 50, 25)
print(f"random.triangular(10, 50, 25) -> {val_triangular}")


# ==============================================================================
# 3. SEQUENCE SELECTION AND MANIPULATION FUNCTIONS
# ==============================================================================
print("\n--- 3. SEQUENCE SELECTION AND MANIPULATION ---")

items = ['apple', 'banana', 'cherry', 'date', 'elderberry']

# choice(seq)
# Returns a single random element from a non-empty sequence (e.g., list, tuple).
val_choice = random.choice(items)
print(f"random.choice(items) -> {val_choice}")

# choices(population, weights=None, k=1)
# Returns a list of k elements chosen WITH replacement (items can repeat).
# Supports optional probability weights.
val_choices = random.choices(items, weights=[10, 1, 1, 1, 1], k=3)
print(f"random.choices(items, weights=[10, 1, 1, 1, 1], k=3) -> {val_choices}")

# sample(population, k)
# Returns a list of k unique elements chosen WITHOUT replacement from population.
val_sample = random.sample(items, k=3)
print(f"random.sample(items, k=3) -> {val_sample}")

# shuffle(seq)
# Shuffles the sequence IN-PLACE (modifies the original list directly, returns None).
deck = [1, 2, 3, 4, 5]
random.shuffle(deck)
print(f"random.shuffle(deck) -> shuffled list: {deck}")


# ==============================================================================
# 4. SEEDING AND STATE MANAGEMENT FUNCTIONS
# ==============================================================================
print("\n--- 4. SEEDING AND STATE MANAGEMENT ---")

# seed(a)
# Initializes the random number generator. Fixed seed value yields reproducible results.
random.seed(42)
seeded_val1 = random.randint(1, 100)
random.seed(42)  # Reset seed to 42
seeded_val2 = random.randint(1, 100)
print(f"random.seed(42) -> 1st call randint(1, 100): {seeded_val1}")
print(f"random.seed(42) -> 2nd call after re-seed: {seeded_val2} (reproducible!)")

# getstate() and setstate(state)
# Captures and restores internal generator state to repeat identical sequences.
state = random.getstate()
num_before = random.random()
random.setstate(state)
num_after = random.random()
print(f"random.getstate() & setstate() -> before: {num_before}, after restore: {num_after}")


# ==============================================================================
# 5. STATISTICAL / REAL-VALUED DISTRIBUTIONS
# ==============================================================================
print("\n--- 5. STATISTICAL / REAL-VALUED DISTRIBUTIONS ---")

# gauss(mu, sigma)
# Gaussian / Normal distribution with mean mu and standard deviation sigma.
val_gauss = random.gauss(mu=0, sigma=1)
print(f"random.gauss(mu=0, sigma=1) -> {val_gauss}")

# expovariate(lambd)
# Exponential distribution where lambd is 1.0 divided by the desired mean.
val_expovariate = random.expovariate(lambd=1.5)
print(f"random.expovariate(lambd=1.5) -> {val_expovariate}")

# betavariate(alpha, beta)
# Beta distribution (alpha > 0, beta > 0). Values range between 0 and 1.
val_betavariate = random.betavariate(alpha=2.0, beta=5.0)
print(f"random.betavariate(alpha=2.0, beta=5.0) -> {val_betavariate}")

# gammavariate(alpha, beta)
# Gamma distribution (alpha > 0, beta > 0).
val_gammavariate = random.gammavariate(alpha=9.0, beta=2.0)
print(f"random.gammavariate(alpha=9.0, beta=2.0) -> {val_gammavariate}")


# ==============================================================================
# 6. CRYPTOGRAPHICALLY SECURE RANDOMNESS
# ==============================================================================
print("\n--- 6. CRYPTOGRAPHICALLY SECURE RANDOM GENERATOR ---")

# SystemRandom()
# Uses OS-provided entropy source (os.urandom) suitable for cryptographic use.
sys_rand = random.SystemRandom()
sys_val = sys_rand.randint(1000, 9999)
print(f"random.SystemRandom().randint(1000, 9999) -> {sys_val}")

print("\n" + "=" * 65)

