import markdown

try:
    with open("index.md", "r") as m:
        markdown_content = m.read()
        html = markdown.markdown(markdown_content)
    try:
        with open("index.html", "w") as i:
            i.write(html)
    except IOError:
        print("Failed to save as html")
except Exception as error:
    print(f"Failed to open and conver markdown: {error}")

