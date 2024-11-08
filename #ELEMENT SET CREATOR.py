# Define the name of the node set representing the face
face_node_set_name = "FaceNodes"

# Define the name of the element set representing the face
face_element_set_name = "FaceElements"

# Initialize a set to store node labels
face_node_labels = set()

# Open the .inp file for reading
with open("last.inp", "r") as file:
    # Flag to indicate if we are parsing the node set
    parsing_node_set = False

    # Read the file line by line
    for line in file:
        # Split the line into tokens
        tokens = line.strip().split(",")

        # Check if the line defines a node set
        if tokens[0] == "*Nset":
            if tokens[1].strip() == face_node_set_name:
                parsing_node_set = True
            else:
                parsing_node_set = False
        # Check if we are parsing node labels
        elif parsing_node_set and len(tokens) > 1:
            # Attempt to convert the token to an integer (node label)
            try:
                label = int(tokens[0])
                face_node_labels.add(label)
            except ValueError:
                pass  # Skip the line if conversion fails

# Create or update the element set representing the face
with open("last.inp", "a") as file:
    file.write("*Elset, elset=" + face_element_set_name + "\n")
    # Iterate through each line in the .inp file again
    with open("last.inp", "r") as infile:
        for line in infile:
            # Split the line into tokens
            tokens = line.strip().split(",")
            # Check if the line defines an element and if all its nodes are in the face node set
            if tokens[0] == "*Element" and all(node.isdigit() and int(node) in face_node_labels for node in tokens[1:]):
                file.write(",".join(tokens[1:]) + ",\n")

print("Element set", face_element_set_name, "created or updated in last.inp.")