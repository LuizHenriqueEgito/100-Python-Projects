# Faça uma API de locação de carros
- Base de Dados de Carros:
    - ID, Marca, Modelo, Ano, Cor, Placa, Status de disponibilidade (disponivel, alugado, em manutenção), Preço da Locação, Quilometragem
    - Sub-bases (Marca, Modelo, Ano, Cor, Placa, Status de disponibilidade (disponivel, alugado, em manutenção))
- Base de Dados Clientes:
    - Nome Completo, CPF (ID), Endereço, Telefone, Data de Nascimento
- Base de Alugueis atuais Cliente -> Carro:
    - ID do aluguel, Id carro, Id pessoa, data aluguel, data devolução, status aluguel (ativo, finalizado, encerrado), Valor od aluguel

- Autenticação
