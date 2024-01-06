This project will bring the following skills together for real-world practice:

1) How to work with strings
2) Object-oriented programming
3) Dates and times

In this project, we'll work with a dataset of submissions to popular technology site Hacker News.

Hacker News is a site started by the startup incubator Y Combinator, where user-submitted stories (known as "posts") receive votes and comments, similar to reddit. Hacker News is extremely popular in technology and startup circles, and posts that make it to the top of the Hacker News listings can get hundreds of thousands of visitors as a result.

Below are descriptions of the columns:

1) id => the unique identifier from Hacker News for the post
2) title => the title of the post
3) url => the URL that the posts links to, if the post has a URL
4) num_points => the number of points the post acquired, calculated as the total number of upvotes minus the total number of downvotes
5) num_comments => the number of comments on the post
6) author => the username of the person who submitted the post
7) created_at => the date and time of the post's submission

We're specifically interested in posts with titles that begin with either Ask HN or Show HN. Users submit Ask HN posts to ask the Hacker News community a specific question. Likewise, users submit Show HN posts to show the Hacker News community a project, product, or just something interesting.

We'll compare these two types of posts to determine the following:

- Do Ask HN or Show HN receive more comments on average?
- Do posts created at a certain time receive more comments on average?
- Do Ask HN or Show HN posts received more points on average?
- Do posts created at a certain time are more likely to receive more points?
- Compare the results to the average number of comments and points other posts receive
