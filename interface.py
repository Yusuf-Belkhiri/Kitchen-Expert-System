import tkinter as tk
from tkinter import ttk
import random

def next_button_click():
    if checkbox1_var.get() == 1:
        replace_window_content("Option 1")
    elif checkbox2_var.get() == 1:
        replace_window_content("Option 2")

def checkbox1_click():
    checkbox2_var.set(0)  # Uncheck the second checkbox

def checkbox2_click():
    checkbox1_var.set(0)  # Uncheck the first checkbox

def replace_window_content(option):
    # Clear the current window
    for widget in root.winfo_children():
        widget.destroy()

    # Create the new content based on the selected option
    if option == "Option 1":
        label = ttk.Label(root, text="Option 1 is selected", font=("Helvetica", 16))
        label.pack()
        back_button = ttk.Button(root, text="Back", command=go_back)
        back_button.pack()

        # Create the table for ingredient list
        table_frame = ttk.Frame(root)
        table_frame.pack(pady=10)

        # Create the table headers
        headers = ["Ingredient Name", "Have Ingredient ?", "Quantity"]
        for col, header in enumerate(headers):
            header_label = ttk.Label(table_frame, text=header, font=("Helvetica", 12, "bold"))
            header_label.grid(row=0, column=col, padx=5, pady=5)

        # Generate random ingredient data
        ingredients = generate_random_ingredients(10)

        # Create the table rows
        for row, ingredient in enumerate(ingredients, start=1):
            ingredient_label = ttk.Label(table_frame, text=ingredient, font=("Helvetica", 12))
            ingredient_label.grid(row=row, column=0, padx=5, pady=5)

            checkbox_var = tk.IntVar()
            checkbox = ttk.Checkbutton(table_frame, variable=checkbox_var)
            checkbox.grid(row=row, column=1, padx=5, pady=5)

            quantity_entry = ttk.Entry(table_frame, width=8)
            quantity_entry.grid(row=row, column=2, padx=5, pady=5)
            quantity_entry.insert(tk.END, "g")

    elif option == "Option 2":
        label = ttk.Label(root, text="Option 2 is selected", font=("Helvetica", 16))
        label.pack()
        back_button = ttk.Button(root, text="Back", command=go_back)
        back_button.pack()

def go_back():
    # Clear the current window
    for widget in root.winfo_children():
        widget.destroy()

    # Recreate the initial content
    title_label.pack()
    frame1.pack()
    frame2.pack()
    next_button.pack()

def generate_random_ingredients(n):
    ingredients = []
    for _ in range(n):
        ingredient = random.choice(["Ingredient A", "Ingredient B", "Ingredient C", "Ingredient D", "Ingredient E"])
        ingredients.append(ingredient)
    return ingredients

root = tk.Tk()
root.attributes('-fullscreen', True)  # Make the window fullscreen

# Create a canvas with gradient background
canvas = tk.Canvas(root, width=root.winfo_screenwidth(), height=root.winfo_screenheight())
canvas.pack()

# Create gradient background
canvas.create_rectangle(0, 0, root.winfo_screenwidth(), root.winfo_screenheight(), fill="#FF9A8B", width=0)
canvas.create_rectangle(0, 0, root.winfo_screenwidth(), root.winfo_screenheight(), fill="#FF3D68", width=0)

# Create the title label
title_label = ttk.Label(root, text="My Cookbook", font=("Helvetica", 24, "bold"))
title_label.place(relx=0.5, rely=0.2, anchor=tk.CENTER)

# Create the first frame
frame1 = ttk.Frame(root)
frame1.place(relx=0.15, rely=0.4, relwidth=0.3, relheight=0.2)

# Add text to the first frame
label1 = ttk.Label(frame1, text="What can I cook using my ingredients?", font=("Helvetica", 14))
label1.pack()

# Create the checkbox for the first frame
checkbox1_var = tk.IntVar(value=1) # Set the default value to 1 (checked)
checkbox1 = ttk.Checkbutton(frame1, text="Select", variable=checkbox1_var, command=checkbox1_click)
checkbox1.pack()

# Create the second frame
frame2 = ttk.Frame(root)
frame2.place(relx=0.55, rely=0.4, relwidth=0.3, relheight=0.2)

# Add text to the second frame
label2 = ttk.Label(frame2, text="Can I cook this dish using my ingredients?", font=("Helvetica", 14))
label2.pack()

# Create the dropdown menu for the second frame
dropdown_values = ['Option 1', 'Option 2', 'Option 3', 'Option 4', 'Option 5', 'Option 6','Option 7', 'Option 8', 'Option 9', 'Option 10']
dropdown_var = tk.StringVar(value=dropdown_values[0]) # Set the default value
dropdown = ttk.Combobox(frame2, textvariable=dropdown_var, values=dropdown_values, state="readonly", font=("Helvetica", 12))
dropdown.pack()

# Create the checkbox for the second frame
checkbox2_var = tk.IntVar()
checkbox2 = ttk.Checkbutton(frame2, text="Select", variable=checkbox2_var, command=checkbox2_click)
checkbox2.pack()

# Create the "Next" button
next_button = ttk.Button(root, text="Next", command=next_button_click)
next_button.place(relx=0.5, rely=0.7, relwidth=0.1, relheight=0.1)

root.mainloop()
