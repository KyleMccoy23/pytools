

def main():
    from imap_tools import MailBox, NOT
    from os import getenv

    pwd = getenv("EmailCleannerPwd")
    if not pwd:
        exit(1)

    user = "kyle.mccoy0523@gmail.com"

    def threeMonthsAgo():
        import datetime
        from dateutil.relativedelta import relativedelta
        # Get the current date
        today = datetime.datetime.now()

        # Calculate the date 3 months ago
        three_months_ago = today - relativedelta(months=3)


        return datetime.date(three_months_ago.year, three_months_ago.month, three_months_ago.day)

    delList = []

    with MailBox('imap.gmail.com').login(user, pwd) as mailbox:

        date = threeMonthsAgo()

        for msg in mailbox.fetch(NOT(date_gte=date)):
            if '\\Flagged' in msg.flags:
                print("Flagged:",msg.subject, '|', msg.flags)
                continue

            print("To delete:", msg.subject, '|', msg.date_str)
            delList.append(msg.uid)

            mailbox.delete(delList)
            
        print(f"DONE!! | {len(delList)} emails have been deleted")