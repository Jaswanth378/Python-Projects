# Cache Management Algorithms

This Python script implements two cache management algorithms: First-In-First-Out (FIFO) and Least Frequently Used (LFU).

## Author

- Name: Jaswanth Kattubavi Sreenivasulu

## Algorithms

### FIFO (First-In-First-Out)

The FIFO algorithm manages the cache by removing the oldest item when the cache is full. It follows the principle of "first in, first out."

### LFU (Least Frequently Used)

The LFU algorithm manages the cache by removing the least frequently used item when the cache is full. It keeps track of the frequency of each item in the cache and removes the item with the lowest frequency.

## Usage

1. Run the script using Python.
2. Enter a series of integers representing the requests, one per line. Press Enter without entering a value to finish the input.
3. Enter the preference for the cache management algorithm:
   - Enter "1" for FIFO algorithm.
   - Enter "2" for LFU algorithm.
   - Enter "Q" to quit the program.
4. The script will simulate the cache management algorithm based on the provided requests and cache size.
5. The final state of the cache will be displayed.
