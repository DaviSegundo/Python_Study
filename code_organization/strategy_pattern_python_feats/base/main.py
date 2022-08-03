"""
Support ticket handling example.
"""

from app import CustomerSupport
from ticket import SupportTicket


def main():
    # create the application
    app = CustomerSupport()

    app.add_ticket(SupportTicket("Davi", "Fan"))
    app.add_ticket(SupportTicket("Segundo", "Speaker"))
    app.add_ticket(SupportTicket("Pinheiro", "Battery"))

    app.process_tickets("random")


if __name__ == '__main__':
    main()