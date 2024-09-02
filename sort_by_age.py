def sort_by_age(tuples_list):
    # Sort tuples by age (second element)
    return sorted(tuples_list, key=lambda x: x[1])

# Example usage
if __name__ == "__main__":
    data = [("Alice", 30), ("Bob", 25), ("Charlie", 35)]
    sorted_data = sort_by_age(data)
    print("Sorted by age:", sorted_data)
