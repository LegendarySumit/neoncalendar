import tkinter as tk
from tkinter import ttk, messagebox
import calendar
from datetime import datetime

class ModernCalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("✨ Neon Calendar & Reminders")
        self.root.geometry("450x650")
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
        
        # Dictionary to store reminders: {"YYYY-MM-DD": ["Task 1", "Task 2"]}
        self.reminders = {}

        self.setup_ui()
        self.update_calendar()
        self.update_reminder_list()

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
        reminder_container.pack(fill="both", expand=True, padx=20, pady=20)
        
        self.selected_date_label = tk.Label(reminder_container, text="Reminders", font=("Segoe UI", 14, "bold"), 
                                            bg=self.colors["frame_bg"], fg=self.colors["accent_blue"])
        self.selected_date_label.pack(pady=(15, 5))

        # Listbox for viewing reminders
        self.reminder_listbox = tk.Listbox(reminder_container, font=("Segoe UI", 11), bg="#181825", 
                                           fg=self.colors["text"], selectbackground=self.colors["accent_blue"], 
                                           relief="flat", borderwidth=0, highlightthickness=0)
        self.reminder_listbox.pack(fill="both", expand=True, padx=15, pady=5)

        # Entry field and Add Button
        input_frame = tk.Frame(reminder_container, bg=self.colors["frame_bg"])
        input_frame.pack(fill="x", padx=15, pady=10)

        self.reminder_entry = tk.Entry(input_frame, font=("Segoe UI", 12), bg="#181825", 
                                       fg=self.colors["text"], relief="flat", insertbackground="white")
        self.reminder_entry.pack(side="left", fill="x", expand=True, ipady=5)
        
        add_btn = tk.Button(input_frame, text=" + ", font=("Arial", 12, "bold"), bg=self.colors["accent_green"], 
                            fg="#1E1E2E", relief="flat", command=self.add_reminder)
        add_btn.pack(side="right", padx=(10, 0))

        # Delete button at the very bottom
        del_btn = tk.Button(reminder_container, text="Delete Selected", font=("Segoe UI", 10, "bold"), 
                            bg=self.colors["accent_pink"], fg="#1E1E2E", relief="flat", command=self.delete_reminder)
        del_btn.pack(pady=(0, 15))

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
        self.selected_date_label.config(text=date_obj.strftime("%B %d, %Y"))

        if self.selected_date in self.reminders:
            for item in self.reminders[self.selected_date]:
                self.reminder_listbox.insert(tk.END, f"  {item}")

    def add_reminder(self):
        text = self.reminder_entry.get().strip()
        if text:
            if self.selected_date not in self.reminders:
                self.reminders[self.selected_date] = []
            
            self.reminders[self.selected_date].append(text)
            self.reminder_entry.delete(0, tk.END)
            self.update_reminder_list()
            self.update_calendar() # Redraw calendar to show the dot indicator (•)

    def delete_reminder(self):
        selected_index = self.reminder_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            # Remove from dictionary
            del self.reminders[self.selected_date][index]
            
            # Clean up empty days
            if not self.reminders[self.selected_date]:
                del self.reminders[self.selected_date]
                
            self.update_reminder_list()
            self.update_calendar() # Redraw to remove dot indicator if empty
        else:
            messagebox.showinfo("Select Item", "Please select a reminder to delete.")

if __name__ == "__main__":
    root = tk.Tk()
    root.eval('tk::PlaceWindow . center')
    app = ModernCalendarApp(root)
    root.mainloop()
