import flet as ft
from datetime import datetime

def main_page(page: ft.Page):
    page.title = "Мое первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting_text = ft.Text(value="Hello world")
    history_text = ft.Text("История приветствий:")

    greeting_history = []      
    last_name = {"value": None}  


    def on_button_click(_):
        name = name_input.value.strip()

        if name:
            greeting_text.color = None
            greeting_text.value = f"Hello {name}"
            name_input.value = None
            last_name["value"] = name

            now = datetime.now()
            greeting_history.append({"time": now, "name": name})
            update_history_text(greeting_history)
        else:
            greeting_text.value = "Вы не ввели имя!"
            greeting_text.color = ft.Colors.RED

        page.update()

    
    def update_history_text(items):
        if items:
            lines = [
                f"{item['time'].strftime('%d/%m/%Y %H:%M:%S')}  {item['name']}"
                for item in items
            ]
            history_text.value = "История приветствий:\n" + "\n".join(lines)
        else:
            history_text.value = "История приветствий пуста"
        page.update()


    def clear_history(_):
        greeting_history.clear()
        update_history_text(greeting_history)

    #  новая функция: сортировка истории по алфавиту
    def sort_history(_):
        # сортируем список greeting_history по полю "name" без учета регистра
        greeting_history.sort(key=lambda x: x["name"].lower())
        # обновляем отображение после сортировки
        update_history_text(greeting_history)

    
    def theme_mode(_):
        page.theme_mode = (
            ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        )
        page.update()

    
    name_input = ft.TextField(label="Введите имя", on_submit=on_button_click)
    send_button = ft.TextButton(text="Send", icon=ft.Icons.SEND_ROUNDED, on_click=on_button_click)
    clear_button = ft.ElevatedButton(text="Очистить", icon=ft.Icons.DELETE, on_click=clear_history)

    #  новая кнопка "Сортировать по алфавиту"
    sort_button = ft.ElevatedButton(
        text="Сортировать по алфавиту",           # надпись на кнопке
        icon=ft.Icons.SORT_BY_ALPHA_ROUNDED,              # иконка сортировки
        on_click=sort_history                     # действие при нажатии вызов sort_history
    )

    theme_button = ft.IconButton(icon=ft.Icons.BRIGHTNESS_6, on_click=theme_mode)

    
    #добавлена sort_button в строку с другими кнопками
    page.add(greeting_text,name_input,send_button, ft.Row([clear_button, sort_button, theme_button]), history_text,)
    

ft.app(target=main_page)

