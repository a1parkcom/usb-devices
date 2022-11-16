from dataclasses import dataclass


@dataclass
class PaperStatus:
    paper: bool = True
    not_paper: bool = False

    paper_abundance: bool = True
    not_paper_abundance: bool = False

    ticket_present: bool = True
    not_ticket_present: bool = False

    virtual: bool = True
    not_virtual: bool = False


@dataclass
class Paper:
    paper: bool = True
    abundance: bool = True
    ticket: bool = True
    virtual: bool = True
