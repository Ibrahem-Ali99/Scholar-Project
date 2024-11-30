# Scrum Board Setup

This repository contains a Scrum board organized for agile project management, focusing on stories, sprints, and epics. Below is an overview of the board's sections and functionality.

## Board Structure

### Tabs

1. **All Stories**: Displays a comprehensive list of all stories, including labels like `story`, `bug`, and `spike`. Use this view to see all tasks in one place.
2. **Next Sprint**: Displays tasks planned for the next sprint, divided into the following columns:
   - **Todo**: Tasks that haven't been started.
   - **In Progress**: Tasks currently being worked on.
   - **Done**: Completed tasks.
   - **Canceled**: Tasks that were canceled.
3. **My Stories for Next Sprint**: Similar to the Next Sprint view, but filtered for tasks assigned to the current user.
4. **My Current Sprint**: Displays stories assigned to the user for the current sprint with the same columns as above for tracking personal progress.
5. **Epics**: A timeline view for managing and scheduling epics. This allows for a high-level overview of long-term goals and major features.

### Columns and Labels

- **Todo**: Tasks that are planned but not started.
- **In Progress**: Tasks actively being worked on.
- **Done**: Completed tasks.
- **Canceled**: Tasks that were removed from the sprint.
- **Labels**: Each story can be labeled as a `story`, `bug`, or `spike` for categorization and prioritization.

### Key Features

- **Story Points**: Tracks effort estimation for each story.
- **Filters**: Ability to filter tasks by labels, status, and assignees.
- **Timeline View (Epics)**: Visualize epic-level tasks over time for project roadmap planning.
- **Status Update**: Option to add status updates, mark milestones, and sort by date for effective sprint management.

## Usage

- **Add Items**: Use `Control + Space` to quickly add new stories or tasks to any column.
- **Sprint Planning**: Assign tasks to `Next Sprint` or `My Current Sprint` to organize workload for upcoming sprints.
- **Story Management**: Update each story's status by moving them across columns (Todo, In Progress, Done, Canceled).
- **Epic Planning**: Use the Epics tab to map out high-level tasks and align them with project milestones.
## Database Setup

### Schema Creation
- The `schema.sql` file contains the structure of the database.
- To create the database, run the following command:
  ```bash
  mysql -u <username> -p < database/schema.sql
  
### Seeding Initial Data
- The seed_data.sql file contains initial data for the database.
- To populate the database, run:
  ```bash
  mysql -u <username> -p < database/seed_data.sql

### Verify Setup
- Log in to MySQL and check the tables and data:
```bash
mysql -u <username> -p
USE <database_name>;
SHOW TABLES;
SELECT * FROM <table_name>;
```
# Frontend Setup and Usage Guide

This guide explains how to set up and run the frontend code of a React-based web application. Follow the instructions below to get started with the project.

## Table of Contents

1. [Project Setup](#project-setup)
2. [Installation](#installation)
3. [Running the Application](#running-the-application)
4. [Folder Structure](#folder-structure)
5. [How to Use](#how-to-use)
6. [Scrum Board Setup](#scrum-board-setup)
7. [Database Setup](#database-setup)

---

## Project Setup

### Prerequisites

Before getting started, ensure that the following tools are installed on your local machine:

- *Node.js*: A JavaScript runtime that is required to run the React application.
  - [Install Node.js](https://nodejs.org/)
  
- *npm (Node Package Manager)*: A package manager that comes with Node.js to install dependencies.
  - npm comes pre-installed with Node.js.

### Folder Structure

components/: This folder contains the reusable React components such as headers, footers, sidebars, etc.
pages/: This folder contains page-level components that render different sections of the app.
App.js: This is the main component that holds the routing logic for the app.
index.js: The entry point of the application that renders the App.js component into the root DOM node.
public/ - Public Files
index.html: This is the HTML template where the React application is injected into the div#root element.

## Installation

Follow these steps to set up the project locally:

1. *Clone the Repository*:

   Open your terminal or command prompt and clone the repository:

   ```bash
   git clone https://github.com/Ibrahem-Ali99/Scholar-Project.git

2. **Navigate to the Project Directory:

   Change into the project directory: 

   cd Scholar-Project

3. **Install Dependencies:
Use npm to install the required dependencies:
npm install
This will install all the necessary packages defined in package.json.

Running the Application
Once the dependencies are installed, you can start the development server:

1. **Start the Development Server:

###Run the following command to start the development server:
npm start

This will start the app and open it in your default browser at http://localhost:3000. Any changes made to the code will automatically reload the page.

2. **Build the Application for Production:

To build the optimized production version of the app, run:
npm run build
This will create a build/ directory with all the production-ready files that can be deployed to a server.
