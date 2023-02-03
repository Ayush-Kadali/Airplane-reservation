import mysql.connector
import matplotlib.pyplot as plt
import random
import string
import sys


# Connect to the database
cnx = mysql.connector.connect(
    user="root", password="tiger123", host="localhost", database="AIRPLANE"
)


# Add a cursor object
cursor = cnx.cursor()


def main():
    options = {1: sign_in, 2: sign_up, 3: delete_account, 4: exit}

    while True:
        
        print("Menu:")
        print("1. Sign in")
        print("2. Sign up")
        print("3. Delete account")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice in [1,2,3,4]:
            options[choice]()
        else:
            print("Please enter a valid answer!!")
            main()



def sign_in():
    options = {1: sign_in_admin, 2: sign_in_user}

    print("Sign in as:")
    print("1. Admin")
    print("2. User")
    choice = int(input("Enter your choice: "))
    if choice in [1,2]:
        options[choice]()
    else:
        print("Enter a valid option!!!")
        sign_in()

def sign_in_admin():

    # Get the email and password to sign in with
    global email
    global password
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Execute a SELECT query to get the admin with the given email and password
    query = f"SELECT * FROM ADMIN WHERE EMAIL='{email}' AND PASSWORD='{password}'"
    cursor.execute(query)
    admin = cursor.fetchone()

    if admin is None:
        print("Invalid email or password. Please try again.")
        print("*" * 50)
    else:
        print("*" * 50)
        print(f"Welcome, {admin[2]} {admin[3]}!")
        print("*" * 50)
        admin_menu()


def sign_in_user():
    # Get the email and password to sign in with
    global email
    global password
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Execute a SELECT query to get the user with the given email and password
    query = f"SELECT * FROM USER WHERE EMAIL='{email}' AND PASSWORD='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user is None:
        print("Invalid email or password. Please try again.")
    else:
        print("*" * 50)
        print(f"Welcome, {user[2]} {user[3]}!")
        print("*" * 50)
        user_menu()


def sign_up():
    options = {1: sign_up_admin, 2: sign_up_user}

    print("Sign up as:")
    print("1. Admin")
    print("2. User")
    choice = int(input("Enter your choice: "))
    if choice in [1,2]:
        options[choice]()
    else:
        print("Enter a valid choice!!!")
        sign_up()

def sign_up_admin():
    # Get the email and password to sign up with
    email = input("Enter email: ")
    password = input("Enter password: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")

    # Execute an INSERT query to add a new admin to the ADMIN table
    query = f"INSERT INTO ADMIN (EMAIL, PASSWORD, FNAME, LNAME, PHONE) VALUES ('{email}', '{password}', '{first_name}', '{last_name}', '{phone}')"
    cursor.execute(query)
    cnx.commit()
    print("Account Addd successfully!")
    print("*" * 50)


def sign_up_user():
    # Get the email and password to sign up with
    email = input("Enter email: ")
    password = input("Enter password: ")
    first_name = input("Enter first name: ")
    last_name = input("Enter last name: ")
    phone = input("Enter phone number: ")
    user_type = input("Enter user type (Traveller or Agent): ")

    # Execute an INSERT query to add a new user to the USER table
    query = f"INSERT INTO USER (EMAIL, PASSWORD, FNAME, LNAME, PHONE, TYPE_OF_USER) VALUES ('{email}', '{password}', '{first_name}', '{last_name}', '{phone}', '{user_type}')"
    cursor.execute(query)
    cnx.commit()
    print("Account Addd successfully!")
    print("*" * 50)


def delete_account():
    options = {1: delete_admin_account, 2: delete_user_account}

    print("Delete account for:")
    print("1. Admin")
    print("2. User")
    choice = int(input("Enter your choice: "))
    if choice in [1,2]:
        options[choice]()
    else:
        print("Enter a valid choice!!!")
        delete_account()


def delete_admin_account():
    # Get the email and password to delete the account for
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Execute a DELETE query to delete the admin with the given email and password
    query = f"DELETE FROM ADMIN WHERE EMAIL='{email}' AND PASSWORD='{password}'"
    cursor.execute(query)
    cnx.commit()
    print("Account deleted successfully!")
    print("*" * 50)


def delete_user_account():
    # Get the email and password to delete the account for
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Execute a DELETE query to delete the user with the given email and password
    query = f"DELETE FROM USER WHERE EMAIL='{email}' AND PASSWORD='{password}'"
    cursor.execute(query)
    cnx.commit()
    print("Account deleted successfully!")
    print("*" * 50)


def exit():
    # Close the cursor and connection
    cursor.close()
    cnx.close()
    sys.exit()


def admin_menu():
    options = {1: airport_menu, 2: airline_company_menu, 3: exit}

    while True:
        print("Menu:")
        print("1. Airport operations")
        print("2. Airline company operations")
        print("3. Exit")
        choice = int(input("Enter your choice: "))
        if choice in [1,2,3]:
            options[choice]()
        else:
            print("Enter a valid choice")
            admin_menu()


def airport_menu():
    options = {1: Add_airport, 2: read_airport, 3: update_airport, 4: delete_airport}

    while True:
        print("Airport menu:")
        print("1. Add airport")
        print("2. Read airport")
        print("3. Update airport")
        print("4. Delete airport")
        print("5. Go back")
        choice = int(input("Enter your choice: "))
        if choice == 5:
            break
        if choice in [1,2,3,4]:
            options[choice]()
        else:
            print("Enter a valid choice!!!")
            airport_menu()


def Add_airport():
    # Get the airport code, name, location, city, state, country, and zip code to Add a new airport
    airport_code = input("Enter airport code: ")
    airport_name = input("Enter airport name: ")
    location = input("Enter location: ")
    city = input("Enter city: ")
    state = input("Enter state: ")
    country = input("Enter country: ")
    zip_code = input("Enter zip code: ")

    # Execute an INSERT query to add a new airport to the AIRPORT table
    query = f"INSERT INTO AIRPORT (AIRPORT_CODE, AIRPORT_NAME, LOCATION, CITY, STATE, COUNTRY, ZIP) VALUES ('{airport_code}', '{airport_name}', '{location}', '{city}', '{state}', '{country}', '{zip_code}')"
    cursor.execute(query)
    cnx.commit()

    cursor.execute("SELECT AIRPORT_CODE FROM AIRPORT")
    existing_airports = [row[0] for row in cursor.fetchall()]

    for airport in existing_airports:
        if airport != airport_code : 
            distance = int(input(f"Enter the distance between {airport_code} and {airport}: "))
            sql = f"INSERT INTO AIRPORT_DISTANCE (DEPARTURE_AIRPORT_CODE, ARRIVAL_AIRPORT_CODE, DISTANCE) VALUES ('{airport_code}', '{airport}', {distance})"
            # Executing the SQL query
            cursor.execute(sql)
            cnx.commit()


    print("Airport Addd successfully!")
    print("*" * 50)


def read_airport():

    # Execute a SELECT query to get the airport with the given airport code
    query = f"SELECT * FROM AIRPORT"
    cursor.execute(query)
    airport = cursor.fetchall()

    for row in airport:
        print(f"Airport code: {row[0]}")
        print(f"Airport name: {row[1]}")
        print(f"Location: {row[2]}")
        print(f"City: {row[3]}")
        print(f"State: {row[4]}")
        print(f"Country: {row[5]}")
        print(f"Zip code: {row[6]}")
        print("*" * 50)


def update_airport():
    # Get the airport code to update
    airport_code = input("Enter airport code: ")

    # Execute a SELECT query to get the airport with the given airport code
    query = f"SELECT * FROM AIRPORT WHERE AIRPORT_CODE='{airport_code}'"
    cursor.execute(query)
    airport = cursor.fetchone()

    if airport is None:
        print("Airport not found.")
        print("*" * 50)
    else:
        # Get the updated airport code, name, location, city, state, country, and zip code
        airport_name = input("Enter updated airport name: ")
        location = input("Enter updated location: ")
        city = input("Enter updated city: ")
        state = input("Enter updated state: ")
        country = input("Enter updated country: ")
        zip_code = input("Enter updated zip code: ")


        # Execute an UPDATE query to update the airport with the given airport code
        query = f"UPDATE AIRPORT SET AIRPORT_NAME='{airport_name}', LOCATION='{location}', CITY='{city}', STATE='{state}', COUNTRY='{country}', ZIP='{zip_code}' WHERE AIRPORT_CODE='{airport_code}'"
        cursor.execute(query)
        cnx.commit()

        cursor.execute("SELECT AIRPORT_CODE FROM AIRPORT")
        existing_airports = [row[0] for row in cursor.fetchall()]

        for airport in existing_airports:
            if airport != airport_code : 
                distance = int(input(f"Enter the distance between {airport_code} and {airport}: "))
                sql = f"UPDATE AIRPORT_DISTANCE SET DEPARTURE_AIRPORT_CODE = '{airport_code}', ARRIVAL_AIRPORT_CODE = '{airport}', DISTANCE = '{distance}' WHERE AIRPORT_CODE='{airport_code}')"
                # Executing the SQL query
                cursor.execute(sql)
                cnx.commit()

        print("Airport updated successfully!")
        print("*" * 50)


def delete_airport():
    # Get the airport code to delete
    airport_code = input("Enter airport code: ")

    # Execute a DELETE query to delete the airport with the given airport code
    query = f"DELETE FROM AIRPORT WHERE AIRPORT_CODE='{airport_code}'"
    cursor.execute(query)
    cnx.commit()
    print("Airport deleted successfully!")
    print("*" * 50)


def airline_company_menu():
    options = {
        1: Add_airline_company,
        2: read_airline_company,
        3: update_airline_company,
        4: delete_airline_company,
    }

    while True:
        print("Airline company menu:")
        print("1. Add airline company")
        print("2. Read airline company")
        print("3. Update airline company")
        print("4. Delete airline company")
        print("5. Go back")
        choice = int(input("Enter your choice: "))
        if choice == 5:
            break
        if choice in [1,2,3,4]:
            options[choice]()
        else:
            print("Enter a valid choice!!!")
            airline_company_menu()


def Add_airline_company():
    # Get the company ID and name to Add a new airline company
    company_id = input("Enter company ID: ")
    company_name = input("Enter company name: ")

    # Execute an INSERT query to add a new airline company to the AIRLINE_COMPANY table
    query = f"INSERT INTO AIRLINE_COMPANY (COMPANY_ID, COMPANY_NAME) VALUES ('{company_id}', '{company_name}')"
    cursor.execute(query)
    cnx.commit()
    print("Airline company Addd successfully!")
    print("*" * 50)


def read_airline_company():

    # Execute a SELECT query to get the airline company with the given company ID
    query = f"SELECT * FROM AIRLINE_COMPANY"
    cursor.execute(query)
    airline_company = cursor.fetchall()

    for row in airline_company:
        print(f"Company ID: {row[0]}")
        print(f"Company name: {row[1]}")
        print("*" * 50)


def update_airline_company():
    # Get the company ID to update
    company_id = input("Enter company ID: ")

    # Execute a SELECT query to get the airline company with the given company ID
    query = f"SELECT * FROM AIRLINE_COMPANY WHERE COMPANY_ID='{company_id}'"
    cursor.execute(query)
    airline_company = cursor.fetchone()

    if airline_company is None:
        print("Airline company not found.")
        print("*" * 50)
    else:
        # Get the updated company name
        company_name = input("Enter updated company name: ")

        # Execute an UPDATE query to update the airline company with the given company ID
        query = f"UPDATE AIRLINE_COMPANY SET COMPANY_NAME='{company_name}' WHERE COMPANY_ID='{company_id}'"
        cursor.execute(query)
        cnx.commit()
        print("Airline company updated successfully!")
        print("*" * 50)


def delete_airline_company():
    # Get the company ID to delete
    company_id = input("Enter company ID: ")

    # Execute a DELETE query to delete the airline company with the given company ID
    query = f"DELETE FROM AIRLINE_COMPANY WHERE COMPANY_ID='{company_id}'"
    cursor.execute(query)
    cnx.commit()
    print("Airline company deleted successfully!")
    print("*" * 50)


def user_menu():
    options = {
        1: RESERVATION_menu,
        2: pie_chart,
        3: cancel_flight,
        4: ticket_validation,
    }
    while True:
        print("Airline company menu:")
        print("1. Book Flight")
        print("2. See a Pie chart on which airline is used the most")
        print("3. Cancel Flight")
        print("4. Ticket Validation")
        print("5. Go Back")
        choice = int(input("Enter your choice: "))
        if choice == 5:
            break
        if choice in [1,2,3,4,5]:
            options[choice]()
        else:
            print("Please enter a valid choice")
            user_menu()


def RESERVATION_menu():

    # Get the email and password of the user
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Execute a SELECT query to get the user with the given email and password
    query = f"SELECT * FROM USER WHERE EMAIL='{email}' AND PASSWORD='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user is None:
        # Get the email and password of the user
        print("Incorrect Password! Try again")

    else:
        # Get the list of airports
        query = "SELECT AIRPORT_CODE, AIRPORT_NAME FROM AIRPORT"
        cursor.execute(query)
        airports = cursor.fetchall()
        print("Airports:")
        for airport in airports:
            print(f"{airport[0]}: {airport[1]}")

        # Get the from airport code and to airport code
        from_airport = input("Enter from airport code: ")
        to_airport = input("Enter to airport code: ")

        # Get the list of airline companies
        query = "SELECT COMPANY_ID, COMPANY_NAME FROM AIRLINE_COMPANY"
        cursor.execute(query)
        companies = cursor.fetchall()
        print("Airline companies:")
        for company in companies:
            print(f"{company[0]}: {company[1]}")

        # Get the airline company ID
        company_id = input("Enter airline company ID: ")
        query = f"SELECT COMPANY_NAME FROM AIRLINE_COMPANY WHERE COMPANY_ID = '{company_id}'"
        cursor.execute(query)
        temp = cursor.fetchone()
        airline = temp[0]

        # Get the seat class
        seat_class = input("Enter seat class (economy, business, first): ")

        # Generate a random PNR
        number = str(random.randint(1000, 9999))
        char = f"{company_id}".join(random.choices(string.ascii_uppercase, k=4))
        pnr = char + number

        # Execute an INSERT query to add a new RESERVATION to the RESERVATION table
        query = f"INSERT INTO RESERVATION (PNR, EMAIL, FROM_AIRPORT, TO_AIRPORT, AIRLINE, SEAT_CLASS) VALUES ('{pnr}', '{email}', '{from_airport}', '{to_airport}', '{airline}', '{seat_class}')"
        cursor.execute(query)
        cnx.commit()
        print(f"Flight booked successfully! PNR: {pnr}")
        print("*" * 50)

        print("*" * 50)
        print("Ticket overview:")
        print(f"PNR: {pnr}")
        print(f"From: {from_airport}")
        print(f"To: {to_airport}")
        print(f"Airline: {company_id}")
        print(f"Seat class: {seat_class}")
        print(f"Email: {email}")
        print("*" * 50)


def pie_chart():
    # Execute a query to get the number of reservations for each airline
    query = """
    SELECT AIRLINE, COUNT(*) as count
    FROM RESERVATION
    GROUP BY AIRLINE
    """
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Extract the data you want to plot
    airline_ids = [row[0] for row in results]
    reservation_counts = [row[1] for row in results]

    # Create the pie chart
    plt.pie(reservation_counts, labels=airline_ids, autopct="%1.1f%%")

    # Add a title
    plt.title("Percentage of Airlines choosed")

    # Show the plot
    plt.show()


def cancel_flight():
    # Get the PNR, email, and password of the user
    pnr = input("Enter PNR: ")
    email = input("Enter email: ")
    password = input("Enter password: ")

    # Execute a SELECT query to get the user with the given email and password
    query = f"SELECT * FROM USER WHERE EMAIL='{email}' AND PASSWORD='{password}'"
    cursor.execute(query)
    user = cursor.fetchone()

    if user is None:
        print("Invalid email or password.")
        print("*" * 50)
    else:
        # Execute a SELECT query to get the RESERVATION with the given PNR and email
        query = f"SELECT * FROM RESERVATION WHERE PNR='{pnr}' AND EMAIL='{email}'"
        cursor.execute(query)
        RESERVATION = cursor.fetchone()

        if RESERVATION is None:
            print("RESERVATION not found.")
        else:
            # Execute a DELETE query to delete the RESERVATION with the given PNR
            query = f"DELETE FROM RESERVATION WHERE PNR='{pnr}'"
            cursor.execute(query)
            cnx.commit()
            print("Flight cancelled successfully!")
            print("*" * 50)


def ticket_validation():
    # Get the PNR and email of the user
    pnr = input("Enter PNR: ")
    email = input("Enter email: ")

    # Execute a SELECT query to get the RESERVATION with the given PNR and email
    query = f"SELECT * FROM RESERVATION WHERE PNR='{pnr}' AND EMAIL='{email}'"
    cursor.execute(query)
    RESERVATION = cursor.fetchone()

    if RESERVATION is None:
        print("Ticket not valid.")
        print("*" * 50)
    else:
        # Execute a SELECT query to get the from airport and to airport with the given airport codes
        from_query = f"SELECT * FROM AIRPORT WHERE AIRPORT_CODE='{RESERVATION[2]}'"
        to_query = f"SELECT * FROM AIRPORT WHERE AIRPORT_CODE='{RESERVATION[3]}'"
        cursor.execute(from_query)
        from_airport = cursor.fetchone()
        cursor.execute(to_query)
        to_airport = cursor.fetchone()

        # Execute a SELECT query to get the airline company with the given company name
        query = f"SELECT * FROM AIRLINE_COMPANY WHERE COMPANY_NAME = '{RESERVATION[4]}'"
        cursor.execute(query)
        company = cursor.fetchone()

        print("*" * 50)
        print("Ticket overview:")
        print(f"PNR: {RESERVATION[0]}")
        print(f"From: {from_airport[1]} ({RESERVATION[2]})")
        print(f"To: {to_airport[1]} ({RESERVATION[3]})")
        print(f"Airline: {company[1]} ({RESERVATION[4]})")
        print(f"Seat class: {RESERVATION[5]}")
        print(f"Email: {RESERVATION[6]}")
        print("*" * 50)


main()
