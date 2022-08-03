"""
Support ticket handling example.
"""

from app import CustomerSupport, FifoOrderingStrategy, FiloOrderingStrategy, RandomOrderingStrategy
from ticket import SupportTicket


def main():
    # create the application
    app = CustomerSupport()
    strategy = FifoOrderingStrategy()

    app.add_ticket(SupportTicket("Davi", "Fan"))
    app.add_ticket(SupportTicket("Segundo", "Speaker"))
    app.add_ticket(SupportTicket("Pinheiro", "Battery"))

    app.process_tickets(strategy)


if __name__ == '__main__':
    main()