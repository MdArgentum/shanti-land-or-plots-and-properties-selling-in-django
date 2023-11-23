from django import template

register = template.Library()

@register.filter(name='insert_line_breaks')
def insert_line_breaks(value, max_chars=70):
    words = value.split()
    lines = []
    current_line = ''

    for word in words:
        if len(current_line) + len(word) <= max_chars:
            current_line += ' ' + word
        else:
            lines.append(current_line.strip())
            current_line = word

    if current_line:
        lines.append(current_line.strip())

    return '<br>'.join(lines)
