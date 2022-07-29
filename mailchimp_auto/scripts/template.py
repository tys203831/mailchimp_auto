from jinja2 import Environment, FileSystemLoader
from mailchimp_auto.scripts import directory
from mailchimp_auto.scripts.campaign_detail import Info
from configparser import RawConfigParser
import os
import logging

config = RawConfigParser()
config.read(directory.template_config)


def generate_html_template(account_choice:str, template_name: str, 
                           input_fileName: str="master.htm",
                           preview: bool = False) -> None:
     
    #print(f"123 generate_html_content account_choice: {account_choice}")
    fileLoader = FileSystemLoader(searchpath=directory.template_folder)
    env = Environment(loader=fileLoader)
    
    # use json/csv and for loop to render
    template_loc = f"{template_name}/{input_fileName}"
    data=Info(account_choice=account_choice,template_choice=template_name).gethtmlContent()
    #print(data)
    #print(f"test template_loc1: {template_loc}")
    rendered = env.get_template(template_loc).render(data=data)
    
    if preview:
        output_file = os.path.join(directory.output_folder, "index.htm")
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(rendered)
        print(f"Please check your generated template output at {output_file}")
    return rendered