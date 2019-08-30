import click
import pyperclip


@click.group()
def clip():
    pass


@clip.command()
@click.option('-f', '--file', default='clip.txt', type=click.File('w'),
              help='Export file path.')
def save(file):
    '''Exports text from clipboard to file in path.'''
    file.write(pyperclip.paste().replace('\r\n', '\n'))


@clip.command()
@click.argument('file', type=click.File('r'))
def copy(file):
    '''Import text from file in path to clipboard.'''
    pyperclip.copy(file.read())


if __name__ == '__main__':
    clip()
