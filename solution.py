import heapq

class Solution:
  """
  Solves the most frequent books problem.
  """
  def mostFrequentBooks(self, A, B):
    """
    Calculates the highest number of copies for any single book at each step.

    Args:
      A: A list of integers representing book IDs.
      B: A list of integers representing the change in book copies.

    Returns:
      A list of integers where each element is the maximum number of copies
      of any book after the corresponding step.
    """
    book_counts = {}
    count_freq = {}
    # Use a min-heap to simulate a max-heap by storing negative counts
    counts_max_heap = []
    result = []

    for i in range(len(A)):
        book_id = A[i]
        change = B[i]

        # --- Update based on the old count of the book ---
        old_count = book_counts.get(book_id, 0)
        if old_count > 0:
            count_freq[old_count] -= 1
            # Stale entries in the heap will be cleaned up lazily later.

        # --- Update the book's count ---
        new_count = old_count + change
        book_counts[book_id] = new_count

        # --- Update based on the new count of the book ---
        if new_count > 0:
            current_freq = count_freq.get(new_count, 0)
            # If this count is appearing for the first time, add it to the heap.
            if current_freq == 0:
                heapq.heappush(counts_max_heap, -new_count)
            count_freq[new_count] = current_freq + 1

        # --- Find the current maximum count ---
        # Clean up stale entries from the top of the heap.
        # A stale entry is a count that is no longer present for any book.
        while counts_max_heap and count_freq.get(-counts_max_heap[0], 0) == 0:
            heapq.heappop(counts_max_heap)

        if not counts_max_heap:
            result.append(0)
        else:
            result.append(-counts_max_heap[0])

    return result

# The verification block has been removed for final submission.
if __name__ == '__main__':
    pass
