# Py-restaurant
# Restaurant App 

A Flask-based restaurant app that allows users to register, log in, view a menu, place orders, and download an order summary in PDF format. The app uses MongoDB for data storage and `wkhtmltopdf` for HTML to PDF conversion.

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/restaurant-app.git
cd restaurant-app

### 2. Install Dependencies

pip install Flask
pip install flask_pymongo
pip install werkzeug
pip install pdfkit
pip install pymongo

### 3. Install wkhtmltopdf (This is required in order to convert an html document to pdf i.e used to diplay bill at last)

Download the installer from (https://wkhtmltopdf.org/downloads.html) this link i.e wkhtmltopdf download page.
This page will display number of options for Windows,ubuntu,macOS etc.(I used windows 64-bit)
After downloading in your downloads Run the installer and follow the installation instructions.
Then go to c drive --> Program files --> wkhtmltopdf --> bin --> then copy the path it will be in the format of C:\Program Files\wkhtmltopdf\bin
Then you need to add this path to your system variables
once added to system variables open command prompt and check its versio using  wkhtmltopdf --version
if everything is done properly it will diplay version else repeat above steps properly


###  4. Set Up MongoDB

You need to have MongoDB installed and running. Follow the steps below to set it up:

1. Install MongoDB
Download and install MongoDB from the official MongoDB download page.
2. Install MongoDB Compass
Download MongoDB Compass (a GUI for MongoDB) from the MongoDB Compass download page and install it.

Create the Database and Collections
Open MongoDB Compass and connect to your MongoDB server.
Create a new database named restaurant_app_1.
Inside the restaurant_app_1 database, create two collections: users and menu_items.

Format for Collections
1)For 'users' collection there is no need to add any format as in this collection youll see who has logged in
2)For 'menu_items' collection you will have to specify menu items which will be in the format of 
  {
  "name": "Chicken Curry",
  "price": 250
  }

note: Add this type of 4 to 5 menu items as per your restaurant's menu(basically tis will display menu items which you want to display in your menu)

### 5. Running the Application
 simple go to app.py file and run it command shell of vs code you will get an link which will take you to app interface


Application Flow
Home Page: The user is greeted with a home page where they can choose to log in or register.
User Registration: Users can register by providing a username and password. The password is securely hashed before being stored in the database.
User Login: Users can log in with their registered credentials. If successful, they are redirected to the menu page.
Menu Page: The menu page displays all the available dishes fetched from the menu_items collection in MongoDB.
Order Placement: Users can select menu items and place an order.
Order Summary: After placing the order, users are shown a summary of their order along with the total price. They have the option to download this summary as a PDF.
PDF Generation: When the user opts to download the order summary, wkhtmltopdf is used to convert the summary into a PDF document, which is then available for download.
Logout: Users can log out, which clears their session.




















