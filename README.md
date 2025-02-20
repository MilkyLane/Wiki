

# Wiki

This repository is a Wikipedia-like online encyclopedia built using Django. Users can create, edit, and search for encyclopedia entries. The platform supports Markdown formatting for entries.

## Live Demo: 
https://youtu.be/I8pOWEyZsHc

## Features
- Create, edit, and view encyclopedia entries.
- Search functionality to find entries.
- Markdown support for formatting entries.
- Random entry feature.

## Technologies Used
- Python
- Django (Backend Framework)
- SQLite (Database)
- HTML/CSS (Frontend)
- Markdown (Content Formatting)

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/MilkyLane/Wiki.git
   cd Wiki
 
2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt

3. Run migrations to set up the database:
   ```bash
   python manage.py migrate

4. Run the Django development server:
   ```bash
   python manage.py runserver

5. Open your browser and navigate to http://127.0.0.1:8000/ to access the encyclopedia.

   ## Usage
- Create a new entry by clicking "Create New Page."
- Edit existing entries by clicking "Edit" on the entry page.
- Use the search bar to find entries.
- Click "Random Page" to view a random entry.

## Note
- This project is a simplified version of an online encyclopedia and is intended for educational purposes.
