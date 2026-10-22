"""Truecolor terminal palette utility."""
import argparse
import json
import re
from pathlib import Path
PALETTES = {'ember': ['#211a1d', '#e85d04', '#ffba08', '#fff3b0'], 'moss': ['#122620', '#426b45', '#a7c957', '#f2e8cf']}
def rgb(value):
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', value): raise ValueError('expected #RRGGBB')
    return tuple(int(value[i:i+2],16) for i in (1,3,5))
def hex_color(values):
    if len(values)!=3 or any(type(v) is not int or not 0<=v<=255 for v in values): raise ValueError('RGB requires three integers in 0..255')
    return '#' + ''.join(f'{v:02x}' for v in values)
def palette(name, custom=None):
    colors = json.loads(Path(custom).read_text()) if custom else PALETTES.get(name)
    if not isinstance(colors,list) or not colors: raise ValueError('palette must be a nonempty JSON array of HEX colors')
    for color in colors:
        if not isinstance(color,str): raise ValueError('colors must be strings')
        rgb(color)
    return colors
def main():
    p=argparse.ArgumentParser(description=__doc__); s=p.add_subparsers(dest='command',required=True)
    s.add_parser('list')
    for name in ('preview','export'):
        q=s.add_parser(name);q.add_argument('palette',nargs='?',default='moss');q.add_argument('--file')
    q=s.add_parser('convert');q.add_argument('values',nargs='+')
    a=p.parse_args()
    try:
        if a.command=='list': print('\n'.join(PALETTES));return
        if a.command=='convert':
            print(json.dumps(rgb(a.values[0])) if len(a.values)==1 else hex_color([int(v) for v in a.values]));return
        colors=palette(a.palette,a.file)
        if a.command=='export': print(json.dumps(colors));return
        for c in colors:
            r,g,b=rgb(c);print(f'\033[48;2;{r};{g};{b}m    \033[0m {c} ({r}, {g}, {b})')
    except (ValueError,OSError,TypeError) as e: p.error(str(e))
if __name__=='__main__': main()
