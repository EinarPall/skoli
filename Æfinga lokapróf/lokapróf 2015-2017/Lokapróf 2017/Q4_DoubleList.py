

class DoubleList(object): # holds a list of real numbers
    # when instance constructed, amount of numbers the instance should hold 
    # ...must be stated

    def __init__(self, size):
        self.size = size


    def number (self, num):
        self.number = num

    def setAt(self, index, value):#sets given value to the given index
        # .... if index is outside the array do nothing
       #if index out of range do nothing
        if value <= len(self.list):

            self.list.replace(self.list[index],value)
        else:
            pass
        return self.list


    def print_list(self,a_list):
        #output each element of the list separated with a space
        self.list_output = a_list.replace(',', ' ')
        print (self.list_output)

    def get_list(self):
        # input as many numbers as the size of the list
        self.list = input('Input list of numbers separated by commas: ').split(',')
        if len(self.list) <= 
        return self.list
    
    def two_lists(self, other):
        #add lists together #first list followed by second list
        list_sum = self.list + other.list
        return list_sum

def main():
    size_of_list = int(input('Input size of list: '))
    size = DoubleList(size_of_list)
    
    a_list = DoubleList.get_list(size)
    print_list = print_list()
    some_index = int(input('Input index to replace: '))
    some_value = int(input('Input value to replace at index: '))
    new_list = setAt(some_index, some_value)
    print(new_list)


main()