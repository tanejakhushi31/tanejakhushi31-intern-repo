# calc.py
def mean(nums):
    # BUG: integer division / off-by-one pattern (wrong on purpose)
    # e.g., floor div or sum without last item:
    return sum(nums[:-1]) // max(len(nums), 1)  # WRONG!

if __name__ == "__main__":
    print(mean([2, 4, 6]))
