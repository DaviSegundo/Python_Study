import random
from typing import Callable, List
from ticket import SupportTicket


TicketOrderingStrategy = Callable[[List[SupportTicket]], List[SupportTicket]]

def fifo_strategy(tickets: List[SupportTicket]) -> List[SupportTicket]:
    return tickets.copy()

def filo_strategy(tickets: List[SupportTicket]) -> List[SupportTicket]:
    return list(reversed(tickets.copy()))

def random_strategy(tickets: List[SupportTicket]) -> List[SupportTicket]:
    random_list = tickets.copy()
    random.shuffle(random_list)
    return random_list


class CustomerSupport:

    def __init__(self) -> None:
        self.tickets: List[SupportTicket] = []

    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        ordered_list = processing_strategy(self.tickets)

        if len(ordered_list) == 0:
            print("There are no tickets to process. Well done!")
            return
        
        for ticket in ordered_list:
            ticket.process()

        self.tickets = []