def delete_lines_between_indices(original_file, start_index, end_index):
    with open(original_file, 'r') as f:
        lines = f.readlines()

    # Filter out lines between start_index and end_index
    lines = [line for i, line in enumerate(lines) if i < start_index or i > end_index]

    with open(original_file, 'w') as f:
        f.writelines(lines)

if __name__ == "__main__":
    original_file = 'final_output.inp'
    start_index = 791  # Index of the first line to keep (inclusive)
    end_index = 912    # Index of the last line to keep (inclusive)

    delete_lines_between_indices(original_file, start_index, end_index)


tr_remove = "".join(map(str, remove))