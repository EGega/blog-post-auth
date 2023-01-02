# blog-post-authentication
## This is a basic project focused on django filtering, searching, authentication and authorization
### This is the link that gets the categories, you can view each category but can not POST, PUT, or DELETE them http://127.0.0.1:8000/blog/categories/ or
http://127.0.0.1:8000/blog/categories/ (insert an id number here) if you want to try POST, PUT, DELETE actions which eventually won't work
### This is the link that gets the blog posts, you can view each category but can POST, PUT, or DELETE them only if you log in. http://127.0.0.1:8000/blog/posts/ or
http://127.0.0.1:8000/blog/categories/ (insert an id number here) if you want to try POST, PUT, DELETE actions which eventually will work only if you log in.
### Here is the link to create a user http://127.0.0.1:8000/user/register/, your token will be displayed as a response, token authentication instead of basic authentication is being used.

#### The project is not online so you need to clone code into your local machine and then try by using postman to check the responses.
#### The blog titles and content make no sense at all since I have just used a faker file and dummy text.
