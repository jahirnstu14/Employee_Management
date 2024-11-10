
# Employee_Management 

Welcome to the **Employee_Management** project! This project is a Django-based web application for managing employee records, which includes features to add, edit, delete, and view employee details. The application also features an admin panel specifically designed for managing employee information, making it easy for administrators to oversee and update employee records efficiently.

## Table of Contents

1.  **Project Overview**
2.  **Features**
3.  **Technologies Used**
4.  **Installation**
5.  **Usage**

----------

## Project Overview

The **Employee_Management** project offers a user-friendly interface for handling essential employee management functions. Administrators can log in to the system to add new employees, update existing employee records, delete employees, and view a comprehensive list of all employees. The project is designed using Django as the backend framework, with HTML, CSS, and Bootstrap to create a responsive and interactive frontend experience.

## Features

1.  **Admin Authentication**: Secure login for admin users to access employee management functionalities.
2.  **Add Employee**: Allows admins to input details and create new employee records.
3.  **Edit Employee**: Enables updating of existing employee details, including name, department, role, and more.
4.  **Delete Employee**: Provides the ability to remove employee records as needed.
5.  **Employee List**: Displays a complete list of all employees in the system.
6.  **Admin Panel**: A dedicated area where admins can perform all CRUD (Create, Read, Update, Delete) operations on employee records.

## Technologies Used

-   **Django**: Used for backend processing, URL routing, and data management.
-   **HTML**: For structuring the pages.
-   **CSS**: For styling the user interface.
-   **Bootstrap**: For responsive design and UI components.
-   **SQLite3**: For storing employee data (depending on configuration).

## Installation

To set up and run the **Employee Management** project locally, follow these steps:

### 1. Clone the Repository
`https://github.com/jahirnstu14/Employee_Management.git` 

### 2. Set Up a Virtual Environment

Navigate to the project folder and create a virtual environment.

``cd Employee_Management``
``python -m venv env``   # On Windows use `env\Scripts\activate` `` 


### 3. Configure the Database

By default, Django uses SQLite.

-   Update the `DATABASES` setting in `settings.py`.
-   Apply migrations for initial database setup.

### 4. Run Migrations

`python manage.py migrate` 

### 5. Create a Superuser

Set up an admin account to access the admin panel.

`python manage.py createsuperuser` 

### 6. Start the Development Server

`python manage.py runserver` 

## Usage

1.  **Admin Login**  
    Go to the admin login page to access the dashboard.
    
2.  **Adding an Employee**  
    Use the “Add Employee” option to create new employee records by filling in their details.
    
3.  **Editing an Employee**  
    Select an employee from the list to update their information.
    
4.  **Deleting an Employee**  
    Choose an employee from the list and delete their record if needed.
    
5.  **Viewing Employee List**  
    View a complete list of all employees in a table format, including their details.
    
6.  **Admin Panel**  
    Log in as an admin user to manage the full range of CRUD operations.
