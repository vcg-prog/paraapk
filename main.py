#hola mundo
import flet as ft

def main(page: ft.Page):
    page.title = "Hola Mundo con Flet"
    page.vertical_alignment = "center"
    page.horizontal_alignment = "center"

    def on_click(e):
        text.value = "¡Hola, mundo!"
        page.update()

    text = ft.Text(value="")
    button = ft.Button("Haz clic aquí", on_click=on_click)

    page.add(ft.Column([text, button], alignment="center"))

ft.run(main)