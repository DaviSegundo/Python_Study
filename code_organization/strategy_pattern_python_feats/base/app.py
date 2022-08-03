import random
from typing import List
from ticket import SupportTicket


class CustomerSupport:

    def __init__(self) -> None:
        self.tickets: List[SupportTicket] = []

    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)

    def process_tickets(self, processing_strategy: str = "fifo"):
        if len(self.tickets) == 0:
            print("There are no tickets to process. Well done!")
            return
        
        if processing_strategy == "fifo":
            for ticket in self.tickets:
                ticket.process()
        elif processing_strategy == "filo":
            for ticket in reversed(self.tickets):
                ticket.process()
        elif processing_strategy == "random":
            random.shuffle(self.tickets)
            for ticket in self.tickets:
                ticket.process()

        self.tickets = []