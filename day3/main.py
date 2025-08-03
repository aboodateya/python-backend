import utils
data = [10, 20, 30, 40, 50]
stats = utils.describe_data(data)
print("=== Data Statistics ===")
for key, value in stats.items():
    print(f"{key.capitalize()}: {value}")
print("\n=== Utility Functions ===")
print(f"Is 10 even? {utils.is_even(10)}")
print(f"Factorial of 5: {utils.factorial(5)}")
print("\n=== GitHub API Status ===")
print(f"GitHub status code: {utils.get_github_status()}")
