# chatapp.py
import reflex as rx
from web_python_reflex import style
from web_python_reflex.state import State

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, style=style.question_style),
            text_align="right",
        ),
        rx.box(
            rx.text(answer, style=style.answer_style),
            text_align="left",
        ),
        margin_y="1em",
    )

def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return  rx.hstack(
        rx.input(
            placeholder="Ask a question",
            on_blur=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Ask",
            on_click=State.answer,
            style=style.button_style,
        ),
        )


def index() -> rx.Component:
    return rx.vstack(
        rx.heading("My own chatGPT app with Python", font_size="2em", color="black"),
        rx.spacer(),
        (rx.container(
        chat(),
        action_bar(),
        )),
        rx.spacer(),
        rx.text("For this project I used Python, Reflex, and Open AI.", font_size="1em", as_="i"))

app = rx.App()
app.add_page(index)
app.compile()