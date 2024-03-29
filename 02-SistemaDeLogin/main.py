# Run the program
from src.front import MyProgram
from src.database import create_ifnot_exists

# Criando o database de controle
create_ifnot_exists()

myprogram = MyProgram()
while True:
    myprogram.login_window()