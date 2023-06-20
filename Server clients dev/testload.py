import os

# def load_list_from_file(file_path):
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         # Remove newline characters and any leading/trailing whitespace
#         lines = [line.strip() for line in lines]
#     return lines

# # Example usage
# current_directory = os.getcwd()
# print("Current working directory:", current_directory)
# file_path = current_directory+"/"+'20230611094646.txt'  # Replace with the actual file path
# loaded_list = load_list_from_file(file_path)
# print(loaded_list)

i = "admin -l 20230611095443.txt"
i = i[0:7]
print(i+"-")

# def load_list_from_file(file_name):
#     current_directory = os.getcwd()
#     file_path = current_directory+"/"+file_name
#     with open(file_path, 'r') as file:
#         lines = file.readlines()
#         # Remove newline characters and any leading/trailing whitespace
#         lines = [line.strip() for line in lines]
#     return lines
# print(load_list_from_file("20230611095443.txt"))

# text = "admin -l 20230611095443.txt"
# cut_index = (text.index("-l "))+3  # Find the index of the point where you want to cut
# cut_text = text[cut_index:]  # Cut out everything before the index
# print(cut_text+"==")  # Output: Hello

# inpput = ['a','a','a','a','a','a','a','a','a','b','b','b','b','b','b','b','b','b','b','b']
print(inpput)
length = len(inpput)
print(inpput[(length-10):(length)])
