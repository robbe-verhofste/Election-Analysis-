#Add our dependencies
import csv
import os

#assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
#assign a variable to save the file to a path
file_to_save = os.path.join("Election-Analysis-", "election_analysis.txt")

#Initialize a total vote counter
total_votes = 0

#candidate options and candidate voters
candidate_options = []
candidate_votes = {}

#track the winning candidate, vote count, and percentage_votes
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#Open the election results and read the file
with open(file_to_load) as election_data:
  file_reader = csv.reader(election_data)

  #read the header row
  headers = next(file_reader)

  #print each row in the CSV file
  for row in file_reader:
    #add to the total vote count
    total_votes += 1

    #get the candidate name from each row
    candidate_name = row[2]

    #if the candidate does not match any existing candidate  add the candidate to the list
    if candidate_name not in candidate_options:
      #add candidate to the candidate list_
      candidate_options.append(candidate_name)
      #add begin tracking that candidate's voter count
      candidate_votes[candidate_name] = 0
    #add a vote to that candidates count
    candidate_votes[candidate_name] += 1
#save the results to our text file
with open(file_to_save, "w") as txt_file:
  election_results = (
      f"\nElectionResults\n"
      f"-----------------------\n"
      f"Total Votes: {total_votes:,}\n"
      f"-----------------------\n")
  print(election_results, end="")
  #save the final vote count to the text file
  txt_file.write(election_results)
  
  for candidate_name in candidate_votes:
      #retrieve vote count and percentage
      votes = candidate_votes[candidate_name]
      vote_percentage = float(votes) /float(total_votes) *100

      #print each candidate, their voter count, and percentage to the terminal
      #determine winning vote count, winning percentage, and candidate
      if (votes > winning_count) and (vote_percentage > winning_percentage):
        winning_count = votes
        winning_candidate = candidate_name
        winning_percentage = vote_percentage
  #print the winning candidates results to the terminal
winning_candidate_summary = (
    f"--------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_percentage:.1f}%\n"
    f"---------------------------\n")