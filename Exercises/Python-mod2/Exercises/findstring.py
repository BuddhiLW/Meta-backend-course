names = ["Al", "Bo", "Chi", "Ma"]
def ispresent(person):
    if person in names:
        return True
    else:
        return False

def nodigit(person):
    if person.isaplha():
        return True
    else:
        return False
