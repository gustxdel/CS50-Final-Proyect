# CS50-Final-Project
## Video Demo:  <https://youtu.be/R-9hQdpgjsQ>
## Heroku Link: <https://budgetark.herokuapp.com/>
## Description:

The aim of this project was to build a Web application using the skills learned troughout cs50's course. The web-app is called Budgetark and its a simple budgeting app that lets the user register, login, set up a budget, and input the monthly expenses.

For the name and logo, I used a random name and logo generator found online. The colors used were a ligth green and purple as an accent since both symbolize money and wealth.

The app was developed using flask and python for the backend. Also for the frontend I used the help of Bootstrap to facilitate some layouts.

### Backend Setup

The project starts with run.py. I separated some of the py files to have a better looking code. The main is run.py that only call for app run. Everything else I put it inside a folder named final. Since I moved the othe py files into this folder I needed a way to import functions defined in this files, so to be able to use the folder Final as a package I created an _init__.py file, which contains the app configurations (key, session, session file, session type), the database initialization and an import conecction to routes.py.

The forms.py is a file in which I imported FlaskForm, wtform, and wtform.validators. This packages facilitate the creation of any type of input form and using jinja syntax, is very easy to use them in a html file. The forms created were: RegisterForm, LoginForm, BudgetForm, and ExpensesForm.

Routes.py containes, as the name states, all the routes used in the app. This routes are: / for home, /account, /delete, /register, /login, /logout, /budget, and /about.

The / rout is simple. Its just a landing page where the user can see some call to actions, inviting the user to sign up for free.

Using any of the buttons that call to sign up, the user is redirected to the /register route via get. In here the user can see a simple form with username, password, and confirm password. Once the user signs up, is redirected to the login form. To ensure that there are no username duplicates, wrong password inputs or that password and confirm password do not match, I used wtforms validators. I used cs50's SQL for the database. 

The database, named budgetark.db consists of two tables. The first use is a table of users, having id, username password, date created, and budget as columns. The second table is expenses, having id, name, money, date created, and userID to link with previous table.

Once the user signsup, the information is stored in the database using a post method and a db.execute query. The password uses werkzeug for hashing protection.

In the /login route, Forms was use again to ask the user for username and password input. This data is compared to what is on the database and if it matches, the user logs in succesfully. Using the Session import, a session with the user id is created so the user does not need to log in everytime the page is refreshed.

If the user logs in for the very first time, is redirected to the nudget page where he needs to set a budget which is then stored in the users table in the database. Then is redirected to the Account page.

In the /account route, the user can input name of expenses and how much he spent, which are then stored in the expenses table. This information is then showed in a table of monthly expenses that display at the end the total spent. At the top of the page the user can see a card that contains the info on how much he has already spent compared to the budget he set. Alse a progress bar with exact percentage is displayed so it is more user friendly.

The /delete route let the user delete an element from the expenses table, which uses db.execute query to delete this info.

Finally the /logout route clears the session data and redirects to the main landing page.

Via some tutorials online. I learned how to use heroku to deploy the web app online commiting via github. 

### Frontend Setup

It starts with the layout.html file. This countains all the elements that are going to be displayed in all the pages. First it has the nav bar on top, which consists of the logo at the left and to the right the links to the other pages. If the user is not login, it displays home, about, login, and register. When the user is login, it displays home, about, account, budget, and logout. the main body is block using jinja syntax so it can be easily used in the other html files. At the bottom there is a footer containing the logo.

The home.html contains the landing page and call to action information, prompting the usr to register or log in. The login, register, and budget files are very similar to eachother. They only changed on waht the user has to input.

The account file is the main page where the user inputs the expenses. Then they are display in a table made using jinja syntaxt to retrieve the info from database and bootstrap for the styling. In the top of the page the user can see a card that contains the info on how much he has already spent compared to the budget he set. Alse a progress bar with exact percentage is displayed so it is more user friendly. 

### Future considerations

There was not enough time to fully implement all the functions that I originalyy had in mind. Some like: email verification, password change, settings menu, which are very common nowadays in almost every web app, are not implemented in budgetark. Displaying month by month the expenses info, creating graphs, creating alerts to prompt the user that the set budget is almost reach, gererating expense reports by month, are a handfull of the many functions that I had in mind for this project, which I would like to implement little by little on my free time 