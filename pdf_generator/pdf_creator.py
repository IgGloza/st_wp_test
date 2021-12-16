import json
import os
from pathlib import PurePath

import weasyprint
from jinja2 import Environment, FileSystemLoader

ROOT = "pdf_generator/pdf_data"
TEMPLATE_SRC = PurePath(ROOT, "templates")
CSS_SRC = PurePath(ROOT, "static/css")
DEST_DIR = PurePath(ROOT, "output")

TEMPLATE = "template.html"
CSS = "style.css"
OUTPUT_FILENAME = "rt.pdf"


def start():
    print("start generate report...")
    env = Environment(loader=FileSystemLoader(TEMPLATE_SRC))
    template = env.get_template(TEMPLATE)
    css = os.path.join(CSS_SRC, CSS)

    # read json file
    with open("pdf_generator/pdf_data/assets/route.json") as route_data:
        route_information = json.load(route_data)

    # variables
    template_vars = {
        "statistics_data": route_information,
    }

    # rendering to html string
    rendered_string = template.render(template_vars)
    html = weasyprint.HTML(string=rendered_string)
    report = os.path.join(DEST_DIR, OUTPUT_FILENAME)
    html.write_pdf(report, stylesheets=[css])
    print(
        f"file is generated successfully and under "
        f"{DEST_DIR}\\{OUTPUT_FILENAME}"
    )


if __name__ == "__main__":
    start()
