import psycopg2
from decouple import config 
from Services.database import db_connect # Assuming you're using decouple for environment variables

# This function helps to establish db connection
def db_connection():
    print("inside db_connection")
    pgConnection = psycopg2.connect(
    host=config('PG_ADMIN_HOST_NP'),
    database=config('PG_ADMIN_DB_NAME_NP'),
    user=config('PG_ADMIN_USERNAME_NP'),
    password=config('PG_ADMIN_PASSWORD_NP')
)
    return pgConnection

# This function helps to retreive issue ids from db
def get_id():
    print("inside get_id function")

    try:
        #Establish connection
        pgConnection = db_connection()
        print('db connected\n')
        cursor = pgConnection.cursor()
        # Get issue_id from db
        cursor.execute("""
            SELECT EXISTS (
                SELECT FROM pg_tables
                WHERE tablename = %s
            );
        """, ("jira_story_table",))
        result = cursor.fetchone()[0]
        if result == True:
           cursor.execute("SELECT issue_id FROM jira_story_table")
           result = cursor.fetchall()
           issue_ids = [item[0] for item in result]
           cursor.close()
           pgConnection.close()
           return issue_ids
        else:
            cursor.execute("""CREATE EXTENSION IF NOT EXISTS "uuid-ossp";""")
            cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
            cursor.execute("""CREATE TABLE IF NOT EXISTS public.jira_story_table
            (
            issue_id character varying COLLATE pg_catalog."default",
            labels character varying COLLATE pg_catalog."default",
            due_date character varying COLLATE pg_catalog."default",
            issue_links character varying COLLATE pg_catalog."default",
            issue_type character varying COLLATE pg_catalog."default",
            application_name character varying COLLATE pg_catalog."default",
            assigned_to character varying COLLATE pg_catalog."default",
            issue_description character varying COLLATE pg_catalog."default",
            vector_column vector(1536),
            project_name character varying COLLATE pg_catalog."default",
            status character varying COLLATE pg_catalog."default"
        )""")
            pgConnection.commit()
            cursor.close()
            pgConnection.close()
            return []

    except psycopg2.Error as e:
        print("Error in insertKB:", e)

# This function helps to check whether the consumed id is already in the db or not.
def check_id(jira_issue,embeddings):
    print("inside check_id function")

    try:
        #Establish connection
        pgConnection = db_connection()
        print('db connected\n')
        cursor = pgConnection.cursor()
        # Get issue_id
        issue_ids = get_id()
        print(issue_ids, "issue iddsssss")
        print(jira_issue,",,,,,")
        # If consumed issue already in the db then it will update
        if jira_issue["issues_id"] in issue_ids:
            cursor.execute("""
                UPDATE public.jira_kb
                SET 
                    labels = %s,
                    due_date = %s,
                    issue_links = %s,
                    issue_type = %s,
                    assigned_to = %s,
                    issue_description = %s,
                    project_name = %s,
                    status = %s,
                    vector_column = %s
                WHERE issue_id = %s;
            """, [
                ','.join(jira_issue['labels']),
                jira_issue['duedate'],
                f"https://enterprise-search.atlassian.net/browse/{jira_issue['issues_link']}",
                jira_issue['issues_type'],
                jira_issue['assigned_to'], 
                jira_issue['summary'],
                jira_issue['project_name'],
                jira_issue['status'],
                embeddings,
                str(jira_issue['issues_id'])
            ])
            print("Updated issue_id: ", jira_issue["issues_id"])
        else:
        # If If consumed issue not already in the db then it will insert the issue
            cursor.execute("INSERT INTO public.jira_story_table(issue_id, labels, due_date, issue_links, issue_type,assigned_to,issue_description,project_name,status, vector_column)	VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s,%s);",[
                str(jira_issue['issues_id']),
                str(','.join(jira_issue['labels'])),
                str(jira_issue['duedate']),
                str(f"https://enterprise-search.atlassian.net/browse/{jira_issue["issues_link"]}" ),
                str(jira_issue['issues_type']),
                str(jira_issue['assigned_to']), 
                str(jira_issue['summary']),
                str(jira_issue['project_name']),
                str(jira_issue['status']),
                embeddings
            ])
            # Confirm successful insertion
            print("Insertion Success --> jira Id : ", jira_issue["issues_id"])

        pgConnection.commit()
        cursor.close()
        pgConnection.close()

    except psycopg2.Error as e:
        print("check_id function in kb_updation file error")
        print(str(e))
    
