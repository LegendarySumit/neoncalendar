import tkinter as tk
from tkinter import ttk, messagebox
import calendar
from datetime import datetime
import json
import os
import threading
import time

class ModernCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Neon Calendar & Reminders")
        self.root.geometry("550x650")
        self.root.configure(bg="#1E1E2E") # Deep dark background
        
        # Color Palette
        self.colors = {
            "bg": "#1E1E2E",
            "frame_bg": "#313244",
            "text": "#CDD6F4",
            "accent_blue": "#89B4FA",   # For selected day
            "accent_pink": "#F38BA8",   # For current real-world day
            "accent_green": "#A6E3A1",  # For days with reminders
            "btn_hover": "#45475A"
        }

        # App State
        self.current_date = datetime.now()
        self.display_year = self.current_date.year
        self.display_month = self.current_date.month
        self.selected_date = f"{self.current_date.year}-{self.current_date.month:02d}-{self.current_date.day:02d}"
        
        # Dictionary to store reminders: {"YYYY-MM-DD": [{"task": "...", "time": "HH:MM", "completed": False}, ...]}
        self.reminders = {}
        self.reminder_file = "reminders.json"
        self.load_reminders()

        self.setup_ui()
        self.update_calendar()
        self.update_reminder_list()
        
        # Start reminder checker thread
        self.start_reminder_checker()

    def setup_ui(self):
        # --- HEADER (Month / Year Navigation) ---
        header_frame = tk.Frame(self.root, bg=self.colors["bg"])
        header_frame.pack(fill="x", pady=15, padx=20)

        prev_btn = tk.Button(header_frame, text="◀", font=("Arial", 14), bg=self.colors["bg"], 
                             fg=self.colors["accent_blue"], relief="flat", activebackground=self.colors["btn_hover"],
                             command=self.prev_month)
        prev_btn.pack(side="left")

        self.month_year_label = tk.Label(header_frame, text="", font=("Segoe UI", 18, "bold"), 
                                         bg=self.colors["bg"], fg=self.colors["text"])
        self.month_year_label.pack(side="left", expand=True)

        next_btn = tk.Button(header_frame, text="▶", font=("Arial", 14), bg=self.colors["bg"], 
                             fg=self.colors["accent_blue"], relief="flat", activebackground=self.colors["btn_hover"],
                             command=self.next_month)
        next_btn.pack(side="right")

        # --- CALENDAR GRID ---
        self.cal_frame = tk.Frame(self.root, bg=self.colors["bg"])
        self.cal_frame.pack(fill="x", padx=20)

        # Days of the week header
        days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
        for i, day in enumerate(days):
            lbl = tk.Label(self.cal_frame, text=day, font=("Segoe UI", 10, "bold"), 
                           bg=self.colors["bg"], fg=self.colors["text"])
            lbl.grid(row=0, column=i, pady=5, sticky="nsew")

        # Configure grid weights for equal sizing
        for i in range(7):
            self.cal_frame.grid_columnconfigure(i, weight=1)

        # --- REMINDER SECTION ---
        reminder_container = tk.Frame(self.root, bg=self.colors["frame_bg"], bd=0)
        reminder_container.pack(fill="both", expand=False, padx=20, pady=(10, 0), ipady=8)
        
        self.selected_date_label = tk.Label(reminder_container, text="Reminders for Today", font=("Segoe UI", 14, "bold"), 
                                            bg=self.colors["frame_bg"], fg=self.colors["accent_blue"])
        self.selected_date_label.pack(pady=(8, 5))

        # Listbox frame with scrollbar
        listbox_frame = tk.Frame(reminder_container, bg=self.colors["frame_bg"])
        listbox_frame.pack(fill="both", expand=True, padx=15, pady=3)
        
        scrollbar = tk.Scrollbar(listbox_frame, bg=self.colors["btn_hover"], activebackground=self.colors["accent_blue"])
        scrollbar.pack(side="right", fill="y")

        self.reminder_listbox = tk.Listbox(listbox_frame, font=("Segoe UI", 12), bg="#181825", 
                                           fg=self.colors["text"], selectbackground=self.colors["accent_blue"], 
                                           relief="flat", height=5, yscrollcommand=scrollbar.set)
        self.reminder_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.reminder_listbox.yview)

        # Input frame for adding reminders
        input_frame = tk.Frame(reminder_container, bg=self.colors["frame_bg"])
        input_frame.pack(fill="x", padx=15, pady=(5, 0))

        # Task input
        self.reminder_entry = tk.Entry(input_frame, font=("Segoe UI", 12), bg="#181825", 
                                       fg=self.colors["text"], relief="flat", insertbackground="white")
        self.reminder_entry.pack(side="left", fill="x", expand=True, ipady=5, padx=(0, 5))
        self.reminder_entry.insert(0, "Enter task...")
        self.reminder_entry.bind("<FocusIn>", self.on_entry_focus)
        self.reminder_entry.bind("<FocusOut>", self.on_entry_unfocus)

        # Time input
        self.time_entry = tk.Entry(input_frame, font=("Segoe UI", 12), bg="#181825", 
                                   fg=self.colors["text"], relief="flat", insertbackground="white", width=8)
        self.time_entry.pack(side="left", padx=(0, 5), ipady=5)
        self.time_entry.insert(0, "HH:MM")
        self.time_entry.bind("<FocusIn>", self.on_time_focus)
        self.time_entry.bind("<FocusOut>", self.on_time_unfocus)

        # Add button
        add_btn = tk.Button(input_frame, text=" Add ", font=("Arial", 12, "bold"), bg=self.colors["accent_green"], 
                            fg="#1E1E2E", relief="flat", command=self.add_reminder)
        add_btn.pack(side="right")

        # Delete button
        del_btn = tk.Button(reminder_container, text="Delete Selected", font=("Segoe UI", 11, "bold"), 
                            bg=self.colors["accent_pink"], fg="#1E1E2E", relief="flat", command=self.delete_reminder)
        del_btn.pack(pady=(3, 0))

    def on_entry_focus(self, event):
        if self.reminder_entry.get() == "Enter task...":
            self.reminder_entry.delete(0, tk.END)
            self.reminder_entry.config(fg=self.colors["text"])

    def on_entry_unfocus(self, event):
        if self.reminder_entry.get() == "":
            self.reminder_entry.insert(0, "Enter task...")
            self.reminder_entry.config(fg="#888888")

    def on_time_focus(self, event):
        if self.time_entry.get() == "HH:MM":
            self.time_entry.delete(0, tk.END)
            self.time_entry.config(fg=self.colors["text"])

    def on_time_unfocus(self, event):
        if self.time_entry.get() == "":
            self.time_entry.insert(0, "HH:MM")
            self.time_entry.config(fg="#888888")

    def update_calendar(self):
        # Update header text
        month_name = calendar.month_name[self.display_month]
        self.month_year_label.config(text=f"{month_name} {self.display_year}")

        # Clear existing calendar days (skip row 0, which is the Mon-Sun header)
        for widget in self.cal_frame.winfo_children():
            if int(widget.grid_info()["row"]) > 0:
                widget.destroy()

        # Generate days for the month
        cal = calendar.monthcalendar(self.display_year, self.display_month)
        
        for row, week in enumerate(cal, start=1):
            for col, day in enumerate(week):
                if day != 0:
                    date_str = f"{self.display_year}-{self.display_month:02d}-{day:02d}"
                    
                    # Default colors
                    btn_bg = self.colors["bg"]
                    btn_fg = self.colors["text"]
                    
                    # Highlight logic
                    is_today = (day == self.current_date.day and 
                                self.display_month == self.current_date.month and 
                                self.display_year == self.current_date.year)
                    
                    if is_today:
                        btn_fg = self.colors["accent_pink"]
                    
                    if date_str == self.selected_date:
                        btn_bg = self.colors["btn_hover"]
                        btn_fg = self.colors["accent_blue"]
                        
                    if date_str in self.reminders and self.reminders[date_str]:
                        # Visual indicator that a reminder exists on this day
                        text_display = f"{day} •" 
                        if not is_today and date_str != self.selected_date:
                            btn_fg = self.colors["accent_green"]
                    else:
                        text_display = str(day)

                    btn = tk.Button(self.cal_frame, text=text_display, font=("Segoe UI", 12), 
                                    bg=btn_bg, fg=btn_fg, relief="flat", activebackground=self.colors["btn_hover"],
                                    command=lambda d=date_str: self.select_date(d))
                    btn.grid(row=row, column=col, sticky="nsew", padx=2, pady=2, ipadx=5, ipady=5)

    def select_date(self, date_str):
        self.selected_date = date_str
        self.update_calendar() # Redraw to update the highlight
        self.update_reminder_list()

    def prev_month(self):
        if self.display_month == 1:
            self.display_month = 12
            self.display_year -= 1
        else:
            self.display_month -= 1
        self.update_calendar()

    def next_month(self):
        if self.display_month == 12:
            self.display_month = 1
            self.display_year += 1
        else:
            self.display_month += 1
        self.update_calendar()

    def update_reminder_list(self):
        self.reminder_listbox.delete(0, tk.END)
        
        # Format label date nicely
        date_obj = datetime.strptime(self.selected_date, "%Y-%m-%d")
        self.selected_date_label.config(text=f"📅 {date_obj.strftime('%B %d, %Y')}")

        if self.selected_date in self.reminders:
            for idx, item in enumerate(self.reminders[self.selected_date]):
                task = item.get("task", "Unknown")
                reminder_time = item.get("time", "No time")
                status = "✓" if item.get("completed", False) else "○"
                # Format: status task (aligned left) ... time (aligned right)
                padding = 40 - len(task)
                if padding < 0:
                    padding = 1
                display = f"  {status} {task}{'.' * padding}{reminder_time}"
                self.reminder_listbox.insert(tk.END, display)
        else:
            self.reminder_listbox.insert(tk.END, "  No reminders for this date")

    def add_reminder(self):
        task = self.reminder_entry.get().strip()
        reminder_time = self.time_entry.get().strip()
        
        # Validate input
        if task == "" or task == "Enter task...":
            messagebox.showwarning("Input Error", "Please enter a task!")
            return
        
        if reminder_time == "" or reminder_time == "HH:MM":
            reminder_time = "No time"
        else:
            # Validate time format
            try:
                datetime.strptime(reminder_time, "%H:%M")
            except ValueError:
                messagebox.showerror("Invalid Time", "Please use HH:MM format (e.g., 14:30)")
                return
        
        # Add reminder
        if self.selected_date not in self.reminders:
            self.reminders[self.selected_date] = []
        
        self.reminders[self.selected_date].append({
            "task": task,
            "time": reminder_time,
            "completed": False,
            "created": datetime.now().isoformat()
        })
        
        # Clear inputs
        self.reminder_entry.delete(0, tk.END)
        self.reminder_entry.insert(0, "Enter task...")
        self.time_entry.delete(0, tk.END)
        self.time_entry.insert(0, "HH:MM")
        
        # Save and update display
        self.save_reminders()
        self.update_reminder_list()
        self.update_calendar()
        
        messagebox.showinfo("Success", f"✓ Reminder added for {self.selected_date}!")

    def delete_reminder(self):
        selected_index = self.reminder_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            
            if self.selected_date in self.reminders and index < len(self.reminders[self.selected_date]):
                del self.reminders[self.selected_date][index]
                
                # Clean up empty days
                if not self.reminders[self.selected_date]:
                    del self.reminders[self.selected_date]
                
                self.save_reminders()
                self.update_reminder_list()
                self.update_calendar()
                messagebox.showinfo("Deleted", "Reminder deleted!")
        else:
            messagebox.showinfo("Select Item", "Please select a reminder to delete.")

    def save_reminders(self):
        try:
            with open(self.reminder_file, "w") as f:
                json.dump(self.reminders, f, indent=2)
        except Exception as e:
            messagebox.showerror("Save Error", f"Could not save reminders: {e}")

    def load_reminders(self):
        try:
            if os.path.exists(self.reminder_file):
                with open(self.reminder_file, "r") as f:
                    self.reminders = json.load(f)
            else:
                self.reminders = {}
        except Exception as e:
            messagebox.showerror("Load Error", f"Could not load reminders: {e}")
            self.reminders = {}

    def start_reminder_checker(self):
        def check_reminders():
            while True:
                try:
                    now = datetime.now()
                    current_date = now.strftime("%Y-%m-%d")
                    current_time = now.strftime("%H:%M")
                    
                    if current_date in self.reminders:
                        for reminder in self.reminders[current_date]:
                            if reminder.get("time") == current_time and not reminder.get("completed"):
                                # Pop-up notification
                                messagebox.showinfo(
                                    "⏰ Reminder Alert!", 
                                    f"🔔 {reminder.get('task', 'Task')}\n\nTime: {current_time}"
                                )
                                reminder["completed"] = True
                                self.save_reminders()
                    
                    time.sleep(60)  # Check every minute
                except:
                    time.sleep(60)
        
        # Run in background thread
        checker_thread = threading.Thread(target=check_reminders, daemon=True)
        checker_thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    app = ModernCalendarApp(root)
    root.mainloop()
