import wolframalpha
client = wolframalpha.Client("JAJQQG-WXWA2W27UW")

import wikipedia

import PySimpleGUI as sg                      
sg.theme('DarkAmber')
# Define the window's contents
layout = [  [sg.Text("What would you like to know?")],     
            [sg.Input()],
            [sg.Button('Ok')],  [sg.Button('Cancel')] ]
# Create the window
window = sg.Window('KORONA | Quarantine Buddy 👌', layout)     

#speech-to-text initiation
import pyttsx3
engine = pyttsx3.init()

#upload
# Display and interact with the Window
# Wikipedia gives more detailed information of the search.
while True:
  event, values = window.read()
  if event in (None, 'Cancel'):
      break

  #brings up the information
  wiki_res = wikipedia.summary(values[0], sentences=2)
  wolfram_res = next(client.query(values[0]).results).text
  introduction_sentence = engine.say("Here's what we've found about" + values[0])
  call_wolfram = engine.say(wolfram_res)
  call_wiki = engine.say(wiki_res)
  
  try:
      introduction_sentence
      call_wolfram
      sg.PopupNonBlocking("Wolfram Result: ", wolfram_res, "Wikipedia Result: ", wiki_res)
  except wikipedia.exceptions.DisambiguationError:
      introduction_sentence
      call_wolfram
      sg.PopupNonBlocking(wolfram_res)
  except wikipedia.exceptions.PageError:
      introduction_sentence
      call_wolfram
      sg.PopupNonBlocking(wolfram_res)
  except:
      introduction_sentence
      call_wiki
      sg.PopupNonBlocking(wiki_res)
  
  engine.runAndWait()

# Finish up by removing from the screen
window.close()                                  


##additional notes for later;
# print (valuese[0])
# print(sg.tkinter.Tcl().eval('info patchlevel'))
