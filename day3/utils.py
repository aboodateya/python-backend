import math
import statistics
import requests

def is_even(n):
    return n % 2 == 0

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

def describe_data(data):
    return {
        "mean": statistics.mean(data),
        "median": statistics.median(data),
        "stdev": statistics.stdev(data),
        "sqrt_mean": math.sqrt(statistics.mean(data)),
    }

def get_github_status():
    try:
        response = requests.get("https://api.github.com", timeout=5)
        return response.status_code
    except requests.RequestException as e:
        return f"Error: {e}"
