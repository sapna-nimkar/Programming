from mymodule import my_func
from MyMainPackage import some_main_script
from MyMainPackage.SubPackage import my_subscript

my_func()
my_subscript.second_sub_report()
some_main_script.report_main()


# Hackerrank Lisa's workbook
def workbook(n, k, arr):
    # Write your code here
    pages = List(set(int))
    total_pages = 0

    for i in range(len(arr)):  # chapter iteration
        pages_in_chapter = 0
        quotient = arr[i] // k
        remainder = arr[i] % k
        if (remainder > 0):
            pages_in_chapter = quotient + 1
        else:
            pages_in_chapter = quotient
        total_pages += pages_in_chapter
