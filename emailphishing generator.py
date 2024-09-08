import random

def generate_phishing_email():
    """
    Generates a sample phishing email with random elements.
    """
    subjects = [
        "Urgent: Account Verification Required",
        "Action Needed: Update Your Payment Information",
        "Security Alert: Unusual Activity Detected",
        "Your Account Has Been Suspended"
    ]

    bodies = [
        "Dear user, your account has been compromised. Please provide your login credentials immediately to secure your account.",
        "We have detected suspicious activity on your account. Click the link below to verify your information and prevent suspension.",
        "Your account will be locked if you do not update your payment details within 24 hours. Click the link below to update.",
        "Your recent transaction could not be processed. Please confirm your payment information by clicking the link below."
    ]

    subject = random.choice(subjects)
    body = random.choice(bodies)

    return subject, body

# Example usage
if __name__ == "__main__":
    subject, body = generate_phishing_email()
    print(f"Subject: {subject}")
    print(f"Body: {body}")
