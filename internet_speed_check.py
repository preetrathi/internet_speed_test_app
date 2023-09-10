# Import necessary libraries
import tkinter as tk
from tkinter import Label, Button, ttk
import speedtest
import threading

# Create a class for the Internet Speed Test application
class InternetSpeedTestApp:
    def __init__(self, root):
        # Initialize the main window
        self.root = root
        self.root.title('Internet Speed Test')  # Set the window title
        self.root.geometry("500x600")  # Set the window size
        self.root.config(bg="#216869")  # Set the background color
        
        # Create the graphical user interface
        self.create_gui()
    
    def create_gui(self):
        # Create a label for the application title
        self.heading = Label(self.root, text='Internet Speed Test', font=("Times New Roman", 30, "bold"), bg='#216869', fg='#dce1de')
        self.heading.place(x=30, y=30, height=40, width=440)
        
        # Create labels for download and upload speed sections
        self.download_speed = Label(self.root, text='Download Speed', font=("Times New Roman", 30, "bold"),  bg='#9cc5a1', fg='#1F2421')
        self.download_speed.place(x=30, y=120, height=40, width=440)
        
        self.download_value = Label(self.root, text='00', font=("Times New Roman", 30, "bold"), bg='#9cc5a1', fg='#1F2421')
        self.download_value.place(x=30, y=180, height=40, width=440)
        
        self.upload_speed = Label(self.root, text='Upload Speed', font=("Times New Roman", 30, "bold"),  bg='#9cc5a1', fg='#1F2421')
        self.upload_speed.place(x=30, y=270, height=40, width=440)
        
        self.upload_value = Label(self.root, text='00', font=("Times New Roman", 30, "bold"),  bg='#9cc5a1', fg='#1F2421')
        self.upload_value.place(x=30, y=330, height=40, width=440)

        # Create labels for progress and a progress bar
        self.progress_label = Label(self.root, text='', font=("Times New Roman", 16),  bg='#9cc5a1', fg='#1F2421')
        self.progress_label.place(x=30, y=390)
        
        self.progress = ttk.Progressbar(self.root, orient="horizontal", length=440, mode="indeterminate")
        self.progress.place(x=30, y=420)

        # Create a button to start the speed test
        self.btn_speed_check = Button(self.root, text="Check Speed", font=("Times New Roman", 30, "bold"), relief=tk.RAISED,  bg='#9cc5a1', fg='#216869', command=self.start_speed_check)
        self.btn_speed_check.place(x=100, y=450, height=50, width=300)
        
        # Initialize a variable to track if the speed test is running
        self.speedtest_running = False
    
    def start_speed_check(self):
        # Start the speed test if it's not already running
        if not self.speedtest_running:
            self.speedtest_running = True
            self.btn_speed_check.config(state=tk.DISABLED)  # Disable the "Check Speed" button during the test
            self.progress_label.config(text="Fetching speeds...")
            self.progress.start()
            self.root.update()  # Force an update to display the progress bar
            
            # Run the speed test in a separate thread
            self.speedtest_thread = threading.Thread(target=self.run_speed_test)
            self.speedtest_thread.start()

    def run_speed_test(self):
        # Perform the speed test and display results
        sp = speedtest.Speedtest()
        sp.get_best_server()
        
        download_speed = sp.download() / 10 ** 6
        upload_speed = sp.upload() / 10 ** 6
        
        self.download_value.config(text=f"{download_speed:.3f} Mbps")
        self.upload_value.config(text=f"{upload_speed:.3f} Mbps")
        
        self.progress_label.config(text="Speeds fetched")
        self.progress.stop()
        self.speedtest_running = False
        self.btn_speed_check.config(state=tk.NORMAL)  # Re-enable the "Check Speed" button

# Define the main function to create the GUI
def main():
    root = tk.Tk()  # Create the main window
    app = InternetSpeedTestApp(root)  # Initialize the Internet Speed Test application
    root.mainloop()  # Start the main event loop

# Entry point for the program
if __name__ == "__main__":
    main()  # Call the main function to run the application
