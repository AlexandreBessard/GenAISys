import sys
# How many items from data can I take before their total size in memory exceeds a limit
def get_batch_size(data, limit=4000000):
    batch_size = 0
    total_size = 0
    # Each item expect to be a dictionary
    # item example:
    # {
    #     "id": 1,
    #     "text": "hello",
    #     "score": 0.95
    # }
    for item in data:
        # Measure size of one item at the time
        # values() gets all the values in the dictionary
        # ["hello", 0.95]
        # For each value, measure its memory size:
        # [54, 24]
        # sum adds them together: 78
        item_size = sum([sys.getsizeof(v) for v in item.values()])
        if total_size + item_size > limit:
            break
        total_size += item_size
        batch_size += 1
    return batch_size