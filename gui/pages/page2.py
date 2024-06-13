import flet as ft

class Page2(ft.UserControl):
    def __init__(self, page):
        super().__init__()
        self.page = page        

    def build(self):
        return ft.Container(
            content=ft.Column(
                [
                    ft.Row(
                        [
                            ft.Text("Legourmet by Geniiia", size=24, color='#FFFFFF'),
                        ],
                        alignment='start'
                    ),
                    ft.Row(
                        [
                            ft.Text("¡Bienvenidos!", size=72, weight='bold', color='#FF6F3C'),
                        ],
                        alignment='center'
                    ),
                    ft.Row(
                        [
                            ft.Text("A Legourmet, el único restaurante dirigido por inteligencia artificial.", size=24, color='#00FFA3'),
                        ],
                        alignment='center'
                    ),
                    ft.Row(
                        [
                            ft.Text("Antes de empezar con la experiencia indícanos el número de platos que deseas ordenar:", size=24, color='#00FFA3'),
                        ],
                        alignment='center'
                    ),
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.Text("Vemos que nos acompañan # visitantes, ¿desean ordenar # platos?", size=24, color='#FFFFFF'),
                                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                border_radius=20,
                                bgcolor='#3A3A3A'
                            )
                        ],
                        alignment='center'
                    ),
                    ft.Container(height=100),  # Añadir un contenedor vacío para mover los botones más abajo
                    ft.Row(
                        [
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Text("DECLINAR", size=32, color='#FF3131', weight='bold', font_family='Poppins'),
                                    on_click=self.on_decline_click,
                                    bgcolor='#ff8d8d'
                                ),
                                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                border_radius=20,
                            ),
                            ft.Image(src="assets/robot.png", width=150, height=150),  # Añadir la imagen entre los botones
                            ft.Container(
                                content=ft.ElevatedButton(
                                    content=ft.Text("ACEPTAR", size=32, color='#008F5C', weight='bold', font_family='Poppins'),
                                    on_click=self.on_accept_click,
                                    bgcolor='#00FFA3'
                                ),
                                padding=ft.padding.symmetric(horizontal=20, vertical=10),
                                border_radius=20,
                            )
                        ],
                        alignment='center',
                        spacing=100  # Aumentar el espacio entre los botones
                    ),
                    
                ],
                alignment='center',
                spacing=20
            ),
            padding=ft.padding.all(20),
            gradient=ft.LinearGradient(
                begin=ft.alignment.top_left,
                end=ft.alignment.bottom_right,
                colors=['#003e4b', '#0c0822']
            ),
            expand=True,
            width=self.page.window_width,
            height=self.page.window_height,
        )
    def on_decline_click(self, e):
        self.page.go("/")

    def on_accept_click(self, e):
        self.page.go("/page3")

