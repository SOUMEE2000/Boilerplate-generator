import click
import os
import pandas as pd
import csv

@click.group()
def cli():
    pass

@click.command(help="Generating required file")
@click.argument("language", type=str, required=True)
@click.option("-name", default="hello-world",show_default=True)
def generate(language,name):

    generate= language.lower()
    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "templates"
    abs_file_path = os.path.join(script_dir, rel_path)
    df= pd.read_csv(abs_file_path+"/templates.csv")
    for i in range(len(df)):
        if generate== df["Language"][i]:
            generate= df["Extensions"][i]
            break
    if generate[0]!='.':
        raise Exception("Language not supported. Proceed to add")
    file=check_file_name(name,generate)
    f= open(file,'w')
    temp=open(abs_file_path+'\\_'+ generate,'r')
    f.write(temp.read())
    f.close()
    temp.close()

@click.command(help="Adding new templates")
@click.argument("lang")
@click.argument("file")

def add(lang,file):
    count=0
    str=""
    lang= lang.lower()
    for i in file:
        if i != '.':
            str=str+ i
            count= count+1
        else:
            break

    extension=file[-(len(file)-count):]
    new_file="_"+extension

    script_dir = os.path.dirname(__file__) #<-- absolute dir the script is in
    rel_path = "templates"
    abs_file_path = os.path.join(script_dir, rel_path)
    if os.path.isfile(abs_file_path+'\\'+new_file):
        click.echo("File already exists")
    else:
        n_f= open(abs_file_path+'\\'+ new_file ,'w')
        f= open(file, 'r')
        n_f.write(f.read())
        f.close()
        n_f.close()
        click.echo("Template added")
        csvfile= open(abs_file_path+'\\'+ "templates.csv",'a+')
        writer=csv.writer(csvfile)
        writer.writerow([lang,extension])
        csvfile.close()

def check_file_name(name,generate):
    file= name +generate
    while True:
        if os.path.exists('./'+file):
            name=click.prompt("%s already exists.\nPress Y to overwrite it or give a new name" %file)
            if name =="Y" or name=="y":
                return file
            else:
                file= name +"."+generate
        else:
            return file


cli.add_command(generate)
cli.add_command(add)

if __name__=="__main__":
    cli()
