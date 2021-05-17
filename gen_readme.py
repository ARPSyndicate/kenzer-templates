import os, plazy
path = plazy.list_files(os.getcwd())
templates = []
for file in path:
    if ".yaml" in file:
        templates.append(file)
markdown = "| TEMPLATE | TOOL | FILE |\r"
markdown += "| :----: | :----: | :----: |\r"
templates.sort()
for template in templates:
    tool = template.split("\\")[1].split(".")[0]
    sign = template.split("\\")[-1].split(".")[0]
    path = "https://github.com/ARPSyndicate/kenzer-templates/tree/main"+template.replace("\\","/")
    markdown += "| {0} | {1} | [{2}]({3}) |\r".format(sign, tool, template.strip("\\"), path)

with open("README.md", "w") as f:
    f.write(markdown)
            
        