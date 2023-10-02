class SimpleMemoryManager:
    def __init__(self, size=128):
        self.memory = [None] * size  # Initialize memory with None
        self.size = size
        self.free_list = list(range(size))  # List of free indices
    
    def allocate(self, size):
        if size > len(self.free_list):
            raise MemoryError("Not enough memory available")
        
        allocated_indices = self.free_list[:size]
        self.free_list = self.free_list[size:]
        
        # Return the start index as a "pointer"
        return allocated_indices[0]
    
    def deallocate(self, pointer, size):
        deallocated_indices = list(range(pointer, pointer + size))
        
        for index in deallocated_indices:
            if index not in self.free_list and 0 <= index < self.size:
                self.memory[index] = None
                self.free_list.append(index)
            else:
                raise ValueError(f"Index {index} is not allocated or out of bounds")
        
        self.free_list.sort()
    
    def write(self, pointer, data):
        if pointer not in self.free_list and 0 <= pointer < self.size:
            self.memory[pointer] = data
        else:
            raise ValueError(f"Pointer {pointer} is not allocated or out of bounds")
    
    def read(self, pointer):
        if pointer not in self.free_list and 0 <= pointer < self.size:
            return self.memory[pointer]
        else:
            raise ValueError(f"Pointer {pointer} is not allocated or out of bounds")


# Example Usage
memory_manager = SimpleMemoryManager()

# Allocate 10 units of memory
pointer = memory_manager.allocate(10)

# Write data to the allocated memory
for i in range(10):
    memory_manager.write(pointer + i, i * 10)

# Read data from the allocated memory
for i in range(10):
    print(memory_manager.read(pointer + i))

# Deallocate the allocated memory
memory_manager.deallocate(pointer, 10)
