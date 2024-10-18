# Student Management System

## Overview
This is a  Django-based Student Management System  designed to manage students, professors, courses, and grades in an academic setting. It leverages Django's ORM to interact with a PostgreSQL database, providing models to store information about students, courses, professors, and scores. The system also includes authentication, permissions, and session management through Django's built-in models.

**Note** If you're a contributer please read CONTRIBUTING.md

## Features
-  Student Management : Add, update, and track student information including personal details, enrollment dates, and contact information.
-  Course Management : Manage course offerings, including course names, schedules, and semesters.
-  Professor Management : Manage professor profiles, including contact details and teaching assignments.
-  Score Tracking : Track student performance by associating grades with specific courses and exams.
-  Authentication and Permissions : Uses Django's built-in authentication system for secure access control.
-  Admin Interface : Manage data through Django's powerful admin interface.

## Models Overview

### 1.  Auth Models 
- `AuthGroup`: Handles user groups.
- `AuthPermission`: Manages permissions associated with actions in the system.
- `AuthUser`: Stores user credentials and other related information like superuser status, login info, and more.
- `AuthUserGroups`: Links users to groups.
- `AuthUserUserPermissions`: Links users to permissions.

### 2.  Academic Models 
- `Student`: Stores student information such as first name, last name, email, phone number, gender, date of birth, and date of admission.
- `Professor`: Stores professor details such as name, contact information, and date of joining.
- `Courses`: Stores course information including course ID, name, semester, start and end dates.
- `Scores`: Associates a student with a course and an exam, and stores their grade.
- `Taken`: Represents the enrollment of students in courses.
- `TaughtBy`: Represents the teaching assignments of professors to specific courses.

### 3.  Admin and Session Models 
- `DjangoAdminLog`: Logs changes made via the admin interface.
- `DjangoSession`: Stores session information for user authentication and data persistence during web sessions.

## Installation

### Prerequisites
- Python 3.x
- Django 4.x
- PostgreSQL database
- Virtual environment (optional but recommended)

### Steps
1.  Clone the repository :
   ```bash
   git clone <repository-url>
   cd student-management-system
   ```

2.  Set up virtual environment  (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3.  Install required dependencies :
   ```bash
   pip install -r requirements.txt
   ```

4.  Set up PostgreSQL database :
   - Create a PostgreSQL database.
   - Update `DATABASES` settings in `settings.py` with your database credentials.

5.  Apply migrations :
   ```bash
   python manage.py migrate
   ```

6.  Create a superuser  (for accessing the admin panel):
   ```bash
   python manage.py createsuperuser
   ```

7.  Run the development server :
   ```bash
   python manage.py runserver
   ```

8.  Access the app :
   - Visit `http://127.0.0.1:8000/` to access the system.
   - Use the admin interface at `http://127.0.0.1:8000/admin/` to manage data.

## Usage

-  Admin Interface : 
   You can add or manage students, professors, courses, and grades through the Django Admin interface.
   
-  Authentication : 
   Django's built-in authentication system allows for secure access and management of permissions.

-  Sessions : 
   Sessions are handled by Django’s session framework, ensuring data persistence across user requests.

## Models Summary
-  AuthGroup : Handles user groups.
-  AuthPermission : Manages permission settings.
-  AuthUser : User details and authentication info.
-  Courses : Course details and metadata.
-  Student : Student personal and academic information.
-  Professor : Professor details.
-  Scores : Tracks scores/grades for students.
-  Taken : Students enrolled in courses.
-  TaughtBy : Professors assigned to teach courses.

