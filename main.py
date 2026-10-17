from pyscript import document, display

# making sets for each grade level


grade_7 = {'Viktoria Camitan', 'Johanna Ramos'}
grade_8 = {'Precious Dolormenta', 'Isabella Acosta'}
grade_9 = {'Kailey Gayas', 'Vyelle Bunag'}
grade_10 = {'Rianne Nicolle', 'Megan Gacita'}

# combining the sets using union 

members = grade_7 | grade_8 | grade_9 | grade_10

# displaying the total of members
def show_members(message=""):
     members_list = "<br>".join(sorted(members))
     document.getElementById("output1").innerHTML = f"LIST OF MEMBERS:<br>{members_list}<br>NUMBER OF TOTAL MEMBERS: {len(members)}"

# adding new club member

def invite_members(e):
    first_name = document.getElementById('first_name').value.strip().title()
    last_name = document.getElementById('last_name').value.strip().title()
    full_name = first_name + " " + last_name

# adding new member using union 

    members.add(full_name)
    message = f"{full_name} is now added to the Rainbow Catering Club imnida!"
    show_members(message)

    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""

show_members()







    