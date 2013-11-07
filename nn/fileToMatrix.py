def get_data(filepath):
    """
    Returns the information specified in
    the assigned file as a list of tuples.
    Values are delimited by spaces. A variable
    amount of inputs can be inserted.
    The last member of each line is the output.
    """

    with open(filepath) as input_file:
        return [tuple([float(item) for item in line.strip().split(' ')]) for line in input_file]
