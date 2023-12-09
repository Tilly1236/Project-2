import tkinter as tk
from tkinter import messagebox
from typing import List

class GradeCalculator:
    def __init__(self, total_number_entry: tk.Entry, scores_entry: tk.Entry, result_label: tk.Label):
        """
        Initialize the GradeCalculator.

        Parameters:
            total_number_entry (tk.Entry): Entry widget for total number of students.
            scores_entry (tk.Entry): Entry widget for entering scores separated by space.
            result_label (tk.Label): Label widget to display the calculated grades.
        """
        self.total_number_entry = total_number_entry
        self.scores_entry = scores_entry
        self.result_label = result_label

    def calculate_grades(self):
        """
        Calculate letter grades based on user input and update the result label.
        """
        try:
            total_number = int(self.total_number_entry.get())
            if total_number <= 0:
                raise ValueError("Total number must be a positive integer.")

            scores = [int(score) for score in self.scores_entry.get().split()]
            if len(scores) != total_number:
                raise ValueError(f"Please enter {total_number} valid scores.")

            # Define grade ranges
            grade_ranges = {'A': (90, 100), 'B': (80, 89), 'C': (70, 79), 'D': (60, 69), 'F': (0, 59)}

            # Calculate letter grades
            grades = []
            for student_score in scores:
                for grade, (lower, upper) in grade_ranges.items():
                    if lower <= student_score <= upper:
                        grades.append(grade)
                        break

            result_text = "Grades:\n"
            for i, (score, grade) in enumerate(zip(scores, grades), start=1):
                result_text += f'Student {i} score is {score} and grade is {grade}\n'

            self.result_label.config(text=result_text)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

class GradeCalculatorGUI:
    def __init__(self, master: tk.Tk):
        """
        Initialize the GradeCalculatorGUI.

        Parameters:
            master (tk.Tk): The master Tkinter window.
        """
        self.master = master
        self.master.title("Grade Calculator")

        self.create_widgets()

    def create_widgets(self):
        """
        Create and pack the main widgets in the GUI.
        """
        self.total_number_label = tk.Label(self.master, text="Total number of students:")
        self.total_number_label.pack()

        self.total_number_entry = tk.Entry(self.master)
        self.total_number_entry.pack()

        self.scores_label = tk.Label(self.master, text="Enter scores separated by space:")
        self.scores_label.pack()

        self.scores_entry = tk.Entry(self.master)
        self.scores_entry.pack()

        self.calculate_button = tk.Button(self.master, text="Calculate Grades", command=self.calculate_grades)
        self.calculate_button.pack(pady=10)

        self.result_label = tk.Label(self.master, text="")
        self.result_label.pack(pady=10)

        self.grade_calculator = GradeCalculator(self.total_number_entry, self.scores_entry, self.result_label)

    def calculate_grades(self):
        """
        Trigger the calculate_grades method in GradeCalculator.
        """
        self.grade_calculator.calculate_grades()

if __name__ == "__main__":
    root = tk.Tk()
    app = GradeCalculatorGUI(root)
    root.mainloop()
