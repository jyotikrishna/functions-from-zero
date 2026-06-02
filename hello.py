import click

@click.command()
@click.option('--name', prompt='Your name', help='The person to greet.')
def add(x,y):
    return x+y

print(add(2,2))

if __name__ == '__main__':
    add()


 #check code    