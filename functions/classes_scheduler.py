# use your knowledge of functions and loops to match a list of classes to available time slots

"""
create a loop that runs once for each class, 
joins it with a time slot at the same index, and 
saves the schedule in a new list
"""

# parameters of the function = classes and times
# schedule = [] creates an empty list
def schedule_classes(classes, times):
    schedule = []
    index = 0

    while index < len(classes):
        scheduled_class = classes[index] + ": " + times[index]
        schedule.append(scheduled_class)
        index += 1

    return schedule

classes = ["Algebra", "History", "Biology", "Swimming"]
times = ["9 am", "11 am", "1 pm", "3 pm",]

# call the function
schedule = schedule_classes(classes, times)
print(f"Monday's schedule: {schedule}")