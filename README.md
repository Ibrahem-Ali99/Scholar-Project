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
