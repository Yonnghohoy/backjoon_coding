import re

def solution(new_id):
    print(new_id)
    new_id = new_id.lower()
    print(new_id)
    new_id = re.sub("[^a-z0-9-_.]", "", new_id)
    print(new_id)
    new_id = re.sub("\.+", ".", new_id)
    print(new_id)
    new_id = re.sub("^[.]|[.]$", "", new_id)
    print(new_id)
    new_id = "a" if len(new_id) == 0 else new_id
    new_id = new_id[:15] if len(new_id) > 15 else new_id
    new_id = re.sub("[.]$", "", new_id)
    # return answer

solution("...!@BaT#*..y.abcdefghijklm")