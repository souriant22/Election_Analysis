# The data we need to retrieve


# Import OS and CVS modules to add dependencies
import os
import csv

# Assign a variable to load from a path
file_to_load = os.path.join("Resources", "election_results.csv")

# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1. Initialize a total vote counter
total_votes = 0

# Candidate Options
candidate_options = []

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: Read and analyse the data here.
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 2. Add to the total vote count.
        total_votes += 1

        # Print the candidate name from each row.
        candidate_name = row[2]

        # Fi the candidate does not match any existing candidate
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

# Print the candidate list
print(candidate_options)

# # Print the total votes.
# print(total_votes)


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