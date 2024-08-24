class Clients:
    def __init__(
            self, 
            id: int,
            first_name: str,
            last_name: str,
            cpf: str,
            address: str,
            telephone: str,
            birth_date: str
        ) -> None:
        self.id = id
        self.first_name = first_name
        self.lasit_name = last_name
        self.cpf = cpf
        self.address = address 
        self.telephone = telephone 
        self.birth_date = birth_date