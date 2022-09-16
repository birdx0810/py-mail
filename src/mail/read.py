import imaplib

DEFAULT_IMAP_HOST = "outlook.office365.com"
DEFAULT_IMAP_PORT = 993
DEFAULT_EMAIL = ""
DEFAULT_PASS = ""


def read_mail(host, email, port, password, interval=60):
    """

    Args:
        host (str): the mail server host
        port (int): the mail server port
        email (str): the email account
        password (str): the password for logging in to email
        interval (int): interval for reading mail (minutes)

    Returns:
        list of dict: A list of emails
    """
    # Connect to IMAP Server
    imap = imaplib.IMAP4_SSL(host=host, port=port)
    imap.authenticate("XOAUTH2", )
    # Login to IMAP Server
    imap.login(user=email, password=password)

    # Get mail from inbox
    status, mail = imap.select("INBOX")

    print(f"Status: {status}")
    print(f"# of Mail: {len(mail)}")


if __name__ == "__main__":
    read_mail(
        host=DEFAULT_IMAP_HOST,
        port=DEFAULT_IMAP_PORT,
        email=DEFAULT_EMAIL,
        password=DEFAULT_PASS,
    )
