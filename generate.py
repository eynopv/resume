import json
from typing import List
import weasyprint
from datetime import datetime
from jinja2 import Template, Environment, FileSystemLoader


def main():
    env = setup_jinja_environment()

    with open("./resume.json", "r") as resume_file:
        data = json.load(resume_file)

    html_template = open_template(env, "./template.html.jinja")
    final_html = html_template.render(data, title=data["basics"]["name"])

    with open("resume.html", "w") as html_file:
        html_file.write(final_html)

    pdf = weasyprint.HTML(string=final_html).write_pdf()
    if pdf:
        open("resume.pdf", "wb").write(pdf)


def setup_jinja_environment() -> Environment:
    env = Environment(loader=FileSystemLoader("./"))
    env.filters["format_date"] = format_date
    env.filters["join_skills"] = join_skills
    return env


def format_date(date: str) -> str:
    date_obj = datetime.strptime(date, "%Y-%m")
    return date_obj.strftime("%B %Y")


def join_skills(skills: List[dict]) -> str:
    return ", ".join(item for skill in skills for item in skill.get("keywords", []))


def open_template(env: Environment, template_path: str) -> Template:
    return env.get_template(template_path)


if __name__ == "__main__":
    main()
