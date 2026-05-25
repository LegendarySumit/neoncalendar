<div align="center">

# ✨ Neon Calendar & Reminders

**Modern desktop calendar with integrated task management and reminders**

![Python](https://img.shields.io/badge/Python-3.10%2B-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/Tkinter-GUI-green?logo=python)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-blue)
![Stars](https://img.shields.io/github/stars/LegendarySumit/neoncalendar?style=social)

**Beautiful • Intuitive • Fast • No Dependencies**

[📥 Download](#-quick-start) • [✨ Features](#-features) • [🎮 Demo](#-demo) • [🚀 Getting Started](#-getting-started) • [📅 Usage](#-usage)

</div>

---

## 📖 About

**Neon Calendar & Reminders** is a sleek, modern desktop calendar application designed for productivity. Built with Python and Tkinter, it combines a beautiful dark-mode calendar interface with an integrated reminder system using a custom grid layout and vibrant neon accents.

Perfect for planning your month, tracking important dates, and managing daily tasks—all with zero external dependencies and a stunning UI that feels right at home on any desktop.

**Perfect for:** Busy professionals 💼 • Students 📚 • Project managers 📅 • Planners ✨

---

## ✨ Features

- ✅ **Month Navigation** — Effortlessly browse between months with next/previous controls
- ✅ **Visual Date Highlighting**
  - 🔴 **Pink** — Today's date (real-world)
  - 🔵 **Blue** — Currently selected date
  - 🟢 **Green (with dot)** — Days with saved reminders
- ✅ **Integrated Reminder Management** — Add, view, and delete reminders per day
- ✅ **Smart Reminder Indicator** — Visual dot (•) on calendar days that have tasks
- ✅ **Beautiful Dark Theme** — Cyberpunk-inspired color palette with neon accents
- ✅ **Responsive Grid Layout** — Custom-built calendar grid that updates dynamically
- ✅ **Lightweight & Fast** — Pure Python, minimal dependencies, instant startup
- ✅ **Cross-Platform** — Works on Windows, Linux, and macOS
- ✅ **Object-Oriented Design** — Clean, maintainable, extensible codebase

---

## 🛠️ Tech Stack

### Core
- **Python** 3.10+ — Programming language
- **Tkinter** — Native GUI framework (built-in with Python)
- **calendar** module — Month calculations
- **datetime** module — Date handling

### Build & Distribution
- **PyInstaller** — Package as standalone executable
- **Git** — Version control

---

## 📁 Project Structure

```
neoncalendar/
├── calendar_app.py            # Main application (~250 lines)
├── requirements.txt           # Python dependencies (Tkinter built-in)
├── README.md                  # This file
├── LICENSE                    # MIT License
├── .gitignore                 # Git ignore rules
├── run.bat                    # Windows launcher
├── run.sh                     # Linux/macOS launcher
├── dist/
│   └── NeonCalendar.exe       # Standalone Windows executable
└── build/                     # PyInstaller build artifacts
```

---

## 🎮 Demo

### Visual Calendar States

```
May 2026

Mon  Tue  Wed  Thu  Fri  Sat  Sun
                          1    2
3    4    5    6    7    8    9
10   11   12   13   14   15   16
17   18   19   20   21   22   23
24   25   26 🔵  27   28   29   30
31

• Pink (accent) → Today is May 26
• Blue highlight → Selected date
• Green • → Days with reminders
```

### Workflow Example

1. Click on a date to select it
2. Type a reminder in the input field
3. Click `+` to add the reminder
4. Selected date now shows a green dot indicator
5. Switch to other dates and add more reminders
6. Delete reminders by selecting and clicking "Delete Selected"

---

## 🚀 Quick Start

### Option 1: **Standalone Executable** (Easiest - Windows Only)

No Python? No problem! Download and run the executable:

1. Go to [GitHub Releases](https://github.com/LegendarySumit/neoncalendar/releases)
2. Download `NeonCalendar.exe`
3. Double-click → **Calendar launches instantly** ✨
4. That's it! No installation, no dependencies

**Supported:** Windows 7 and later

---

### Option 2: **Run from Source** (Recommended for Developers)

No setup needed—just run:

```bash
python calendar_app.py
```

Or on Linux/macOS:

```bash
python3 calendar_app.py
```

**Windows users** can also double-click `run.bat`

**Requirements:**
- Python 3.10+
- Tkinter (included with Python by default)

---

### Option 3: **Clone & Run**

```bash
# Clone the repository
git clone https://github.com/LegendarySumit/neoncalendar.git
cd neoncalendar

# Run the app
python calendar_app.py
```

---

## 📅 Usage

### Adding a Reminder

1. **Click a date** on the calendar (it will highlight in blue)
2. **Type your task** in the text field at the bottom
3. **Click `+`** to add the reminder
4. The date now shows a **green dot (•)** indicator
5. Your reminder appears in the **Reminders** list

### Viewing Reminders

- **Click any date** to see all reminders for that day
- The **date label** updates to show the selected date
- **Green highlight** on calendar indicates days with reminders

### Deleting Reminders

1. **Click the date** containing the reminder
2. **Select the reminder** from the list
3. **Click "Delete Selected"** to remove it
4. If all reminders are deleted, the green dot disappears

### Navigating Months

- **Click `◀`** to go to the previous month
- **Click `▶`** to go to the next month
- Calendar automatically updates to show all days for that month

---

## 🎨 Color Palette

Inspired by modern cyberpunk and productivity design:

| Element | Hex Color | Purpose |
|---------|-----------|---------|
| Background | `#1E1E2E` | Deep purple |
| Frame BG | `#313244` | Medium purple |
| Text | `#CDD6F4` | Light lavender |
| Selected Day | `#89B4FA` | Neon blue |
| Today | `#F38BA8` | Neon pink |
| Reminders | `#A6E3A1` | Neon green |
| Hover State | `#45475A` | Darker purple |

---

## 🔧 How It Works

### Architecture

The application uses **Object-Oriented Programming** with a single `ModernCalendarApp` class:

```
ModernCalendarApp
├── __init__()           → Initialize state, reminders dict, UI
├── setup_ui()           → Create header, calendar grid, reminder panel
├── update_calendar()    → Regenerate calendar grid for current month
├── select_date()        → Handle date selection
├── prev_month()         → Navigate to previous month
├── next_month()         → Navigate to next month
├── update_reminder_list()  → Refresh reminder display
├── add_reminder()       → Add new task to selected date
└── delete_reminder()    → Remove selected reminder
```

### Key Implementation Details

1. **Calendar Grid**
   - Uses Python's `calendar.monthcalendar()` to get proper day layout
   - Dynamically creates buttons for each day
   - Updates instantly when changing months

2. **Reminder Storage**
   - Dictionary: `{"YYYY-MM-DD": ["Task 1", "Task 2", ...]}`
   - Simple key-value lookup for fast retrieval
   - No database needed

3. **Visual Indicators**
   - **Pink**: Checks if day == current_date
   - **Blue**: Checks if date == selected_date
   - **Green (•)**: Checks if date exists in reminders dict
   - Smart layering prevents colors from conflicting

4. **Dynamic UI Updates**
   - `update_calendar()` destroys old buttons and creates new ones
   - `update_reminder_list()` refreshes listbox content
   - Seamless transitions between date selections

---

## 💡 Design Philosophy

- **Zero External Dependencies** — Only Python built-ins (tkinter, calendar, datetime)
- **Fast & Lightweight** — Pure Python, no bloat
- **Extensible** — Easy to add features (notifications, persistence, sync)
- **Accessible** — Large text, clear colors, intuitive controls
- **Beautiful** — Modern dark theme with neon accents

---

## 📈 Usage Examples

### Daily Task Management
```
1. Open app (or pin to taskbar)
2. Click today's date
3. Add morning tasks
4. Check throughout the day
```

### Monthly Planning
```
1. Navigate to next month
2. Click each important date
3. Add milestones and deadlines
4. Visual reminders on calendar
```

### Project Tracking
```
1. Create reminders for phases
2. Use green dot indicators as progress markers
3. Delete completed tasks
```

---

## 🚧 Future Enhancements

- [ ] Persistent storage (JSON or SQLite)
- [ ] Alarm notifications & desktop alerts
- [ ] Color-coded reminder categories
- [ ] Recurring reminders
- [ ] Export calendar to .ics format
- [ ] Integration with system calendar
- [ ] Reminder priority levels
- [ ] Search & filter reminders

---

## 📝 License

MIT License — Free to use, modify, and distribute. See [LICENSE](LICENSE) for details.

---

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs and issues
- Suggest new features
- Submit pull requests
- Improve documentation

---

## 👨‍💻 Author

Built with ❤️ by [LegendarySumit](https://github.com/LegendarySumit)

Bringing productivity and beauty to desktop applications. ✨📅

---

<div align="center">

**Made with Python 🐍 and Tkinter 🎨**

[⬆ Back to top](#-neon-calendar--reminders)

</div>
