import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog
import random

# User Data
users = {
    "Subasri": {"password": "pass", "points": 0, "subjects": {"Science": [], "Math": [], "Computer Science": []}},
    "Sunmathi": {"password": "pass", "points": 0, "subjects": {"Science": [], "Math": [], "Computer Science": []}},
    "Sowmiya": {"password": "pass", "points": 0, "subjects": {"Science": [], "Math": [], "Computer Science": []}},
}
admin_credentials = {"user": "pass"}

# Quiz Data
questions = {
    "Science": [
        ("What is the chemical symbol for water?", "H2O", ["H2O", "O2", "CO2", "NaCl"]),
        ("What planet is known as the Red Planet?", "Mars", ["Venus", "Earth", "Mars", "Jupiter"]),
    ],
    "Math": [
        ("What is 2 + 2?", "4", ["3", "4", "5", "6"]),
        ("What is the square root of 16?", "4", ["2", "4", "8", "16"]),
    ],
    "Computer Science": [
        ("What does CPU stand for?", "Central Processing Unit", ["Central Processing Unit", "Control Program Unit", "Central Programming Unit", "Central Process Utility"]),
        ("What is the binary representation of 2?", "10", ["01", "10", "11", "00"]),
    ],
}

# Main Application Class
class FlashcardApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Flashcard Learning App")
        self.root.geometry("800x600")  # Set the window size to be large
        self.root.configure(bg="#f0f8ff")  # Light blue background for a colorful design
        self.current_user = None

        self.login_screen()

    def login_screen(self):
        self.clear_screen()

        tk.Label(self.root, text="Flashcard Learning App", font=("Arial", 24, "bold"), bg="#4682b4", fg="white", padx=10, pady=10).pack(pady=10)
        tk.Label(self.root, text="Username:", font=("Arial", 14), bg="#f0f8ff").pack()
        self.username_entry = tk.Entry(self.root, font=("Arial", 14))
        self.username_entry.pack()

        tk.Label(self.root, text="Password:", font=("Arial", 14), bg="#f0f8ff").pack()
        self.password_entry = tk.Entry(self.root, show="*", font=("Arial", 14))
        self.password_entry.pack()

        tk.Button(self.root, text="Login", command=self.login, font=("Arial", 14), bg="#87ceeb", fg="black").pack(pady=5)
        tk.Button(self.root, text="Admin Login", command=self.admin_login, font=("Arial", 14), bg="#87ceeb", fg="black").pack()

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in users and users[username]["password"] == password:
            self.current_user = username
            self.student_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid username or password.")

    def admin_login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username in admin_credentials and admin_credentials[username] == password:
            self.admin_dashboard()
        else:
            messagebox.showerror("Login Failed", "Invalid admin credentials.")

    def student_dashboard(self):
        self.clear_screen()

        tk.Label(self.root, text=f"Welcome {self.current_user}", font=("Arial", 22, "bold"), bg="#4682b4", fg="white", padx=10, pady=10).pack(pady=10)
        tk.Button(self.root, text="View Subjects", command=self.view_subjects, font=("Arial", 14), bg="#87ceeb", fg="black").pack(pady=5)
        tk.Button(self.root, text="Take Quiz", command=self.take_quiz, font=("Arial", 14), bg="#87ceeb", fg="black").pack(pady=5)
        tk.Button(self.root, text="Leaderboard", command=self.show_leaderboard, font=("Arial", 14), bg="#87ceeb", fg="black").pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.login_screen, font=("Arial", 14), bg="#ffa07a", fg="black").pack(pady=5)

    def admin_dashboard(self):
        self.clear_screen()

        tk.Label(self.root, text="Admin Dashboard", font=("Arial", 22, "bold"), bg="#4682b4", fg="white", padx=10, pady=10).pack(pady=10)
        tk.Button(self.root, text="View Subjects", command=self.view_subjects, font=("Arial", 14), bg="#87ceeb", fg="black").pack(pady=5)
        tk.Button(self.root, text="Add Subject", command=self.add_subject, font=("Arial", 14), bg="#87ceeb", fg="black").pack(pady=5)
        tk.Button(self.root, text="Logout", command=self.login_screen, font=("Arial", 14), bg="#ffa07a", fg="black").pack(pady=5)

    def view_subjects(self):
        self.clear_screen()

        tk.Label(self.root, text="Subjects", font=("Arial", 22, "bold"), bg="#4682b4", fg="white", padx=10, pady=10).pack(pady=10)
        for subject in questions.keys():
            tk.Label(self.root, text=subject, font=("Arial", 14), bg="#f0f8ff").pack()

        tk.Button(self.root, text="Back", command=self.student_dashboard if self.current_user else self.admin_dashboard, font=("Arial", 14), bg="#ffa07a", fg="black").pack(pady=10)

    def add_subject(self):
        new_subject = simpledialog.askstring("Add Subject", "Enter the subject name:")
        if new_subject and new_subject not in questions:
            questions[new_subject] = []
            for user in users.values():
                user["subjects"][new_subject] = []
            messagebox.showinfo("Success", f"Subject '{new_subject}' added.")
        else:
            messagebox.showerror("Error", "Subject already exists or invalid name.")
        self.admin_dashboard()

    def take_quiz(self):
        self.clear_screen()

        tk.Label(self.root, text="Select a Subject", font=("Arial", 22, "bold"), bg="#4682b4", fg="white", padx=10, pady=10).pack(pady=10)
        for subject in questions.keys():
            tk.Button(self.root, text=subject, command=lambda s=subject: self.start_quiz(s), font=("Arial", 14), bg="#87ceeb", fg="black").pack(pady=5)

        tk.Button(self.root, text="Back", command=self.student_dashboard, font=("Arial", 14), bg="#ffa07a", fg="black").pack(pady=10)

    def start_quiz(self, subject):
        self.clear_screen()

        if not questions[subject]:
            messagebox.showinfo("No Questions", f"No questions available for {subject}.")
            self.take_quiz()
            return

        question, answer, options = random.choice(questions[subject])

        tk.Label(self.root, text=question, font=("Arial", 16), bg="#f0f8ff").pack(pady=10)
        for opt in options:
            tk.Button(self.root, text=opt, command=lambda o=opt: self.check_answer(o, answer, subject), font=("Arial", 14), bg="#add8e6", fg="black").pack(pady=5)

    def check_answer(self, selected, correct, subject):
        if selected == correct:
            users[self.current_user]["points"] += 10
            messagebox.showinfo("Correct", "Your answer is correct!")
        else:
            messagebox.showerror("Wrong", "Your answer is incorrect.")
        self.take_quiz()

    def show_leaderboard(self):
        self.clear_screen()

        tk.Label(self.root, text="Leaderboard", font=("Arial", 22, "bold"), bg="#4682b4", fg="white", padx=10, pady=10).pack(pady=10)
        sorted_users = sorted(users.items(), key=lambda x: x[1]["points"], reverse=True)
        for i, (user, data) in enumerate(sorted_users, start=1):
            tk.Label(self.root, text=f"{i}. {user} - {data['points']} points", font=("Arial", 14), bg="#f0f8ff").pack()

        tk.Button(self.root, text="Back", command=self.student_dashboard, font=("Arial", 14), bg="#ffa07a", fg="black").pack(pady=10)

    def clear_screen(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Run the application
root = tk.Tk()
app = FlashcardApp(root)
root.mainloop()
