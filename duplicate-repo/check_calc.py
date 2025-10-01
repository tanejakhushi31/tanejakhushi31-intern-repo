import sys
from calc import mean

def run_checks():
    # Basic correctness checks
    assert abs(mean([2, 4, 6]) - 4.0) < 1e-9
    assert abs(mean([1, 2, 3, 4]) - 2.5) < 1e-9
    assert abs(mean([10]) - 10.0) < 1e-9
    # Edge behavior: float result expected, not int
    assert isinstance(mean([2, 3]), float)

if __name__ == "__main__":
    try:
        run_checks()
        sys.exit(0)   # success  GOOD commit
    except Exception as e:
        # You can print e for debugging if you want:
        # print(f"FAILED: {e}")
        sys.exit(1)   # failure  BAD commit

