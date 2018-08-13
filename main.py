from Crawler.Page import Page
from Crawler.Image import Image
from Crawler.Css import Css
from Image.Download import Download
import functions
import threading
from queue import Queue

if __name__ == '__main__':
    NUMBER_OF_THREADS = 4
    URL = 'https://exponea.com/'

    queue = Queue()
    page = Page(URL)
    all_links = page.fetch_links()
    links = set()
    css_styles = set()
    css_styles_scan = set()
    # filtering only links from URL
    for lnk in all_links:
        if lnk.find(URL) == 0:
            links.add(lnk)


    def create_jobs():
        for link in sorted(links):
            queue.put(link)
        queue.join()


    # Create worker threads (will die when main exits)
    def create_workers():
        for _ in range(NUMBER_OF_THREADS):
            t = threading.Thread(target=downloading)
            t.daemon = True
            t.start()


    def downloading():
        while True:
            try:
                link = queue.get()
                print(threading.current_thread().name + ' Download ' + link)
                img = Image(link)
                images = img.fetch_links()

                css = Css(link)
                styles = css.fetch_links()
                for style in styles:
                    if style.find('.css') >= 0:
                        css_styles.add(style)
                        css_styles_scan.add(style)

                down = Download(links=images, path=functions.get_folder_name(link))
                down.start()
                queue.task_done()
                print(threading.current_thread().name + ' Done ' + link)
                if queue.empty():
                    break
            except:
                queue.task_done()
                continue


    # download images from pages
    create_workers()
    create_jobs()

    # finding images in css
    css_images = set()
    while len(css_styles_scan) > 0:
        new_styles = set()
        for css in css_styles_scan:
            css_text = functions.get_html(css)
            new_csss = functions.find_import(css_text)
            for new_css in new_csss:
                if new_css not in css_styles:
                    css_styles.add(new_css)
                    new_styles.add(new_css)

            new_images = functions.find_image_in_css(css_text)
            css_images = css_images | new_images

        css_styles_scan = new_styles
    print('\nImages from site saves in /storage \n List of images from CSS: \n')
    for image in css_images:
        print(image)
