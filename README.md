# log-external-connections
A python program that logs external connections to a .txt file

## Installation
1. Install Python on your Windows 10 machine if you haven't already: https://www.python.org/downloads/windows/
2. Install the psutil library using pip: pip install psutil
3. Clone or download this repository to your local machine
4. Navigate to the directory where you cloned/downloaded the repository in a terminal/command prompt
5. Run the program with the following command: python log_connections.py
6. Verify that a file named external_connections.log has been created and contains log entries of external connections

## Auto-start on Boot
1. Create a batch file to run the program automatically on boot by following these steps:
    a. Open a text editor such as Notepad
    b. Type the following command in the editor: python <path_to_script>/log_connections.py
    c. Replace <path_to_script> with the absolute path to the directory where you cloned/downloaded the repository
    d. Save the file with a .bat extension (e.g. run_log_connections.bat)
2. Create a task in the Task Scheduler to run the batch file on boot by following these steps:
    a. Open the Task Scheduler by typing Task Scheduler in the Windows search bar and clicking on the result
    b. Click on Create Basic Task from the Actions panel on the right side of the window
    c. Give the task a name (e.g. Log Connections) and provide a description if desired
    d. Select the When the computer starts trigger and click Next
    e. Choose Start a program as the action and click Next
    f. Browse to the location of the batch file created in step 1 and select it
    g. Click Finish to complete the task creation
    
Test the auto-start functionality by restarting your computer and checking the external_connections.log file for entries.
You should now have the program logging external connections on your Windows 10 machine, and it will automatically start logging connections on boot.
