from rich.theme import Theme
from rich.traceback import install
from rich.console import Console

install(show_locals=True)

theme = Theme({"info": "bold green", "error": "bold red", "warrning": "bold yellow"})

console = Console(theme=theme)

console.print("hello, [info]world![/info]", ":vampire,", locals())


def campare_numbers(num1, num2) -> None:
    console.log(log_locals=True)  # log the local variables
    if num1 > num2:
        console.print(f"{ num1 } is greater than { num2 }", style="info")
    elif num1 < num2:
        console.print(f"{ num1 } is less than { num2 }", style="info")
    else:
        console.print(f"{ num1 } is equal to { num2 }", style="warrning")


campare_numbers(10, 20)
campare_numbers(20, 10)
campare_numbers(10, 10)

campare_numbers(10, "linuxdex")
