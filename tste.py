import os
import sys
from typing import Callable, Dict, List, Tuple


def add(left: float, right: float) -> float:
    return left + right


def subtract(left: float, right: float) -> float:
    return left - right


def multiply(left: float, right: float) -> float:
    return left * right


def divide(left: float, right: float) -> float:
    if right == 0:
        raise ValueError("Divisão por zero não é permitida.")
    return left / right


OPERATORS: Dict[str, Callable[[float, float], float]] = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def supports_color() -> bool:
    return sys.stdout.isatty()


def color(text: str, code: str) -> str:
    if not supports_color():
        return text
    return f"\033[{code}m{text}\033[0m"


def fmt_result(value: float) -> str:
    if value.is_integer():
        return str(int(value))
    text = f"{value:.10f}".rstrip("0").rstrip(".")
    return text


def print_banner() -> None:
    title = " Calculadora "
    line = "═" * 30
    print(color(f"╔{line}╗", "36"))
    print(color(f"║{title.center(30, ' ')}║", "36"))
    print(color(f"╚{line}╝", "36"))
    print(
        "Fluxo: Informe NÚMERO 1 -> OPERAÇÃO -> NÚMERO 2.\n"
        "Comandos: "
        + color("h", "33")
        + "/help, "
        + color("c", "33")
        + "/clear, "
        + color("hist", "33")
        + ", "
        + color("q", "33")
        + "/quit/exit"
    )


def clear_screen() -> None:
    os.system("cls" if os.name == "nt" else "clear")


def read_number(prompt: str) -> float | None:
    while True:
        raw = input(color(prompt, "32")).strip().lower().replace(",", ".")
        if raw in {"q", "quit", "exit"}:
            return None
        if raw in {"h", "help"}:
            print_banner()
            continue
        if raw in {"c", "clear"}:
            clear_screen()
            print_banner()
            continue
        if raw == "":
            continue
        try:
            return float(raw)
        except ValueError:
            print(color("Número inválido. Tente novamente.", "31"))


def read_operator() -> str | None:
    choices = "+ - * /"
    while True:
        raw = input(color(f"Operação ({choices}): ", "33")).strip().lower()
        if raw in {"q", "quit", "exit"}:
            return None
        if raw in {"h", "help"}:
            print_banner()
            continue
        if raw in {"c", "clear"}:
            clear_screen()
            print_banner()
            continue
        if raw in OPERATORS:
            return raw
        print(color("Operação inválida. Use + - * /", "31"))


def main() -> None:
    history: List[Tuple[str, str]] = []
    print_banner()

    while True:
        n1 = read_number("Número 1: ")
        if n1 is None:
            break

        op = read_operator()
        if op is None:
            break

        n2 = read_number("Número 2: ")
        if n2 is None:
            break

        try:
            result = OPERATORS[op](n1, n2)
            res_text = fmt_result(result)
            expr = f"{fmt_result(n1)} {op} {fmt_result(n2)}"
            print(color(f"Resultado: {res_text}", "34"))
            history.append((expr, res_text))
        except ValueError as exc:
            print(color(f"Erro: {exc}", "31"))

        # continuar novo ciclo automaticamente (Número 1 -> Operação -> Número 2)


if __name__ == "__main__":
    main()


