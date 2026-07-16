import sys
from pathlib import Path

from streamlit.web import cli as stcli


def obter_caminho_base() -> Path:
    """
    Retorna a pasta correta tanto durante o desenvolvimento
    quanto depois que o aplicativo for empacotado.
    """
    if getattr(sys, "frozen", False):
        return Path(sys._MEIPASS)

    return Path(__file__).resolve().parent


def main() -> None:
    pasta_base = obter_caminho_base()
    arquivo_app = pasta_base / "src" / "app.py"

    if not arquivo_app.exists():
        print(f"Erro: arquivo não encontrado: {arquivo_app}")
        input("Pressione Enter para fechar...")
        raise SystemExit(1)

    sys.argv = [
        "streamlit",
        "run",
        str(arquivo_app),
        "--global.developmentMode=false",
        "--browser.gatherUsageStats=false",
        "--server.headless=false",
    ]

    raise SystemExit(stcli.main())


if __name__ == "__main__":
    main()