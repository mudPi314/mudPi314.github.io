import mistletoe
import sys
import os

if __name__=="__main__":
    args = sys.argv
    filename = args[1]
    title = ""

    # Determine the title. Inputted title > existing title > ""

    if len(args) > 2:
        title = args[2]
    else:
        try:
            with open(f"{filename}.html") as file:
                fulltext = file.read()
                title = fulltext.split("<title>")[1].split("</title>")[0]
        except FileNotFoundError:
            print("No title found. Making empty title.")
            title = ""

    # Read template from template.html

    template = ""
    templatepath = "template.html"
    with open(templatepath, 'r') as file:
        template = file.read()

    # Convert the md file to html

    body = ""
    with open(f"{filename}.md", 'r') as file:
        body = mistletoe.markdown(file)

    # Add the title and write to the html file

    fullhtml = template.format_map({"body": body, "title": title})
    with open(f"{filename}.html", 'w') as file:
        file.write(fullhtml)
