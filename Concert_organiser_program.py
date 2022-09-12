#Author :Conor Pasley
#Description: Blackwater Annual Concert Assignment

#constants
MINUTES_IN_HOURS = 60
LONG_PERFORMANCE = 15
MENU_OPTIONS = (1 , 2 , 3 )


#setting initialise to 0
initialise = 0 
#initial user input
while initialise not in (MENU_OPTIONS):
    try:
        print()
        print("Black Water Annual Music Concert")
        print("-"*30)
        initialise = int(input("1. Adding Performers\n2. Generate Concert Details\n3. Quit\n>>> "))

        if initialise < 1 or initialise > 3:
            print()
            print("Please enter 1, 2 or 3")
            
    except ValueError:
        print()
        print("You have entered an invalid value, please try again")
        
#infinite loop until 3 is pressed
while initialise !=3:
    #Checking if adding performers was selected (option 1)
    if initialise == 1: 

        #all of these variables are reset when option 1 is selected.
        #empty string variables
        highest_performance_details = ""
        formatted_performers = "" 

        #variables for highest duration and total duration
        highest_duration = 0
        total_duration = 0

        #counter variables
        singer_count = 0
        Musician_count = 0 
        dancer_count = 0

        print()
        print(f"({initialise}) Adding Performers")
        print("-" * 30)
        #Asking for number of performers 
        performers_amount = int(input("How many performances would you like to add: "))

        if performers_amount > 0:
            connection = open("performance.txt", "a")

            #looping through range of performers and asking user for information about each performer
            for i in range(performers_amount):
                print()
                print(f"Booking {i+1}/{performers_amount}: ")

                name = str(input("Enter your name: "))
                surname = str(input("Enter your surname: "))
                performance = 0
                while performance not in (MENU_OPTIONS):
                    try:
                        performance = int(input("Type of Performance\n 1. Musician \n 2. Singer \n 3. Dance\n>>> "))
                        
                        if performance < 1 or performance > 3:
                            print()
                            print("Please enter 1, 2 or 3")
                        
                    except ValueError:
                        print()
                        print("You have entered an invalid value, please try again")

                duration = int(input("Time slot required(mins)?: "))
                total_duration += duration

                #checking which type of performance was seleceted and assigning string
                if performance == 1:
                    performance_type = "Musician"
                    Musician_count +=1

                elif performance == 2:
                    performance_type = "Singer" 
                    singer_count += 1

                elif performance == 3:
                    performance_type = "Dancer"
                    dancer_count +=1

                #checking for performance with highest duration
                if duration > highest_duration:
                    highest_duration = duration
                    highest_performance_details = f"{name} {surname} ({performance_type})"
                
                #formatting performance details usings string accumulation 
                formatted_performers += f"{i+1}: {surname},{name:12} {performance_type:12} {duration} minutes\n"
                
                #printing performance details to performance.txt 
                print(f"{surname} {name} {performance_type} {duration}", file=connection)
            
            connection.close()

            #converting time to hours and minutes
            total_hours = total_duration // MINUTES_IN_HOURS
            total_minutes = total_duration % MINUTES_IN_HOURS
            
            #printing each performance details to screen
            print()
            print("The following information has been added.")
            print()
            print(formatted_performers)

            #printing additional information 
            print("Sumarry Notes:")
            print("-" * 30)
            print(f"{Musician_count} Musician(s)\n{singer_count} Singer(s)\n{dancer_count} Dancer(s)")
            print(f"Total time required: {total_hours} hour(s), {total_minutes} min(s)")
            print(f"The longest act added is {highest_performance_details} {highest_duration} minutes")

        #prints message if amount of performers is < 1
        else:
            print()
            print("No performers were added")
        
    #checking if Generating concert details was selected(option 2)
    elif initialise == 2:
        #counter variables
        line_count = 0
        data_count = 0

        print()
        print(f"({initialise}) Generating Concert Details")
        print("-" * 30)

        #reading from performance.txt and formatting details
        connection_reading = open("performance.txt", "r")

        #spliting up the data
        for each_line in connection_reading:
            split_the_data = each_line.split(' ')
            data_fullname = split_the_data[1] + " " + split_the_data[0]
            data_surname = split_the_data[0]
            data_firstname = split_the_data[1]
            data_performence = split_the_data[2]
            data_duration = int(split_the_data[3])

            #checking if performance duration is longer than 15 minutes
            if data_duration > LONG_PERFORMANCE:
                # data_surname = data_surname + '*'
                data_fullname += "*"

            #printing concert details
            print(f"{line_count+1}: {data_fullname:15} ({data_performence:8}) {data_duration:<2} minutes")
            line_count +=1
            data_count += 1

        #prints messsage if file is empty
        if data_count == 0:
            print("The file is empty please add performers and try again")
        connection_reading.close()
   
    #sets initialise to 0
    initialise = 0 
    #runs a while loop until 1,2,3 is selected
    while initialise not in (MENU_OPTIONS):
        try:
            print()
            print("Black Water Annual Music Concert")
            print("-"*30)
            initialise = int(input("1. Adding Performers\n2. Generate Concert Details\n3. Quit\n>>> "))

            if initialise < 1 or initialise > 3:
                print()
                print("Please enter 1, 2 or 3")
                
        except ValueError:
            print()
            print("You have entered an invalid value, please try again")
            
#Displays message if exit (option 3) is selected
print()
print(f"({initialise}) Exiting Program")
print("-"*30)