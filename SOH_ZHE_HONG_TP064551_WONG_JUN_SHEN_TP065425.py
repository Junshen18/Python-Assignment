import time
import datetime
import os

#Soh Zhe Hong
#TP064551

#Wong Jun Shen
#TP065425


def timer_end(time_elapsed):
    current_time = datetime.datetime.now()
    total_time = (
            current_time - time_elapsed).total_seconds()  # Subtract current time with the time the program started to total get time elapsed
    return total_time


# Function to create a directory with its name accepted as parameter
def createdirectory(directory):
    if os.path.exists(directory):  # Check if the directory exists at the file location the program is started
        pass
    else:
        os.makedirs(directory)  # Create directory at the same file location as program
    return directory


# Function to create a log file with predetermined contents such as creation time, fields to specify attribute of each column.
def createlogfile(directory, file_name):
    open_date = datetime.datetime.now().strftime(
        'Logging started at %d/%m/%Y %H:%M:%S\n')  # Get the time the log file is created and format it as shown.
    field = 'Field: date-time type description\n\n'  # Specify the fields of the log file
    msg = 'DETAILS OF OPERATION\n\n'
    log_header = [open_date, field, msg]  # Set the header format of the log file
    file_path = f"{directory}\{file_name}"  # Determine the directory and file name the contents will be saved at.

    # Append the log file header into the specified file location.
    with open(file_path, "a") as afile:
        for item in log_header:
            afile.write(item)
    return file_path


# Function to accept information from the program and log them into specific log files.
def log(file_path, log_type, description):
    log_type = f'[{log_type.upper()}]'  # Specify the type of action logged, Example: Error, info etc
    time = datetime.datetime.now().strftime(
        '[%Y.%m.%d-%H.%M.%S]')  # Get the time where an action is performed and format it into string.
    log_content = time + log_type + description  # Combine the time, logging type and description of action together

    # Append the log contents into the specified file
    with open(file_path, "a") as afile:
        afile.write(log_content)
        afile.write("\n")


# Function that plays a loading animation with a user-specified duration
def loading(duration):
    # Defining the frames of the loading animation
    animation = [
        "[             ]",
        "[=            ]",
        "[==           ]",
        "[===          ]",
        "[===l         ]",
        "[===lo        ]",
        "[===loa       ]",
        "[===load      ]",
        "[===loadi     ]",
        "[===loadin    ]",
        "[===loading   ]",
        "[===loading=  ]",
        "[===loading== ]",
        "[===loading===]",
        "[ ==loading===]",
        "[  =loading===]",
        "[   loading===]",
        "[    oading===]",
        "[     ading===]",
        "[      ding===]",
        "[       ing===]",
        "[        ng===]",
        "[         g===]",
        "[          ===]",
        "[           ==]",
        "[            =]",
        "[             ]",
        "[             ]",
        "[             ]",
    ]

    starting_frame = 0  # The animation starts at the first frame
    pause_time = duration / len(animation)  # Time delay when switching between frames

    while True:
        frame_num = starting_frame % len(animation)
        print(animation[frame_num],
              end='\r')  # Prints the animation and refreshes the line whenever the next frame will be played.
        time.sleep(pause_time)
        starting_frame += 1  # Move on to the next frame

        # Stop the animation after it has played for the user-specified duration.
        if starting_frame * (pause_time) == duration:
            break


# Function to prompt users before continuing an action
def confirm_prompt(message):
    options_for_yes = ["yes", "y"]
    options_for_no = ["no", "n"]
    while True:
        user_input = input(message)
        if user_input.lower() in options_for_yes:
            return True
        elif user_input.lower() in options_for_no:
            return False
        else:
            print(f"Input {user_input} is unrecognised, please try again")


def pause():
    input("Press any key to continue...\n")


# Function to validate the username and password from a specified file.
def ValidateUser(name, password, userfile_path):
    found = False  # Initial verification would be False
    with open(userfile_path, 'r') as ufile:
        for record in ufile:
            tempRecord = record.rstrip().split(
                ",")  # Convert the login credentials from userfile and split them into list elements.
            if tempRecord[0] == name and tempRecord[1] == password:
                found = True  # Set to True after both username and password matches the records.
    return found


# Function to get user type based on username and password
def getUserData(file_path, username, password, column):
    users = FiletoList(file_path)  # Convert file to list
    data = None
    for record in users:
        if username == record[0] and password == record[
            1]:  # If both username and password matches, return user type
            data = record[column]
            break
    return data


def Login(userfile_path, attempts_allowed):
    count = 0  # Set current attempt to 0
    ValidateStatus = False
    while count < attempts_allowed:  # Break the loop after exceeded maximum attemped allowed.
        username = input("Please enter username: ")
        password = input("Please enter password: ")
        flag = ValidateUser(username, password,
                            userfile_path)  # Accepts user input for username, password then ensure they match the records.
        if flag == True:
            user = getUserData(userfile_path, username, password, 2)  # Obtain user's name in the records
            usertype = getUserData(userfile_path, username, password, 3)  # Obtains relevant usertype and returns it
            ValidateStatus = True  # Return True if username and password match the records.
            break
        else:
            print("Invalid Login Credentials!")
            count += 1  # +1 to current attempt after failing validation
            print("Remaining attempts: ", (attempts_allowed - count))
    return ValidateStatus, user, usertype


def PasswordChecker(password):
    special_chars = "`~!@#$%^&*()_+-=[{]}\|;:\"'<>?"  # Detailing a string of characters that are not alphabets or numbers
    recommended_inputs = ["Lowercases", "Uppercases", "Special Characters", "Numbers"]  # Types of input recommended
    password_info = []
    # For loop in every If statement since any() function only returns True\False and doesn't allow iterations
    if any('a' <= letter <= 'z' for letter in password):
        recommended_inputs.remove("Lowercases")  # Remove "Lowercase" from missing input types if there are lowercase characters

    if any('A' <= letter <= 'Z' for letter in password):
        recommended_inputs.remove("Uppercases")  # Remove "Uppercase" from missing input types if there are uppercase characters

    if any(letter in special_chars for letter in password):
        recommended_inputs.remove("Special Characters")  # Remove "Special Characters" from missing input types if there are special characters

    if any(letter.isdigit() for letter in password):
        recommended_inputs.remove("Numbers")  # Remove "Numbers" from missing input types if there are numbers

    # Loop to check for repeating characters (3 same characters in a row)
    index = 0  # Start from beginning of password string
    repetition = 0  # No repetiting characters by default
    while index < len(password):
        try:
            # If statement to check if there are 3 identical characters in a row
            if password[index] == password[index + 1] == password[index + 2]:
                repetition += 1  # +1 after detecting identical characters
                index += 3  # If yes, move on to the next 3 characters after the previous group
            else:
                index += 1  # Move forward by 1 character after not detecting repetitive characters
        except IndexError:
            break

    missing_types = len(recommended_inputs)

    error = max(missing_types,
                repetition)  # Determine the largest value between number of repeating characters or missing input types

    # Display number of repeating characters if only repetition exists
    if repetition > 0:
        repeated_chars = "Repeated characters: " + str(repetition)
        password_info.append(repeated_chars)

    # Display number of missing input types if only the error existsa
    if missing_types > 0:
        missing_inputs = "Missing types: " + ", ".join(recommended_inputs)
        password_info.append(missing_inputs)

    overview = "\n".join(password_info)

    # Check for number of errors and determine password strength based on the errors.
    if error == 0:
        print("Password Strength: Excellent")

    elif error == 1:
        print("Password Strength: Good\n", overview)

    elif error == 2:
        print("Password Strength: Average\n", overview)

    elif error == 3:
        print("Password Strength: Below Average\n", overview)

    else:
        print("Password Strength: Poor\n", overview)

    # Provide option to input another password if unsatisfied
    confirmation = confirm_prompt("Do you want to continue with current password? [Y] for Yes, [N] for No")
    return confirmation


# Function to verify name by accepting an argument
def VerifyName(text):
    invalid_char = "\"!#$%&'()*+-/:;<=>?@[\]^_`{|}~"  # List of characters that cannot be in the text
    flag = False  # False because no invalid characters found yet
    if text != "":  # Check if the text argument is not blank
        for i in invalid_char:  # Iterate through every invalid characters
            for z in text:  # Iterate through the text argument
                if i == z:
                    flag = True  # True if there is invalid characters in the text argument
                    break
        # Check if there are invalid characters detected
        if flag == True:
            print("Special Characters are restricted, please try again.")
            return False
        else:
            return True
    else:
        print("Invalid Details! Please try again")
        return False


def VerifyDate(date):
    try:
        current_date = datetime.datetime.now()
        check_date = datetime.datetime.strptime(date,"%d/%m/%Y")  # Convert the date argument from string into datetime for comparison
        dd, mm, yy = date.split('/')  # Split date argument into day (dd), month (mm), year (yy) as integers
        dd = int(dd)
        mm = int(mm)
        yy = int(yy)

        # Determining the maximum amount of days based on month
        if (mm == 1 or mm == 3 or mm == 5 or mm == 7 or mm == 8 or mm == 10 or mm == 12):
            days = 31
        elif (mm == 4 or mm == 6 or mm == 9 or mm == 11):
            days = 30
        elif (mm == 2 and yy % 4 == 0):
            days = 29
        elif (mm == 2 and yy % 4 != 0):
            days = 28
        else:
            print("Month is Invalid!")  # Month entered is not within 1 - 12
            return False

        # Check if day entered is within day count range of the month
        if (dd < 1 or dd > days):
            print("Day is invalid!")
            return False

        # Check if date entered is ahead of current date.
        if check_date > current_date:
            print("Date is invalid")
            return False
        else:
            return True
    except ValueError:
        print("Invalid input method")
        return False


# Function to verify if input is within the 12 months
def VerifyMonth(month):
    data = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    if month in data:
        return True
    else:
        print("Invalid Details! Please try again by inputting months in their short-form! Eg. Jan")
        return False


# Function to ensure payment is only answered with paid or unpaid
def VerifyPaymentStatus(text):
    status = ["Paid", "Unpaid"]
    if text != "":
        if text.lower().capitalize() in status:
            return True
        else:
            print("Invalid input! Only 'Paid' or 'Unpaid' is acceptable!")
            return False

    else:
        print("Invalid Details! Please try again")
        return False


# Function to count the age based on date of birth
def countage(date_of_birth):
    birth_year = datetime.datetime.strptime(date_of_birth, '%d/%m/%Y')
    current_year = datetime.date.today().year
    age = current_year - birth_year.year
    return age


# Function to get date outside of a certain range with validation
def getDateoutsideRange(text, compared_date, range):
    while True:
        estimated_date = InputData(text, str, VerifyDate)
        date1 = datetime.datetime.strptime(estimated_date, '%d/%m/%Y')
        date2 = datetime.datetime.strptime(compared_date, '%d/%m/%Y')
        difference = date1.year - date2.year
        outside_range = False

        # Determine if "range" input is negative or positive
        if range > 0:
            if difference >= range:  # Ensure only return positive value outside defined range
                outside_range = True
        else:
            if difference <= range:  # Ensure only return negative value
                outside_range = True

        # Prompt user to continue after getting invalid data
        if outside_range:
            return estimated_date
        else:
            print(f"Date entered is not outside the \"{range}\" range, please try again")


# Function to determine if the person is a mature or minor through date of birth
def VerifyMatureMinor(date_of_birth):
    adult = False
    date_verification = VerifyDate(date_of_birth)
    if date_verification:
        age = countage(date_of_birth)
        if age >= 18:
            adult = True
        else:
            print("Subject is still a minor!")
    return adult


# Function to verify if the number argument is a numerical value
def VerifyDigits(number):
    try:
        number = float(
            number)  # If the argument can be converted to float then it is a numerical value, otherwise an error would occur and be captured
        return True
    except ValueError:
        print("Invalid input! Please try again")
        return False


# Function to verify if tenant ID exists within the file
def GetID(question, file_path, column):
    while True:
        ID = InputData(question, str, VerifyName)
        # Search tenant file for the ID and return results by comparing length of result list
        data = SearchData(file_path, column, ID)
        if len(data) > 0 or ID.lower() == "none":
            return ID
        else:
            print("ID does not exist, either enter [None] or a correct value")


# Return all files with required format from a specified directory
# single-asterisk argument is used to accomodate multiple file formats
def getFilesfromDirectory(directory, *file_format):
    try:
        all_files = os.listdir(f"{directory}/")  # Returning all files from the directory into a list
        filtered_files = []
        # Iterate the list to validate file items and filter them for required file formats
        for file in all_files:
            for format in file_format:
                if file.endswith(format):  # Check for matching characters at the end of the file's name
                    filtered_files.append(file)
        return filtered_files
    except TypeError:
        print("File format is not recognised")


# Function to check if records or data in a specific records have duplicates
def CheckDuplicateinFile(file_path, duplicate):
    recordexists = False
    with open(file_path, "r") as rfile:
        for record in rfile:
            record = record.rstrip().split(",")  # Convert each record into list for iteration
            if duplicate in record:
                recordexists = True  # True if a duplicate is detected
                break
    return recordexists


# Function to convert all individual records in a file into a list
def FiletoList(file_path):
    item_list = []
    data = []
    with open(file_path, 'r') as rfile:
        for line in rfile:
            item_list.append(line.rstrip(" \n"))  # Append all records into an array for iteration

    # Iterate through each records and convert them into lists
    for record in item_list:
        record = record.split(",")
        data.append(record)
    return data


# Function to overwrite the entire file with new_file argument
def OverwriteFile(file_path, new_file):
    with open(file_path, "w") as wfile:
        for record in new_file:
            data = ",".join(record)  # Join elements in record into a string with "," as separator
            wfile.write(data + "\n")


def ModifyRecord(file_path, column, key, replacement_data):
    mlist = FiletoList(file_path)  # Convert file to be modified into list for iteration
    for index, data in enumerate(
            mlist):  # Enumerate to get the position of record in the file (index) and the data at the position
        if data[0] == key:
            data[column] = replacement_data  # Replace old data with new data at its specific position in a line
            mlist[index] = data  # Replace the whole line of record with new record with modified data
            break
    OverwriteFile(file_path, mlist)


# Function to save data to a specific file
def SaveData(data, file_path):
    data = ",".join(data)  # Join data into a string before writing to file
    with open(file_path, "a") as afile:
        afile.write(data)  # Appending data to the file that act as saving
        afile.write("\n")


# Function to search matching records and return them in a list
def SearchData(file_path, column, keyword):
    file = FiletoList(file_path)
    file_items = []
    # Iterate through every record in file and find records that matches the keyword
    for record in file:
        if (keyword in record[column]) and (len(keyword) == len(record[column])):
            file_items.append(record)
    return file_items


# Function to delete the specific data with keyword in specific file
def DeleteData(file_path, keyword, column):
    item_list = FiletoList(file_path)
    for index, data in enumerate(item_list):
        if data[column] == keyword:  # Compare the data in list with keyword before proceed
            del_item = item_list[index]
            item_list.remove(del_item)  # Remove the specific data in list
            break
    OverwriteFile(file_path, item_list) # Overwrite the old list with new list


# Function to move matching records from one file to the another
def MoveRecordtoFile(file_path, keyword, newfile_path):
    item_list = FiletoList(file_path)
    for index, data in enumerate(item_list):
        if data[0] == keyword:
            del_item = item_list[index]
            DeleteData(file_path, keyword, 0)
            print(f"Data from {file_path} has been moved to {newfile_path}!")
            break
    SaveData(del_item, newfile_path)


def InputData(text, type, validator):
    verification = False
    while verification == False:
        data = input(text)  # Set the text argument to be input message
        verification = validator(data)  # Validate the input and return True False
    return type(data)  # Convert the data class to "type" argument before returning it


def GenerateID(reference_file, identification_letter):
    with open(reference_file, "r") as rfile:
        ID_num = len(
            rfile.readlines()) + 1  # Reads all lines and stores it in list, list length = line count (+1 since line count starts from 0)
    ID = f"{identification_letter}{ID_num}"  # Set identification letter in front to differentiate IDs for different files
    with open(reference_file, "a") as wfile:
        wfile.write(ID + "\n")
    return ID


def DeleteID(file_path):
    ID_List = FiletoList(file_path)
    ID_List = ID_List[:-1]  # Remove the latest ID generated
    OverwriteFile(file_path, ID_List)


# Function to accept a list containing one tenant record and print it
def PrintTenantDetails(data):
    print(f"1. ID                      : {data[0]}")
    print(f"2. Name                    : {data[1]}")
    print(f"3. Age                     : {data[2]}")
    print(f"4. Date of Birth           : {data[3]}")
    print(f"5. Date of Rental          : {data[4]}")
    print(f"6. Place of Birth          : {data[5]}")
    print(f"7. City of Birth           : {data[6]}")
    print(f"8. Work History            : {data[7]}")
    print(f"9. Current Employer's Name : {data[8]}")
    print("\n")


# Function to accept a list containing one apartment record and print it
def PrintApartmentDetails(data):
    print(f"1. ID                          : {data[0]}")
    print(f"2. Current occupant's ID       : {data[1]}")
    print(f"3. Date of Acquisition         : {data[2]}")
    print(f"4. Square footage of apartment : {data[3]} square ft")
    print(f"5. Expected Rent               : RM{data[4]}")
    print(f"6. Rental History of occupant  : {data[5]} past tenant/s")
    print(f"7. Deposit from occupant       : RM{data[6]}")
    print("\n")


# Function to accept a list containing one transaction record and print it
def PrintTransactionDetails(data):
    print(f"1. Tenant ID               : {data[0]}")
    print(f"2. Apartment ID            : {data[1]}")
    print(f"3. Payment Month           : {data[2]}")
    print(f"4. Rental Fees             : RM{data[3]}")
    print(f"5. Payment status          : {data[4]}")
    print("\n")


# Function to register for new user to access UMS
def GenerateCredentials(userfile, user, usertype):
    username = InputData("Please enter new username for user: ", str, VerifyName)
    password = InputData("Please enter new password for user: ", str, PasswordChecker)
    login_credential = [username, password, user, usertype]
    SaveData(login_credential, userfile)


# Function to collect tenant details and save in tenant details file
def AddTenantDetails(file_path, userfile):
    continue_input = True

    while continue_input:

        Name = InputData("Tenant's Name : ", str, VerifyName)
        DateOfBirth = InputData("Date of Birth of Tenant (d/m/y) : ", str, VerifyMatureMinor)
        DateofRental = getDateoutsideRange("Date of Apartment Rental (d/m/y) : ", DateOfBirth, 18)
        PlaceOfBirth = InputData("Place of Birth of Tenant : ", str, VerifyName)
        CityOfBirth = InputData("City of Birth of Tenant : ", str, VerifyName)
        Work_History = InputData("Work History about Tenant : ", str, VerifyName)
        Current_Employer = InputData("Current employer's name of Tenant : ", str, VerifyName)
        ID = GenerateID("Tenant_ID", "T")   # Auto generated ID
        Age = countage(DateOfBirth)     # Count tenant's age by date of birth provided
        details = [ID, Name, str(Age), DateOfBirth, DateofRental, PlaceOfBirth, CityOfBirth, Work_History,
                   Current_Employer]
        PrintTenantDetails(details)     # Print the output in order to double check the details
        option = confirm_prompt(
            "Please make sure your details are correct!\n"
            "Do you wish to proceed with current data? [Y] for yes [N] for no\n: ")
        if option:
            GenerateCredentials(userfile, Name, "t")    # Generate the UMS account for tenant
            SaveData(details, file_path)            # Save data into file
            print(f"Tenant record has been saved into {file_path}")
        else:
            DeleteID("Tenant_ID.txt")  # Remove the ID previously auto generated as user decided to clear the details
        # Continue input or exit
        continue_input = confirm_prompt("Do you wish to continue input? [Y] for yes [N] for no\n: ")


# Function to collect apartment details and save in apartment details file
def AddApartmentDetails(file_path, tenantfile):
    continue_input = True

    while continue_input:
        Tenant_ID = GetID("Current occupant's ID : ", tenantfile, 0).capitalize()
        Date_Acquisition = InputData("Date of Acquisition (d/m/y) : ", str, VerifyDate)
        Footage = InputData("Square footage of apartment : ", float, VerifyDigits)
        Expected_Rent = InputData("Expected Rent : ", float, VerifyDigits)
        Rental_History = InputData("Rental History of occupant : ", int, VerifyDigits)
        Deposit = InputData("Deposit from occupant : ", float, VerifyDigits)
        ID = GenerateID("Apartment_ID", "AP")   # Auto generated ID
        details = [ID, Tenant_ID, Date_Acquisition, str(Footage), str(Expected_Rent),
                   str(Rental_History), str(Deposit)]
        PrintApartmentDetails(details)      # Print the output in order to double check the details
        option = confirm_prompt(
            "Please make sure your details are correct!\n"
            "Do you wish to proceed with current data? [Y] for yes [N] for no\n: ")    # Save data or Clear data
        if option:
            SaveData(details, file_path)            # Save data into file
            print(f"Apartment record has been saved into {file_path}")
        else:
            DeleteID("Apartment_ID.txt")    # Remove the ID previously auto generated as user decided to clear the details
        # Continue input or exit
        continue_input = confirm_prompt("Do you wish to continue input? [Y] for yes [N] for no\n: ")


# Function to collect transaction details and save in transaction details file
def AddTransactionDetails(file_path, tenantfile, apartmentfile):
    continue_input = True
    while continue_input:
        Tenant_ID = GetID("Enter tenant's ID : ", tenantfile, 0)
        Apartment_ID = GetID("Enter Apartment's ID : ", apartmentfile, 0)
        Rental_Month = InputData("Rental fees for which month (Exp:Apr): ", str, VerifyMonth)
        Rental_Fees = InputData("Enter expected rental fees: ", float, VerifyDigits)
        Payment_Status = InputData("State the payment status (Paid/Unpaid): ", str, VerifyPaymentStatus).capitalize()
        details = [Tenant_ID, Apartment_ID, Rental_Month, str(Rental_Fees), Payment_Status]
        PrintTransactionDetails(details)      # Print the output in order to double check the details
        option = confirm_prompt(
            "Please make sure your details are correct!\n"
            "Do you wish to proceed with current data? [Y] for yes [N] for no\n: ")
        if option:
            SaveData(details, file_path)        # Save data into file
            print(f"Transaction Details has been saved into {file_path}")
        # Continue input or exit
        continue_input = confirm_prompt("Do you wish to continue input? [Y] for yes [N] for no\n: ")


# Function to return specific tenant details from tenant details file with keyword
def SearchTenantDetails(file_path):
    option = InputData(
        "Please specify attribute\n"
        "1. Tenant ID                6. Place of Birth\n"
        "2. Name                     7. City of Birth\n"
        "3. Age                      8. Work History\n"
        "4. Date of Birth            9. Current Employer's Name\n"
        "5. Date of Rental           10. All Current Data\n"
        "SELECTION: ",
        int, VerifyDigits)
    if option <= 9:
        keyword = input("Please input search keyword : ")
        details = SearchData(file_path, option - 1, keyword)    # Return specific list into variable with keyword
        if len(details) > 0:        # Check whether list is empty
            for data in details:
                PrintTenantDetails(data)
        else:
            raise ValueError(f"Failed to acquire Tenant record in {file_path}")

    elif option == 10:      # Return all tenant details in tenant details file
        tenant_list = FiletoList(file_path)
        for data in tenant_list:
            PrintTenantDetails(data)
    else:
        raise ValueError("Invalid Search Operation!")
    pause()


# Function to return specific apartment details from apartment details file with keyword
def SearchApartmentDetails(file_path):
    option = InputData(
        "Please specify search attribute\n"
        "1. Apartment ID          5. Expected Rent\n"
        "2. Occupant's ID         6. Rental History\n"
        "3. Acquisition Date      7. Deposit\n"
        "4. Square Footage        8. All current records\n"
        "SELECTION: ",
        int, VerifyDigits)
    if option <= 7:
        keyword = input("Please input search keyword : ")
        details = SearchData(file_path, option - 1, keyword)    # Return specific list into variable with keyword
        if len(details) > 0:        # Check whether list is empty
            for data in details:
                PrintApartmentDetails(data)
        else:
            raise ValueError(f"Failed to acquire Apartment record in {file_path}")

    elif option == 8:        # Return all apartment details in apartment details file
        apartment_list = FiletoList(file_path)
        for data in apartment_list:
            PrintApartmentDetails(data)

    else:
        raise ValueError("Invalid Search Operation!")
    pause()


# Function to return empty apartment details from apartment details file
def SearchEmptyApartment(file_path):
    emptyunit = 0
    details = SearchData(file_path, 1, "None")      # Return apartment unit with "None" at occupant column
    print("Empty units in the apartment:\n")
    if len(details) > 0:           # Check whether list is empty
        for data in details:
            emptyunit += 1          # Count the empty units
            PrintApartmentDetails(data)
    else:
        print("Unfortunately, there are no empty apartments right now")
    print(f"Empty units in the apartment: {emptyunit}")     # List the total of empty units
    pause()


# Function to return specific transaction details from transaction details file with keyword
def SearchTransactionDetails(file_path):
    option = InputData("Please specify attribute\n"
                       "1. Tenant ID                4. Rental Fees\n"
                       "2. Apartment ID             5. Payment Status\n"
                       "3. Rental Month             6. All current records\n"
                       "SELECTION: ", int, VerifyDigits)
    if option <= 5:
        keyword = input("Please input search keyword : ")
        details = SearchData(file_path, option - 1, keyword)    # Return specific list into variable with keyword
        if len(details) > 0:            # Check whether list is empty
            for data in details:
                PrintTransactionDetails(data)
        else:
            raise ValueError(f"Failed to acquire Transaction record in {file_path}")

    elif option == 6:       # Return all transaction details in transaction details file
        transaction_list = FiletoList(file_path)
        for data in transaction_list:
            PrintTransactionDetails(data)

    else:
        raise ValueError("Invalid Search Operation!")
    pause()


# Function to return total unpaid rental bills from transaction details file
def ViewUnpaidDebts(file_path, user_ID):
    unpaid = 0
    total_rental_debt = 0
    unpaid_months = []

    details = SearchData(file_path, 0, user_ID)
    for data in details:
        PrintTransactionDetails(data)

        if data[4] == "Unpaid":
            unpaid += 1     # Count total unpaid rental bills
            unpaid_months.append(data[2])
            total_rental_debt += float(data[3])       # Subtotal amount of unpaid rental bills

    unpaid_months = ", ".join(unpaid_months)
    print(f"Unpaid rent: {unpaid}")
    print(f"Months where rent is overdue: {unpaid_months}")
    print(f"Total unpaid rental fees: RM{total_rental_debt}")
    pause()


# Select all log files from a directory for viewing
def ViewLogFiles(directory):
    try:
        file_list = getFilesfromDirectory(directory, ".txt", ".log")  # There is only 2 file formats for log files
        continue_viewing = True
        if len(file_list) > 0:
            while continue_viewing:
                # Printing the files with format for easier viewing
                for index, file in enumerate(file_list):
                    file = file.rstrip(".txt").rstrip(".log")
                    print(f"{index + 1}. {file}")

                selection = InputData("Please select log file to view (Enter number)\n", int, VerifyDigits)
                if (0 < selection <= len(file_list)):  # Ensure selection is within file count
                    file_path = f"{directory}\{file_list[selection-1]}"  # Formatting the file_path to acquire files
                    with open(file_path, "r") as rfile:
                        print(rfile.read())
                    continue_viewing = confirm_prompt(
                        "Do you want to continue viewing? [Yes] to return [No] to abort\n:")  # Loop back if users say yes and no to break
                else:
                    print("Invalid selection, please try again")
        else:
            # Catching exceptions for missing files and directories
            print("No log files were found within the directory")
            raise ValueError("Log files non-existent in directory, view operation terminated")
    except FileNotFoundError as e:
        raise FileNotFoundError(f"Directory \"{directory}\"is not existent!") from e


# Function to modify the tenant details in tenant details file
def ModifyTenantRecord(file_path):
    flag = False
    Alist = FiletoList(file_path)
    key = input("Please enter Tenant ID for modications : ")
    for data in Alist:
        if data[0] == key:
            PrintTenantDetails(data)    # Display the specific tenant details
            flag = True
            break

    if flag:
        while True:
            # Modify specific details of selected tenant by selecting number from the data displayed above
            option = InputData("Which data you would like to modify? (Select number)\n= ", int, VerifyDigits)
            if option == 1:
                print("ID cannot be modified")
            elif option == 2:
                newdata = InputData("Enter new Name: ", str, VerifyName)
                break
            elif option == 3:
                print("Age cannot be modified, please modify Date of Birth to change the Age")
            elif option == 4:
                date_of_rental = [data for record in SearchData(file_path, 0, key) for data in record][4]
                newdata = getDateoutsideRange("Enter new Date of Birth: ", date_of_rental, -18)
                break
            elif option == 5:
                date_of_birth = [data for record in SearchData(file_path, 0, key) for data in record][3]
                newdata = getDateoutsideRange("Enter new Date of Apartment Rental: ", date_of_birth, 18)
                break
            elif option == 6:
                newdata = InputData("Enter new Place of Birth: ", str, VerifyName)
                break
            elif option == 7:
                newdata = InputData("Enter new City of Birth: ", str, VerifyName)
                break
            elif option == 8:
                newdata = InputData("Enter new Work History: ", str, VerifyName)
                break
            elif option == 9:
                newdata = InputData("Enter new Employer's Name: ", str, VerifyName)
                break
            else:
                print("Invalid option! Please try again")
        ModifyRecord(file_path, option - 1, key, str(newdata))   # Confirm and overwrite new details into file
    else:
        raise ValueError("Invalid search results, Tenant modify program aborted!")


# Function to modify the apartment details in apartment details file
def ModifyApartmentRecord(file_path, tenantfile):
    flag = False
    Alist = FiletoList(file_path)
    key = input("Please enter Apartment ID for modications : ")
    for data in Alist:
        if data[0] == key:
            PrintApartmentDetails(data)     # Display the specific apartment details
            flag = True
            break

    if flag:
        while True:
            # Modify specific details of selected apartment by selecting number from the data displayed above
            option = InputData("Which data you would like to modify? (Select number)\n= ", int, VerifyDigits)
            if option == 1:
                print("Apartment ID cannot be modified")
            elif option == 2:
                newdata = GetID("Enter new occupant's ID : ", tenantfile, 0)
                break
            elif option == 3:
                newdata = InputData("Enter new Date of Acquisition: ", str, VerifyDate)
                break
            elif option == 4:
                newdata = InputData("Enter new Square Footage: ", float, VerifyDigits)
                break
            elif option == 5:
                newdata = InputData("Enter new Expected Rent: ", float, VerifyDigits)
                break
            elif option == 6:
                newdata = InputData("Enter new Rental History: ", int, VerifyDigits)
                break
            elif option == 7:
                newdata = InputData("Enter new Deposit: ", float, VerifyDigits)
                break
            else:
                print("Invalid option! Please try again")
        ModifyRecord(file_path, option - 1, key, str(newdata))    # Confirm and overwrite new details into file
    else:
        raise ValueError("Invalid search results, Apartment modify program aborted!")


# Function to modify payment record in transaction details file
def ModifyTransactionRecord(file_path):
    flag = False
    Tlist = FiletoList(file_path)
    key1 = input("Please enter the Tenant ID : ")
    key2 = input("Please enter the Apartment ID : ")
    key3 = InputData("Please enter rental month : ", str, VerifyMonth)
    for data in Tlist:
        if data[0] == key1 and data[1] == key2 and data[2] == key3:     # Specific tenant ID, apartment ID and month
            PrintTransactionDetails(data)
            flag = True
            break

    if flag:
        # Change the payment status to Paid or Unpaid
        Payment_Status = InputData("State the payment status (Paid/Unpaid): ", str, VerifyPaymentStatus).capitalize()
        for index, data in enumerate(
                Tlist):  # Enumerate to get the position of record in the file (index) and the data at the position
            if data[0] == key1 and data[1] == key2 and data[2] == key3:
                data[4] = Payment_Status  # Replace old data with new data at its specific position in a line
                Tlist[index] = data  # Replace the whole line of record with new record with modified data
                break
        OverwriteFile(file_path, Tlist)  # Rewrite the old data with new data

    else:
        raise ValueError("Invalid search results, Transaction modify program aborted!")


# Function to remove admin
def DeleteAdmin(file_path):
    adminname = input("Please enter Admin's name for deletion: ")
    adminexists = CheckDuplicateinFile(file_path, adminname)    # Check if admin exists
    if adminexists:
        DeleteData(file_path, adminname, 2) # Only delete if admin's name exactly matches record
    else:
        raise ValueError("Admin does not exist!")


def UpdateApartmentDetails(file_path, keyword):
    item_list = FiletoList(file_path)
    
    for data in item_list:
        if data[1] == keyword:
            data[1] = "None"
            # Remove last few string characters from the data to perform addition with integers
            data[5] = int(data[5]) + 1
            break
    OverwriteFile(file_path, item_list)


# Function to remove tenant
def DeleteTenantData(file_path, userfile, apartmentfile, pasttenantfile):
    keyword = input("Please enter Tenant ID to data deletion: ")
    details = SearchData(file_path, 0, keyword)     # Return the specific list with keyword to variable
    if len(details) > 0:        # Check whether list is empty
        for data in details:
            PrintTenantDetails(data)    # Display the specific list

        while True:
            option = InputData("Please validate the data above!\n"
                               "Press:\n"
                               " [1] to confirm deletion and move record to past tenant's file.\n"
                               " [2] to confirm deletion without updating other files.\n"
                               " [3] to abort deletion and exit.\n"
                               "SELECT OPTION: ", int, VerifyDigits)
	    # Get tenant name
            tenantname = [data for record in SearchData(file_path, 0, keyword) for data in record][1]
	
            if option == 1:     # Delete from tenant details file and move to past tenant's file
                # Modify the occupant to "None" and rental history +1
                UpdateApartmentDetails(apartmentfile, keyword)
                # Move tenant details from tenant details file to past tenant file
                MoveRecordtoFile(file_path, keyword, pasttenantfile)
		# Delete tenant username and password
                DeleteData(userfile, tenantname, 2)
                break
            elif option == 2:
                # Modify the occupant to "None" and rental history +1
                UpdateApartmentDetails(apartmentfile, keyword)
                # Delete tenant details
                DeleteData(file_path, keyword, 0)
                # Delete tenant username and password
                DeleteData(userfile, tenantname, 2)
                break
            elif option == 3:
                break
            else:
                print("Invalid option! Please try again")
    else:
        raise ValueError("Failed to acquire Tenant record!")


# Function to remove apartment
def DeleteApartmentData(file_path):
    keyword = input("Please enter Apartment ID for data deletion: ")
    details = SearchData(file_path, 0, keyword)     # Return the specific list with keyword to variable
    if len(details) > 0:        # Check whether list is empty
        for data in details:
            PrintApartmentDetails(data)     # Display the specific list

        while True:
            option = InputData("Please confirm with the data above!\n"
                               "Press:\n"
                               " [1] to confirm deletion of selected data.\n"
                               " [2] to keep the selected data and exit.\n"
                               "SELECT OPTION: ", int, VerifyDigits)

            if option == 1:
                DeleteData(file_path, keyword, 0)  # Delete apartment details in file
                break
            elif option == 2:       # Keep the data and back to main menu
                break
            else:
                print("Invalid option! Please try again!")
    else:
        raise ValueError("Failed to acquire Apartment record")


# Function to remove transaction
def DeleteTransactionData(file_path):
    keyword = input("Please enter Tenant ID for data deletion: ")
    keyword2 = input("Please enter Apartment ID linked to Tenant ID: ")
    keyword3 = InputData("Please enter the specific month's transaction record for deletion: ", str, VerifyMonth)
    transactionfile = FiletoList(file_path)
    try:
        Tenant = [data for record in SearchData(file_path, 0, keyword) for data in record][0]
        Apartment = [data for record in SearchData(file_path, 1, keyword2) for data in record][1]
        Month = [data for record in SearchData(file_path, 2, keyword3) for data in record][2]
        details = [record for record in transactionfile if Tenant in record and Apartment in record and Month in record]
        if len(details) > 0:        # Check whether list is empty
            for data in details:
                PrintTransactionDetails(data)       # Display the specific list

                option = InputData("Please confirm with the data above!\n"
                                "Press:\n"
                                " [1] to confirm deletion of selected data.\n"
                                " [2] to keep the selected data and exit.\n"
                                "SELECT OPTION: ", int, VerifyDigits)
                if option == 1:
                    for data in details:
                        transactionfile.remove(data)
                    OverwriteFile(file_path, transactionfile)
                    break
                elif option == 2:
                    break
                else:
                    print("Invalid option! Please try again!")
        else:
            raise ValueError("Failed to acquire Transaction record")
    except IndexError as e:
        raise ValueError("Failed to acquire Transaction record") from e


# Function to remove past tenant data
def DeletePastTenantData(file_path):
    keyword = input("Please enter past tenant ID for data deletion: ")
    details = SearchData(file_path, 0, keyword)     # Get the specific list into variable
    if len(details) > 0:        # Check whether list is empty
        for data in details:
            PrintTenantDetails(data)    # Display the specific list

        while True:
            option = InputData("Please confirm with the data above!\n"
                               "Press:\n"
                               " [1] to confirm deletion of selected data.\n"
                               " [2] to keep the selected data and exit.\n"
                               "SELECT OPTION: ", int, VerifyDigits)

            if option == 1:
                DeleteData(file_path, keyword, 0)  # Delete past tenant details in file
                break
            elif option == 2:
                break
            else:
                print("Invalid option! Please try again")
    else:
        raise ValueError("Failed to acquire Tenant record!")


# Function to verify login status
def VerifyLoginCredentials(new_name, new_password, file_path, attempts_allowed):
    retry = 0
    while True:
        usernameexist = CheckDuplicateinFile(file_path, new_name)   # Check username in file
        passwordexist = CheckDuplicateinFile(file_path, new_password)   # Check password in file
        if usernameexist == False and passwordexist == False:
            # Double confirm new username and password by compare first insert and second insert
            confirm_name = input("Please confirm your username\n")
            confirm_password = input("Please confirm your password\n")
            if confirm_name == new_name and confirm_password == new_password:
                return True
            else:
                retry += 1
                if retry < attempts_allowed:    # Check whether attempts reach limits
                    print("Wrong username or password!", (attempts_allowed - retry), "retries remaining.")
                else:
                    print("Exceeded maximum number of tries!")
                    return False
        else:
            print("Username or password already exists, please try a different username or password")
            return False


# Function to change username and password
def ModifyLoginCredentials(file_path):
    continue_operation = True
    while continue_operation:
        username = input("Please enter old username: ")
        password = input("Please enter old password: ")
        # Verify username and password with the data in file
        userconfirmation = ValidateUser(username, password, file_path)
        if userconfirmation:
            new_username = InputData("Please enter new username: ", str, VerifyName)
            new_password = InputData("Please enter new password: ", str, PasswordChecker)
            # Reinsert new username and password to avoid mistakes
            flag = VerifyLoginCredentials(new_username, new_password, file_path, 3)
            if flag:
                credentials = FiletoList(file_path)
                for index, data in enumerate(credentials):
                    if username == data[0] and password == data[1]:     # Make sure old username and password is correct
                        data[0], data[1] = new_username, new_password   # Replace with new username and password
                        credentials[index] = data
                OverwriteFile(file_path, credentials)   # Overwrite new list into file
                break
        else:
            print("Validation of User Failed!")
            continue_operation = confirm_prompt("Do you wish to continue? [Y] for yes [N] for no")
    else:
        raise ValueError("Modifications of Login Credentials aborted due to failed user validation")


# Main Menu design for super admin
def Main_Menu_SA(logfile):
    mainmenutitle = """::::    ::::      :::     ::::::::::: ::::    :::  ::::    ::::  :::::::::: ::::    ::: :::    ::: 
+:+:+: :+:+:+   :+: :+:       :+:     :+:+:   :+:  +:+:+: :+:+:+ :+:        :+:+:   :+: :+:    :+: 
+:+ +:+:+ +:+  +:+   +:+      +:+     :+:+:+  +:+  +:+ +:+:+ +:+ +:+        :+:+:+  +:+ +:+    +:+ 
+#+  +:+  +#+ +#++:++#++:     +#+     +#+ +:+ +#+  +#+  +:+  +#+ +#++:++#   +#+ +:+ +#+ +#+    +:+ 
+#+       +#+ +#+     +#+     +#+     +#+  +#+#+#  +#+       +#+ +#+        +#+  +#+#+# +#+    +#+ 
#+#       #+# #+#     #+#     #+#     #+#   #+#+#  #+#       #+# #+#        #+#   #+#+# #+#    #+# 
###       ### ###     ### ########### ###    ####  ###       ### ########## ###    ####  ########  \n"""
    mainmenusystem = """° 　. ● . ★ ° . *　　　°　.　°☆ 　. * ● ¸ . ★ °　★ 　° :●. 　 * ★　 .　 *
★ ° . *　°　★ 　. David, Welcome to Main Menu!• ○ ★ ° :● . ★ ° .  *　°
　.　°☆ 　. * ● ¸ . 　　　★ 　° :.★ ° . *　　　°　.　°☆ 　. * ● ¸ 　°☆ 　. 
        1. Insert Data          5. Delete Data
        2. Modify Data          6. Change Login Credentials
        3. View Log History     7. Exit
        4. View Data
        SELECT OPTION: """
    insertdatasystem = """\n° 　. ● . ★ ° . *　　　°　.　°☆ 　. * ● ¸ . ★ °　★ 　° :● ★　 *  .　
★ ° . *　 ° .　• .　Insert Data System!:. 　 *  • ○ ° ★* • ○  ★ 
.　°☆ 　. * ● :.★ ° . *　　　°　.　°☆ 　. *.　°☆ 　. * ● *　　　°　.
        1. New Tenant Data          4. New Admin Data
        2. New Apartment Data       5. Exit
        3. New Transaction Data
        SELECT OPTION: """
    modifydatasystem = """\n° 　. ● . ★ ° . *　　　°　.　°☆ 　. * ● ¸ . ★ °　★ 　° :● ★　 *  .　
★ ° . *　 ° .　• .　Modify Data System!:. 　 *  • ○ ° ★* • ○  ★ 
.　°☆ 　. * ● :.★ ° . *　　　°　.　°☆ 　. *.　°☆ 　. * ● *　　　°　.
        1. Modify Tenant Data       3. Modify Transaction Data
        2. Modify Apartment Data    4. Exit
        SELECT OPTION: """
    viewdatasystem = """\n° 　. ● . ★ ° . *　　　°　.　°☆ 　. * ● ¸ . ★ °　★ 　° :● ★　 *  .　
★ ° . *　 ° .　• .　View Data System!:. 　 *  •  ○ °  ★* • ○  ★ 
.　°☆ 　. * ● :.★ ° . *　　　°　.　°☆ 　. *.　°☆ 　. * ● *　　　°　.
        1. View Tenant Data         4. View Past Tenant Data
        2. View Apartment Data      5. Exit
        3. View Transaction Data   
        SELECT OPTION: """
    deletedatasystem = """\n° 　. ● . ★ ° . *　　　°　.　°☆ 　. * ● ¸ . ★ °　★ 　° :● ★　 *  .　
★ ° . *　 ° .　• .　Delete Data System!:. 　 *  • ○ ° ★* • ○  ★ 
.　°☆ 　. * ● :.★ ° . *　　　°　.　°☆ 　. *.　°☆ 　. * ● *　　　°　.
        1. Delete Tenant Data       4. Delete Past Tenant Data
        2. Delete Apartment Data    5. Delete Admin Record
        3. Delete Transaction Data  6. Exit
        SELECT OPTION: """
    log_directory = "Logs"
    apartmentfile = "Apartment Details.txt"
    tenantfile = "Tenant Details.txt"
    transactionfile = "Transaction Details.txt"
    pasttenantfile = "Past Tenant Details.txt"
    userfile = "userfile.txt"
    continue_msg = "Do you wish to continue operation? [Y] for Yes [N] for No\n:"
    logout_msg = "Are you sure you want to logout? [Y] for Yes [N] for No\n:"
    invalid_msg = "Invalid option! Please try again"
    exit_program = False
    while exit_program == False:
        try:
            print(mainmenutitle)
            continue_operation = True
            selection = InputData(mainmenusystem, int, VerifyDigits)
            if selection == 1:  # Insert Section
                while continue_operation:
                    option = InputData(insertdatasystem, int, VerifyDigits)
                    if option == 1:
                        AddTenantDetails(tenantfile, userfile)
                        log(logfile, "info", f"New records added to {tenantfile}")

                    elif option == 2:
                        AddApartmentDetails(apartmentfile, tenantfile)
                        log(logfile, "info", f"New records added to {apartmentfile}")

                    elif option == 3:
                        AddTransactionDetails(transactionfile, tenantfile, apartmentfile)
                        log(logfile, "info", f"New records added to {transactionfile}")

                    elif option == 4:
                        adminname = InputData("Please enter Admin's Name: ", str, VerifyName)
                        GenerateCredentials(userfile, adminname, "a")
                        log(logfile, "info", f"Added new Admin {adminname}'s Login Credentials to {userfile}")

                    elif option == 5:
                        break

                    else:
                        print(invalid_msg)

                    continue_operation = confirm_prompt(continue_msg)

            elif selection == 2:  # Modify Section
                while continue_operation:
                    option = InputData(modifydatasystem, int, VerifyDigits)
                    if option == 1:
                        ModifyTenantRecord(tenantfile)
                        log(logfile, "info", f"Records modified in {tenantfile}")

                    elif option == 2:
                        ModifyApartmentRecord(apartmentfile, tenantfile)
                        log(logfile, "info", f"Records modified in {apartmentfile}")

                    elif option == 3:
                        ModifyTransactionRecord(transactionfile)
                        log(logfile, "info", f"Records modified in {transactionfile}")

                    elif option == 4:
                        break

                    else:
                        print(invalid_msg)

                    continue_operation = confirm_prompt(continue_msg)

            elif selection == 3:  # view log history
                ViewLogFiles(log_directory)
                log(logfile, "info", f"Returned log files from {log_directory} for viewing")

            elif selection == 4:  # View Section
                while continue_operation:
                    option = InputData(viewdatasystem, int, VerifyDigits)
                    if option == 1:
                        SearchTenantDetails(tenantfile)
                        log(logfile, "info", f"Returned records from {tenantfile} for viewing")

                    elif option == 2:
                        SearchApartmentDetails(apartmentfile)
                        log(logfile, "info", f"Returned records from {apartmentfile} for viewing")

                    elif option == 3:
                        SearchTransactionDetails(transactionfile)
                        log(logfile, "info", f"Returned records from {transactionfile} for viewing")

                    elif option == 4:
                        SearchTenantDetails(pasttenantfile)
                        log(logfile, "info", f"Returned records from {pasttenantfile} for viewing")

                    elif option == 5:
                        break

                    else:
                        print(invalid_msg)

                    continue_operation = confirm_prompt(continue_msg)

            elif selection == 5:  # Delete Section
                while continue_operation:
                    option = InputData(deletedatasystem, int, VerifyDigits)
                    if option == 1:
                        DeleteTenantData(tenantfile, userfile, apartmentfile, pasttenantfile)
                        log(logfile, "info", f"Deleted records in {tenantfile}")

                    elif option == 2:
                        DeleteApartmentData(apartmentfile)
                        log(logfile, "info", f"Deleted records in {apartmentfile}")

                    elif option == 3:
                        DeleteTransactionData(transactionfile)
                        log(logfile, "info", f"Deleted records in {transactionfile}")

                    elif option == 4:
                        DeletePastTenantData(pasttenantfile)
                        log(logfile, "info", f"Deleted records in {pasttenantfile}")

                    elif option == 5:
                        DeleteAdmin(userfile)
                        log(logfile, "info", f"Deleted admin in {userfile}")

                    elif option == 6:
                        break

                    else:
                        print(invalid_msg)

                    continue_operation = confirm_prompt(continue_msg)

            elif selection == 6:  # Change login Details
                ModifyLoginCredentials(userfile)
                log(logfile, "info", f"Super Admin David successfully modified personal login credentials in {userfile}")

            elif selection == 7:  # Exit program
                exit_program = confirm_prompt(logout_msg)

            else:
                print("Invalid option! Please try again")
                log(logfile, "error", "Invalid Menu Option")
        except Exception as e:
            log(logfile, "warn", str(e))
            print(f"{e} Returning to Main Menu")


# Main Menu design for admin
def Main_Menu_A(username, logfile):
    mainmenutitle = """::::    ::::      :::     ::::::::::: ::::    :::  ::::    ::::  :::::::::: ::::    ::: :::    ::: 
+:+:+: :+:+:+   :+: :+:       :+:     :+:+:   :+:  +:+:+: :+:+:+ :+:        :+:+:   :+: :+:    :+: 
+:+ +:+:+ +:+  +:+   +:+      +:+     :+:+:+  +:+  +:+ +:+:+ +:+ +:+        :+:+:+  +:+ +:+    +:+ 
+#+  +:+  +#+ +#++:++#++:     +#+     +#+ +:+ +#+  +#+  +:+  +#+ +#++:++#   +#+ +:+ +#+ +#+    +:+ 
+#+       +#+ +#+     +#+     +#+     +#+  +#+#+#  +#+       +#+ +#+        +#+  +#+#+# +#+    +#+ 
#+#       #+# #+#     #+#     #+#     #+#   #+#+#  #+#       #+# #+#        #+#   #+#+# #+#    #+# 
###       ### ###     ### ########### ###    ####  ###       ### ########## ###    ####  ########  \n"""
    mainmenusystem = f"""° 　. ● . ★ ° . *　　　°　.　°☆ 　. * ● ¸ . ★ °　★ 　° :●. 　 * ★　 .　 * 　.　
★ ° . *　°　★ 　. Admin {username}, Welcome to Main Menu!• ○ ★ ° :● . ★ ° .  *　°
　.　°☆ 　. * ● ¸ . 　　　★ 　° :.★ ° . *　　　°　.　°☆ 　. * ● ¸ °　.　°☆ . 
        1. Insert Data          4. Delete Data
        2. Modify Data          5. Change Login Credentials
        3. View Data            6. Exit
        SELECT OPTION: """
    insertdatasystem = """° 　. ● . ★ ° . *　　　°　.　°☆ 　. * ● ¸ . ★ °　★ 　° :● ★　 *  .　
	★ ° . *　 ° .　• .　Insert Data System!:. 　 *  • ○ ° ★* • ○  ★
	.　°☆ 　. * ● :.★ ° . *　　　°　.　°☆ 　. *.　°☆ 　. * ● *　　　°　.
		1. New Tenant Data          3. New Transaction Data
		2. New Apartment Data       4. Exit
		SELECT OPTION: """
    modifydatasystem = """\n° 　. ● . ★ ° . *　　　°　.　°☆ 　. * ● ¸ . ★ °　★ 　° :● ★　 *  .　
★ ° . *　 ° .　• .　Modify Data System!:. 　 *  • ○ ° ★* • ○  ★ 
.　°☆ 　. * ● :.★ ° . *　　　°　.　°☆ 　. *.　°☆ 　. * ● *　　　°　.
        1. Modify Tenant Data       3. Modify Transaction Data
        2. Modify Apartment Data    4. Exit
        SELECT OPTION: """
    viewdatasystem = """\n° 　. ● . ★ ° . *　　　°　.　°☆ 　. * ● ¸ . ★ °　★ 　° :● ★　 *  .　
★ ° . *　 ° .　• .　View Data System!:. 　 *  •  ○ °  ★* • ○  ★ 
.　°☆ 　. * ● :.★ ° . *　　　°　.　°☆ 　. *.　°☆ 　. * ● *　　　°　.
        1. View Tenant Data         4. View Past Tenant Data
        2. View Apartment Data      5. Exit
        3. View Transaction Data    
        SELECT OPTION: """
    deletedatasystem = """\n° 　. ● . ★ ° . *　　　°　.　°☆ 　. * ● ¸ . ★ °　★ 　° :● ★　 *  .　
★ ° . *　 ° .　• .　Delete Data System!:. 　 *  • ○ ° ★* • ○  ★ 
.　°☆ 　. * ● :.★ ° . *　　　°　.　°☆ 　. *.　°☆ 　. * ● *　　　°　.
        1. Delete Tenant Data       4. Delete Past Tenant Data
	2. Delete Apartment Data    5. Exit
	3. Delete Transaction Data
        SELECT OPTION: """
    userfile = "userfile.txt"
    apartmentfile = "Apartment Details.txt"
    tenantfile = "Tenant Details.txt"
    transactionfile = "Transaction Details.txt"
    pasttenantfile = "Past Tenant Details.txt"
    continue_msg = "Do you wish to continue operation? [Y] for Yes [N] for No\n:"
    invalid_msg = "Invalid option! Please try again"
    logout_msg = "Are you sure you want to logout? [Y] for Yes [N] for No\n:"
    exit_program = False
    while exit_program == False:
        try:
            print(mainmenutitle)
            continue_operation = True
            selection = InputData(mainmenusystem, int, VerifyDigits)
            if selection == 1:  # Insert Section
                while continue_operation:
                    option = InputData(insertdatasystem, int, VerifyDigits)
                    if option == 1:
                        AddTenantDetails(tenantfile, userfile)
                        log(logfile, "info", f"New records added to {tenantfile}")

                    elif option == 2:
                        AddApartmentDetails(apartmentfile, tenantfile)
                        log(logfile, "info", f"New records added to {apartmentfile}")

                    elif option == 3:
                        AddTransactionDetails(transactionfile, tenantfile, apartmentfile)
                        log(logfile, "info", f"New records added to {transactionfile}")

                    elif option == 4:
                        break

                    else:
                        print(invalid_msg)

                    continue_operation = confirm_prompt(continue_msg)

            elif selection == 2:  # Modify Section
                while continue_operation:
                    option = InputData(modifydatasystem, int, VerifyDigits)
                    if option == 1:
                        ModifyTenantRecord(tenantfile)
                        log(logfile, "info", f"Records modified in {tenantfile}")

                    elif option == 2:
                        ModifyApartmentRecord(apartmentfile, tenantfile)
                        log(logfile, "info", f"Records modified in {apartmentfile}")

                    elif option == 3:
                        ModifyTransactionRecord(transactionfile)
                        log(logfile, "info", f"Records modified in {transactionfile}")

                    elif option == 4:
                        break

                    else:
                        print(invalid_msg)

                    continue_operation = confirm_prompt(continue_msg)

            elif selection == 3:  # View Section
                while continue_operation:
                    option = InputData(viewdatasystem, int, VerifyDigits)
                    if option == 1:
                        SearchTenantDetails(tenantfile)
                        log(logfile, "info", f"Returned records from {tenantfile} for viewing")

                    elif option == 2:
                        SearchApartmentDetails(apartmentfile)
                        log(logfile, "info", f"Returned records from {apartmentfile} for viewing")

                    elif option == 3:
                        SearchTransactionDetails(transactionfile)
                        log(logfile, "info", f"Returned records from {transactionfile} for viewing")

                    elif option == 4:
                        SearchTenantDetails(pasttenantfile)
                        log(logfile, "info", f"Returned records from {pasttenantfile} for viewing")

                    elif option == 5:
                        break

                    else:
                        print(invalid_msg)

                    continue_operation = confirm_prompt(continue_msg)

            elif selection == 4:  # Delete Section
                while continue_operation:
                    option = InputData(deletedatasystem, int, VerifyDigits)
                    if option == 1:
                        DeleteTenantData(tenantfile, userfile, apartmentfile, pasttenantfile)
                        log(logfile, "info", f"Deleted records in {tenantfile}")

                    elif option == 2:
                        DeleteApartmentData(apartmentfile)
                        log(logfile, "info", f"Deleted records in {apartmentfile}")

                    elif option == 3:
                        DeleteTransactionData(transactionfile)
                        log(logfile, "info", f"Deleted records in {transactionfile}")

                    elif option == 4:
                        DeletePastTenantData(pasttenantfile)
                        log(logfile, "info", f"Deleted records in {pasttenantfile}")

                    elif option == 5:
                        break

                    else:
                        print(invalid_msg)

                    continue_operation = confirm_prompt(continue_msg)

            elif selection == 5:  # Change login Details
                ModifyLoginCredentials(userfile)
                log(logfile, "info", f"Admin {username} successfully modified personal login credentials")

            elif selection == 6:  # Exit program
                exit_program = confirm_prompt(logout_msg)

            else:
                print("Invalid option! Please try again")
                log(logfile, "error", "Invalid Menu Option")

        except Exception as e:
            log(logfile, "warn", str(e))
            print(f"{e} Returning to Main Menu")


# Main Menu design for tenant
def Main_Menu_T(username, logfile):
    mainmenutitle = """::::    ::::      :::     ::::::::::: ::::    :::  ::::    ::::  :::::::::: ::::    ::: :::    ::: 
    +:+:+: :+:+:+   :+: :+:       :+:     :+:+:   :+:  +:+:+: :+:+:+ :+:        :+:+:   :+: :+:    :+: 
    +:+ +:+:+ +:+  +:+   +:+      +:+     :+:+:+  +:+  +:+ +:+:+ +:+ +:+        :+:+:+  +:+ +:+    +:+ 
    +#+  +:+  +#+ +#++:++#++:     +#+     +#+ +:+ +#+  +#+  +:+  +#+ +#++:++#   +#+ +:+ +#+ +#+    +:+ 
    +#+       +#+ +#+     +#+     +#+     +#+  +#+#+#  +#+       +#+ +#+        +#+  +#+#+# +#+    +#+ 
    #+#       #+# #+#     #+#     #+#     #+#   #+#+#  #+#       #+# #+#        #+#   #+#+# #+#    #+# 
    ###       ### ###     ### ########### ###    ####  ###       ### ########## ###    ####  ########  \n"""
    mainmenusystem = f"""° 　. ● . ★ ° . *　　　°　.　°☆ 　. * ● ¸ . ★ °　★ 　° :●. 　 * ★　 .　 * 　.　
    ★ ° . *　°　★ 　. Tenant {username}, Welcome to Main Menu!• ○ ★ ° :● . ★ ° .  *　°
    　.　°☆ 　. * ● ¸ . 　　　★ 　° :.★ ° . *　　　°　.　°☆ 　. * ● ¸ °　.　°☆ . 
            1. View Empty Unit           4. Change Login Credentials
            2. View Personal Details     5. Exit
            3. View Transaction History  
            SELECT OPTION: """
    userfile = "userfile.txt"
    apartmentfile = "Apartment Details.txt"
    tenantfile = "Tenant Details.txt"
    transactionfile = "Transaction Details.txt"
    userid = [data for record in SearchData(tenantfile, 1, username) for data in record][0]
    invalid_msg = "Invalid option! Please try again"
    logout_msg = "Are you sure you want to logout? [Y] for Yes [N] for No\n:"
    exit_program = False
    while exit_program == False:
        try:
            print(mainmenutitle)
            selection = InputData(mainmenusystem, int, VerifyDigits)
            if selection == 1:      # View empty apartment unit
                SearchEmptyApartment(apartmentfile)
                log(logfile, "info", f"Successfully returned empty units from {apartmentfile} for viewing")

            elif selection == 2:    # View personal details
                print(" ★ ° .  *　° Tenant Personal Details ● . ★ . *　°　.")
                details = SearchData(tenantfile, 1, username)
                for data in details:
                    PrintTenantDetails(data)
                pause()
                print("Please inform admin for any modifications regarding personal details!")
                log(logfile, "info", f"Returned user personal details from {tenantfile} for viewing")

            elif selection == 3:    # View personal transaction details
                print(" ★ ° .  *　° Transaction History ● . ★ . *　°　.")
                ViewUnpaidDebts(transactionfile, userid)
                log(logfile, "info", f"Returned transaction history of user from {transactionfile} for viewing")

            elif selection == 4:    # Change login credentials
                ModifyLoginCredentials(userfile)
                log(logfile, "info", f"User ID {userid} successfully modified personal login credentials")

            elif selection == 5:    # Exit
                exit_program = confirm_prompt(logout_msg)

            else:
                print(invalid_msg)
                log(logfile, "error", f"Failed returning system option with input \"{selection}\"")

        except Exception as e:
            log(logfile, "warn", str(e))
            print(f"{e} Returning to Main Menu")


def UMS():
    userfile = "userfile.txt"
    log_file_name = datetime.datetime.now().strftime('UMS - %Y.%m.%d-%H.%M.%S.txt')
    log_directory = createdirectory("Logs")
    logfile = createlogfile(log_directory, log_file_name)
    start_time = datetime.datetime.now()
    try:
        print("Welcome to User Management System!")
        loginstatus, username, usertype = Login(userfile, 3)
        if loginstatus == True:
            if usertype == "sa":    # Super admin main menu
                loading(1.5)
                log(logfile, "info", f"Super Admin, {username} Login Successful")
                Main_Menu_SA(logfile)
            elif usertype == "a":   # Admin main menu
                loading(1.5)
                log(logfile, "info", f"Admin, {username} Login Successful")
                Main_Menu_A(username, logfile)
            elif usertype == "t":   # Tenant main menu
                loading(1.5)
                log(logfile, "info", f"Tenant, {username} Login Successful")
                Main_Menu_T(username, logfile)

            log(logfile, "info", f"System exited, time elapsed: {timer_end(start_time)}")
            loading(.3)
        else:
            print("Invalid Login Attempt! Exiting System....")
            loading(0.5)
            log(logfile, "critical", "Failed Unknown Login Attempt!")
    except KeyboardInterrupt:
        print("Emergency Quit Command Detected! Exiting System....")
        log(logfile, "error", f"Execution of program interrupted abruptly, time elapsed: {timer_end(start_time)}")


UMS()
