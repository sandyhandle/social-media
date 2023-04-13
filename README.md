- An APIs for a social media platform in Python Django
- The API supports features like getting a user profile, follow a user, upload a post, delete a post, like a post, unlike and like a post
- The database used here is PostgreSQL

The project is hosted on the below url on render.com

https://social-media-app-m6of.onrender.com

What it dose:

- POST /api/authenticate should perform user authentication and return a JWT token.
    - INPUT: Email, Password
    - RETURN: JWT token
- POST /api/follow/{id} authenticated user would follow user with {id}
- POST /api/unfollow/{id} authenticated user would unfollow a user with {id}
- GET /api/user should authenticate the request and return the respective user profile.
    - RETURN: User Name, number of followers & followings.
- POST api/posts/ would add a new post created by the authenticated user.
    - Input: Title, Description
    - RETURN: Post-ID, Title, Description, Created Time(UTC).
- DELETE api/posts/{id} would delete post with {id} created by the authenticated user.
- POST /api/like/{id} would like the post with {id} by the authenticated user.
- POST /api/unlike/{id} would unlike the post with {id} by the authenticated user.
- GET /api/all_posts would return all posts created by authenticated user sorted by post time.
    - RETURN: For each post return the following values
        - id: ID of the post
        - title: Title of the post
        - desc: Description of the post
        - created_at: Date and time when the post was created
        - comments: Array of comments, for the particular post
        - likes: Number of likes for the particular post
        

### **Stacks**

- Backend: Python (using Django). Use other helping libraries.
- Database: PostgreSQL
