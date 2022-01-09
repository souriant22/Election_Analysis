# The data we need to retrieve


# Import OS and CVS modules
import os
import csv

# Assign a variable to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: Read and analyse the data here.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)

    # Print each row in the file_reader:
    # for row in file_reader:
    #     for i in range(len(row)):
    #         print([i])



# 1. The total number of votes cast 

# 2. A complete list of candidates who received votes 

# 3. The percentage of votes each candidate won

# 4. The total number of votes each candidate won

# 5. The winner of the election based on popular vote.

# Close the file.
election_data.close()