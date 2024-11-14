import openai


def open_article(article):
    try:
        file = open(article, "r", encoding="utf-8")
        text = file.read()
    except FileNotFoundError:
        print("File does not exist")
        text = ""
    else:
        file.close()

    return text


def ai_response(text):
    if text != "":
        response = openai.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": 'Jesteś stworzony do przerobienia otrzymanego tekstu w kod html, '
                                                  'powinieneś używać odpowiednich tagów do strukturyzacji treści, '
                                                  'w miejscach w których twoim zdaniem warto wstawić grafiki uzyj '
                                                  'tagu img z atrybutem src="image_placeholder.jpg" oraz alt w którym '
                                                  'opiszesz tą grafike, pod każdą grafiką umieść jej podpis w '
                                                  'odpowiednim tagu. Nie używaj kodu css oraz js, zwrócony kod '
                                                  'powinien być stworzony do wstawienia pomiedzy tagi <body> i '
                                                  '</body>'},
                    {"role": "user", "content": text}
                ]
            )
        html_body = response.choices[0].message.content
    else:
        html_body = ""

    return html_body


def generate_html(body):
    layout_file = open("szablon.html", "r", encoding="utf-8")
    body_file = open(body, "r", encoding="utf-8")
    generate_file = open("podglad.html", "a", encoding="utf-8")

    lines = layout_file.readlines()

    for line in lines:
        generate_file.write(line)
        if "<body>" in line:
            generate_file.write(body_file.read())

    layout_file.close()
    generate_file.close()


def main():
    API_KEY = open("api_key.txt", "r")
    openai.api_key = API_KEY.read()
    API_KEY.close()

    text = open_article("tresc_artykulu.txt")

    file = open("artykul.html", "w", encoding="utf-8")
    file.write(ai_response(text))
    file.close()

    generate_html("artykul.html")


if __name__ == '__main__':
    main()


