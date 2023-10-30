#!/usr/bin/env python3


class Queue(object):
    def __init__(self, size):
        self.__maxSize = size  # size of circular array
        self.__queue = [None] * size  # queue stored as empty list
        self.__front = 1  # empty queue has front 1 (index)
        self.__rear = 0  # after rear and  (index)
        self.__nItems = 0  # no items in queue

    def insert(self, item):
        """
        Insert item as the rear of the queue if it's not full
        """
        if self.isFull():
            raise Exception("Queue overflow")
        self.__rear += 1  # move rear one to the right
        if self.__rear == self.__maxSize:  # wrap around the circular array
            self.__rear = 0
        self.__queue[self.__rear] = item  # store new item at rear
        self.__nItems += 1
        return True

    def remove(self):
        """
        Remove front item from the queue and shift the front pointer to the
        next item
        """
        if self.isEmpty():
            raise Exception("Queue underflow")
        front = self.__queue[self.__front]  # get value at front
        self.__queue[self.__front] = None  # remove reference
        self.__front += 1  # move front pointer to the next item
        if self.__front == self.__maxSize:  # wrap around
            self.__front = 0
        self.__nItems -= 1
        return front

    def remove_josephus(self, index):
        if self.isEmpty():
            raise Exception("Queue underflow")
        items_remaining = self.__nItems  # items remaining after each "elmination"
        index_pointer = index  # where we'll start eliminating
        eliminated = []

        # eliminate where we're starting
        eliminated.append((self.__queue[index_pointer], index_pointer))
        self.__queue[index_pointer] = None
        items_remaining -= 1
        count = 0

        # start elminating the remaining soldiers
        while items_remaining > 1:
            # find the next non-null element
            index_pointer = (index_pointer + 1) % self.__maxSize
            if self.__queue[index_pointer] == None:
                continue

            # if it is not null
            count += 1

            if count == index:
                eliminated.append((self.__queue[index_pointer], index_pointer))
                self.__queue[index_pointer] = None
                items_remaining -= 1
                count = 0

        index_pointer = 0
        while True:
            if self.__queue[index_pointer] != None:
                survivor = self.__queue[index_pointer]
                break
            index_pointer += 1

        print("\nEliminating order (name, original position):")
        for i in range(len(eliminated)):
            print(f"{i+1}. {eliminated[i]}")
        print(f"The survivor is {survivor} at the original spot {index_pointer}")

    def peek(self):
        """
        Return frontmost item
        """
        return None if self.isEmpty() else self.__queue[self.__front]

    def isEmpty(self):
        return self.__nItems == 0

    def isFull(self):
        return self.__nItems == self.__maxSize

    def __len__(self):
        return self.__nItems

    def __str__(self):
        ans = "["
        for i in range(self.__nItems):
            if len(ans) > 1:  # format first item
                ans += ", "
            j = i + self.__front
            if j >= self.__maxSize:  # wrap around
                j -= self.__maxSize
            ans += str(self.__queue[j])
        ans += "]"
        return ans


soldiers = []
num_soldiers = int(input("How many soldiers? > "))
print("Enter soldier's names:")
for i in range(num_soldiers):
    soldier = input("> ")
    soldiers.append(soldier)

# insert names into queue
queue = Queue(num_soldiers)
for soldier in soldiers:
    queue.insert(soldier)

position = int(input("\nEnter n-th position to eliminate > "))
queue.remove_josephus(position)