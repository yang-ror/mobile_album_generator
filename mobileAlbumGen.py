import os


# generate a html page for each sub-directory with picture in the directory.
# html files are stored in ./html/
def generate_html():
    htmlFiles = []
    htmlFolderName = 'html'
    subDirectory = './' + htmlFolderName + '/'
    if not os.path.exists(htmlFolderName):
        os.mkdir(htmlFolderName)
    
    for directory in os.listdir():
        if os.path.isdir(directory) and directory != htmlFolderName:
            title = directory
            filename = subDirectory + title + ".html"
            print("Generating: ", filename)

            file = open(filename, "w", encoding="utf8")

            file.write('<!doctype html>\n')
            file.write('<html lang="en">\n')
            file.write('<head>\n')
            file.write('<title>'+ title +'</title>')
            file.write('<meta name="viewport" content="width=device-width, initial-scale=1.0" charset=utf-8>\n')
            file.write("</head>\n")
            file.write("<body style>\n")

            for image in os.listdir(directory):
                if not image.startswith('.'):
                    line = '<img src="../' + os.path.join(directory, image) + '" width=100%' + ' border="0" style="display:block;">\n'
                    file.write(line)

            file.write("</body>\n")
            file.write("</html>\n")
            htmlFiles.append(filename)
    return htmlFiles


# generate an index.html for all the html pages generated above.
def generate_index(htmlFiles):
    albumTitle = "My Mobile Album"

    file = open("index.html", "w")
    
    file.write('<!doctype html>\n')
    file.write('<html lang="en">\n')
    file.write('<head>\n')
    file.write('<title>' + albumTitle + '</title>')
    file.write('<meta name="viewport" content="width=device-width, initial-scale=1.0" charset=utf-8>\n')
    file.write("</head>\n")
    file.write("<body style>\n")
    
    for htmlFilename in htmlFiles:
        line = '<a href="' + htmlFilename + '">' + htmlFilename[7:-5] +'</a>\n'
        file.write(line)
        file.write('<br>')

    file.write("</body>\n")
    file.write("</html>\n")


# this method only works in localhost, using "python3 -m http.server" instead to open access to other devices on the same network.
# def hostSite():
#     PORT = 8000

#     handler = http.server.SimpleHTTPRequestHandler

#     ipAddr = socket.gethostbyname(socket.gethostname())

#     with socketserver.TCPServer(("", PORT), handler) as httpd:
#         print('********************************************************************************************************\n')
#         print("Succeed! Now press Ctrl + C to end localhost, then run 'python3 -m http.server' to host in LAN")
#         print("Lastly, open the browser on your phone and visit: " + ipAddr + ':' + str(PORT))
#         print('\n********************************************************************************************************')
#         httpd.serve_forever()


# this script does not need to be run again if there's no change in the directory.
if __name__ == "__main__":
    generate_index(generate_html())
    print('****************************************************************************************************************************************')
    print('*                                                                                                                                      *')
    print("*       Succeed! Now run 'python3 -m http.server' to host in LAN then open the browser on your phone and visit: you-local-ip:8000      *")
    print('*                                                                                                                                      *')
    print('****************************************************************************************************************************************')

