def get_data(filepath):
    """
    Returns the JSON information specified in
    the assigned file as a JSON object.
    """

    with open(filepath) as input_file:
        return [tuple([float(item) for item in line.strip().split(' ')]) for line in input_file]
