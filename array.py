from itertools import chain

class Array:

    def __init__(self, shape, *values):
        """
        
        Initialize an array of 1-dimensionality. Elements can only be of type:
        - int
        - float
        - bool
        
        Make sure that you check that your array actually is an array, which means it is homogeneous (one data type).
        Args:
            shape (tuple): shape of the array as a tuple. A 1D array with n elements will have shape = (n,).
            *values: The values in the array. These should all be the same data type. Either numeric or boolean.
        Raises:
            ValueError: If the values are not all of the same type.
            ValueError: If the number of values does not fit with the shape.
        """
        
        # Check if the values are of valid type
        self._array = []
        if len(shape) == 2:
            if shape[1] == 0:
                self.shape = (shape[0], )
            else:
                self.shape = shape
        else:
            self.shape = shape
        self.values = values 
        # print(len(values))
        self._type_vals = type(values[0])
        if len(shape) == 2:
            if shape[0]*shape[1] != len(values): 
                raise ValueError(f"Must have the same number of values as shape {shape} specifies! {values}")
        elif len(shape) == 1:
            if shape[0] != len(values): 
                raise ValueError(f"Must have the same number of values as shape {shape} specifies! {values}")
        elif (len(shape) > 2) or (len(shape) < 1):
                raise ValueError(f"Len(shape) must be either 1 or 2!")
        elif shape[0] < 1 or shape[1] < 1:
            raise ValueError("Cannot have empty Array or negative shape!")

        # Initialize the array.
        # If shape[1] != 0 we represent the two dimensions as a nested list with one list for
        # each row of the array. 
        counter_i = 0
        counter_j = 0 
        if len(shape) == 2: 
            array_list = [[0]*shape[1] for i in range(0, shape[0])]
       
        for val in values:
            if not isinstance(val, (int, float, bool)):  
                raise ValueError("Array can only be of type int, float or bool!")
            elif not type(val) == self._type_vals:
                raise ValueError("Array must be homogenous!")
            elif len(shape) == 1:
                self._array.append(val)
            
            elif len(shape) == 2:
                if counter_j < shape[1]-1:
                    array_list[counter_i][counter_j] = val
                    counter_j += 1
                    
                else:
                    array_list[counter_i][counter_j] = val
                    counter_j = 0
                    counter_i += 1
                
        if len(shape) == 2:
            self._array = array_list

        # Define flat array and flat_shape to use with some of the methods
        if len(shape) == 2:
            self._flat_array = self.flat_array()
            self.flat_shape = (len(self._flat_array), )
        else:
            self._flat_array = self._array
            self.flat_shape = self.shape

        # print(self._array)

    def __str__(self):
        """Returns a nicely printable string representation of the array.
        Returns:
            str: A string representation of the array.
        """
        if len(self.shape) == 1:
            str = "["
            for val in self._array[:-1]:
                str += f"{val}, "
            str += f"{self._array[-1]}]"
            return str 
        else:
            str = ""
            for list_ in self._array:
                str += " | "
                for val in list_:
                    str += f" {val:3} "
                str += " | \n"
            return str

    def __getitem__(self, item):
        """Returns value of item in array.
            Args:
                item (int): Index of value to return.
            Returns:
                value: Value of the given item.
        """
        return self._array[item]
        
    def flat_array(self):
        """Flattens the N-dimensional array of values into a 1-dimensional array.
        Returns:   
            list: flat list of array values
        """
        if (self.shape[1] == None) or (self.shape[1] == 0):
            return self._array
        flat_array = self._array 
        for _ in range(len(self.shape[1:])):
            flat_array = list(chain(*flat_array))
        return flat_array

    def __add__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        
        # check that the method supports the given arguments (check for data type and shape of array)
        # If the shapes are unequal we add them together anyway
        if not isinstance(self, (Array, int, float) or not isinstance(other, (Array, int, float))):
            raise TypeError(f"Unvalid arguments for +: {type(self)} + {type(other)}. Must be Array, int or float!")
        elif isinstance(self, (Array)) and isinstance(other, (Array)):
            new_list = []
            if self.flat_shape == other.flat_shape:
                for i in range(0, self.flat_shape[0]):
                    new_list.append(self._flat_array[i] + other._flat_array[i])
                return Array(self.shape, *new_list)
            
            else:
                raise ValueError(f"operands could not be broadcast together with shapes {self.shape} {other.shape}")
        elif isinstance(self, (Array)) and isinstance(other, (int, float)):
            new_list = []
            for i in range(0, self.flat_shape[0]):
                new_list.append(self._flat_array[i] + other)
            return Array(self.shape, *new_list)  
        else:
            return NotImplemented

    def __radd__(self, other):
        """Element-wise adds Array with another Array or number.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to add element-wise to this array.
        Returns:
            Array: the sum as a new array.
        """
        return self.__add__(other)
                
    def __sub__(self, other):
        """Element-wise subtracts an Array or number from this Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to subtract element-wise from this array.
        Returns:
            Array: the difference as a new array.
        """
        # check that the method supports the given arguments (check for data type and shape of array)
        # If the shapes are unequal we add them together anyway
        if not isinstance(self, (Array, int, float) or not isinstance(other, (Array, int, float))):
            raise TypeError(f"Unvalid arguments for -: {type(self)} - {type(other)}. Must be Array, int or float!")
        elif isinstance(self, (Array)) and isinstance(other, (Array)):
            new_list = []
            if self.shape == other.shape:
                for i in range(0, self.flat_shape[0]):
                    new_list.append(self._flat_array[i] - other._flat_array[i])
                return Array(self.shape, *new_list)
            else:
                raise ValueError(f"operands could not be broadcast together with shapes {self.shape} {other.shape}")
        elif isinstance(self, (Array)) and isinstance(other, (int, float)):
            new_list = []
            for i in range(0, self.flat_shape[0]):
                new_list.append(self._flat_array[i] - other)
            return Array(self.shape, *new_list)  
        else:
            return NotImplemented

    def __rsub__(self, other):
        """Element-wise subtracts this Array from a number or Array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number being subtracted from.
        Returns:
            Array: the difference as a new array.
        """
        return self.__sub__(other)

    def __mul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        # check that the method supports the given arguments (check for data type and shape of array)
        # If the shapes are unequal we add them together anyway
        if not isinstance(self, (Array, int, float) or not isinstance(other, (Array, int, float))):
            raise TypeError(f"Unvalid arguments for *: {type(self)} * {type(other)}. Must be Array, int or float!")
        elif isinstance(self, (Array)) and isinstance(other, (Array)):
            new_list = []
            if self.shape == other.shape:
                for i in range(0, self.flat_shape[0]):
                    new_list.append(self._flat_array[i] * other._flat_array[i])
                return Array(self.shape, *new_list)
            else:
                raise ValueError(f"operands could not be broadcast together with shapes {self.shape} {other.shape}")
        elif isinstance(self, (Array)) and isinstance(other, (int, float)):
            new_list = []
            for i in range(0, self.flat_shape[0]):
                new_list.append(self._flat_array[i] * other)
            return Array(self.shape, *new_list)  
        else:
            return NotImplemented

    def __rmul__(self, other):
        """Element-wise multiplies this Array with a number or array.
        If the method does not support the operation with the supplied arguments
        (specific data type or shape), it should return NotImplemented.
        Args:
            other (Array, float, int): The array or number to multiply element-wise to this array.
        Returns:
            Array: a new array with every element multiplied with `other`.
        """
        # Hint: this solution/logic applies for all r-methods
        return self.__mul__(other)

    def __eq__(self, other):
        """Compares an Array with another Array.
        If the two array shapes do not match, it should return False.
        If `other` is an unexpected type, return False.
        Args:
            other (Array): The array to compare with this array.
        Returns:
            bool: True if the two arrays are equal (identical). False otherwise.
        """
        if not isinstance(other, (Array)):
            return False 
        elif not self.shape == other.shape:
            return False
        else:
            for i in range(0, self.flat_shape[0]):
                if self._flat_array[i] != other._flat_array[i]:
                    return False
            return True 

    def is_equal(self, other):
        """Compares an Array element-wise with another Array or number.
        If `other` is an array and the two array shapes do not match, this method should raise ValueError.
        If `other` is not an array or a number, it should return TypeError.
        Args:
            other (Array, float, int): The array or number to compare with this array.
        Returns:
            Array: An array of booleans with True where the two arrays match and False where they do not.
                   Or if `other` is a number, it returns True where the array is equal to the number and False
                   where it is not.
        Raises:
            ValueError: if the shape of self and other are not equal.
        """
        if not isinstance(other, (Array, int, float)):
            return False 
        elif isinstance(other, (Array)) and self.shape != other.shape: 
            return False
        elif isinstance(other, (Array)):
            new_list = []
            for i in range(0, self.flat_shape[0]):
                if self._flat_array[i] == other._flat_array[i]:
                    new_list.append(True)
                else:
                    new_list.append(False)
            return Array(self.shape, *new_list)
        else:
            new_list = []
            for i in range(0, self.flat_shape[0]):
                if self._flat_array[i] == other:
                    new_list.append(True)
                else:
                    new_list.append(False)
            return Array(self.shape, *new_list)
        
    def min_element(self):
        """Returns the smallest value of the array.
        Only needs to work for type int and float (not boolean).
        Returns:
            float: The value of the smallest element in the array.
        """
        if isinstance(self._type_vals, (bool)):
            raise ValueError("type bool has no minimal element!")
        min_val = self._flat_array[0]
        print(self._flat_array)
        for i in range(1, self.flat_shape[0]):
            if self._flat_array[i] < min_val:
                min_val = self._flat_array[i]
        return min_val


if __name__ == '__main__':
    pass
    

 