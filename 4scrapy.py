from lxml import html
import sys, requests, os, wget

def main():
    url = sys.argv[1]
    folder = os.path.basename(url)
    page = requests.get(url)
    tree = html.fromstring(page.content)
    imgs = tree.xpath('//a[@target="_blank"][@class="fileThumb"]/@href')
    num = 0

    if "#" in folder:
        folder = folder.split("#")[0]

    if not os.path.exists(folder):
        os.makedirs(folder)

    for i in imgs:
        imgs[num] = 'http:' + imgs[num]

        if '4chan.org' in imgs[num]:
            del imgs[num]

        num += 1

    os.chdir(folder)

    for img in imgs:
        wget.download(img)

        print(img)
    
    print(str(len(imgs)) + " images download.")

if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("usage: 4scrapy.py <url>")
    else:
        main()
