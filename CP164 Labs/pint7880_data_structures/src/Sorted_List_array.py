"""
-------------------------------------------------------
Array version of the Sorted_List ADT.
-------------------------------------------------------
Author:  Melissa Pinto
ID:      190647880
Email:   pint7880@wlu.ca
Term:    Winter 2020
__updated__ = "2020-01-16"
-------------------------------------------------------
"""
from copy import deepcopy


class Sorted_List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty Sorted_List.
        Use: target = Sorted_List()
        -------------------------------------------------------
        Returns:
            a Sorted_List object (Sorted_List)
        -------------------------------------------------------
        """
        self._values = []

    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if source contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if source contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """

        return self._binary_search(key) != -1

    def __getitem__(self, i):
        """
        ---------------------------------------------------------
        Returns a copy of the nth element of source.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of source (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'

        return deepcopy(self._values[i])

    def __len__(self):
        """
        -------------------------------------------------------
        Returns the size of a sorted list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in source.
        -------------------------------------------------------
        """
        
        return len(self._values)

    def _binary_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the sorted list. 
        Performs a stable search.
        Private helper method - used only by other ADT methods.
        Use: i = self._binary_search(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the index of the first occurrence of key in
                the list, -1 if key is not found. (int)
        -------------------------------------------------------
        """
        i = 0
        j = len(self._values) - 1
        while i <= j:
            m = (i + j) // 2
            if key == self._values[m]:
                return m
            elif self._values[m] < key:
                j = m - 1
            elif key < self._values[m]:
                i = m + 1

        return -1

    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(Sorted_List) to len(Sorted_List) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        return i >= -len(self._values) and i <= len(self._values) - 1

    def clean(self):
        """
        ---------------------------------------------------------
        Removes duplicates from source.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            source contains one and only one of each value formerly present
            in source. The first occurrence of each value is preserved.
        -------------------------------------------------------
        """
        i = len(self) - 1
        while i > 0:
            for j in range(0, i):
                if self._values[i] == self._values[j]:
                    self._values.pop(i)
            i -= 1

        return

    def _sort(self):
        """
        ---------------------------------------------------------
        Helper function for sorting.
        Use: source.sort()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        for i in range(len(self._values)):
            for j in range(i + 1, len(self._values)):
                if self._values[j] < self._values[i]:
                    self._values[i], self._values[j] = self._values[j], self._values[i]

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Values are sorted.
        (iterative algorithm)
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.extend(source1._values)
        self._values.extend(source2._values)
        source1._values = []
        source2._values = []
        self._sort()

        return

    def copy(self):
        """
        ---------------------------------------------------------
        Copies the contents of this list to another sorted list.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a sorted list containing a copy of the contents 
                of source (Sorted_List)
        -------------------------------------------------------
        """
        l = Sorted_List()
        l._values = deepcopy(self._values)

        return l

    def count(self, key):
        """
        -------------------------------------------------------
        Determines the number of times key appears in source.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            number - the number of times key appears in source (int)
        -------------------------------------------------------
        """
        i = 0
        for v in self._values:
            if v == key:
                i += 1

        return i

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of value in source that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        index = self._binary_search(key)
        if index != -1:
            return deepcopy(self._values[index])

        return None

    def index(self, key):
        """
        -------------------------------------------------------
        Finds the location of the first occurrence of key in source.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            i - the location of the value matching key, otherwise -1 (int)
        -------------------------------------------------------
        """
        return self._binary_search(key)

    def insert(self, value):
        """
        -------------------------------------------------------
        Inserts value at the proper place in source.
        Must be a stable insertion, i.e. consecutive insertions
        of the same value must keep their order preserved.
        Use: source.insert(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))
        self._sort()

        return

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values = []
        for v in source1._values:
            if v not in self._values and v in source2._values:
                self._values.append(v)
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if source is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if source is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values) == 0

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are is_identical, i.e. same values appear
        in the same locations in both lists. (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (Sorted_List)
        Returns:
            identical - True if source contains the same values as target
                in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        if len(self) != len(target):
            return False
        for i in range(len(self)):
            if self[i] != target[i]:
                return False
        return True

    def max(self):
        """
        -------------------------------------------------------
        Returns the maximum value in source.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'

        
        return deepcopy(self._values[-1])

    def min(self):
        """
        -------------------------------------------------------
        Returns the minimum value in source.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'

        return deepcopy(self._values[0])

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in source.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in source (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty list'

        return deepcopy(self._values[0])

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in source with index i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
                args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], otherwise 
                the last value in source, value is removed from source (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in source
        that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        index = self._binary_search(key)
        if index == -1:
            return None
        return self._values.pop(index)

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first item in source.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty list'

        return self.pop(0)

    def remove_many(self, key):
        """
        ---------------------------------------------------------
        Removes all values that match key in source.
        Use: source.remove_many(key)
        ---------------------------------------------------------
        Parameters:
            key - the key to match (?)
        Returns:
            None
        ---------------------------------------------------------
        """
        index = self._binary_search(key)
        while index != -1:
            self._values.pop(index)
            index = self._binary_search(key)

        return

    def split(self):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. source becomes empty.
        Use:  target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (Sorted_List)
            target2 - a new List with <= 50% of the original List (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        if len(self) % 2 == 0:
            target1._values = self._values[:len(self._values) // 2]
            target2._values = self._values[len(self._values) // 2:]
        else:
            target1._values = self._values[:len(self._values) // 2 + 1]
            target2._values = self._values[len(self._values) // 2 + 1:]
        self._values = []
        return target1, target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Split a List into two parts. target1 contains the even indexed
        elements, target2 contains the odd indexed elements.
        Order of target1 and target2 is not significant. 
        source is empty after the function executes.
        (iterative version)
        Use: target1, target2 = source.split_alt()
        -------------------------------------------------------
        Returns:
            target1 - the even indexed elements of the list (Sorted_List)
            target2 - the odd indexed elements of the list (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        for i in range(len(self._values)):
            if i % 2 == 0:
                target1._values.append(self._values[i])
            else:
                target2._values.append(self._values[i])
        self._values = []
        return target1, target2

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        for v in self._values:
            if func(v):
                target1._values.append(v)
            else:
                target2._values.append(v)

        return target1, target2

    def split_key(self, key):
        """
        ---------------------------------------------------------
        Splits list into two parts. target1 contains all values < key,
        target2 all values >= key. source becomes empty.
        Use:  target1, target2 = source.split_key(key)
        -------------------------------------------------------
        Returns:
            target1 - a new List with values < key (Sorted_List)
            target2 - a new List with values >= key (Sorted_List)
        -------------------------------------------------------
        """
        target1 = Sorted_List()
        target2 = Sorted_List()
        for v in self._values:
            if v < key:
                target1._values.append(v)
            else:
                target2._values.append(v)

        return target1, target2

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (Sorted_List)
            source2 - an array-based list (Sorted_List)
        Returns:
            None
        -------------------------------------------------------
        """
        for v in source1._values:
            if v not in self._values:
                self._values.append(deepcopy(v))
        for v in source2._values:
            if v not in self._values:
                self._values.append(deepcopy(v))
        self._sort()
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through source
        from front to rear.
        Use: for value in source:
        -------------------------------------------------------
        Returns:
            value - the next value in source (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value
