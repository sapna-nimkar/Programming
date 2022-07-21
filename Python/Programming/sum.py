def my_sum(*args) -> int:
    result = 0
    for item in args:
        result += item
    return result

def full_name(first_name: str, last_name: str) -> str:
    return f"{first_name} {last_name}"


if __name__ == '__main__':

    print(my_sum(10, 50, 20, 30))
    
    my_nums = (10, 50, 20, 30, 40)
    #(a, b, c, d) = my_nums
    print()
    my_sum(*my_nums)
    my_sum(my_nums[0], my_nums[1], my_nums[2], my_nums[3], my_nums[4])

    user = {"first_name": "Sapna", "last_name": "Nimkar"}
    print(full_name(**user))