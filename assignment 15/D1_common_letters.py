## assignment 15

# dæmi 1


def make_set(first,last):
    first_set = set(first)
    last_set = set(last)
    return first_set, last_set


def intersection_list(first, last):
    result_list = []
    for elem in first:
        if elem in last:
            if elem not in result_list:
                result_list.append(elem)
    return result_list


def intersection_set(first_set, last_set):
    return first_set & last_set     


def main():
    name = input('Enter name: ').lower()
    first, last = name.split(' ')
    #print(first,last)

    # aðferð 1
    intersec_list = intersection_list(first, last)
    print(sorted(intersec_list))

    # aðferð 2
    first_set, last_set = make_set(first,last)
    intersec_set = intersection_set(first_set,last_set)
    print(sorted(intersec_set))
main()
