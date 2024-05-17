import flet
from flet import *
from data import photo

def main(page:Page):
    page.window_width=300
    page.scroll = "always"
    st = Stack()
    listlike = Row()
    listreject = Row()

    def youchoice(e:DragUpdateEvent):
        pass

    #Base de fotos e nomes
    for x in photo:
        st.controls.append(
            #
            GestureDetector(
                mouse_cursor=MouseCursor.MOVE,
                on_pan_update=youchoice,
                left=10,
                right=10,
                top=10,
                content=Container(
                    width=300,
                    height=300,
                    bgcolor='blue',
                    padding=10,
                    content=Column([
                        Image(src=x['image'],
                              width=300,
                              height=250,
                              fit='cover'
                              ),
                        Text(x['name'],size=25,weight='bold ')
                    ])
                )
            )
        )

    page.overlay.append(
            Container(
                margin=margin.only(400),
                padding=10,
                content=Column([
                    Text('Like', size=25),
                    Container(
                        bgcolor="green",
                        padding=10,
                        content=listlike
                    ),
                    #Para os reijeitados
                    Text("Hoje não Faro",size=25),
                    Container(
                        bgcolor='red200',
                        padding=10,
                        content=listreject
                    )
                ])
            )
        )

flet.app(target=main)