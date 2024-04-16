import random
import string


# class variables
class Ticket:
    ticketCounter = 2000
    openTickets = 0
    resolvedTickets = 0

    # ticket attributes
    def __init__(self, staffID, creatorName, contactEmail, desc):
        self.ticketNo = Ticket.ticketCounter
        Ticket.ticketCounter += 1
        self.staffID = staffID
        self.creatorName = creatorName
        self.contactEmail = contactEmail
        self.desc = desc
        self.response = "Not Yet Provided"
        self.status = "Open"
        Ticket.openTickets += 1
        self.password = None

    # displaying ticket info
    def displayTicket(self):
        print(f"Ticket Number: {self.ticketNo}")
        print(f"Ticket Creator: {self.creatorName}")
        print(f"Staff ID: {self.staffID}")
        print(f"Email Address: {self.contactEmail}")
        print(f"Description: {self.desc}")
        print(f"Response: {self.response}")
        if self.password:
            print(f"Password: {self.password}")
        print(f"Ticket Status: {self.status}\n")

    # submitting response
    def submitResponse(self, response):
        self.response = response
        self.status = "Closed"
        Ticket.openTickets -= 1
        Ticket.resolvedTickets += 1

    # resolving password change request and closing ticket
    def resolvePC(self):
        if "password change" in self.desc.lower():  # checking for lowercase
            newPassword = self.generatePassword()
            self.response = f"Password changed to: {newPassword}"
            self.status = "Closed"
            Ticket.openTickets -= 1
            Ticket.resolvedTickets += 1
            self.password = newPassword

        # generating a new password
    def generatePassword(self):
        # extracting the first two characters of staffID and the first three characters of the ticket creatorName
        staffID_chars = self.staffID[:2]
        creatorName_chars = self.creatorName[:3]

        # generating a random 3-character string for additional complexity
        random_chars = ''.join(random.choices(string.ascii_letters, k=3))

        # concatenation
        newPassword = staffID_chars + creatorName_chars + random_chars

        return newPassword

    # reopening closed ticket
    def reopenTicket(self):
        self.status = "Reopened"
        Ticket.openTickets += 1
        Ticket.resolvedTickets -= 1

    # displaying ticket statistics
    @classmethod
    def ticket_stats(cls):
        return f"Tickets Created: {cls.ticketCounter - 2000}\nTickets Resolved: {cls.resolvedTickets}\nTickets To Solve: {cls.openTickets}"


# MAIN PROGRAM
def main():
    tickets = []

    while True:
        # Display menu for user interaction
        print("\nMenu:")
        print("1. Create Ticket")
        print("2. Resolve Ticket")
        print("3. Change Password (if Password Change Request)")
        print("4. View All Tickets")
        print("5. View Open Tickets")
        print("6. View Closed Tickets")
        print("0. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            creatorName = input("Enter Creator Name: ")
            staffID = input("Enter Staff ID: ")
            contactEmail = input("Enter Email Address: ")
            desc = input("Enter Description: ")

            tickets.append(Ticket(staffID, creatorName, contactEmail, desc))
            print("Ticket created successfully.")
        elif choice == "2":
            for i, ticket in enumerate(tickets, start=1):
                print(f"{i}. Ticket Number: {ticket.ticketNo} (Status: {ticket.status})")
            ticket_index = int(input("Enter the index of the ticket to resolve: ")) - 1
            if 0 <= ticket_index < len(tickets):
                response = input("Enter response for the selected ticket: ")
                tickets[ticket_index].submitResponse(response)
                print("Ticket resolved successfully.")
            else:
                print("Invalid ticket index.")
        elif choice == "3":
            print("Open Tickets:\n")
            for i, ticket in enumerate(tickets, start=1):
                if ticket.status == "Open":
                    print(f"{i}. Ticket Number: {ticket.ticketNo} (Status: {ticket.status})")

            ticket_index = int(input("Enter the index of the Password Change Request to change the password: ")) - 1
            if 0 <= ticket_index < len(tickets):
                tickets[ticket_index].resolvePC()
                print("Password changed successfully.")
            else:
                print("Invalid ticket index.")
        elif choice == "4":
            print("\nAll Tickets:")
            for ticket in tickets:
                ticket.displayTicket()
            print("\nTicket Statistics:")
            print(Ticket.ticket_stats())
        elif choice == "5":
            print("\nOpen Tickets:\n")
            for ticket in tickets:
                if ticket.status == "Open":
                    ticket.displayTicket()
            print("\nTicket Statistics (Before Resolution and Password Change):\n")
            print(Ticket.ticket_stats())
        elif choice == "6":
            print("\nClosed Tickets:\n")
            for ticket in tickets:
                if ticket.status == "Closed":
                    ticket.displayTicket()
            print("\nTicket Statistics (Before Resolution and Password Change):\n")
            print(Ticket.ticket_stats())
        elif choice == "0":
            # exit
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    main()
