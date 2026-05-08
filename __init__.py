import aqt
import aqt.editor
import html

FILE_EXT = ["webm"]

DEFAULT_CONFIG = {
    "videoHTMLAttributes": {
        "controls": True,
        "controlslist": "nodownload",
        "autoplay": True,
        "loop": False,
        "muted": False
    },
}

config = DEFAULT_CONFIG | (aqt.mw.addonManager.getConfig(__name__) or {})

def build_attrs(attrs: dict):
    if not isinstance(attrs, dict):
        return ""
    parts = []
    for k, v in attrs.items():
        if v is True or v == "":
            parts.append(f'{k}=""')
        elif v is False:
            continue
        else:
            parts.append(f'{k}="{html.escape(str(v))}"')
    return " " + " ".join(parts) if parts else ""

def process_webm_files(
    mime: aqt.QMimeData,
    editorWeb: aqt.editor.EditorWebView,
    _internal: bool,
    extended: bool,
    _drop_event: bool,
):
    if not mime.hasUrls():
        return mime
    
    html_str = ""
    urls = mime.urls()
    processed_urls = set()

    for url in urls:
        fname = editorWeb.editor.urlToFile(url.toString(), FILE_EXT)
        if not fname:
            continue
        attr_str = build_attrs(config.get("videoHTMLAttributes", {}))
        html_str += f'<video{attr_str}><source src="{fname}" type="video/webm"></video>'
        processed_urls.add(url)
    
    if html_str:
        editorWeb.editor.doPaste(html_str, True, extended)

    if processed_urls:
        new_urls = [url for url in urls if url not in processed_urls]
        new_mime = aqt.QMimeData()
        new_mime.setUrls(new_urls)
        return new_mime

    return mime
        
aqt.gui_hooks.editor_will_process_mime.append(process_webm_files)