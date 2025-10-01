def mean(nums):
    # correct mean: sum / count (float)
    return sum(nums) / len(nums)

if __name__ == "__main__":
    print(mean([2, 4, 6]))  # 4.0
