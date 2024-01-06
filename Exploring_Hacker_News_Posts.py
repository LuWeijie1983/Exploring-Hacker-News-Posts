#!/usr/bin/env python
# coding: utf-8

# # Guided Project: Exploring Hacker News Posts

# This guided project will bring the following skills together for real-world practice:
# 
# 1) How to work with strings  
# 2) Object-oriented programming  
# 3) Dates and times  
# 
# A [downsampled dataset](https://www.kaggle.com/datasets/hacker-news/hacker-news-posts) from `Hacker News` will be used in this project. `Hacker News` is extremely popular website in technology and startup cicrles, and posts that make it to the top of the listings can get hundreds of thousands of visitors.
# 
# Primarily, we're specifically interested in posts with title that begin with etiher `Ask HN` or `Show HN`. Users submit `Ask HN` posts to ask `Hacker News` community a specific question while users submit `Show HN` posts to show `Hacker News` community a project, product, or just something interesting.

# ## Description of data column

# | Column      | Description|
# |:-------------|:------------|
# |id           |the unique identifier from Hacker News for the post|
# |title        |the title of the post
# |url          |the URL that the posts link to
# |num_points   |the number of points the post acquired, calculated as the total number of upvotes minus the total number of downvotes|
# |num_comments |the number of comments on the post
# |author       |the name of the account that made the post
# |created_at   |the date and time the post was made (the time zone is Eastern Time in the US)

# ## Project Objective

# This project will compare the 2 types of posts `Ask HN` and `Show HN` to determine:
# 
# - Do `Ask HN` or `Show HN` receive more comments on average?
# - Do posts created at a certain time receive more comments on average?

# ## Read in the csv file as a list of lists

# In[1]:


from csv import reader
opened_file = open('hacker_news.csv')
read_file = reader(opened_file)
hn = list(read_file)
print(hn[:5])


# ### 1. Extract the first row of data as headers

# In[2]:


# Extract headers from data
headers = hn[0]

print('headers:')
print(headers)


# ### 2. Remove headers

# In[3]:


# Remove header first row from hn
hn = hn[1:]

print('First 5 row of hn data without headers:')
print(hn[:5])


# ## Find the posts with titles beginning with `Ask HN` or `Show HN`

# In[4]:


# Create 3 empty lists
ask_posts = []
show_posts = []
other_posts = []


# In[5]:


# Seperate the posts
for row in hn:
    title = row[1]
    if title.lower().startswith('ask hn'):
        ask_posts.append(row)
    elif title.lower().startswith('show hn'):
        show_posts.append(row)
    else:
        other_posts.append(row)


# In[6]:


# Count the number of posts in each list
length_ask_posts = len(ask_posts)
print(f'Number of "Ask HN" posts: {length_ask_posts}')

print()

length_show_posts = len(show_posts)
print(f'Number of "Show HN" posts: {length_show_posts}')

print()

length_other_posts = len(other_posts)
print(f'Number of other posts: {length_other_posts}')


# ## Display the first 5 rows of data beginning with `Ask HN` and `Show HN`

# In[7]:


# Display first 5 rows of data for 'ask_posts' list
print('First 5 rows from ask_posts:')
print(ask_posts[:5])


# In[8]:


# Display first 5 rows of data for 'show_posts' list
print('First 5 rows from show_posts:')
print(show_posts[:5])


# ## Calculate the average number of comments for `Ask HN` and `Show HN` posts

# In[9]:


# Find the total number of comments on ask posts

total_ask_comments = 0
for row in ask_posts:
    num_of_ask_comments = int(row[4])
    total_ask_comments += num_of_ask_comments

# Find the average number of comments on ask posts
avg_ask_comments = total_ask_comments // length_ask_posts

print(f'The average number of comments on ask posts is {avg_ask_comments}')


# In[10]:


# Find the total number of comments on show posts

total_show_comments = 0
for row in show_posts:
    num_of_show_comments = int(row[4])
    total_show_comments += num_of_show_comments

# Find the average number of comments on show posts
avg_show_comments = total_show_comments // length_show_posts

print(f'The average number of comments on show posts is {avg_show_comments}')


# ## Find the Number of `Ask HN` Posts and Comments by Hour Created

# We'll determine if ask posts created at a certain time are mor likely to attract comments. To perform this analysis:
# 
# 1. Calculate the number of ask posts created in each hour of the day, along with the number of comments received.
# 
# 2. Calculate the average number of comments ask posts receive by hour created

# ### Step 1 - Calculate the number of `Ask HN` posts created in each hour of the day, along with the number of comments received.

# In[11]:


# Import the datetime module
import datetime as dt

# Create an empty list 'result_list'
result_list = []

# Iterate over 'ask_posts' list to append number of comments and created date
# number of comments in index 4 and created date in index 6
for post in ask_posts:
    result_list.append([post[6], int(post[4])])

# Create dictionaries 'counts_by_hour' and 'comments_by_hour'
counts_by_hour = {}
comments_by_hour = {}

for item in result_list:
    date = item[0]
    comment = item[1]
    date_format = '%m/%d/%Y %H:%M'
    
    # First is to parse string into datetime object using strptime, then extract the hour portion using strftime
    time = dt.datetime.strptime(date, date_format).strftime('%H')
    
    if time in counts_by_hour:
        comments_by_hour[time] += comment
        counts_by_hour[time] += 1
    else:
        comments_by_hour[time] = comment
        counts_by_hour[time] = 1

comments_by_hour


# ### Step 2 - Calculate the Average Number of Comments for `Ask HN` Posts by Hour

# Next, we use the two dictionaries `comments_by_hour` and `counts_by_hour` to calculate the average number of comments for posts created during each hour of the day

# In[12]:


avg_by_hour = []

for hour in comments_by_hour:
    avg_by_hour.append([hour, comments_by_hour[hour] / counts_by_hour[hour]])

avg_by_hour


# ## Sorting and Printing Values

# Sort the obtained results in order to identify the hours with the highest number of comments

# In[13]:


# Create empty list 'swap_avg_by_hour'
swap_avg_by_hour = []

for row in avg_by_hour:
    swap_avg_by_hour.append([row[1], row[0]])

print(swap_avg_by_hour)

sorted_swap = sorted(swap_avg_by_hour, reverse=True)

sorted_swap


# In[14]:


# Sort the values and print out the top 5 hours with highest average number of comments
print('Top 5 Hours for Ask Posts Comments')
for avg, hr in sorted_swap[:5]:
    print(
        '{hour}: {avg_comment:.2f} average comments per post'.format(
            hour = dt.datetime.strptime(hr,'%H').strftime('%H:%M'), avg_comment = avg))


# The dataset timezone is in US Eastern Time

# Based on the above analysis, 15:00 hrs had the highest number of average comments per post (38.59), followed by 02:00 hrs (23.81), 20:00 hrs (21.52), 16:00 hrs (16.80) and 21:00 hrs (16.01).
# 
# Therefore, to have a higher chance of receiving comments for post created, it is advisable to create a post at either 15:00 hrs (or 04:00 hrs SGT) or 02:00 hrs (or 15:00hrs SGT)

# ## Determine if show or ask posts receive more points on average

# ### Calculate average number of points received by show posts

# In[15]:


print(f'Total number of show posts: {length_show_posts}')

print()

# Find the total number of points received by show posts
total_points_show_posts = 0

for row in show_posts:
    points_show_post = int(row[3])
    total_points_show_posts += points_show_post

print(f"Total number of points received by show posts: {total_points_show_posts}")

print()

# Find average number of points received by show posts
avg_points_show_posts = total_points_show_posts // length_show_posts

print(f'Average number of points received by show posts: {avg_points_show_posts}')


# ### Calculate average number of points received by ask posts

# In[16]:


print(f'Total number of ask posts: {length_ask_posts}')

print()

# Find the total number of points received by ask posts
total_points_ask_posts = 0

for row in ask_posts:
    points_ask_post = int(row[3])
    total_points_ask_posts += points_ask_post

print(f"Total number of points received by ask posts: {total_points_ask_posts}")

print()

# Find average number of points received by ask posts
avg_points_ask_posts = total_points_ask_posts // length_ask_posts

print(f'Average number of points received by ask posts: {avg_points_ask_posts}')


# Based on the above calculation, it can be seen that show posts receive a higher number of points (27) on average as compared to ask posts (15)

# ## Determine if `Ask HN` posts created at a certain time are more likely to receive more points

# ### Step 1 - Calculate the number of `Ask Posts` created in each hour of the day, along with the number of points received.

# In[17]:


# Import the datetime module
import datetime as dt

# Create an empty list 'ask_point_date_list'
ask_point_date_list = []

# Iterate over 'ask_posts' list to append number of points and created date
# number of points in index 3 and created date in index 6
for post in ask_posts:
    ask_point_date_list.append([post[6], int(post[3])])

# Create dictionaries 'ask_counts_by_hour' and 'ask_points_by_hour'
# ask_counts_by_hour tracks number of occurrences for each hour of the day
# ask_points_by_hour tracks number of points for each hour of the day
ask_counts_by_hour = {}
ask_points_by_hour = {}

for item in ask_point_date_list:
    date = item[0]
    point = item[1]
    date_format = '%m/%d/%Y %H:%M'
    
    # First is to parse string into datetime object using strptime, then extract the hour portion using strftime
    time = dt.datetime.strptime(date, date_format).strftime('%H')
    
    if time in ask_counts_by_hour:
        ask_points_by_hour[time] += point
        ask_counts_by_hour[time] += 1
    else:
        ask_points_by_hour[time] = point
        ask_counts_by_hour[time] = 1

print(f'Number of ask points by hour: \n{ask_points_by_hour}')

print()

print(f'Ask counts by hour: {ask_counts_by_hour}')


# ### Step 2 - Calculate the average number of points for `Ask HN` Posts by Hour

# In[18]:


# Create empty list 'avg_ask_points_by_hour'
avg_ask_points_by_hour = []

# Iterate through the list 'ask_points_by_hour'
# Append hour of the day and average points per hour to the list 'avg_ask_points_by_hour'
for hour in ask_points_by_hour:
    avg_ask_points_by_hour.append([hour, ask_points_by_hour[hour] / ask_counts_by_hour[hour]])

avg_ask_points_by_hour


# ### Step 3 - Sort the obtained values to identify the top 5 results with highest average number of points and the corresponding hour created 

# In[19]:


# Create empty list 'swap_avg_ask_points_by_hour'
swap_avg_ask_points_by_hour = []

# Swap the position of average points per hour and the hour of the day
for row in avg_ask_points_by_hour:
    swap_avg_ask_points_by_hour.append([row[1], row[0]])

print(swap_avg_ask_points_by_hour)

# Sort the list 'swap_avg_ask_points_by_hour' in descending order
sorted_swap = sorted(swap_avg_ask_points_by_hour, reverse=True)

sorted_swap


# In[20]:


# Print out the top 5 hours with highest average number of points
print('Top 5 Hours for Ask Posts average number of points')
for avg, hr in sorted_swap[:5]:
    print(
        '{hour}: {avg_points:.2f} average points per post'.format(
            hour = dt.datetime.strptime(hr,'%H').strftime('%H:%M'), avg_points = avg))


# The dataset timezone is in US Eastern Time

# Based on the above analysis, 15:00 hrs had the highest number of average points per ask post (29.99), followed by 13:00 hrs (24.26), 16:00 hrs (23.35), 17:00 hrs (19.41) and 10:00 hrs (18.68).
# 
# Therefore, to have a higher chance of scoring points for post created, it is advisable to create a post at either 15:00 hrs (or 04:00 hrs SGT) or 13:00 hrs (or 02:00hrs SGT)

# ## Determine if `Show HN` posts created at a certain time are more likely to receive more points

# ### Step 1 - Calculate the number of `Show HN` posts created in each hour of the day, along with the number of points received.

# In[21]:


# Import the datetime module
import datetime as dt

# Create an empty list 'show_point_date_list'
show_point_date_list = []

# Iterate over 'show_posts' list to append number of points and created date
# number of points in index 3 and created date in index 6
for post in show_posts:
    show_point_date_list.append([post[6], int(post[3])])

# Create dictionaries 'counts_by_hour' and 'points_by_hour'
# counts_by_hour tracks number of occurrences for each hour of the day
# points_by_hour tracks number of points for each hour of the day
show_counts_by_hour = {}
show_points_by_hour = {}

for item in show_point_date_list:
    date = item[0]
    point = item[1]
    date_format = '%m/%d/%Y %H:%M'
    
    # First is to parse string into datetime object using strptime, then extract the hour portion using strftime
    time = dt.datetime.strptime(date, date_format).strftime('%H')
    
    if time in show_counts_by_hour:
        show_points_by_hour[time] += point
        show_counts_by_hour[time] += 1
    else:
        show_points_by_hour[time] = point
        show_counts_by_hour[time] = 1

print(f'Number of show points by hour: \n{show_points_by_hour}')

print()

print(f'Show counts by hour: {show_counts_by_hour}')


# ### Step 2 - Calculate the average number of points for `Show HN` Posts by Hour

# In[22]:


# Create empty list 'avg_show_points_by_hour'
avg_show_points_by_hour = []

# Iterate through the list 'show_points_by_hour'
# Append hour of the day and average points per hour to the list 'avg_show_points_by_hour'
for hour in show_points_by_hour:
    avg_show_points_by_hour.append([hour, show_points_by_hour[hour] / show_counts_by_hour[hour]])

avg_show_points_by_hour


# ### Step 3 - Sort the obtained values to identify the top 5 results with highest average number of points and the corresponding hour created 

# In[23]:


# Create empty list 'swap_avg_show_points_by_hour'
swap_avg_show_points_by_hour = []

# Swap the position of average points per hour and the hour of the day
for row in avg_show_points_by_hour:
    swap_avg_show_points_by_hour.append([row[1], row[0]])

print(swap_avg_show_points_by_hour)

# Sort the list 'swap_avg_show_points_by_hour' in descending order
sorted_show_swap = sorted(swap_avg_show_points_by_hour, reverse=True)

sorted_show_swap


# In[24]:


# Print out the top 5 hours with highest average number of points
print('Top 5 Hours for Show Posts average number of points')
for avg, hr in sorted_show_swap[:5]:
    print(
        '{hour}: {avg_points:.2f} average points per post'.format(
            hour = dt.datetime.strptime(hr,'%H').strftime('%H:%M'), avg_points = avg))


# The dataset timezone is in US Eastern Time

# Based on the above analysis, 23:00 hrs had the highest number of average points per show post (42.39), followed by 12:00 hrs (41.69), 22:00 hrs (40.35), 00:00 hrs (37.84) and 18:00 hrs (36.31).
# 
# Therefore, to have a higher chance of scoring points for show post created, it is advisable to create a post at either 15:00 hrs (or 04:00 hrs SGT) or 13:00 hrs (or 02:00hrs SGT)

# ## Compare the average number of comments received by other posts to `Ask HN` and `Show HN` posts

# ### Calculate the average number of comments received by other posts

# In[25]:


# Find the total number of comments on other posts

total_other_comments = 0
for row in other_posts:
    num_of_other_comments = int(row[4])
    total_other_comments += num_of_other_comments

# Find the average number of comments on other posts
avg_other_comments = total_other_comments // length_other_posts

print(f'The average number of comments on other posts is {avg_other_comments}')


# From previous analysis, the average number of comments on `Ask HN` posts is 14 and the average number of comments on `Show HN` posts is 10. Hence, we can observe that other posts garnered higher average number of comments than `Ask HN` and `Show HN` posts.

# ## Compare the average number of points received by other posts to `Ask HN` and `Show HN` posts

# ### Calculate the average number of comments received by other posts

# In[26]:


print(f'Total number of other posts: {length_other_posts}')

print()

# Find the total number of points received by other posts
total_points_other_posts = 0

for row in other_posts:
    points_other_post = int(row[3])
    total_points_other_posts += points_other_post

print(f"Total number of points received by other posts: {total_points_other_posts}")

print()

# Find average number of points received by other posts
avg_points_other_posts = total_points_other_posts // length_other_posts

print(f'Average number of points received by other posts: {avg_points_other_posts}')


# From previous analysis, the average number of points on `Ask HN` posts is 15 and the average number of points on `Show HN` posts is 27. Hence, we can observe that other posts garnered higher average number of points than `Ask HN` and `Show HN` posts.
