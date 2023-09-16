def idfy(txt: str) -> str:
    return (txt
            .replace("'", "")
            .replace(".", "")
            .lower()
            .replace(" ", "_"))
