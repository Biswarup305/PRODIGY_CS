import re

def check_password_strength(password):
    # Define regex patterns for character types
    uppercase_pattern = re.compile(r'[A-Z]')
    lowercase_pattern = re.compile(r'[a-z]')
    digit_pattern = re.compile(r'\d')
    special_char_pattern = re.compile(r'[!@#$%^&*()\-_=+[\]{};:\'",.<>/?\\|`~]')

    # Check length
    if len(password) < 12:
        return "Very Weak", "Password should be at least 12 characters long."

    # Check uppercase, lowercase, digits, and special characters
    criteria_met = 0
    if uppercase_pattern.search(password):
        criteria_met += 1
    if lowercase_pattern.search(password):
        criteria_met += 1
    if digit_pattern.search(password):
        criteria_met += 1
    if special_char_pattern.search(password):
        criteria_met += 1

    # Calculate rating based on criteria met
    if criteria_met == 4:
        rating = "Excellent"
    elif criteria_met == 3:
        rating = "Strong"
    elif criteria_met == 2:
        rating = "Moderate"
    elif criteria_met == 1:
        rating = "Weak"
    else:
        rating = "Very Weak"

    # Check for consecutive characters
    if re.search(r'(.)\1\1', password):
        return rating, "Password should not contain consecutive characters."

    # Check for sequential characters
    if re.search(r'(?=012|123|234|345|456|567|678|789|890|098|987|876|765|654|543|432|321|210)', password):
        return rating, "Password should not contain sequential characters."

    return rating, "Password meets all criteria for strength."

def print_password_tips():
    tips = [
        "Here are some quick tips for creating a secure password:",
        "1. Length: Aim for at least 12 characters.",
        "2. Mix Characters: Use a combination of uppercase, lowercase, numbers, and symbols.",
        "3. Avoid Common Words: Don't use easily guessable information.",
        "4. No Personal Info: Avoid using names, birthdays, or personal details.",
        "5. Use Passphrases: Consider combining multiple words or a sentence.",
        "6. Unique for Each Account: Don't reuse passwords across multiple accounts.",
        "7. Regular Updates: Change passwords periodically.",
        "8. Enable 2FA: Use Two-Factor Authentication where possible.",
        "9. Be Wary of Phishing: Avoid entering passwords on suspicious sites.",
        "10. Password Manager: Consider using one for secure and unique passwords."
    ]
    for tip in tips:
        print(tip)

def main():
    print_password_tips()
    password = input("\nEnter your password: ")
    rating, feedback = check_password_strength(password)
    print(f"\nRating: {rating}")
    print(f"Feedback: {feedback}")

if __name__ == "__main__":
    main()
