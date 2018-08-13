import urllib.parse
import urllib.request


def get_folder_name(base_url) -> object:
    base_url = urllib.parse.urlparse(base_url).netloc
    parts = base_url.split(".")
    if len(parts) == 3:
        return parts[1]
    elif len(parts) == 2:
        return parts[0]
    else:
        return "-".join(parts)


def get_html(css):
    try:
        request = urllib.request.Request(css, headers={
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.84 Safari/537.36"})
        response = urllib.request.urlopen(request)
        html_bytes = response.read()
        html_string = html_bytes.decode("utf-8")

    except Exception as e:
        return None
    return html_string


def find_import(css):
    text = css
    res = set()
    while True:
        start_pos = text.find('@import')
        if start_pos < 0:
            break
        text = text[start_pos:]
        end_pos = text.find(';')
        f_text = text[8:end_pos]
        if f_text.find('.css') >= 0:
            sp = f_text.find('url(')
            if sp >= 0:
                f_text = f_text[sp+4:f_text.find(')')]
            f_text = f_text.strip().strip("'").strip('"')
            res.add(f_text)
        text = text[end_pos:]
    return res


def find_image_in_css(css):
    text = css
    res = set()
    while True:
        start_pos = text.find('url(')
        if start_pos < 0:
            break
        text = text[start_pos:]
        end_pos = text.find(')')
        f_text = text[4:end_pos]
        f_text = f_text.strip("'").strip('"')
        if f_text.find('font') < 0:
            res.add(f_text)
        text = text[end_pos:]
    return res
