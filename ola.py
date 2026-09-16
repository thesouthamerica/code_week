"""SI Code Week 2026 · Desafio 0 · teste do ambiente Python."""
import sys

VERSAO_MINIMA = (3, 12)


def main() -> None:
    atual = sys.version_info[:2]
    if atual >= VERSAO_MINIMA:
        print(f"Python {atual[0]}.{atual[1]}: tudo certo. Pode seguir para a semana.")
    else:
        print(
            f"Você está com Python {atual[0]}.{atual[1]}. Os testes dos Desafios 02 e Final rodam em 3.12. "
            "Seu código provavelmente funciona, mas, se puder, atualize em python.org/downloads antes de terça."
        )


if __name__ == "__main__":
    main()
