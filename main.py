import flet as ft

def main(page: ft.Page):
    page.title = 'Конвертер величин'
    page.window.width = 320
    page.window.height = 500
    page.window.resizable = False
    page.vertical_alignment = ft.MainAxisAlignment.CENTER


    input_field = ft.TextField(
        label='Введіть значення',
        width = 200,
        keyboard_type=ft.KeyboardType.NUMBER,
        autofocus=True,
    )

    unit_selector = ft.Dropdown(
        label='Виберіть одиницю вимірювання',
        options=[
            ft.dropdown.Option('Дні'),
            ft.dropdown.Option('Години'),
            ft.dropdown.Option('Хвилини'),
            ft.dropdown.Option('Секунди'),
            ft.dropdown.Option('Мілісекунди'),
            ft.dropdown.Option('Тижні'),
        ],
        value='Дні',
        width=280
    )

    result_fields={
        'Дні': ft.Text("0", size=16),
        'Години': ft.Text("0", size=16),
        'Хвилини': ft.Text("0", size=16),
        'Секунди': ft.Text("0", size=16),
        'Мілісекунди': ft.Text("0", size=16),
        'Тижні': ft.Text("0", size=16),
    }

    def convert(e):
        try:
            number = float(input_field.value)
            unit = unit_selector.value

            if unit == "Дні":
                days = number

            elif unit == "Години":
                days = number / 24

            elif unit == "Хвилини":
                days = number / (24 * 60)

            elif unit == "Секунди":
                days = number / (24 * 60 * 60)

            elif unit == "Мілісекунди":
                days = number / (24 * 60 * 60 * 1000)

            elif unit == "Тижні":
                days = number * 7

            hours = days * 24
            minutes = hours * 60
            seconds = minutes * 60
            milliseconds = seconds * 1000
            weeks = days / 7

            result_fields["Дні"].value = f"{days:.2f}"
            result_fields["Години"].value = f"{hours:.2f}"
            result_fields["Хвилини"].value = f"{minutes:.2f}"
            result_fields["Секунди"].value = f"{seconds:.2f}"
            result_fields["Мілісекунди"].value = f"{milliseconds:.2f}"
            result_fields["Тижні"].value = f"{weeks:.2f}"
        except ValueError:
            input_field.error_text = "Вкажіть коректне значення!"
            for key in result_fields:
                result_fields[key].value = "0"
        finally:
            page.update()

    def reset(e):
        input_field.value = ""
        input_field.error_text = None
        for key in result_fields:
            result_fields[key].value = "0"

        page.update()

    page.add(
        ft.Column(
            [
                unit_selector,
                input_field,
                ft.Button("Конвертувати", on_click=convert),
                ft.Button("Очистити", on_click=reset),
                ft.Divider(),
                ft.Column(
                    [
                        ft.Row([ft.Text(f"{key}: ", size=14), result_fields[key]])
                        for key in result_fields
                    ],
                    spacing=5
                )
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            spacing=15
        )
    )

if __name__ == "__main__":
    ft.run(main)