import random
from typing import List
from abc import ABC, abstractmethod
from ticket import SupportTicket


class TicketOrderingStrategy(ABC):
    """Interface to define structure of ordering strategy."""

    @abstractmethod
    def create_ordering(self, tickets: List[SupportTicket]) -> List[SupportTicket]:
        """Returns an ordered list of tickets."""


class FifoOrderingStrategy(TicketOrderingStrategy):

    def create_ordering(self, tickets: List[SupportTicket]) -> List[SupportTicket]:
        return tickets.copy()

class FiloOrderingStrategy(TicketOrderingStrategy):

    def create_ordering(self, tickets: List[SupportTicket]) -> List[SupportTicket]:
        return list(reversed(tickets.copy()))

class RandomOrderingStrategy(TicketOrderingStrategy):

    def create_ordering(self, tickets: List[SupportTicket]) -> List[SupportTicket]:
        random_list = tickets.copy()
        random.shuffle(random_list)
        return random_list


class CustomerSupport:

    def __init__(self) -> None:
        self.tickets: List[SupportTicket] = []

    def add_ticket(self, ticket: SupportTicket):
        self.tickets.append(ticket)

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        ordered_list = processing_strategy.create_ordering(self.tickets)

        if len(ordered_list) == 0:
            print("There are no tickets to process. Well done!")
            return
        
        for ticket in ordered_list:
            ticket.process()

        self.tickets = []