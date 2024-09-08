import re

# Define some common phishing keywords
PHISHING_KEYWORDS = [
    'urgent', 'verify', 'account suspended', 'login credentials', 
    'update your information', 'security alert', 'suspicious activity'
]

def is_phishing_email(subject, body):
    """
    Simple function to detect phishing emails based on keywords in the subject and body.
    """
    # Convert subject and body to lower case for matching
    subject = subject.lower()
    body = body.lower()

    # Check if any phishing keyword is in the subject or body
    for keyword in PHISHING_KEYWORDS:
        if keyword in subject or keyword in body:
            return True
    return False

# Example usage
if __name__ == "__main__":
    email_subject = "Urgent: Update Your Account Information"
    email_body = "Dear user, please verify your account details immediately to avoid suspension."

    if is_phishing_email(email_subject, email_body):
        print("This email might be a phishing attempt.")
    else:
        print("This email appears to be legitimate.")
