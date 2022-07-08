import string
import random
from typing import List
from dataclasses import dataclass, field
from abc import ABC, abstractmethod

def generate_id(length=8):
    """helper function for generating an id."""
    return ''.join(random.choices(string.ascii_uppercase, k=length))


@dataclass
class SupportTicket:
    id: str = field(init=False)
    customer: str
    issue: str

    def __post_init__(self):
        self.id = generate_id()


class TicketOrderingStrategy(ABC):
    @abstractmethod
    def create_ordering(self, tickets_list: List[SupportTicket]) -> List[SupportTicket]:
        pass

class FifoOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets_list: List[SupportTicket]) -> List[SupportTicket]:
        return tickets_list.copy()

class FiloOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets_list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = tickets_list.copy()
        list_copy.reverse()
        return list_copy

class RandomOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets_list: List[SupportTicket]) -> List[SupportTicket]:
        list_copy = tickets_list.copy()
        random.shuffle(list_copy)
        return list_copy

class BlackHoleOrderingStrategy(TicketOrderingStrategy):
    def create_ordering(self, tickets_list: List[SupportTicket]) -> List[SupportTicket]:
        return []


@dataclass
class CustomerSupport:
    tickets: List[SupportTicket] = field(default_factory=list)

    def create_ticket(self, customer, issue):
        """Add a new ticket to the list of tickets to process."""
        self.tickets.append(SupportTicket(customer=customer, issue=issue))

    def process_tickets(self, processing_strategy: TicketOrderingStrategy):
        """Process the tickets by a given type of strategy."""
        tickets_list = processing_strategy.create_ordering(self.tickets)
        
        if len(tickets_list) == 0:
            print("There are no tickets to process. Well done!")
            return

        for ticket in tickets_list:
            self.__process_ticket(ticket)

    def __process_ticket(self, ticket: SupportTicket):
        print("==================================")
        print(f"Processing ticket id: {ticket.id}")
        print(f"Customer: {ticket.customer}")
        print(f"Issue: {ticket.issue}")
        print("==================================")

if __name__ == '__main__':
    cs = CustomerSupport()
    cs.create_ticket(customer='Davi', issue='Fan')
    cs.create_ticket(customer='Segundo', issue='Battery')
    cs.create_ticket(customer='Pinheiro', issue='Speakers')
    
    cs.process_tickets(processing_strategy=RandomOrderingStrategy())
