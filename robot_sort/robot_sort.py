class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"
    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"
    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # given the rules of the sort game it looks like a modification to Bubble sort will work
        # Can use the light on or off to toggle the swaps or lack thereof
        # use the compare and swap instead of using the val at (pointer) to the val at (pointer + 1)
        # light on == True will be a 1 and the loop will exit (a swap did not occur on this pass through the list and the list is sorted True means done)
        # light on == False will be a zero and the loop will continue (a swap has happened and false means go)
        
        while self.light_is_on() == False: # need this toggle to get the outer loop started
            self.set_light_on()    # Tun on so that when a swap occurs you can turn it off
        
            # as long as you are able to move left, swap the current item, move left and repeat
            while self.can_move_left() == True:
                self.swap_item()
                self.move_left()

                # if current item < 0 (), swap the item and turn off the light
                if self.compare_item() < 0:
                    self.swap_item()
                    self.set_light_off()

                # move to the right. If there is an item, pick it up and move left
                self.move_right()
                self.swap_item()
                self.move_left()

            # repeat the above steps for moving to the right. (Reverse the compare logic and move steps)
            while self.can_move_right() == True:
                self.swap_item()
                self.move_right()

                if self.compare_item() > 0:
                    self.swap_item()
                    self.set_light_off()

                self.move_left()
                self.swap_item()
                self.move_right()

        # while self.can_move_right():
        #     # while there is room to the right, check if item is less value, 
        #     # if true grab it and move right, else just move right
        #     if self.compare_item() == -1 or self.compare_item() is None:
        #         self.swap_item()
        #         self.move_right()
        #     else:
        #         self.move_right()
        #     # while there is room to the left,check if item has greater value, 
        #     # if so, grab it and move left, else just go left young man
        # while self.can_move_left():
        #     if self.compare_item() == 1:
        #         self.swap_item()
        #         self.move_left()
        #     else:
        #         self.move_left()
        # if self._item is not None:
        #     self.sort()


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [15, 41, 58, 49, 26, 4, 28, 8, 61, 60, 65, 21, 78, 14, 35, 90, 54, 5, 0, 87, 82, 96, 43, 92, 62, 97, 69, 94, 99, 93, 76, 47, 2, 88, 51, 40, 95, 6, 23, 81, 30, 19, 25, 91, 18, 68, 71, 9, 66, 1, 45, 33, 3, 72, 16, 85, 27, 59, 64, 39, 32, 24, 38, 84, 44, 80, 11, 73, 42, 20, 10, 29, 22, 98, 17, 48, 52, 67, 53, 74, 77, 37, 63, 31, 7, 75, 36, 89, 70, 34, 79, 83, 13, 57, 86, 12, 56, 50, 55, 46]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)