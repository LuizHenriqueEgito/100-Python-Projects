from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.clock import Clock
from plyer import notification


class PomodoroTimer(App):
    # Config.window_icon = "images/tomato.png"
    def build(self):
        self.icon = "images/tomato.png"
        self.window = GridLayout()
        self.window.cols = 1
        self.size = (20, 20)
        self.window.size_hint = (None, None)
        self.window.size = (400, 300)
        self.window.pos_hint = {"center_x": 0.5, "center_y": 0.5}

        self.window.add_widget(Image(source='images/tomato.png'))

        self.greeting = Label(
            text="TIMER",
            font_size=42,
            color='#f46370',
            bold=True
        )
        self.window.add_widget(self.greeting)

        self.timer = TextInput(
            multiline=False,
            size_hint=(0.5, 0.5),
        )
        self.window.add_widget(self.timer)

        self.start = Button(
            text="START",
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='#f46370',
            background_normal=""
        )
        self.start.bind(on_press=self.callback)
        self.window.add_widget(self.start)

        self.pause = Button(
            text="PAUSE",
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='#f23042',
            background_normal=""
        )
        self.pause.bind(on_press=self.callback)
        self.window.add_widget(self.pause)

        self.reset = Button(
            text="RESET",
            size_hint=(0.5, 0.5),
            bold=True,
            background_color='#960613',
            background_normal=""
        )
        self.reset.bind(on_press=self.callback)
        self.window.add_widget(self.reset)

        self.is_running = False
        self.is_paused = False
        self.time_left = 0

        return self.window

    def callback(self, instance):
        if instance.text == 'START':
            self.click_on_start()
        elif instance.text == 'PAUSE':
            self.click_on_pause()
        elif instance.text == 'RESET':
            self.click_on_reset()

    def click_on_start(self):
        if not self.is_running and not self.is_paused:
            try:
                self.time_left = int(self.timer.text) * 60
            except ValueError:
                self.greeting.text = "Enter a valid number!"
                return
            self.is_running = True
            self.greeting.text = "Pomodoro Timer!"
            Clock.schedule_interval(self.update_time, 1)
        elif self.is_paused:
            self.is_running = True
            self.is_paused = False
            Clock.schedule_interval(self.update_time, 1)
    
    def click_on_pause(self):
        if self.is_running:
            self.is_running = False
            self.is_paused = True
            Clock.unschedule(self.update_time)
            self.greeting.text = f"Paused at {self.greeting.text}!"
        elif self.is_paused:
            self.is_running = True
            self.is_paused = False
            Clock.schedule_interval(self.update_time, 1)
            self.greeting.text = "Resumed!"

    def click_on_reset(self):
        self.is_running = False
        self.is_paused = False
        Clock.unschedule(self.update_time)
        self.time_left = 0
        self.greeting.text = "TIMER"

    def update_time(self, dt):
        if self.time_left > 0:
            self.time_left -= 1
            minutes, seconds = divmod(self.time_left, 60)
            self.greeting.text = f"{minutes:02}:{seconds:02}"
        else:
            self.greeting.text = "Time's up!"
            self.is_running = False
            Clock.unschedule(self.update_time)
            self.show_notification()

    def show_notification(self):
        notification.notify(
            title='Pomodoro Timer',
            message="Time's up!",
            app_icon=None,  # Você pode especificar um caminho para o ícone aqui
            timeout=10  # Duração da notificação em segundos
        )

if __name__ == "__main__":
    PomodoroTimer().run()