def password_checker(password):
    if len(password) == 0:
        return "Password should not be empty"
    if len(password) < 8:
        return "Password should be at least 8 characters long"
    if not any(char.isdigit() for char in password):
        return "Password should contain at least one digit"
    if not any(char.isupper() for char in password):
        return "Password should contain at least one uppercase letter"
    if not any(char.islower() for char in password):
        return "Password should contain at least one lowercase letter"
    if not any(char in '@#$%^&*()!=_-'  for char in password):
        return "Password should contain at least one special character (@#$%^&*()!=_-)"
    return f"{password} Password is valid"
password = input("Enter your password: ")
result = password_checker(password)
print(result)


def passwordChecker(password):
    score = 0
    positive_feedback = []
    negative_feedback = []
    if(len(password) >= 8):
        score += 1
        positive_feedback.append("Password length is valid")
    else:
        negative_feedback.append("Password length is not valid")
    if any(char.isdigit() for char in password):
        score += 1
        positive_feedback.append("Password contains at least one digit")
    else:
        negative_feedback.append("Password does not contain any digit")
    if any(char.isupper() for char in password):
        score += 1
        positive_feedback.append("Password contains at least one uppercase letter")
    else:
        negative_feedback.append("Password does not contain any uppercase letter")
    if any(char.islower() for char in password):
        score += 1
        positive_feedback.append("Password contains at least one lowercase letter")
    else:
        negative_feedback.append("Password does not contain any lowercase letter")
    if any(char in '@#$%^&*()!=_-' for char in password):
        score += 1
        positive_feedback.append("Password contains at least one special character")
    else:
        negative_feedback.append("Password does not contain any special character")
    return score,positive_feedback,negative_feedback
password = input("Enter the Password:")
score,positive_feedback,negative_feedback = passwordChecker(password)
print("Password Strength:")
print("----------------")
print(f"Score:{score}/5")
print("----------------")
if positive_feedback:
    print("Positive Feedback:")
    for i in positive_feedback:
        print(f"- {i}")
    print("----------------")
if negative_feedback:
    print("Negative Feedback:")
    for i in negative_feedback:
        print(f"- {i}")
    print("----------------")
