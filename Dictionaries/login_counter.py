# User Login Counter (easy)

# You are given a dictionary that stores how many times users logged into a system during the day.

# Use a for loop to iterate through the dictionary.

# Print each user name and how many times they logged in.

# Count how many users logged in more than 3 times.

# At the end, print the total number of users that logged in more than 3 times.

logins = {
    
          "Bob": 5,
          "Charlie": 4,
          "David": 3,
          "Diana": 4
}

count_more_than_three = 0

for key, value in logins.items():

  print(f'User: {key} - Logins: {value}')

  if value>3:
    count_more_than_three+=1

print(f'Users with moore than 3 logins is {count_more_than_three}')
