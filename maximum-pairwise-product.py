def max_product(nums):
    m = nums.max()
    nums.remove(m)
    n = nums.max()
    return m*n


if __name__ == "__main__":
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_product(input_numbers))
