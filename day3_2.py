def highest_bit(nums, index):
    ones_count = sum(x[index] for x in nums)
    return int(ones_count >= (len(nums) / 2))

def oxygen_generator_rating(numbers):
    def filter_oxygen(nums, index=0):
        bit = highest_bit(nums, index)

        nums = [n for n in nums if bit == n[index]]
        if len(nums) == 1:
            return nums[0]
        return filter_oxygen(nums, index + 1)

    return int("".join(str(x) for x in filter_oxygen(numbers)), 2)

def co2_scrubber_rating(numbers):
    def filter_co2(nums, index=0):
        bit = highest_bit(nums, index)

        nums = [n for n in nums if bit != n[index]]
        if len(nums) == 1:
            return nums[0]
        return filter_co2(nums, index + 1)

    return int("".join(str(x) for x in filter_co2(numbers)), 2)

def main():
    with open('input3.txt') as f:
        lines = [n.strip() for n in f.readlines()]

    # Turn binary strings (0010001) into lists of numbers ([0, 0, 1, 0, 0, 0, 1])
    numbers = [[int(x) for x in l] for l in lines]

    o_rating = oxygen_generator_rating(numbers)
    print(f"oxygen generator rating: {o_rating}")
    co2_rating = co2_scrubber_rating(numbers)
    print(f"co2 scrubber rating: {co2_rating}")
    print(f"answer: {o_rating*co2_rating}")

if __name__ == '__main__':
    main()