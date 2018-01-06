"""
There is a queue for the self-checkout tills at the supermarket. Your task is write a function to calculate the total
time required for all the customers to check out!

The function has two input variables:

customers: an array (list in python) of positive integers representing the queue. Each integer represents a customer,
and its value is the amount of time they require to check out.
n: a positive integer, the number of checkout tills.

The function should return an integer, the total time required.
"""


def queue_time(customers, n):
    tills = {}
    time = 0
    for i in range(n):
        tills[i] = 0
    print(tills)
    while len(customers):
        for key in tills:
            if tills[key] == 0 and len(customers):
                tills[key] = customers.pop(0)
        for key in tills:
            tills[key] -= 1
        time += 1
    m = 0
    for key in tills:
        m = max((tills[key], m))

    return time + m

print(queue_time([1,2,3,4,5], 1))