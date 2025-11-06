import flet as ft
from datetime import datetime

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'

    #Определяем приветствие по времени суток
    hour = datetime.now().hour
    if 6 <= hour < 12:
        greet = "Доброе утро"
    elif 12 <= hour < 18:
        greet = "Добрый день"
    elif 18 <= hour < 24:
        greet = "Добрый вечер"
    else:
        greet = "Доброй ночи"

    greeting_text = ft.Text(value=f"{greet}!", size=20)
    name_input = ft.TextField(label='Введите имя')

    def on_button_click(_):
        name = name_input.value.strip()
        greeting_text.value = f"{greet}, {name}!" if name else "Введите имя!"
        greeting_text.color = ft.Colors.GREEN if name else ft.Colors.RED
        page.update()

    input_button = ft.TextButton(
        text='send',
        icon=ft.Icons.SEND_ROUNDED,
        on_click=on_button_click
    )

    page.add(greeting_text, name_input, input_button)

ft.app(target=main_page)
