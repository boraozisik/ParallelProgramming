import time
import tracemalloc


def performance(function):
    def _performance(*args, **kwargs):
        if not hasattr(performance, "counter"):
            performance.counter = 0
            performance.total_time = 0
            performance.total_mem = 0

        performance.counter += 1

        started_time = time.perf_counter()

        tracemalloc.start()

        function_result = function(*args, **kwargs)

        ended_time = time.perf_counter()

        execution_time = ended_time - started_time

        performance.total_time += execution_time
        performance.total_mem += tracemalloc.get_traced_memory()[1]

        return function_result

    return _performance

def format_memory(memory_bytes):
    """
        This function takes memory value as bytes
        and converts it to kilobits or megabits.

        :param memory_bytes: First param.
        :type memory_bytes: int
        :return: kilobits or megabits.
    """

    if memory_bytes < 8:
        return f"{memory_bytes} b"
    elif memory_bytes < 8 * 1024:
        return f"{memory_bytes / 8:.2f} Kb"
    else:
        return f"{memory_bytes / (8 * 1024):.2f} Mb"


@performance
def function_will_be_measured():
    print('My name is Bora')

for i in range(9):
    function_will_be_measured()


print("Total function calls:", performance.counter)
print(f"Total execution time is {performance.total_time} seconds")
print("Total memory used:",format_memory(performance.total_mem))