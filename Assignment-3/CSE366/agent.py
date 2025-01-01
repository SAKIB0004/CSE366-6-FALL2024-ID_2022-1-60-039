import numpy as np
import random
import pygame

# Agent: Represents individual students
class Student:
    def __init__(self, id, availability, preference, num_students):
        self.id = id  # Unique identifier for each student
        self.availability = availability  # List of available time slots
        self.preference = preference  # Priority for specific slots
        self.schedule = []  # List of assigned classes (time slots)
        self.students_Preference = np.random.uniform(0.5, 1.5, size=num_students)  # Student preference for days

    def assign_class(self, time_slot, class_priority):
        """
        Assign a class to the student based on availability.
        """
        if time_slot in self.availability:
            # Adjust class priority based on day preference
            day = time_slot % len(self.students_Preference)  # Get the day from the time_slot index
            effective_priority = class_priority * self.students_Preference[day]
            self.schedule.append((time_slot, effective_priority))
        else:
            raise ValueError(f"Time slot {time_slot} is unavailable for student {self.id}.")

    def clear_schedule(self):
        """Clear the schedule for new generations."""
        self.schedule = []

    def total_priority(self):
        """Calculate the total priority of the assigned classes."""
        return sum(priority for _, priority in self.schedule)
