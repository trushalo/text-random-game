import json
# import main

#  obj.__dict__

def write_object_to_file(obj):
    """
    Writes an object to a file as a JSON string.

    Args:
        obj: The object to write.
        filename: The name of the file to write to.
    """
    obj_dict = obj.__dict__
    with open('save_data.py', 'w') as f:
        json.dump(obj_dict, f)
'''
# Example usage
my_object = main.mycharacter
write_object_to_file(my_object, "my_object.json") 


def write_dict_to_list_in_file(dictionary, filename):
  """
  Writes a dictionary to a list within an existing Python file using JSON.

  Args:
    dictionary: The dictionary to be written.
    filename: The name of the Python file.
  """

  try:
    with open(filename, 'r') as f:
      try:
        # Load the existing list from the file using JSON
        existing_list = json.load(f) 
      except (json.JSONDecodeError, ValueError):
        # If the file is empty or contains invalid JSON, 
        # start with an empty list
        existing_list = []

    existing_list.append(dictionary)

    with open(filename, 'w') as f:
      json.dump(existing_list, f, indent=2) 

  except FileNotFoundError:
    print(f"File '{filename}' not found.")
'''