from decorators import timer


@timer
def do_a_calculation(num_times):
    for _ in range(num_times):
        print(_)
        print(sum([i ** 2 for i in range(10000000)]))


do_a_calculation(10)
