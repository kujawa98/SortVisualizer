import copy

import random

from window import Window

WINDOW_WIDTH, WINDOW_HEIGHT = 624, 720


class ArrRenderer:
    def __init__(self):
        self.arr = [i for i in range(312, 0, -1)]
        random.shuffle(self.arr)
        self.or_arr = copy.copy(self.arr)
        self.screen = Window(self)

    def bubble_sort(self):
        self.arr = copy.copy(self.or_arr)
        for i in range(len(self.arr) - 1):
            for j in range(len(self.arr) - 1 - i):
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                self.render_arr()

    def partition(self, left, right):
        i = (left - 1)
        pivot = self.arr[right]

        for j in range(left, right):
            if self.arr[j] <= pivot:
                i = i + 1
                self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
                self.render_arr()
        self.arr[i + 1], self.arr[right] = self.arr[right], self.arr[i + 1]
        return (i + 1)

    def quickSort(self, left, right):
        if len(self.arr) == 1:
            return self.arr
        if left < right:
            pivot = self.partition(left, right)

            self.quickSort(left, pivot - 1)
            self.quickSort(pivot + 1, right)

    def render_arr(self):
        self.screen.update_window()


if __name__ == '__main__':
    arr_ren = ArrRenderer()
    # arr_ren.bubble_sort()
    # arr_ren.arr = copy.copy(arr_ren.or_arr)
    arr_ren.quickSort(0, len(arr_ren.arr) - 1)
