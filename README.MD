# Social Team Builder
### Treehouse Python TechDegree Project #12

by Adam Cameron, 2017

### Project Description

A simple social team builder site in which users can create profiles, projects, and then positions for those projects and solicit applications for positions, then accept or reject applicants based on their profiles.

### Setup

All of the following steps should be completed in the terminal, in the main project directory:

- Make a new virtual environment (my current method is with `python3 -m venv venv`)
- Also from the terminal, install the required packages from requirements.txt with `pip freeze -r requirements.txt`
- Tell Django to do all the initial migrations (including a custom data migration for Skill objects) with `python manage.py migrate`
- Create a superuser with `python manage.py createsuperuser`
- You should be all set to go!
