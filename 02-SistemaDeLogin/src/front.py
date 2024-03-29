# Make the front that asks for login and password
import PySimpleGUI as sg
from functools import wraps
from dataclasses import dataclass, field
from datetime import datetime, timedelta
from src.crud import insert_new_register_in_db, get_password

sg.theme('LightBrown7')


@dataclass
class MyProgram:
    block_dict: dict = field(default_factory=dict)

    def login_window(self):
        layout = [
            [sg.Text('Login', font=('Courier', 15, 'bold'))],
            [sg.Text('User:', font=('Courier', 12), size=(10, 1)), sg.InputText(key='-USER-', font=('Courier'))],
            [sg.Text('Password:',  font=('Courier', 12), size=(10, 1)), sg.InputText(key='-PASSWORD-', font=('Courier'), password_char='*')],
            [sg.Submit(button_text='Enter'), sg.Cancel(button_text='Exit')],
            [sg.Text("You don't have a login yet? Register now"), sg.B(key='-REGISTER_NOW-', button_text='[Register]')]
        ]
        window = sg.Window('Login', layout=layout)
        event, values = window.read()
        window.close()

        print(event)
        match event:
            case '-REGISTER_NOW-':
                self.register_new_user()
            case 'Enter':
                if self.unlock_login(**values):
                    self.authenticator(values=values)
            case 'Exit':
                pass


    def authenticator(self, values):
        password_user = get_password(values=values)
        try:
            assert password_user == values['-PASSWORD-']
            sg.popup('Acess Allowed!')
        except:
            user = values['-USER-']
            sg.popup('Acess Denied!')
            self._user_block(user=user)
    
    def register_new_user(self):
        layout = [
            [
                sg.Text('User:', font=('Courier', 12), size=(20, 1)), 
                sg.InputText(key='-USER_REGISTER-', font=('Courier'))],
            [
                sg.Text('Password:', font=('Courier', 12), size=(20, 1)),
                sg.InputText(key='-PASS_REGISTER-', font=('Courier'), password_char='*')],
            [
                sg.Text('Confirm u pass:', font=('Courier', 12), size=(20, 1)), 
                sg.InputText(key='-PASS_CONFIRM_REGISTER-', font=('Courier'), password_char='*')],
            [
                sg.Submit(button_text='Register', font=('Courier', 12), size=(20, 1)), 
                sg.Cancel(button_text='Cancel')
            ]
        ]

        window = sg.Window('Register', layout=layout)
        event, values = window.read()
        print(f'event: {event}')
        print(f'values: {values}')
        # Valida a senha
        try:
            assert values['-PASS_REGISTER-'] == values['-PASS_CONFIRM_REGISTER-']
            # Salva o regitro em banco
        except:
            sg.popup("how passwords don't match")
        insert_new_register_in_db(values=values)
        window.close()
        sg.popup('you have been registered successfully.')

    def _user_block(self, user: str, time: int = 30):
        delta = datetime.now() + timedelta(seconds=time)
        self.block_dict[user] = delta
        return None

    def unlock_login(self, **kwargs):
        user = kwargs['-USER-']
        if user not in self.block_dict.keys():
            return 'Login'
        block_time = self.block_dict[user]
        now = datetime.now()
        unlock = block_time < now
        time_unlock = (block_time - now).seconds
        print(f'unlocked user: {unlock} | Time to unlock: {time_unlock}')
        return unlock
