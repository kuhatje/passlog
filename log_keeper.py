import tkinter
from datetime import datetime

# Log file to be written to.
file = "C://core_/Posts/logs.log"

# The user cannot enter anything longer than 33 characters, and no more than 20 in the application name box.
entry_character_limit = 33
application_name_limit = 20

# Get the date and time(24h clock).
now = datetime.now()

# Convert the 24h time into 12h time.
if now.hour > 12:
    hour = str(now.hour - 12)
    half = 'PM'
else:
    hour = (str(now.hour))
    half = 'AM'

# If keep the number of minutes at 2 characters.
if now.minute < 10:
    minute = '0' + str(now.minute)

else:
    minute = now.minute

# Formatting for the date and time
date = ("{}-{}-{}".format(now.year, now.month, now.day))
time = ("{:>2}:{}".format(hour, minute))

root = tkinter.Tk()
root.title("log_keeper")


# Screen for the email change option in modify mode.
def modify_email():
    # Set the E.N.A.P option to email.
    enap_mode.set("email")

    # Remove any widgets from other E.N.A.P options.
    for widget in modify_mode_name_widgets:
        widget.grid_forget()
    for widget in modify_mode_alias_widgets:
        widget.grid_forget()
    for widget in modify_mode_password_widgets:
        widget.grid_forget()

    # Account name entry box/label is on row 3(fourth row).
    modify_account_name_label.grid(row=3, column=0)
    modify_account_name_entry.grid(row=3, column=1)

    # Old email entry box/label is on row 4(fifth row).
    old_email_label.grid(row=4, column=0)
    old_email_entry.grid(row=4, column=1)
    # New email entry box/label is on row 5(sixth row).
    new_email_label.grid(row=5, column=0)
    new_email_entry.grid(row=5, column=1)

    # Submit button is on row 6(seventh row)
    submit_button.grid(row=6, column=0)


# Screen for the name change option in modify mode.
def modify_name():
    # Set the E.N.A.P option to name.
    enap_mode.set("name")

    # Remove any widgets from other E.N.A.P options.
    for widget in modify_mode_email_widgets:
        widget.grid_forget()
    for widget in modify_mode_alias_widgets:
        widget.grid_forget()
    for widget in modify_mode_password_widgets:
        widget.grid_forget()

        # Account name entry box/label is on row 3(fourth row).
        modify_account_name_label.grid(row=3, column=0)
        modify_account_name_entry.grid(row=3, column=1)

        # Old name entry box/label is on row 4(fifth row).
        old_name_label.grid(row=4, column=0)
        old_name_entry.grid(row=4, column=1)
        # New name entry box/label is on row 5(sixth row).
        new_name_label.grid(row=5, column=0)
        new_name_entry.grid(row=5, column=1)

        # Submit button is on row 6(seventh row)
        submit_button.grid(row=6, column=0)


# Screen for the alias change option in modify mode.
def modify_alias():
    # Set the E.N.A.P option to alias.
    enap_mode.set("alias")

    # Remove any widgets from other E.N.A.P options.
    for widget in modify_mode_email_widgets:
        widget.grid_forget()
    for widget in modify_mode_name_widgets:
        widget.grid_forget()
    for widget in modify_mode_password_widgets:
        widget.grid_forget()

        # Account name entry box/label is on row 3(fourth row).
        modify_account_name_label.grid(row=3, column=0)
        modify_account_name_entry.grid(row=3, column=1)

        # Old alias entry box/label is on row 4(fifth row).
        old_alias_label.grid(row=4, column=0)
        old_alias_entry.grid(row=4, column=1)
        # New alias entry box/label is on row 5(sixth row).
        new_alias_label.grid(row=5, column=0)
        new_alias_entry.grid(row=5, column=1)

        # Submit button is on row 6(seventh row)
        submit_button.grid(row=6, column=0)


# Screen for the password change option in modify mode.
def modify_password():
    # Set the E.N.A.P option to password.
    enap_mode.set("password")

    # Remove any widgets from other E.N.A.P options.
    for widget in modify_mode_email_widgets:
        widget.grid_forget()
    for widget in modify_mode_name_widgets:
        widget.grid_forget()
    for widget in modify_mode_alias_widgets:
        widget.grid_forget()

    # Account name entry box/label is on row 3(fourth row).
    modify_account_name_label.grid(row=3, column=0)
    modify_account_name_entry.grid(row=3, column=1)

    # Submit button is on row 4(fifth row).
    submit_button.grid(row=4, column=0)


# Screen on create mode.
def create_mode():
    # Set the mode to create.
    mode.set("create")

    # Remove any widgets from other modes.
    for widget in modify_mode_widgets:
        widget.grid_forget()
    for widget in delete_mode_widgets:
        widget.grid_forget()

    # email entry widget is on row 2(third row).
    email_label.grid(row=2, column=0)
    email_entry.grid(row=2, column=1)

    # name entry widget is on row 3(fourth row).
    name_label.grid(row=3, column=0)
    name_entry.grid(row=3, column=1)

    # alias entry widget is on row 4(fifth row).
    alias_label.grid(row=4, column=0)
    alias_entry.grid(row=4, column=1)

    # Put the submit button on the row 5(sixth row).
    submit_button.grid(row=5, column=0)


# Screen on modify mode.
def modify_mode():
    # Set the mode to modify.
    mode.set("modify")

    # Remove any widgets from other modes.
    for widget in create_mode_widgets:
        widget.grid_forget()
    for widget in delete_mode_widgets:
        widget.grid_forget()

    # E.N.A.P selection radiobuttons are positioned on row 2(third row).
    email_change.grid(row=2, column=0)
    name_change.grid(row=2, column=1)
    alias_change.grid(row=2, column=2)
    password_change.grid(row=2, column=3)


# Screen on remove mode.
def remove_mode():
    # Set the mode to remove.
    mode.set("remove")

    # Remove any widgets from other modes.
    for widget in create_mode_widgets:
        widget.grid_forget()
    for widget in modify_mode_widgets:
        widget.grid_forget()

    # Deleted account entry widgets are on row 2(third row).
    deleted_account_label.grid(row=2, column=0)
    deleted_account_entry.grid(row=2, column=1)

    # Put the submit button on the row 3(fourth row).
    submit_button.grid(row=3, column=0)


# When the user clicks the submit button.
def submit():
    # Line is the a single line output text to be logged.
    line = str
    application_name = application_name_entry.get()
    if len(application_name) > application_name_limit:
        # print("The entered Site/Application name is too long to be logged properly.")
        raise SystemExit

    if mode.get() == "create":
        email = email_entry.get()
        name = name_entry.get()
        alias = alias_entry.get()

        # Format the email entry
        if len(email) == 0:
            email = "None"

        elif len(email) > entry_character_limit:
            # print("The entered email is too long to be logged properly.")
            raise SystemExit

        # Format the name entry
        if len(name) == 0:
            name = "None"

        elif len(name) > entry_character_limit:
            # print("The entered name is too long to be logged properly.")
            raise SystemExit

        # Format the alias entry
        if len(alias) == 0:
            alias = "None"

        elif len(alias) > entry_character_limit:
            # print("The entered alias is too long to be logged properly.")
            raise SystemExit

        # Format the line to be entered.
        # Note: email entry on create mode is not nested in quotations, unlike name and alias.
        line = "{:<10} {:5}  {}: --> Create:  {:24}{:37}name {:39}alias {}".format(date, time, half,
                                                                                   application_name,
                                                                                   email,
                                                                                   '"' + name + '"',
                                                                                   '"' + alias + '"')

    elif mode.get() == "modify":
        if enap_mode.get() == "email":
            account_name = modify_account_name_entry.get()
            old_email = old_email_entry.get()
            new_email = new_email_entry.get()

            # Format the account name entry
            if len(account_name) == 0:
                account_name = "None"

            elif len(account_name) > entry_character_limit:
                # print("The entered account name is too long to be logged properly.")
                raise SystemExit

            # Format the old email entry
            if len(old_email) == 0:
                old_email = "None"

            elif len(old_email) > entry_character_limit:
                # print("The entered old email is too long to be logged properly.")
                raise SystemExit

            # Format the new email entry
            if len(new_email) == 0:
                new_email = "None"

            elif len(new_email) > entry_character_limit:
                # print("The entered new email is too long to be logged properly.")
                raise SystemExit

            line = "{:<10} {:5}  {}: --> Modify:  {:24}account {:37}email   {:37}to         {}".format(date, time, half,
                                                                                                       application_name + ":",
                                                                                                       '"' + account_name + '":',
                                                                                                       '"' + old_email + '"',
                                                                                                       '"' + new_email + '"')

        elif enap_mode.get() == "name":
            account_name = modify_account_name_entry.get()
            old_name = old_name_entry.get()
            new_name = new_name_entry.get()

            # Format the account name entry
            if len(account_name) == 0:
                account_name = "None"

            elif len(account_name) > entry_character_limit:
                # print("The entered account name is too long to be logged properly.")
                raise SystemExit

            # Format the old name entry
            if len(old_name) == 0:
                old_name = "None"

            elif len(old_name) > entry_character_limit:
                # print("The entered old name is too long to be logged properly.")
                raise SystemExit

            # Format the new name entry
            if len(new_name) == 0:
                new_name = "None"

            elif len(new_name) > entry_character_limit:
                # print("The entered new name is too long to be logged properly.")
                raise SystemExit

            line = "{:<10} {:5}  {}: --> Modify:  {:24}account {:37}name   {:37}to         {}".format(date, time, half,
                                                                                                      application_name + ":",
                                                                                                      '"' + account_name + '":',
                                                                                                      '"' + old_name + '"',
                                                                                                      '"' + new_name + '"')

        elif enap_mode.get() == "alias":
            account_name = modify_account_name_entry.get()
            old_alias = old_alias_entry.get()
            new_alias = new_alias_entry.get()

            # Format the account name entry
            if len(account_name) == 0:
                account_name = "None"

            elif len(account_name) > entry_character_limit:
                # print("The entered account name is too long to be logged properly.")
                raise SystemExit

            # Format the old alias entry
            if len(old_alias) == 0:
                old_alias = "None"

            elif len(old_alias) > entry_character_limit:
                # print("The entered old alias is too long to be logged properly.")
                raise SystemExit

            # Format the new alias entry
            if len(new_alias) == 0:
                new_alias = "None"

            elif len(new_alias) > entry_character_limit:
                # print("The entered new alias is too long to be logged properly.")
                raise SystemExit

            line = "{:<10} {:5}  {}: --> Modify:  {:24}account {:37}alias   {:37}to         {}".format(date, time, half,
                                                                                                       application_name + ":",
                                                                                                       '"' + account_name + '":',
                                                                                                       '"' + old_alias + '"',
                                                                                                       '"' + new_alias + '"')

        elif enap_mode.get() == "password":
            account_name = modify_account_name_entry.get()

            # Format the account name entry
            if len(account_name) == 0:
                account_name = "None"

            elif len(account_name) > entry_character_limit:
                # print("The entered account name is too long to be logged properly.")
                raise SystemExit

            line = "{:<10} {:5}  {}: --> Modify:  {:24}account {:37}password changed".format(date, time, half,
                                                                                             application_name + ":",
                                                                                             '"' + account_name + '":')

    elif mode.get() == "remove":
        deleted_account_name = deleted_account_entry.get()

        # Format the deleted account name entry
        if len(deleted_account_name) == 0:
            deleted_account_name = "None"

        elif len(deleted_account_name) > entry_character_limit:
            # print("The entered account name is too long to be logged properly.")
            raise SystemExit

        line = "{:<10} {:5}  {}: --> Remove:  {:24}deleted account                      {}".format(date, time, half,
                                                                                                   application_name,
                                                                                                   deleted_account_name)

    # Print the line.
    # print(line)

    # Write the line to the file.
    f = open(file, "a")
    f.write(line + '\n')
    # Program quits when submit button is hit.
    raise SystemExit


# Widgets for the application name form.
application_name_label = tkinter.Label(root, text="Site/Application name?>")
application_name_entry = tkinter.Entry(root, width=50)

# Default mode is modify.
mode = tkinter.StringVar(value="0")

# radiobutton widgets for the mode selection
create_option = tkinter.Radiobutton(root, text="Create", variable=mode, value="create", command=lambda: create_mode())
modify_option = tkinter.Radiobutton(root, text="Modify", variable=mode, value="modify", command=lambda: modify_mode())
remove_option = tkinter.Radiobutton(root, text="Remove", variable=mode, value="remove", command=lambda: remove_mode())

# Mode option radiobuttons are lined up in row 1(second row).
create_option.grid(row=1, column=0)
modify_option.grid(row=1, column=1)
remove_option.grid(row=1, column=2)

# Button widget for the submit button
submit_button = tkinter.Button(root, text="Submit and write changes", command=submit)

# Application name widgets are lined up in row 0.
application_name_label.grid(row=0, column=0)
application_name_entry.grid(row=0, column=1)

# Widgets for the create mode.
# email label and entry.
email_label = tkinter.Label(root, text="Email: ")
email_entry = tkinter.Entry(root, width=50)

# name label and entry.
name_label = tkinter.Label(root, text="Name: ")
name_entry = tkinter.Entry(root, width=50)

# Alias label and entry.
alias_label = tkinter.Label(root, text="Alias: ")
alias_entry = tkinter.Entry(root, width=50)

# Submit button is included in all because its location is mode-specific.
create_mode_widgets = [email_label, email_entry, name_label, name_entry, alias_label, alias_entry, submit_button]

# Widgets for the modify mode.
# Variable for the kind of modification, E.N.A.P(email/name/alias/password change)
enap_mode = tkinter.StringVar(value="0")
# Radiobuttons for E.N.A.P selection
email_change = tkinter.Radiobutton(root, text="Email change",
                                   variable=enap_mode, value="email", command=lambda: modify_email())
name_change = tkinter.Radiobutton(root, text="Name change",
                                  variable=enap_mode, value="name", command=lambda: modify_name())
alias_change = tkinter.Radiobutton(root, text="Alias change",
                                   variable=enap_mode, value="alias", command=lambda: modify_alias())
password_change = tkinter.Radiobutton(root, text="Password change",
                                      variable=enap_mode, value="password", command=lambda: modify_password())

# Widgets for the account name entry
modify_account_name_label = tkinter.Label(root, text="Account: ")
modify_account_name_entry = tkinter.Entry(root, width=50)

# Widgets for the modify email option.
old_email_label = tkinter.Label(root, text="Old email(case sensitive): ")
old_email_entry = tkinter.Entry(root, width=50)
new_email_label = tkinter.Label(root, text="New email(case sensitive): ")
new_email_entry = tkinter.Entry(root, width=50)

# Widgets for the modify name option.
old_name_label = tkinter.Label(root, text="Old name(case sensitive): ")
old_name_entry = tkinter.Entry(root, width=50)
new_name_label = tkinter.Label(root, text="New name(case sensitive): ")
new_name_entry = tkinter.Entry(root, width=50)

# Widgets for the modify alias option.
old_alias_label = tkinter.Label(root, text="Old alias(case sensitive): ")
old_alias_entry = tkinter.Entry(root, width=50)
new_alias_label = tkinter.Label(root, text="New alias(case sensitive): ")
new_alias_entry = tkinter.Entry(root, width=50)

# A list of every widget fot the modify mode. These are useful when removing sets of widgets from the screen.
modify_mode_widgets = [email_change, name_change, alias_change, password_change,
                       old_email_label, old_email_entry, new_email_label, new_email_entry,
                       old_name_label, old_name_entry, new_name_label, new_name_entry,
                       old_alias_label, old_alias_entry, new_alias_label, new_alias_entry,
                       modify_account_name_label, modify_account_name_entry, submit_button]

# Lists of widgets for each option in the modify mode.
modify_mode_email_widgets = [old_email_label, old_email_entry, new_email_label, new_email_entry,
                             modify_account_name_label, modify_account_name_entry, submit_button]
modify_mode_name_widgets = [old_name_label, old_name_entry, new_name_label, new_name_entry, modify_account_name_label,
                            modify_account_name_entry, submit_button]
modify_mode_alias_widgets = [old_alias_label, old_alias_entry, new_alias_label, new_alias_entry,
                             modify_account_name_label, modify_account_name_entry, submit_button]
modify_mode_password_widgets = [modify_account_name_label, modify_account_name_entry, submit_button]

# Widgets for the remove mode.
deleted_account_label = tkinter.Label(root, text="Name of deleted account: ")
deleted_account_entry = tkinter.Entry(root, width=50)

delete_mode_widgets = [deleted_account_label, deleted_account_entry, submit_button]

root.mainloop()
