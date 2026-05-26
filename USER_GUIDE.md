# 📅 Neon Calendar & Reminders — Complete User Guide

## Quick Start (5 Minutes)

### 1️⃣ **Understanding the Layout**

```
┌─────────────────────────────────────┐
│  ◀  May 2026  ▶                     │  ← Navigate months
├─────────────────────────────────────┤
│  Mon Tue Wed Thu Fri Sat Sun       │
│   1   2   3   4   5   6   7        │
│   8   9  10  11 🔵 13  14  15     │  ← Calendar grid
│  ...                               │     Blue = Selected date
├─────────────────────────────────────┤
│  📅 Reminders for May 12, 2026     │
│                                    │
│  ○  Team Meeting          @ 14:00  │  ← Your reminders
│  ○  Lunch with Sarah      @ 12:30  │     ○ = pending
│  ✓  Doctor Appointment    @ 09:00  │     ✓ = completed
│                                    │
│  [Enter task...] [HH:MM] [Add]     │  ← Input fields
│                                    │
│  [Delete Selected]                 │  ← Delete button
└─────────────────────────────────────┘
```

---

## 🎯 Step-by-Step Usage

### **Adding a Reminder**

**Step 1:** Click on a date in the calendar
```
The date will turn BLUE and the reminder section updates
```

**Step 2:** Type your task in the first field
```
Example: "Team Meeting"
         "Buy groceries"
         "Call Mom"
```

**Step 3:** Enter the time in HH:MM format (optional)
```
Examples:  14:00  (2 PM)
           09:30  (9:30 AM)
           23:45  (11:45 PM)

Leave blank or type "No time" if you don't need a specific time
```

**Step 4:** Click `[Add]` button
```
Your reminder appears in the list!
✓ Success message shows
```

### **Viewing Reminders**

Simply **click any date** on the calendar to see all reminders for that day.

```
Date colors:
🔴 PINK   = Today's date
🔵 BLUE   = Currently selected date  
🟢 GREEN  = Days with reminders (marked with •)
```

### **Deleting a Reminder**

**Step 1:** Click on the date containing the reminder
**Step 2:** Click the reminder in the list to select it (it will highlight)
**Step 3:** Click `[Delete Selected]`
**Step 4:** Confirm deletion

---

## ⏰ Timed Reminder Alerts

The app automatically shows **pop-up alerts** when reminder time arrives!

**How it works:**
1. Add a reminder with a specific time (e.g., "Meeting" @ 14:00)
2. Keep the app running
3. At exactly 14:00, a pop-up notification appears: 🔔
4. The reminder status changes to ✓ (completed)

**Example:**
```
┌─────────────────────────────┐
│  ⏰ Reminder Alert!         │
│                             │
│  🔔 Team Meeting            │
│                             │
│  Time: 14:00                │
│                             │
│  [OK]                       │
└─────────────────────────────┘
```

---

## 💾 Automatic Saving

✅ **All reminders are automatically saved** to `reminders.json`

This means:
- Close the app → Reminders still exist
- Reopen the app → All reminders are back
- No data loss!

---

## 📋 Reminder Status

Each reminder shows with a status indicator:

| Symbol | Meaning | Explanation |
|--------|---------|-------------|
| `○` | Pending | Not yet triggered/completed |
| `✓` | Completed | Reminder alert already shown at this time |

---

## 🎨 Color Guide

**Calendar Colors:**
- 🔴 **Pink text** → Today's date (right now)
- 🔵 **Blue background** → Date you clicked (selected)
- 🟢 **Green text with •** → Days that have reminders

**Button Colors:**
- 🟢 Green `[Add]` → Adds reminder
- 🔴 Pink `[Delete Selected]` → Removes reminder
- 🔵 `[◀] [▶]` → Navigate months

---

## 🔧 Tips & Tricks

### ✅ **Make it More Useful**

**1. Set reminders for the future**
```
Click May 30 → Add "Birthday Party" @ 18:00 → Click Add
```

**2. Multiple reminders per day**
```
May 15:
  ○ Morning Workout @ 06:00
  ○ Team Standup @ 09:30
  ○ Lunch break @ 12:00
  ○ Project deadline @ 17:00
```

**3. Plan your month**
```
Navigate through months using ◀ ▶
Add reminders for important dates ahead
Keep app running to get alerts
```

### ❌ **Common Mistakes**

| Mistake | Solution |
|---------|----------|
| "I added a reminder but don't see it" | Make sure the correct date is selected (blue highlight) |
| "Time format error" | Use HH:MM format (e.g., 14:30, not 2:30 PM) |
| "Alert didn't pop up" | App must be running. The alert checks every minute. |
| "Reminder disappeared" | Try closing and reopening the app (it loads from file) |

---

## 📱 Features Explained

### **Monthly Navigation**
- Click `◀` to go back months
- Click `▶` to go forward months
- See full month at a glance

### **Visual Reminder Indicators**
- Green dot (•) on calendar shows busy days instantly
- No need to click every date to find busy days

### **Automatic Alerts**
- Background thread monitors time
- Alerts pop up at exact reminder time
- Even if you're not looking at the app

### **Persistent Storage**
- `reminders.json` file in project directory
- Human-readable JSON format
- Easy to backup or share

---

## 🎯 Example Workflows

### **Scenario 1: Daily Task Management**
```
1. Open app (runs in background)
2. Click today's date
3. Add: "Write report" @ 10:00
4. Add: "Team meeting" @ 14:00
5. Add: "Review code" @ 16:00
6. Get alerts at each time ⏰
```

### **Scenario 2: Monthly Planning**
```
1. Navigate to June 2026 using ▶
2. Click June 5 → Add "Project starts" @ 09:00
3. Click June 15 → Add "Milestone check" @ 17:00
4. Click June 28 → Add "Deadline!" @ 23:59
5. Calendar shows green dots on busy days
```

### **Scenario 3: Event Preparation**
```
1. Click wedding date (June 20)
2. Add "Buy gift" @ 10:00
3. Add "Get ready" @ 17:00
4. Add "Leave for venue" @ 17:45
5. Receive 3 alerts on the day
```

---

## 🐛 Troubleshooting

### **Reminders not appearing?**
- ✅ Make sure you clicked `[Add]` (not just typed)
- ✅ Check if the reminder is on the correct date (selected date shows in blue)
- ✅ Look for confirmation message

### **Alerts not showing up?**
- ✅ Keep the app running in the background
- ✅ Check system clock is correct
- ✅ Make sure you entered time in HH:MM format
- ✅ Alerts check every minute, so wait up to 1 minute

### **Lost reminders after closing?**
- ✅ App saves to `reminders.json` automatically
- ✅ Restart the app to reload
- ✅ Check if file exists in project folder

### **Can't delete a reminder?**
- ✅ Click the reminder in the list first (it should highlight)
- ✅ Then click `[Delete Selected]`
- ✅ If still stuck, select from list again

---

## 💡 Best Practices

✅ **DO:**
- Set specific times for important reminders
- Review the month view regularly
- Use consistent task names ("Meeting" vs "meeting")
- Keep the app running during work hours

❌ **DON'T:**
- Leave blank tasks (add a real task name)
- Use "No time" if you want alerts
- Close the app if you want timed alerts
- Use 24-hour format incorrectly (use 14:30, not 2:30 PM)

---

## 🎓 Advanced Usage

### **Exporting Reminders**
The `reminders.json` file is plain text. You can:
- Copy it to another device
- Edit it with any text editor
- Share with others

**Example JSON format:**
```json
{
  "2026-05-26": [
    {
      "task": "Team Meeting",
      "time": "14:00",
      "completed": false,
      "created": "2026-05-26T10:30:00"
    },
    {
      "task": "Lunch",
      "time": "12:30",
      "completed": true,
      "created": "2026-05-26T09:15:00"
    }
  ]
}
```

### **Backup Your Reminders**
```
Just copy reminders.json to cloud storage or USB!
```

---

## 📞 Quick Reference

| Action | How |
|--------|-----|
| Add reminder | Click date → Type task → Enter time → Click `[Add]` |
| View reminders | Click any date |
| Delete reminder | Select reminder in list → Click `[Delete Selected]` |
| Go to next month | Click `▶` |
| Go to previous month | Click `◀` |
| See days with reminders | Look for green dots (•) |
| Get timed alerts | App must be running + time must match exactly |
| Find today's date | Look for pink text |

---

**Enjoy your beautiful calendar and never miss a reminder again! 📅✨**
