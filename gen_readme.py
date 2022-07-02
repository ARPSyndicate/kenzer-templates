import os
import plazy
path = plazy.list_files(os.getcwd())
templates = []
for file in path:
    if (".yaml" in file or "exploit.sh" in file) and ("freakerdb.yaml" not in file):
        templates.append(file)
templates.sort()
markdown = "# Kenzer Templates [{0}]\r".format(len(templates))
markdown += "| TEMPLATE | TOOL | FILE |\r"
markdown += "| :----: | :----: | :----: |\r"
for template in templates:
    tool = template.split("/")[0].split(".")[0]
    if ".yaml" in template and "/fingerprints/" not in template:
        sign = ".".join(template.split("/")[-1].split(".")[0:-1])
    else:
        sign = template.split("/")[-2]
    path = "https://github.com/ARPSyndicate/kenzer-templates/tree/master/" + \
        template.replace("\\", "/")
    markdown += "| {0} | {1} | [{2}]({3}) |\r".format(sign,
                                                      tool, template, path)

with open("README.md", "w") as f:
    f.write(markdown)