import itertools

def split(nums, index):
    "split nums into two lists based on item at position index"
    a, b = itertools.tee(nums)
    return ([item for item in a if item[index] == 0],
            [item for item in b if item[index] == 1])

def most_common(zeros, ones):
    "return the largest list"
    return zeros if len(zeros) > len(ones) else ones

def least_common(zeros, ones):
    "return the smallest list"
    return zeros if len(zeros) <= len(ones) else ones

def filter_nums(nums, pred, index=0):
    zeros, ones = split(nums, index)
    nums = pred(zeros, ones)
    return nums[0] if len(nums) == 1 else filter_nums(nums, pred, index + 1)

def digit_list_to_int(l):
    "turn list of binary digits (e.g. [0, 1, 0, 1]) into int"
    return int("".join(str(x) for x in l), 2)

def oxygen_generator_rating(numbers):
    return digit_list_to_int(filter_nums(numbers, most_common))

def co2_scrubber_rating(numbers):
    return digit_list_to_int(filter_nums(numbers, least_common))

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