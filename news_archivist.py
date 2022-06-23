
#-----Statement of Authorship----------------------------------------#
#
#  This is an individual assessment item.  By submitting this
#  code I agree that it represents my own work.  I am aware of
#  the University rule that a student must not act in a manner
#  which constitutes academic dishonesty as stated and explained
#  in QUT's Manual of Policies and Procedures, Section C/5.3
#  "Academic Integrity" and Section E/2.1 "Student Code of Conduct".
#
#    Student no: 11178931
#    Student name: Chan Myait Htoo
#
#  NB: Files submitted without a completed copy of this statement
#  will not be marked.  Submitted files will be subjected to
#  software plagiarism analysis using the MoSS system
#  (http://theory.stanford.edu/~aiken/moss/). [1C2202]
#
#--------------------------------------------------------------------#



#-----Task Description-----------------------------------------------#
#
#  News Archivist
#
#  In this task you will combine your knowledge of HTMl/XML mark-up
#  languages with your skills in Python scripting, pattern matching
#  and Graphical User Interface development to produce a useful
#  application for maintaining and displaying archived news or
#  current affairs stories on a topic of your own choice.  See the
#  instruction sheet accompanying this file for full details.
#
#--------------------------------------------------------------------#



#-----Imported Functions---------------------------------------------#
#
# Below are various import statements that were used in our sample
# solution.  You should be able to complete this assignment using
# these functions only.

# Import the function for opening a web document given its URL.
from urllib.request import urlopen

# Import the function for finding all occurrences of a pattern
# defined via a regular expression, as well as the "multiline"
# and "dotall" flags.
from re import findall, MULTILINE, DOTALL

# A function for opening an HTML document in your operating
# system's default web browser. We have called the function
# "webopen" so that it isn't confused with the "open" function
# for writing/reading local text files.
from webbrowser import open as webopen

# A module with useful functions on pathnames including:
# normpath: function for 'normalising' a  path to a file to the path-naming
# conventions used on this computer.  Apply this function to the full name
# of your HTML document so that your program will work on any operating system.
# exists: returns True if the supplied path refers to an existing path
from os.path import *

# An operating system-specific function for getting the current
# working directory/folder.  Use this function to create the
# full path name to your HTML document.
from os import getcwd
 
# Import the standard Tkinter GUI functions.
from tkinter import *

# Import the date and time function.
# This module *may* be useful, depending on the websites you choose.
# Eg convert from a timestamp to a human-readable date:
# >>> datetime.fromtimestamp(1586999803) # number of seconds since 1970
# datetime.datetime(2020, 4, 16, 11, 16, 43)
from datetime import datetime

#
#--------------------------------------------------------------------#



#-----Student's Solution---------------------------------------------#
#
# Put your solution at the end of this file.
#

# Name of the folder containing your archived web documents.  When
# you submit your solution you must include the web archive along with
# this Python program. The archive must contain one week's worth of
# downloaded HTML/XML documents. It must NOT include any other files,
# especially image files.
internet_archive = 'InternetArchive'


################ PUT YOUR SOLUTION HERE #################
#Backend part
#Function to create regular expression patterns which are used to find the matches in xml file.
def extract_tags(xml_content):
    #Create the regular expression pattern for matching titles 
    title_pattern = """</category> <title>(.*?)</title>"""
    title_matches = findall(title_pattern, xml_content)

    #Create the regular expression pattern for matching image links
    image_pattern = '<media:group> <media:content url="(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)"'
    image_matches = findall(image_pattern, xml_content)

    #Create the regular expression pattern for matching links of full story
    link_pattern = '</guid> <link>(http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+)</link>'
    link_matches = findall(link_pattern, xml_content)

    #Create the regular expression pattern for matching publication date
    pubdate_pattern = '<pubDate>(.*?)</pubDate>'
    pubdate_matches = findall(pubdate_pattern, xml_content)

    #Create the regular expression pattern for matching description
    description_pattern = """<description><!\[CDATA\[(.*?)]]></description>"""
    description_matches = findall(description_pattern, xml_content)

    #Reture a tuple of matches
    return (title_matches, image_matches, link_matches, pubdate_matches, description_matches)

#Function to create output html files from the matches extracted by regular expression
def create_html_file(selected_archive):
    #Get the current directory
    current_directory = getcwd()
    #Join the current directory path and archive folder including xml file
    xml_file_directory = join(current_directory, "InternetArchive", selected_archive)

    #Open the document and read the content
    xml_doc= open(xml_file_directory,'r', encoding='UTF-8')
    xml_content = xml_doc.read()
    xml_doc.close()


    #Invoke extract_tag function to extract xml markups to create the output file
    title_matches, image_matches, link_matches, pubdate_matches, description_matches = extract_tags(xml_content)
    #Combine the list of individual matches to form the individal content for each story.
    doc_content = list(zip(title_matches, image_matches, link_matches, pubdate_matches, description_matches))
    #(title, image_link, source_link, puddate, description)

    #Create the html file as the output file of the selected archive
    output_file = open('output.html','w',encoding='UTF-8')
    #Use the css style sheet from the client briefing demonstration
    output_file.write("""
    <!DOCTYPE html>
    <html>
        <head>
            <!-- Title for browser window/tab -->
            <title>Fox News</title>
            <!--Overall document style -->
            <style>
                body {background-color: white;}
                p {width: 80%; margin-left: auto; margin-right: auto; text-align: left;}
                h1 {width: 80%; margin-left: auto; margin-right: auto; text-align: center;}
                h2 {width: 80%; margin-left: auto; margin-right: auto; text-align: center;margin-top: auto;}
                h3 {width: 80%; margin-left: auto; margin-right: auto; text-align: center;margin-top: auto;}
                hr {border-style: solid; margin-top: 1em; margin-bottom: 1em;}
                .center {
                    display: block;
                    margin-left: auto;
                    margin-right:auto;
                    width: 50%;
                }
            </style>
        </head>

        <body>
            <!-- Masthead -->
            <h1>Fox News Archive</h1>
            <h2>FoxNews.com - Breaking news and video. Latest Current News: U.S., World, Entertainment, Health, Business, Technology, Politics, Sports</h2>
            <p style = "text-align: center">
            <img src = "https://www.logo.wine/a/logo/Fox_News/Fox_News-Logo.wine.svg" alt = "WSJ-Logo" width = "200" height = "200">
            </p> 
            <p><strong>New source:</strong><a href = "https://moxie.foxnews.com/feedburner/latest.xml">https://moxie.foxnews.com/feedburner/latest.xml</a><br>
            <strong>Archivist:</strong>Chan Myait Htoo</p>
            <hr width = "80%" size = 5px>
    """)
    #Create the count variable to trace the number of article
    count = 1
    #Iterate through the matches and write these matches to the output file


    for (title, image_link, source_link, pubdate, description)in doc_content:
        title_string = '        <h3>NUMBER.TITLE</h3>\n'
        output_file.write('        <!--A new article-->\n')
        output_file.write('        <!--Headline-->\n')
        output_file.write(title_string.replace('NUMBER', str(count)).replace('TITLE', title))
        output_file.write('        <!--Source of image-->\n')
        output_file.write('        <img src="IMAGE_LINK" class="center" alt ="Sorry, image is not available">\n'.replace('IMAGE_LINK', image_link))
        output_file.write('        <!--Synopsis-->\n')
        output_file.write('        <p>DESCRIPTION</p>\n'.replace('DESCRIPTION', description))
        output_file.write('        <!--Source of full story-->\n')
        output_file.write('        <p><strong>Full story:</strong><a href = "FULL_LINK">FULL_LINK</a></p>\n'.replace('FULL_LINK', source_link))
        output_file.write('        <!--Publication Date-->\n')
        output_file.write('        <p><strong>Dateline:</strong>PUBDATE</p>\n'.replace('PUBDATE', pubdate))
        output_file.write('        <hr width = "80%" size = 5px>\n\n')
        count += 1

    #Finalize the output file.
    output_file.write("""
        </body>
    </html>
    """)

    output_file.close()

#Function to open the output file using a user's default browser
def doc_open():
    #Get the current directory
    current_directory = getcwd()
    #create the directory to open the html file
    full_directory = normpath(join(current_directory, 'output.html'))
    #print(url)
    webopen(full_directory)

#This source code is used from the client briefing and I acknowledge the owner of the code.
#This function is used to dowload the latest news.
def download_news():
    def download(url = 'http://www.wikipedia.org/',
                target_filename = 'download',
                filename_extension = 'xhtml'):

        # Import the function for opening online documents
        from urllib.request import urlopen

        # Import an exception raised when a web server denies access
        # to a document
        from urllib.error import HTTPError

        # Open the web document for reading
        try:
            web_page = urlopen(url)
        except ValueError:
            raise Exception("Download error - Cannot find document at URL '" + url + "'")
        except HTTPError:
            raise Exception("Download error - Access denied to document at URL '" + url + "'")
        except:
            raise Exception("Download error - Something went wrong when trying to download " + \
                            "the document at URL '" + url + "'")

        # Read its contents as a Unicode string
        try:
            web_page_contents = web_page.read().decode('UTF-8')
        except UnicodeDecodeError:
            raise Exception("Download error - Unable to decode document at URL '" + \
                            url + "' as Unicode text")

        # Write the contents to a local text file as Unicode
        # characters (overwriting the file if it already exists!)
        try:
            text_file = open(target_filename + '.' + filename_extension,
                            'w', encoding = 'UTF-8')
            text_file.write(web_page_contents)
            text_file.close()
        except:
            raise Exception("Download error - Unable to write to file '" + \
                            target_filename + "'")

        # Return the downloaded document to the caller
        return web_page_contents


    #-----------------------------------------------------------
    #
    # A main program to call the function.  If you want to download a
    # specific web document, add its URL as the function's argument.
    #
    from datetime import date
    from os.path import normpath, join
    from os import getcwd
    #Get the current date
    today = date.today().strftime('%B %d, %Y')
    days = {
        1: "Mon",
        2: "Tue",
        3: "Wed",
        4: "Thu",
        5: "Fri",
        6: "Sat",
        7: "Sun"
    }
    day = days[date.today().isoweekday()]
    #get current directory
    current_directory = getcwd()
    #Get full directory
    full_directory = normpath(join(current_directory,'InternetArchive'))
    file_name = full_directory + "\\Latest" 
    download('https://moxie.foxnews.com/feedburner/latest.xml', file_name)
# Front end part

#Create a window
archive_window = Tk()

#Give the window a title
archive_window.title('FOX Breaking News Archive')

#Get the current directory of the image file
file_name = "Fox_News_Channel_logo.png"
current_directory = getcwd()
image_file = normpath(join(current_directory, file_name))

#Create a label widget with the Fox news logo
logo_image = PhotoImage(file = image_file)
news_logo  = Label(archive_window, image = logo_image)
news_logo.grid(row = 0, column = 0)

#Declare global varialbes used to communicate between widgets

# When the user's selection is done, change this variable
selected_archive = None 
# Track the completion of selection  
selection_status = False  
# Track the completion of downloading new archive
download_status = False
# Track the completion of extraction status   
extraction_status = False 

#Declare a tuple of options user can choose
options = ('Mon, May 16, 2022', 'Tue, May 17, 2022', 'Wed, May 18, 2022', \
           'Thu, May 19, 2022', 'Fri, May 20, 2022', 'Sat, May 21, 2022', \
           'Sun, May 22, 2022','Latest')

#Create a list variable for the option list
options_var = StringVar(value = options)

#Call back functions that are invoked when the events occur by the user interaction

#Call back functions for display container
#This call back function is called when the user has selected an option
#This function is used to capture the user's selection
def select_archive(event):
    global selection_status, selected_archive
    #Get the index of current selected option from the list
    selected_index = option_listbox.curselection()
    #Get the option from the selected index and assign to selected_archive
    selected_archive = option_listbox.get(selected_index)
    #Change the text of the progess to show the user's choice.
    progress['text'] = 'You chose ' + selected_archive 
    
    #If the user choose 'The Latest Option' without downloading
    #Alert the user to download the new first
    #If not, change selection status to 'Completed'
    try:
        if selected_archive == 'Latest' and (not(download_status)):
            raise Exception('Download the news first before extracting')
        else:
            #Enalbe the extract button
            extract['state'] = NORMAL
            selection_status = True
            #Inform the user to extract the file
            progress['text'] += "\nNow, extract the file."
    except Exception as alert:   
        selection_status = False
        progress['text'] += '\n' + str(alert)
        extract['state'] = DISABLED
        output['state'] = DISABLED
    

#This call back function is called when the user pressed on the extraction button
#This function is used to create new html file depending on the user's selected option.
def create_file():
    try:
        global extraction_status, selection_status, selected_archive
        #To make sure the selection stage is completed
        assert selection_status == True
        #Call the backend function to extract xml files and create files
        create_html_file(selected_archive + '.xhtml')
        #Alter extraction_staus
        extraction_status = True
        #Enable the display button
        output['state'] = NORMAL
        #Display the completion of creating file
        progress['text'] = 'File is created!\nPress the display button'
    except AssertionError:
        extraction_status = False
        progress['text'] = "You've not choosed an archive"
        output['state'] = DISABLED
    except FileNotFoundError:
        extraction_status = False
        progress['text'] = 'Extraction failed.Please the choose the valid archive'
        output['state'] = DISABLED
    except TypeError:
        extraction_status = False
        progress['text'] = "You haven't chosen the date"
        output['state'] = DISABLED

#Check all the stages of interaction are completed       
def check_completion():
    global selection_status,extraction_status,download_status
    if (selection_status and extraction_status) or download_status:
        progress['text'] = 'Now choose a new archive.'

#This call back function is called when the user pressed on the display button
#This function is used to display the html file depending on the user's selection
def display_output():
    try:
        global selection_status, extraction_status, download_status
        #To make sure user has selected the option and extracted the files
        assert selection_status and extraction_status
        #Call the backednd function to display the content on the default browser
        doc_open()
        #Display the status of opening the file
        progress['text'] = 'Opening the file on the browser'
        check_completion()
        selection_status, extraction_status, download_status = (False, False, False)
    except AssertionError:
        progress['text'] = 'File cannot be displayed. Please check the previous steps again'

#This call back function is called when the user pressed the download button
#This function is used to download to latest news
def download_content():
        global selection_status,selected_archive, download_status
        #assert selected_archive == 'Latest'
        download['state'] = NORMAL
        download_news()
        download_status = True
        selection_status = True
        progress['text'] = 'File has been downloaded!\nNow extract the files now.'
        extract['state'] = NORMAL
    
#Containers
#Create a container that wraps the widget 
#that display the progress
#and the selection list
#Display Widget contains the Label widget and the Listbox widget
display = Frame(archive_window, height = 300, width = 300, background = 'white')

#Create the label widget for displaying the progess of procedure
progress = Label(
    display,
    font = ('Arial', 12, 'bold'),
    text = 'Please choose a date',
    width = 50,
    takefocus = False
    )

#Create the Listbox widget
option_listbox = Listbox(
    display,
    listvariable = options_var,
    height = 8,
    width  = 50,
    selectforeground='blue',
    font = ('Times', 12),
    takefocus = False 
)



#Creat a container that wraps the buttons
#that do actions(downloading, extracting, displaying)
# Action widget -> Extract Button, Download Button, Output Button
action = Frame(archive_window, height = 300, width = 300, background = 'white')
#Declare the font for all buttons
button_font = ('Arial', 12)
#Create the download button to download latest news
download = Button(
    action,
    font = button_font,
    text = 'Archive latest\nnews from the web',
    command = download_content
)
#Create the extract button to create a new html file
extract = Button(
    action,
    font = button_font,
    text = "Extract from archive\nto HTML news file",
    command = create_file
)

#Create the display button to display the website on the default browser.
output = Button(
    action,
    font = button_font,
    text = 'Display HTML\nnews file',
    command = display_output
)
#Positioning widgets
#Locate the containters on the window
display.grid(row = 0, column = 1, padx = 5)
action.grid(row = 0, column = 2, padx = 5)

#Locate the progess widget and listbox widget on the display containter widget
progress.grid(row = 0, column = 0, padx = 5, pady = 5)
option_listbox.grid(row = 1, column =0, padx = 5, pady = 5 )

#Locate the buttons on the action container widget
download.grid(row = 0, column = 0, padx = 5, pady = 5, sticky=W)
extract.grid(row = 1, column = 0, padx = 5, pady = 5, sticky=W)
output.grid(row = 2, column = 0, padx = 5, pady = 5, sticky=W)
#Bindings
#when the user selects an options, this binding calls the call_back function.
option_listbox.bind('<<ListboxSelect>>', select_archive)
#Start the event loop
archive_window.mainloop()
