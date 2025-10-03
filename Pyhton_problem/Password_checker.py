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


def password_checker_2_point_0(password):
    score = 0
    feedback = []
    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password should be at least 8 characters long")
    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one digit")
    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one uppercase letter")
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one lowercase letter")
    if any(char in '@#$%^&*()!=_-'  for char in password):
        score += 1
    else:
        feedback.append("Password should contain at least one special character (@#$%^&*()!=_-)")
    return score,feedback
password = input("Enter your password: ")
score,feedback = password_checker_2_point_0(password)
print(f"Password score: {score}/5")
if feedback:
    print("Suggestions to improve your password")
    for ch in feedback:
        print(f"- {ch}")
else:
    print(f"Your password {password} is strong!")        

