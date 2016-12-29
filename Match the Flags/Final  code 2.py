#Modification History
#    Start             End
#2/11/2016 5:30 am     2/11/2016 9:00 am  
#3/11/2016 6:32 pm     3/11/2016 9:30  pm  
#4/11/2016 12:30 am    4/11/2016 7:00 pm
#5/11/2016 3:30 pm     5/11/2016 9:00 pm
#6/11/2016 7:00 am     6/11/2016 10:00 am
#7/11/2016 6:00 am     7/11/2016 12:00 pm
#8/11/2016 3:00 pm     8/11/2016 9:30 pm
#9/11/2016 9:00 am     9/11/2016 12:00 pm
#9/11/2016 1:00 pm     9/11/2016 1:30 pm
#9/11/2016 6:00 pm     9/11/2016 7:15 pm
#10/11/2016 12:00 pm   10/11/2016 8:30 pm
#11/11/2016 8:00 am   11/11/2016 9:42 am
#11/11/2016 12:26 am   11/11/2016 3:15 pm
#13/11/2016 8:29 am   13/11/2016 9:30 pm
#13/11/2016 12:30 am   13/11/2016 2:00 pm
#13/11/2016 12:30 pm   13/11/2016 7:00 pm
#17/11/2016 6:30 pm   17/11/2016 12:00 am
#18/11/2016 5:30 am   18/11/2016 12:00 pm
#19/11/2016 6:05 am   19/11/2016 12:00 pm
#19/11/2016 3:00 pm   19/11/2016 12:00 am
#20/11/2016 12:36 pm   20/11/2016 6:00 pm
#21/11/2016 3:00 pm   21/11/2016 11:00 pm
#22/11/2016 4:00 pm   22/11/2016 9:00 pm
#23/11/2016 10:00 am   23/11/2016 3:00 pm
#24/11/2016 12:00 pm   23/11/2016 12:00 am
#25/11/2016 10:00 am   25/11/2016 4:00 pm
#25/11/2016 8:00 pm   25/11/2016 11:00 pm
import pygame
import random

#This is a dictionary of all the countries in Africa as keys and each key has a value of the country name, country flag image name, and the color of the coutry on the map
#This will be used throughout the game to match flags and check the answers
Africad={'Sudan':['Sudan','Sudan.png',(148,235,216,255),"It's in the North"],'Algeria':['Algeria',"Algeria.png",(112,146,190,255),"It's in the North"],
        'Angola':['Angola',"Angola.png",(218,20,35,255),"It's in the South"],
        'Benin':['Benin',"Benin.png",(247,181,186,255),"It's in the North"] ,
        'Botswana':['Botswana',"Botswana.png",(29,190,45,255),"It's in the South"] ,
        'Burkina Faso':['Burkina Faso','Burkina Faso.png',(148,250,133,255),"It's in the North"] ,
        'Burundi':['Burundi','Burundi.png',(201,253,19,255),"It's in the South"] ,
        'Cameroon':['Cameroon','Cameroon.png',(90,182,159,255),"It's in the North"],
        'Central African Republic':['Central African Republic','Central African Republic.png',(249,252,177,255),"It's in the South"],
        'Chad':['Chad','Chad.png',(255,127,39,255),"It's in the North"] ,'Democratic Republic of the Congo':['Democratic Republic of the Congo','Democratic Republic of the Congo.png',(168, 164, 251, 255),"It's near the centre"],
        'Congo':['Congo','Congo.png',(87,199,215,255),"It's near the centre"],'Djibouti':['Djibouti','Djibouti.png',(200,9,129,255),"It's in the North"],'Egypt':['Egypt','Egypt.png',(237,28,36,255),"It's in the North"],
        'Equatorial Guinea':['Equatorial Guinea','Equatorial Guinea.png',(142,181,91,255),"It's in the North"],
        'Eritrea':['Eritrea','Eritrea.png',(69,163,203,255),"It's near the centre"],'Ethiopia':['Ethiopia','Ethiopia.png',(255,174,201,255),"It's in the North"],
        'Gabon':['Gabon','Gabon.png',(69,10,224,255),"It's near the centre"],'Gambia':['Gambia','Gambia.png',(249,226,196,255),"It's in the South"],
        'Ghana':['Ghana','Ghana.png',(17,237,255,255,"It's in the South")],'Guinea':['Guinea','Guinea.png',(217,250,207,255),"It's in the South"],
        'Guinea-Bissau':['Guinea Bissau','Guinea Bissau.png',(112,186,103,255),"It's in the South"],
        'Kenya':['Kenya','Kenya.png',(221,22,250,255),"It's near the centre"],'Lesotho':['Lesotho','Lesotho.png',(242,182,149,255),"It's in the South"],
        'Liberia':['Liberia','Liberia.png',(184,105,166,255),"It's in the South"],'Libya':['Libya','Libya.png',(200,191,231,255),"It's in the North"],
        'Madagascar':['Madagascar','Madagascar.png',(100,196,4,255),"It's in the South"],'Malawi':['Malawi','Malawi.png',(180,14,155,255),"It's in the South"],
        'Mali':['Mali','Mali.png',(239,228,176,255),"It's in the North"],'Mauritania':['Mauritania','Mauritania.png',(185,122,87,225),"It's in the North"],
        'Morocco':['Morocco','Morocco.png',(34,177,76,255),"It's in the North"],'Mozambique':['Mozambique','Mozambique.png',(20,176,199,255),"It's in the South"],
        'Namibia':['Namibia','Namibia.png',(235,82,235,255)],'Niger':['Niger',"Niger.png",(136,0,21,255),"It's in the North"],
        'Nigeria':['Nigeria','Nigeria.png',(255,130,192,255),"It's in the North"],'Rwanda':['Rwanda','Rwanda.png',(253, 230, 19,255),"It's in the South"],
        'Senegal':['Senegal','Senegal.png',(162,89,200,255),"It's in the North"],'Sierra Leone':['Sierra Leone','Sierra Leone.png',(103,109,186,255),"It's in the North"],
        'Somalia':['Somalia','Somalia.png',(243,249,134,255),"It's near the centre"],'South Africa':['South Africa','South Africa.png',(181,222,169,255),"It's in the South"],
        'Tanzania':['Tanzania','Tanzania.png',(255,255,0,255),"It's in the South"],'Togo':['Togo','Togo.png',(180,233,248,255),"It's in the North"],
        'Tunisia':['Tunisia','Tunisia.png',(153,217,234,255),"It's in the North"],'Uganda':['Uganda','Uganda.png',(17,255,255,255),"It's near the centre"],
        'Zambia':['Zambia','Zambia.png',(221,211,96,255),"It's in the South"],'Zimbabwe':['Zimbabwe','Zimbabwe.png',(165,54,96,255),"It's in the South"],
         "Western Sahara":["Western Sahara","Western Sahara.png",(181, 230, 29, 255),"It's in the North"],'Mauritania':['Mauritania','Mauritania.png',(185, 122, 87, 255),"It's in the North"],
         "Cote d'Ivoire":["Cote d'Ivoire","Cote d'Ivoire.png",(193, 180, 248, 255),"It's in the North"]}
Oceaniad={'Australia':['Australia','Australia.png',(255,127,39,255),"It's a big country"],'New Zealand':['New Zealand','New Zealand.png',(34,177,76,255),"It's not a big country"],
          'Papua New Guinea':['Papua New Guinea','Papua New Guinea.png',(255,242,0,255),"It's not a big  country"]}
Europed={'Albania':['Albania','Albania.png',(180,254,180,255),"It's in the West"],'Armenia':['Armenia','Armenia.png',(0,82,217,255),"It's in the East"],
        'Austria':['Austria','Austria.png',(180,23,1,255),"It's in the West"],'Azerbaijan':['Azerbaijan','Azerbaijan.png',(157,90,186,255),"It's in the East"],
        'Belarus':['Belarus','Belarus.png',(188,232,252,255),"It's in the East"],'Belgium':['Belgium','Belgium.png',(184,22,112,255),"It's in the West"],
        'Bosnia and Herzegovina':['Bosnia and Herzegovina','Bosnia and Herzegovina.png',(208,208,4,255),"It's near the centre"],
        'Bulgaria':['Bulgaria','Bulgaria.png',(34,251,34,255),"It's in the East"],'Croatia':['Croatia','Croatia.png',(72,247,238,255),"It's near the centre"],'Cyprus':['Cyprus','Cyprus.png',(185,122,87,255),"It's in the East"],
        'Czech Republic':['Czech Republic','Czech Republic.png',(6,96,138,255),"It's near the centre"],'Denmark':['Denmark','Denmark.png',(239,228,176,255),"It's in the West"],
        'Estonia':['Estonia','Estonia.png',(200,191,231,255),"It's in the East"],'Finland':['Finland','Finland.png',(112,146,190,255),"It's near the centre"],'France':['France','France.png',(214,163,163,255),"It's in the West"],
        'Georgia':['Georgia','Georgia.png',(82,73,158,255),"It's in the East"],'Germany':['Germany','Germany.png',(34,177,76,255),"It's in the West"],'Greece':['Greece','Greece.png',(3,163,3,255),"It's in the East"],
        'Hungary':['Hungary','Hungary.png',(255,242,0,255),"It's near the centre"],'Iceland':['Iceland','Iceland.png',(136,0,21,255),"It's in the West"],'Ireland':['Ireland','Ireland.png',(252,252,75,255),"It's in the West"],
        'Italy':['Italy','Italy.png',(63,72,204,255),"It's near the centre"],'Latvia':['Latvia','Latvia.png',(254,180,169,255),"It's in the East"],'Lithuania':['Lithuania','Lithuania.png',(188,252,249,255),"It's in the East"],
        'Luxembourg':['Luxembourg','Luxembourg.png',(111,172,168,255),"It's in the West"],'Macedonia':['Macedonia','Macedonia.png',(140,15,176,255),"It's in the East"],'Turkey':['Turkey','Turkey.png',(87,146,198,255),"It's in the East"],
        'Malta':['Malta','Malta.png',(163,73,164,255),"It's in the West"],'Moldova':['Moldova','Moldova.png',(88,196,248,255),"It's in the East"],'Montenegro':['Montenegro','Montenegro.png',(233,179,249,255),"It's in the East"],
        'Netherlands':['Netherlands','Netherlands.png',(57,14,171,255),"It's in the West"],'Norway':['Norway','Norway.png',(228,90,31,255),"It's near the centre"],'Poland':['Poland','Poland.png',(39,107,39,255),"It's near the centre"],
        'Portugal':['Portugal','Portugal.png',(158,71,71,255),"It's in the West"],'Romania':['Romania','Romania.png',(254,68,41,255),"It's in the East"],'Serbia':['Serbia','Serbia.png',(99,46,239,255),"It's in the East"],
        'Slovakia':['Slovakia','Slovakia.png',(170,123,60,255),"It's near the centre"],'Slovenia':['Slovenia','Slovenia.png',(10,148,214,255),"It's in the West"],'Spain':['Spain','Spain.png',(255,127,39,255),"It's in the West"],
        'Sweden':['Sweden','Sweden.png',(153,217,234,255),"It's near the centre"],'Switzerland':['Switzerland','Switzerland.png',(254,254,182,255),"It's in the West"],'Ukraine':['Ukraine','Ukraine.png',(0,162,232,255),"It's in the East"],
        'Ksovo':['Ksovo','Ksovo.png',(216,184,141,255),"It's in the Eastt"],'United Kingdom':['United Kingdom','United Kingdom.png',(255,201,14,255),"It's in the West"],'Russia':['Russia','Russia.png',(181,230,29,255),"It's in the East"]}
Asiad={'Afghanistan':['Afghanistan','Afghanistan.png',(81,52,243,255),"It's in the West"],'Bangladesh':['Bangladesh','Bangladesh.png',(99,241,31,255),"It's in the East"],
    'Bhutan':['Bhutan','Bhutan.png',(185,251,248,255),"It's in the East"],'Burma':['Burma','Burma.png',(112, 146, 190, 255),"It's in the East"],'Cambodia':['Cambodia','Cambodia.png',(194,185,251,255),"It's in the East"],
    'China':['China','China.png',(255,127,39,255),"It's near the centre"],'East Timor':['East Timor','East Timor.png',(128,0,128,255),"It's in the East"],'India':['India','India.png',(215,2,2,255),"It's near the centre"],
    'Indonesia':['Indonesia','Indonesia.png',(251,219,166,255),"It's in the East"],'Iran':['Iran','Iran.png',(201,46,239,255),"It's in the West"],'Iraq':['Iraq','Iraq.png',(152,1,1,255),"It's in the West"],
    'Japan':['Japan','Japan.png',(239,228,176,255),"It's in the East"],'Jordan':['Jordan','Jordan.png',(216,146,82,255),"It's in the West"],'Kazakhstan':['Kazakhstan','Kazakhstan.png',(255,201,14,255),"It's near the centre"],
    'North Korea':['North Korea','North Korea.png',(34,177,76,255),"It's in the East"],'South Korea':['South Korea','South Korea.png',(0,162,232,255),"It's in the East"],
    'Kuwait':['Kuwait','Kuwait.png',(121,79,128,255),"It's in the West"],'Kyrgyzstan':['Kyrgyzstan','Kyrgyzstan.png',(242,64,153,255),"It's near the centre"],
    'Laos':['Laos','Laos.png',(185,122,87,255),"It's in the East"],
    'Lebanon':['Lebanon','Lebanon.png',(3,166,214,255),"It's in the West"],
    'Malaysia':['Malaysia','Malaysia.png',(7,135,129,255),"It's in the East"],
    'Mongolia':['Mongolia','Mongolia.png',(153,217,234,255),"It's in the East"],
    'Nepal':['Nepal','Nepal.png',(186,249,155,255),"It's in the East"],
    'Oman':['Oman','Oman.png',(40,91,46,255),"It's in the West"],
    'Pakistan':['Pakistan','Pakistan.png',(139,14,171,255),"It's near the centre"],'Palestine':['Palestine','Palestine.png',(0,217,173,255),"It's in the West"],
    'Philippines':['Philippines','Philippines.png',(63,72,204,255),"It's in the East"],
    'Qatar':['Qatar','Qatar.png',(1,233,13,255),"It's in the West"],
    'Russia':['Russia','Russia.png',(181,230,29,255),"It's a very big country"],
    'Saudi Arabia':['Saudi Arabia','Saudi Arabia.png',(237, 188, 250, 255),"It's in the West"],
    'Sri Lanka':['Sri Lanka','Sri Lanka.png',(53,145,9,255),"It's in the East"],
    'Syria':['Syria','Syria.png',(149,88,34,255),"It's in the West"],
    'Tajikistan':['Tajikistan','Tajikistan.png',(235,199,167,255),"It's in the West"],
    'Thailand':['Thailand','Thailand.png',(30,9,149,255),"It's in the East"],
    'Turkey':['Turkey','Turkey.png',(87,146,198,255),"It's in the West"],
    'Turkmenistan':['Turkmenistan','Turkmenistan.png',(37,75,109,255),"It's in the West"],
    'United Arab Emirates':['United Arab Emirates','United Arab Emirates.png',(242,248,50,255),"It's in the West"],
    'Uzbekistan':['Uzbekistan','Uzbekistan.png',(163,12,87,255),"It's in the West"],
    'Vietnam':['Vietnam','Vietnam.png',(163,73,164,255),"It's in the East"],
    'Yemen':['Yemen','Yemen.png',(194,228,198,255),"It's in the West"],'Taiwan':['Taiwan','Taiwan.png',(200,191,231,255),"It's in the East"]}
SAd={'Argentina':['Argentina','Argentina.png',(0,162,232,255),"It's in the South"],
    'Bolivia':['Bolivia','Bolivia.png',(237,28,36,255),"It's near the centre"],
    'Brazil':['Brazil','Brazil.png',(255,127,39,255),"It's near the centre"],
    'Chile':['Chile','Chile.png',(163,73,164,255),"It's in the South"],
    'Colombia':['Colombia','Colombia.png',(239,228,176,255),"It's in the North"],
    'Ecuador':['Ecuador','Ecuador.png',(34,177,76,255),"It's in the North"],
    'Guyana':['Guyana','Guyana.png',(181,230,29,255),"It's in the North"],
    'Paraguay':['Paraguay','Paraguay.png',(255,201,14,255),"It's in the South"],
    'Peru':['Peru','Peru.png',(63,72,204,255),"It's near the centre"],
    'Suriname':['Suriname','Suriname.png',(153,217,234,255)],
    'Uruguay':['Uruguay','Uruguay.png',(200,191,231,255),"It's in the South"],
    'Venezuela':['Venezuela','Venezuela.png',(255,242,0,255),"It's in the North"]}
NAd={'Belize':['Belize','Belize.png',(184,245,219,255),"It's in the South"],
    'Canada':['Canada','Canada.png',(255,201,14,255),"It's in the North"],
    'Costa Rica':['Costa Rica','Costa Rica.png',(220,175,220,255),"It's in the South"],
    'Cuba':['Cuba','Cuba.png',(66,227,158,255),"It's in the South"],
    'Dominican Republic':['Dominican Republic','Dominican Republic.png',(163,73,164,255),"It's in the South"],
    'El Salvador':['El Salvador','El Salvador.png',(56,192,237,255),"It's in the South"],
    'Guatemala':['Guatemala','Guatemala.png',(153,217,234,255),"It's in the South"],
    'Haiti':['Haiti','Haiti.png',(0,6,247,255),"It's in the South"],
    'Honduras':['Honduras','Honduras.png',(0,128,255,255),"It's in the South"],
    'Jamaica':['Jamaica','Jamaica.png',(205,181,139,255),"It's in the South"],
    'Mexico':['Mexico','Mexico.png',(255,242,0,255),"It's near the centre"],
    'Nicaragua':['Nicaragua','Nicaragua.png',(28,193,123,255),"It's in the South"],
    'Panama':['Panama','Panama.png',(254,196,167,255),"It's in the South"],
    'United States of America':['United States of America','United States of America.png',(255,127,39,255),"It's near the centre"]}
dictionaries=[Africad,Oceaniad,Europed,Asiad,SAd,NAd]#make a list of the dictionaries used
pygame.init()
Dwidth=1000#set the display width of the window
Dheight=600 #set the display height of the window
midWidth=Dwidth/2#set the mid point of the width of the window
midHeight=Dheight/2#set the mid point of the height of the window
wnd =pygame.display.set_mode((Dwidth,Dheight))#create a new window(surface)
Afrcol = (249,152,64,255)#color for Africa
Ascol= (111,196,98,255)#color for Asia
Ecol = (250,199,63,255)#color for Europe
NAcol=(255,0,0,255)#color for North America
SAcol=(0,183,0,255)#color for South America
Auscol=(201,251,164,255)#color for Oceania
#Default colors used
mainBlue=(45,100,245)
lightBlue=(45,100,235)
green=(0,225,0)
black=(0,0,0)
red=(255,0,0)
white=(255,255,255)
#choose a random continent
Continentd=random.choice(dictionaries)
keys = Continentd.keys()#get a list of the keys in the dictionary
key =random.choice(keys)#get a random key from the dictionary
value = Continentd[key]#get the list of values for that country
img = value[1]#get the image for that country
AfricaValues=Africad.values()#create a new list to put the values of Africa dictionary in
OceaniaValues=Oceaniad.values()
EuropeValues=Europed.values()
AsiaValues=Asiad.values()
NAValues=NAd.values()
SAValues=SAd.values()
#States that will be used to go from one  window to the other
Hints=3
Hint1=False
Hint2=False
Hint3=False
mapFont = "segoeui" #Default font
wrldMap=pygame.image.load("OtherPics/world map 3.bmp")
wrldMap=pygame.transform.scale(wrldMap,(700,600))
play = False
intro = True
instructions=False
#Continents
Africa = False
Oceania=False
Europe=False
Asia=False
NA=False
SA=False
End=False
isClicked = False
isClicked2=False
#Lives
Lives=5
Live1=True
Live2=True
Live3=True
Live4=True
Live5=True
leave=False
#instructions
instruction1=False
instruction3=False
instruction4=False
instruction5=False
instruction6=False
instruction7=False
instruction2=False
instruction3=False
showgrid=False
showAnswer=False #Will be used to display the correct answer if true
#current=None
oldCountry=""#Will be used to store the name of the previous country
Africaw=None
current=""#used to store the current state to go back to it after pausing the game
Score=0#current score
lastScore=0#score before the game ended
#Variable used to control frame per seconds and the timer
frame_count = 0
frame_rate =20
time=180
start_time = time
clock = pygame.time.Clock()#This function will be used to control the frequency at which the window is updated
#This function will be used to display images
def insrtPic(pic,x,y,xScale=None,yScale=None):
    img=pygame.image.load(pic)#load the picture
    if xScale!=None and yScale!=None: #if there is a scale specified
        img=pygame.transform.scale(img,(xScale,yScale))#transform image
    wnd.blit(img,(x,y))#blit the image  on the screen
def Dtext(text,x,y,width=None,height=None,col=white,bg=None,size=30,font=mapFont):#This funtion will be used to display text on the screen or text on a button
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,instructions
    font=pygame.font.SysFont(font,size)#set the font and font size
    if bg!=None:
        word=font.render(text, True,col,bg)#set the text and text color that will be displayed
    else:
        word=font.render(text, True,col)#set the text and text color that will be displayed
    txtWidth = word.get_width()#Get the width of the word
    txtHeight = word.get_height()#get the height of the word
    if width!=None :#if there is width specified (when in a button)
        x= ((x+x+width)/2)-(txtWidth/2)#blit the text in the centre
    if height !=None:#if there is hight specified (when in a button)
        y= ((y+y+height)/2)-(txtHeight/2)#blit the text in the centre
    wnd.blit(word,(x,y))#location of the text on the screen

def button(text,x,y,width=150,height=75,action=None,txtCol=white,InactiveCol=lightBlue,ActiveCol=green,font=mapFont,fontSize=30,txtBg=None):#This function will be used to create a button with options:
    global BG1,BG2,BG1col,BG2col,play,intro,instructions,Europe,Africa,SA,NA,Asia,Oceania,Hints,End,isClicked,Hint1,Hint3,Hint2,time,start_time,leave
    global Lives,Live1,Live2,Live3,Live4,Live5,showgrid,current,instruction1,instruction2,instruction3,instruction4,instruction5,instruction6,instruction7,instruction8
    #text to be written on the button,x,y coordinates, width and height of the button,color when the button is not active,color when the mouse is hovering over the button,font of the text written on the button and the size of the text
    cur = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if (x + width) > cur[0] > x and (y + height) > cur[1] > y:#if the pointer is within the coordinates of the button
        pygame.draw.rect(wnd,ActiveCol,(x,y,width,height))#Make it change color (default green) (draws a rectangle)
        if click[0]==1:#if mouse is pressed
            isClicked = True
        else:
            if isClicked:
                # mouse is released
                isClicked = False
                if action!=None:
                    #Exit the whole game
                    if action == "quit":
                        pygame.quit()
                        quit()
                    #Start the game (playloop)
                    if action=="Single Play":                        
                        instructions = False
                        play=True
                        Africa=False
                        Europe=False
                        Asia= False
                        NA=False
                        SA=False
                        Oceania=False
                        pygame.time.delay(500)
                    #Exit the game, and go to the intro screen
                    if action=="Back2intro":
                        intro =True
                        play=False
                        instructions = False
                        End=False
                    #Go tot the instructions loop
                    if action=="instructions":                  
                        intro =False
                        instructions = True
                    #Resume the game
                    if action=="Back2play":
                        Africa=False
                        Europe=False
                        Asia= False
                        NA=False
                        SA=False
                        Oceania=False
                        intro=False
                        End=False
                        play=True
                    #When the Hints button is clicked: subtract a life and display the hint
                    if action=="hint1Activate":                        
                        if Lives<0:
                            Lives=0
                        if Lives==0:
                            Hints=0                     
                        Hints=Hints-1                        
                        if Hints>=0:
                            Lives=Lives-1                        
                        if Lives==4:
                            Live5=False
                        if Lives==3:
                            Live4=False
                        if Lives==2:
                            Live3=False
                        if Lives==1:
                            Live2=False
                        if Lives==0:
                            Live1=False
                        if Hints==2:                        
                            Hint1=True
                        elif Hints==1:
                            Hint2=True
                        elif Hints==0:
                            Hint3=True
                        if Lives==0:
                            Hints=0                        
                    #will be used to show the grided images 
                    if action=="showthegrid":
                        if SA:
                            insrtPic("OtherPics/ColoredSAg.bmp",50,50,600,525)
                        elif Africa:
                            insrtPic("OtherPics/Afrcolorborder.bmp",0,0,700,600)
                        elif Europe:                          
                            insrtPic("OtherPics/ColoredEurope.bmp",0,0,700,600)
                        elif Asia:
                            insrtPic("OtherPics/Asiacolor.bmp",0,0,700,600)
                        elif NA:
                            insrtPic("OtherPics/ColoredNA.bmp",50,50,600,525)
                    if action=="exitGamenow":#To display the pause window when the pause button is clicked
                        
                        if Africa is True:
                            current='Africaw'
                        elif Asia:
                            current='Asiaw'
                        elif NA:
                            current='NAw'
                        elif SA:
                            current='SAw'
                        elif Oceania:
                            current='Oceaniaw'
                        elif Europe:
                            current='Europew'
                        elif play:
                            current='playw'
                        leave=True
                    if action=="exitall":#will be used to go back to the main menu
                        intro=True
                        play=False
                        leave=False
                    if action=="resume":#will be used to resume the game
                        intro=False
                        leave=False
                        if current == 'Africaw':
                            Africa=True
                        elif current == 'Europew':
                            Europe=True
                        elif current=='NAw':
                            NA=True
                        elif current=='SAw':
                            SA = True
                        elif current=='Oceaniaw':
                            Ociania=True
                        elif current=='playw':
                            play=True
                        elif  current=='Asiaw':
                            Asia=True                        
                     #will be used to show the gridded images   
                    if action=="gridactivate":
                        showgrid=True
                    #will be used to use the ungridded images
                    if action=="giddeactivate":
                        showgrid=False
                    #will be used to navigate through instructions
                    if action=="instruction1":
                        instruction1=True
                    if action=="instruction2":
                        instruction2=True
                    if action=="instruction3":
                        instruction3=True
                    if action=="instruction4":
                        instruction4=True
                    if action=="instruction5":
                        instruction5=True
                    if action=="instruction6":
                        instruction6=True
                    if action=="instruction7":
                        instruction7=True
                    if action=="instruction8":
                        instruction8=True

    else:
        pygame.draw.rect(wnd,InactiveCol,(x,y,width,height))#Make the color blue again if the pointer is not on the button
    Dtext(text,x,y,width,height,txtCol,txtBg,fontSize,font)#Blit the desired text on the button
#This screen will show when it runs out of time
def endScreen():#screen to be displayed when the player runs out of time
    global Africa,NA,SA,Europe,Asia,Oceania,intro,play,instructions,wnd,midHeight,midWIdth,Score,lastScore,mainBlue
    #Disable  other loops
    Africa=False
    NA=False
    Europe=False
    Asia=False
    Oceania=False
    SA=False
    play=False
    intro=False
    #store the scores
    lastScore=Score
    #Fill the background with blue
    wnd.fill(mainBlue)
    #Display text "time's up"
    Dtext("Time's up :(",midWidth-110,midHeight-100,size=70)
    #Display the score
    Dtext("Your Score is : "+str(Score),midWidth-50,midHeight+25,size=20)
    #Button to the main menu
    button("Main Menu",450,400,action="Back2intro")
def exitScreen():#Screen to be displayed when paused
    global Africa,NA,SA,Europe,Asia,Oceania,intro,play,instructions,wnd,midHeight,midWIdth,Score,lastScore
    Africa=False
    NA=False
    Europe=False
    Asia=False
    Oceania=False
    SA=False
    play=False
    intro=False
    #store the score
    lastScore=Score
    #Fill the background with blue
    wnd.fill(mainBlue)
    Dtext("Paused",midWidth-125,midHeight-100,size=60)
    Dtext("Your Score is : "+str(Score),midWidth-100,midHeight+25,size=20)
    button("Exit",225,400,action="exitall")
    button("Back to Game",600,400,210,action="resume")  
    

def timer():
    global start_time,frame_count,frame_rate,wnd,End
    #print frame_count
    total_seconds = start_time - (frame_count / frame_rate)
    if total_seconds < 0:#Exit game if time is zero (Time's up window)
        End=True
        frame_count=0
        total_seconds = 0

    # Divide by 60 to get total minutes
    minutes = total_seconds / 60
 
    # Use modulus (remainder) to get seconds
    seconds = total_seconds % 60
 
    # Use python string formatting to format in leading zeros
    output_string = "Time left: {0:02}:{1:02}".format(minutes, seconds)
    # Blit to the screen
    Dtext(output_string,2,17,font='bell',size=20)
    frame_count += 1 
#http://programarcadegames.com/python_examples/f.php?file=timer.py
    
def addLbl(cur,col):#get the current location of the pointer and the color at that point
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,Africad
    wnd.blit(wrldMap,(0,0))#blit he continent pic on the screen
    if col==Afrcol or (324<cur[0]<382 and 311<cur[1]<400): #if the pointer is pointing at Africa
        font=pygame.font.SysFont(mapFont,25)#set the font and font size of the label
        word=font.render("Africa", True,(0,0,0),Afrcol)#set the text that will be displayed
        wnd.blit(word,(320,304))#put the text on the surface on Africa      
    if col==Ascol or (457<cur[0]<522 and 147<cur[1]<187):#if the pointer is pointing at Asia
        font=pygame.font.SysFont(mapFont,25)#set the font and font size of the label
        word=font.render("Asia", True,(0,0,0),Ascol)#set the text that will be displayed, its color and its background color
        wnd.blit(word,(470,152))#put the text on the surface on Asia
    if col==Ecol or (345<cur[0]<397 and 177<cur[1]<193):#if the pointer is pointing at Europe
        font=pygame.font.SysFont(mapFont,15)#set the font and font size of the label
        word=font.render("Europe", True,(0,0,0),Ecol)#set the text that will be displayed, its color and its background color
        wnd.blit(word,(350,175))#put the text on the surface on Europe
    if col==NAcol or (97<cur[0]<167 and 212<cur[1]<259):#if the pointer is pointing at North America
        font=pygame.font.SysFont(mapFont,15)#set the font and font size of the label
        word=font.render("North", True,(0,0,0),NAcol)#set the text that will be displayed, its color and its background color
        wnd.blit(word,(110,212))#put the text on the surface on North America
        word=font.render("America", True,(0,0,0),NAcol)#set the text that will be displayed, its color and its background color
        wnd.blit(word,(110,240))#put the text on the surface on North America
    if col==SAcol or (188<cur[0]<241 and 407<cur[1]<457):#if the pointer is pointing at North America
        font=pygame.font.SysFont(mapFont,15)#set the font and font size of the label
        word=font.render("South", True,(0,0,0))#set the text that will be displayed, its color and its background color
        wnd.blit(word,(200,408))#put the text on the surface on North America
        font=pygame.font.SysFont(mapFont,12)#set the font and font size of the label
        word=font.render("America", True,(0,0,0))#set the text that will be displayed, its color and its background color
        wnd.blit(word,(195,438))#put the text on the surface on North America
    if col==Auscol or (557<cur[0]<619 and 466<cur[1]<484):#if the pointer is pointing at Europe
        font=pygame.font.SysFont(mapFont,15)#set the font and font size of the label
        word=font.render("Oceania", True,(0,0,0),Auscol)#set the text that will be displayed, its color and its background color
        wnd.blit(word,(560,466))#put the text on the surface on Europe
 
def viewContinent():#This function will be used to view single continents when being clicked from the world map
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,instructions,Africa,cur,col,click,Africad,AfricaColors,Oceania,Europe,Asia,NA,SA,isClicked2
    cur = pygame.mouse.get_pos()#get the position of the pointer
    col=wnd.get_at(cur)#get the color at the position of the pointer
    click = pygame.mouse.get_pressed()#gets a tuple of the mouse clicks (0 is not clicked and 1 is a click)
    if click[0]==1: #if right click 
        isClicked2=True
    else:#if click is released
        if isClicked2:
            isClicked2=False
            if col==Afrcol or (324<cur[0]<382 and 311<cur[1]<400):
                play=False#close the playLoop
                Africa=True#call AfricaLoop            
            elif col==Auscol or (457<cur[0]<522 and 147<cur[1]<187):#if right click and on Oceania(color)
                play=False#close the playLoop
                Africa=False#close AfricaLoop
                Oceania=True
            elif col==Ecol or (345<cur[0]<397 and 177<cur[1]<193):#if right click and on Europe(color)
                play=False#close the playLoop
                Africa=False#close AfricaLoop
                Oceania=False
                Europe=True
            elif col==Ascol or (557<cur[0]<619 and 466<cur[1]<484):#if right click and on Oceania(color)
                play=False#close the playLoop
                Africa=False#close AfricaLoop
                Oceania=False
                Europe=False
                Asia=True
            elif col==NAcol or (97<cur[0]<167 and 212<cur[1]<259):#if right click and on Oceania(color)
                play=False#close the playLoop
                Africa=False#close AfricaLoop
                NA=True
            elif col==SAcol or (188<cur[0]<241 and 407<cur[1]<457):#if right click and on Oceania(color)
                play=False#close the playLoop
                Africa=False#close AfricaLoop
                SA=True


#Intro loop ,resets all the values used in the game (score,hints,lives) and display the menu
def introLoop():
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,instructions,Africad,Score,Live1,Live2,Live3,Live4,Live5,start_time,time,Hint1,Hint2,Hints,Hint3
    global Continentd,key,keys,img,value,Lives,showAnswer,showgrid,frame_count,lastScore,white
    wnd.fill(mainBlue)
    #This will be  used to display the high score
    readScore=open("Score.txt","r")#open score file to read
    filedocs = readScore.readlines()#read the lines
    if (len(filedocs)==0):#if file is empty,write the score in it
        writeFile=open("Score.txt","a")#open file to write the high score in it 
        writeFile.write(str(lastScore))
        writeFile.close()

    for score1 in filedocs:#Read the score in the file 
        if lastScore>int(score1):#if the previous score is less than the current score make the current the high score
            writeFile=open("Score.txt","w")#open file to write the high score in it 
            writeFile.write(str(lastScore))#write the score in the file
            writeFile.close()#close the file 
    readScore2=open("Score.txt","r")#open the file and read the high score
    filedocs2 = readScore2.readlines()    
    HighScore=filedocs2[0]#store the high score in a variable 
    Dtext("High Score : "+str(HighScore),400,150,size=25,col=white)#display the high score
    BG1=False
    BG2=False
  #Lives used
    Lives=5
    Live1=True
    Live2=True
    Live3=True
    Live4=True
    Live5=True
    Score=0
    Hints=3
    Hint1=False
    Hint2=False
    Hint3=False
    showAnswer=False
    showgrid=False
    start_time=time
    frame_count=0
    Continentd=random.choice(dictionaries)#choose a randome dictionary
    keys = Continentd.keys()#get a list of the keys in the dictionary
    key =random.choice(keys)#get a random key from the dictionary
    value = Continentd[key]#get the list of values for that country
    img = value[1]#get the image for that country
    #Buttons 
    button("New Game",midWidth-100,midHeight-100,200,100, action= "Single Play")#start game
    button("Instructions",midWidth-100,midHeight,200,100,action="instruction1")#see instructions
    button("Exit",midWidth-100,midHeight+100,200,100,action="quit")#exit game 
#The window with continents    
def playLoop():
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,img,Africad,AfricaColors,Score, click,Hints
    cur = pygame.mouse.get_pos()
    col=wnd.get_at(cur)
    click = pygame.mouse.get_pressed()
    addLbl(cur,col)
    viewContinent()#this is to move to a continent when clicking on it 
    wnd.fill(white,(700, 0,300, 600))
    pygame.draw.rect(wnd,black,(745,40,210,120))#Makes a rectangular background behind the flag image
    insrtPic('Flags/'+img,750,50,200,100)#display the random flag picture
    if Hints<0:
        Hints=0
    InHint= Hints#used show number of hints left
    button("Hints "+str(InHint),850,425,150,75,action="hint1Activate")#hint button
#instruction loops to be called to view a sequence of instructions (each loop has instruction picture and some buttons), Next go to next instruction,Back go to the previous
#Main Menu, goes to the intro  screen
#Back button goes to the previous instruction
def instr1():
    global play,intro,wnd,wrldMap,instructions,Africad,Score
    wnd.fill(white)
    insrtPic("OtherPics/ss1.jpg",0,0,900,600)
    button("Main Menu",850,500,150,75,action="Back2intro")
    button("Next",850,415,150,75,action="instruction2")
def instr2():
    wnd.fill(white)
    insrtPic("OtherPics/ss2.jpg",0,0,900,600)
    button("Main Menu",850,500,150,75,action="Back2intro")
    button("Next",850,340,150,75,action="instruction3")
    button("Back",850,415,150,75,action="instruction1")

def instr3():
    wnd.fill(white)
    insrtPic("OtherPics/ss4.jpg",0,0,900,600)
    button("Main Menu",850,500,150,75,action="Back2intro")
    button("Next",850,340,150,75,action="instruction4")
    button("Back",850,415,150,75,action="instruction2")
def instr4():
    wnd.fill(white)
    insrtPic("OtherPics/ss5.jpg",0,0,900,600)
    button("Main Menu",850,500,150,75,action="Back2intro")
    button("Next",850,340,150,75,action="instruction5")
    button("Back",850,415,150,75,action="instruction3")
def instr5():
    wnd.fill(white)
    insrtPic("OtherPics/ss6.jpg",0,0,900,600)
    button("Main Menu",850,500,150,75,action="Back2intro")
    button("Next",850,340,150,75,action="instruction6")
    button("Back",850,415,150,75,action="instruction4")
def instr6():
    wnd.fill(white)
    insrtPic("OtherPics/ss7.jpg",0,0,900,600)
    button("Main Menu",850,500,150,75,action="Back2intro")
    button("Next",850,340,150,75,action="instruction7")
    button("Back",850,415,150,75,action="instruction5")
def instr7():
    insrtPic("OtherPics/ss8.jpg",0,0,900,600)
    button("Main Menu",850,500,150,75,action="Back2intro")
    button("Next",850,340,150,75,action="instruction8")
    button("Back",850,415,150,75,action="instruction6")
def instr8():
    wnd.fill(white)
    insrtPic("OtherPics/ss9.jpg",0,0,900,600)
    button("Main Menu",850,500,150,75,action="Back2intro")
    button("Back",850,415,150,75,action="instruction3")
#function used when africa is clicked
def AfricaLoop():
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,instructions,Africa,value,key,Africad,AfricaColors,keys,AfricaValues,Score,midWidth,midHeight,img,isClicked2
    global Continentd,Oceaniad,Asiad,NAd,SAd,Africad,Europed,Hints,Hint1,Hint3,Lives,oldCountry,showAnswer,Hint2
    cur = pygame.mouse.get_pos()#get the position of the pointer
    col=wnd.get_at(cur)#get the color at the position of the pointer
    click = pygame.mouse.get_pressed()#gets a tuple of the mouse clicks (0 is not clicked and 1 is a click)
    wnd.fill(white)#make a white brackground
    button("Back",850,500,150,75,action="Back2play")
    #if show grid is true show the gridded  image 
    if showgrid:
        insrtPic("OtherPics/Afrcolorborderg.bmp",0,0,700,600)
    else:
        insrtPic("OtherPics/Afrcolorborder.bmp",0,0,700,600)
    pygame.draw.rect(wnd,black,(745,40,210,120))#Makes a rectangular background behind the flag image
    #if hints are less than 0 make it equal to 0
    if Hints<0:
        Hints=0
    InHint= Hints#used show number of hints left
    button("Hints "+str(InHint),850,425,150,75,action="hint1Activate")#hint button
    #This loop will be used to display the country name as the pointer hover over it
    for index in range(len(AfricaValues)):#loop through the values in Africad dictionary
        countryValue= AfricaValues[index]#save the index of the value in a variable
        if col==countryValue[2]:#if the color the mouse is pointing at is in the list,blit the country name on the screen
            font=pygame.font.SysFont("ebrima",20,bold=True)#set the font and font size of the label 
            word=font.render(countryValue[0], True,black)
            wnd.blit(word,cur)#put the text on the surface on Asia
    if click[0]==1:
            if col==value[2] and Continentd==Africad:#If the country and the continent are correct
                Dtext("Correct",midWidth,midHeight,size=50,col=green)
                oldCountry=value[0]
                showAnswer=True #Will be used to display the correct answer if true
                Score=Score+1#increase the score by 1 if corrrect
                Continentd=random.choice(dictionaries)#choose a new random country
                keys = Continentd.keys()#get a list of the keys in the dictionary
                key =random.choice(keys)#get a random key from the dictionary
                value = Continentd[key]#get the list of values for that country
                img = value[1]#get the image for that country
                #Remove the hints from the screen
                Hint1=False
                Hint2=False
                Hint3=False
                Hints=3
                pygame.time.delay(500)#wait for 0.5 of a second
            elif col!=value[2] and col!=white and col!=mainBlue and col!=green and cur[0]<700:#if the color is wrong
                Dtext("Wrong",midWidth,midHeight,size=50,col=red)
                oldCountry=value[0]
                showAnswer=True #Will be used to display the correct answer if true
                Continentd=random.choice(dictionaries)#choose a new random country
                keys = Continentd.keys()#get a list of the keys in the dictionary
                key =random.choice(keys)#get a random key from the dictionary
                value = Continentd[key]#get the list of values for that country
                img = value[1]#get the image for that country
                Hint1=False#remove hints from the display
                Hint2=False
                Hint3=False
                Hints=3
                pygame.time.delay(500)#wait for 0.5 of a second
            elif Continentd==Africad and col!=white and col!=mainBlue and col!=green and cur[0]<700:#if the wrong continent and not the buttons
                Dtext("Wrong",midWidth,midHeight,size=50,col=red)
                oldCountry=value[0]
                showAnswer=True #Will be used to display the correct answer if true
                Continentd=random.choice(dictionaries)#choose a new random country
                keys = Continentd.keys()#get a list of the keys in the dictionary
                key =random.choice(keys)#get a random key from the dictionary
                value = Continentd[key]#get the list of values for that country
                img = value[1]#get the image for that country
                Hint1=False#remove hints from the display
                Hint2=False
                Hint3=False
                Hints=3
                pygame.time.delay(500)#wait for 0.5 of a second
#Function called when Oceania is clicked
def OceaniaLoop():
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,instructions,Africa,value,key,Africad,AfricaColors,keys,Score,midWidth,midHeight,img,OceaniaValues
    global Continentd,Oceaniad,Asiad,NAd,SAd,Africad,Europed,Hints,Hint1,Hint3,Lives,oldCountry,showAnswer,Hint2
    cur = pygame.mouse.get_pos()#get the position of the pointer
    col=wnd.get_at(cur)#get the color at the position of the pointer
    click = pygame.mouse.get_pressed()#gets a tuple of the mouse clicks (0 is not clicked and 1 is a click)
    wnd.fill(white)#white background
    button("Back",850,500,150,75,action="Back2play")#This button will be used to the continents view
    insrtPic("OtherPics/Oceaniacolored.bmp",0,0,700,600)
    pygame.draw.rect(wnd,black,(745,40,210,120))#Makes a rectangular background behind the flag image
    #if hints are less than 0 make it equal to 0
    if Hints<0:
        Hints=0
    InHint= Hints#used show number of hints left
    button("Hints "+str(InHint),850,425,150,75,action="hint1Activate")#hint button
    #This loop will be used to display the country name as the pointer hover over it
    for index in range(len(OceaniaValues)):#loop through the values in Africad dictionary
        countryValue= OceaniaValues[index]#save the index of the value in a variable
        if col==countryValue[2]:#if the color the mouse is pointing at is in the list,blit the country name on the screen
            font=pygame.font.SysFont("ebrima",20,bold=True)#set the font and font size of the label 
            word=font.render(countryValue[0], True,black)
            wnd.blit(word,cur)#put the text on the surface on Asia
    if click[0]==1:#if mouse is clicked
        if Continentd!=Oceaniad and col!=white and col!=mainBlue and col!=green and cur[0]<700 and value[0]!="Turkey" and value[0]!="Russia":#if wrong continent
            oldCountry=value[0]#store the name of the previous country in this variable
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Wrong",midWidth,midHeight,size=50,col=red)
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
        elif col==value[2]:#if the country is correct
            oldCountry=value[0]#store the name of the previous country in this variable
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Correct",midWidth,midHeight,size=50,col=green)
            Score=Score+1#increase the score by 1 if corrrect
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
        elif col!=value[2] and col!=white and col!=mainBlue and col!=green and cur[0]<700:#if the color is wrong or wrong continent and not the buttons
            oldCountry=value[0]#store the name of the previous country in this variable
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Wrong",midWidth,midHeight,size=50,col=red)
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
#function used when europe is clicked
def EuropeLoop():
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,instructions,Africa,value,key,Africad,AfricaColors,keys,Score,midWidth,midHeight,img,EuropeValues
    global Continentd,Oceaniad,Asiad,NAd,SAd,Africad,Europed,Hints,Hint1,Hint3,Lives,oldCountry,showAnswer,Hint2
    cur = pygame.mouse.get_pos()#get the position of the pointer
    col=wnd.get_at(cur)#get the color at the position of the pointer
    click = pygame.mouse.get_pressed()#gets a tuple of the mouse clicks (0 is not clicked and 1 is a click)
    wnd.fill(white)#white backgroouond
    button("Back",850,500,150,75,action="Back2play")#This button will be used to the continents view
    if showgrid:#will be used to show the image with the grid
        insrtPic("OtherPics/ColoredEuropeg.bmp",0,0,700,600)
    else:
        insrtPic("OtherPics/ColoredEurope.bmp",0,0,700,600)
    pygame.draw.rect(wnd,black,(745,40,210,120))#Makes a rectangular background behind the flag image
    #if hints are less than 0 make them equal to 0
    if Hints<0:
        Hints=0
    InHint= Hints#used show number of hints left
    button("Hints "+str(InHint),850,425,150,75,action="hint1Activate")#hint button
    #This loop will be used to display the country name as the pointer hover over it
    for index in range(len(EuropeValues)):#loop through the values in Africad dictionary
        countryValue= EuropeValues[index]#save the index of the value in a variable
        if col==countryValue[2]:#if the color the mouse is pointing at is in the list,blit the country name on the screen
            font=pygame.font.SysFont("ebrima",20,bold=True)#set the font and font size of the label 
            word=font.render(countryValue[0], True,black)
            wnd.blit(word,cur)#put the text on the surface on Asia
    if click[0]==1:#if mouse is clicked
        if Continentd!=Europed and col!=white and col!=mainBlue and col!=green and cur[0]<700 and value[0]!="Turkey" and value[0]!="Russia":#if the wrong continent
            oldCountry=value[0]#store the name of the previous country in this variable            
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Wrong",midWidth,midHeight,size=50,col=red)
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
        elif col==value[2]:#if the country is correct
            oldCountry=value[0]#store the name of the previous country in this variable
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Correct",midWidth,midHeight,size=50,col=green)
            Score=Score+1#increase the score by 1 if corrrect
            Continentd=random.choice(dictionaries)
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
        elif col!=value[2] and col!=white and col!=mainBlue and col!=green and cur[0]<700:#if the color is wrong and not the buttons
            oldCountry=value[0]#store the name of the previous country in this variable            
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Wrong",midWidth,midHeight,size=50,col=red)
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
#function used when asia is clicked
def AsiaLoop():
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,instructions,Africa,value,key,Africad,AfricaColors,keys,Score,midWidth,midHeight,img,AsiaValues
    global Continentd,Oceaniad,Asiad,NAd,SAd,Africad,Europed,Hints,Hint1,Hint3,Lives,oldCountry,showAnswer,Hint2
    cur = pygame.mouse.get_pos()#get the position of the pointer
    col=wnd.get_at(cur)#get the color at the position of the pointer
    click = pygame.mouse.get_pressed()#gets a tuple of the mouse clicks (0 is not clicked and 1 is a click)
    wnd.fill(white)#white background
    button("Back",850,500,150,75,action="Back2play")#This button will be used to the continents view
    if showgrid:#will be used to show the image with the grid
        insrtPic("OtherPics/Asiacolorg.bmp",0,0,700,600)
    else:
        insrtPic("OtherPics/Asiacolor.bmp",0,0,700,600)
    pygame.draw.rect(wnd,black,(745,40,210,120))#Makes a rectangular background behind the flag image
    #if hints are less than 0 make them equal to 0
    if Hints<0:
        Hints=0
    InHint= Hints#used show number of hints left
    button("Hints "+str(InHint),850,425,150,75,action="hint1Activate")#hint button
    #This loop will be used to display the country name as the pointer hover over it
    for index in range(len(AsiaValues)):#loop through the values in Africad dictionary
        countryValue= AsiaValues[index]#save the index of the value in a variable
        if col==countryValue[2]:#if the color the mouse is pointing at is in the list,blit the country name on the screen
            font=pygame.font.SysFont("ebrima",20,bold=True)#set the font and font size of the label 
            word=font.render(countryValue[0], True,black)
            wnd.blit(word,cur)#put the text on the surface on Asia
    if click[0]==1 :#if mouse is pressed
        if col==value[2]and Continentd==Asiad:
            oldCountry=value[0]#store the name of the previous country in this variable            
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Correct",midWidth,midHeight,size=50,col=green)
            Score=Score+1#increase the score by 1 if corrrect
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
        elif col!=value[2] and col!=white and col!=mainBlue and col!=green and cur[0]<700 :#if the color is wrong and not the buttons
            oldCountry=value[0]#store the name of the previous country in this variable            
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Wrong",midWidth,midHeight,size=50,col=red)
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
        elif Continentd!=Asiad and col!=white and col!=mainBlue and col!=green and cur[0]<700 :#if the wrong continent
            oldCountry=value[0]#store the name of the previous country in this variable            
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Wrong",midWidth,midHeight,size=50,col=red)
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
#function used when north america is clicked
def NALoop():
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,instructions,Africa,value,key,Africad,AfricaColors,keys,Score,midWidth,midHeight,img,NAValues
    global Continentd,Oceaniad,Asiad,NAd,SAd,Africad,Europed,Hints,Hint1,Hint3,Lives,oldCountry,showAnswer,Hint2
    cur = pygame.mouse.get_pos()#get the position of the pointer
    col=wnd.get_at(cur)#get the color at the position of the pointer
    click = pygame.mouse.get_pressed()#gets a tuple of the mouse clicks (0 is not clicked and 1 is a click)
    wnd.fill(white)#white background
    button("Back",850,500,150,75,action="Back2play")#This button will be used to the continents view
    if showgrid:#will be used to show the image with the grid
        insrtPic("OtherPics/ColoredNAg.bmp",50,50,600,525)
    else:
        insrtPic("OtherPics/ColoredNA.bmp",50,50,600,525)
    pygame.draw.rect(wnd,black,(745,40,210,120))#Makes a rectangular background behind the flag image
    #if hints are less than 0 make them equal to 0 
    if Hints<0:
        Hints=0
    InHint= Hints#used show number of hints left
    button("Hints "+str(InHint),850,425,150,75,action="hint1Activate")#hint button
    #This loop will be used to display the country name as the pointer hover over it
    for index in range(len(NAValues)):#loop through the values in Africad dictionary
        countryValue= NAValues[index]#save the index of the value in a variable
        if col==countryValue[2]:#if the color the mouse is pointing at is in the list,blit the country name on the screen
            font=pygame.font.SysFont("ebrima",20,bold=True)#set the font and font size of the label 
            word=font.render(countryValue[0], True,black)
            wnd.blit(word,cur)#put the text on the surface on Asia
    if click[0]==1 :#if mouse is pressed
        if col==value[2] and Continentd==NAd:#if country and continent are correct
            oldCountry=value[0]#store the name of the previous country in this variable            
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Correct",midWidth,midHeight,size=50,col=green)
            Score=Score+1#increase the score by 1 if corrrect
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
        elif col!=value[2] and col!=white and col!=mainBlue and col!=green and cur[0]<700 :#if the color is wrong and not the buttons
            oldCountry=value[0]#store the name of the previous country in this variable            
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Wrong",midWidth,midHeight,size=50,col=red)
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
        elif Continentd!=NAd and col!=white and col!=mainBlue and col!=green and cur[0]<700 :#if wrong continent and not the buttons
            oldCountry=value[0]#store the name of the previous country in this variable            
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Wrong",midWidth,midHeight,size=50,col=red)
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
#function used when South America is clicked
def SALoop():
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,instructions,Africa,value,key,Africad,AfricaColors,keys,Score,midWidth,midHeight,img,SAValues,Lives
    global Continentd,Oceaniad,Asiad,NAd,SAd,Africad,Europed,Hints,Hint1,Hint3,oldCountry,showAnswer,Hint2
    cur = pygame.mouse.get_pos()#get the position of the pointer
    col=wnd.get_at(cur)#get the color at the position of the pointer
    click = pygame.mouse.get_pressed()#gets a tuple of the mouse clicks (0 is not clicked and 1 is a click)
    wnd.fill(white)#white backgound
    button("Back",850,500,150,75,action="Back2play")#This button will be used to the continents view
    if showgrid:#will be used to show the image with the grid
        insrtPic("OtherPics/ColoredSAg.bmp",100,50,500,525)
    else:
        insrtPic("OtherPics/ColoredSA.bmp",100,50,500,525)
    pygame.draw.rect(wnd,black,(745,40,210,120))#Makes a rectangular background behind the flag image
    label=""
    #if hint is less than 0 make it equal to 0
    if Hints<0:
        Hints=0
    InHint= Hints#used show number of hints left
    button("Hints "+str(InHint),850,425,150,75,action="hint1Activate")#hint button
    #This loop will be used to display the country name as the pointer hover over it
    for index in range(len(SAValues)):#loop through the values in Africad dictionary
        countryValue= SAValues[index]#save the index of the value in a variable
        if col==countryValue[2]:#if the color the mouse is pointing at is in the list,blit the country name on the screen
            font=pygame.font.SysFont("ebrima",20,bold=True)#set the font and font size of the label 
            word=font.render(countryValue[0], True,black)
            wnd.blit(word,cur)#put the text on the surface on Asia
    if click[0]==1 :#if mouse is clicked
        if col==value[2]and Continentd==SAd:#if the continent and the country are correct
            oldCountry=value[0]#store the name of the previous country in this variable            
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Correct",midWidth,midHeight,size=50,col=green)#Display "correct"
            Score=Score+1#increase the score by 1 if corrrect
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
        elif col!=value[2] and col!=white and col!=mainBlue and col!=green and cur[0]<700 :#if the color is wrong
            oldCountry=value[0]#store the name of the previous country in this variable            
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Wrong",midWidth,midHeight,size=50,col=red)
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint2=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
        elif Continentd!=SAd and col!=white and col!=mainBlue and col!=green and cur[0]<700 :#if the wrong continent and not the buttons
            oldCountry=value[0]#store the name of the previous country in this variable            
            showAnswer=True #Will be used to display the correct answer if true
            Dtext("Wrong",midWidth,midHeight,size=50,col=red)
            Continentd=random.choice(dictionaries)#choose a new random country
            keys = Continentd.keys()#get a list of the keys in the dictionary
            key =random.choice(keys)#get a random key from the dictionary
            value = Continentd[key]#get the list of values for that country
            img = value[1]#get the image for that country
            #Remove the hints from the screen
            Hint1=False
            Hint3=False
            Hints=3
            pygame.time.delay(500)#wait for 0.5 of a second
#used to show all the common texts/images in multiple game windows
def showState():
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,instructions,Africad,Score,img,Oceania,Africa,Europe,NA,Asia,SA,Hint1,value,Hint3,Live1,Live2,Live3
    global Live4,Live5,oldCountry,showAnswer,showgrid,Hint2,value   
    pygame.draw.rect(wnd,mainBlue,(0,1,140,75))
    stringScore=str(Score)
    Dtext("Score:",2,0,font='bell',size=20)
    Dtext(stringScore,56,0,font='bell',size=20)
    if showgrid:#will be used to show the grid dividing countries on the map
        button("Hide Grid ",850,350,150,75,action="giddeactivate")#hint button
    else:
        button("Show Grid ",850,350,150,75,action="gridactivate")#hint button
    timer()#Add the timer
    insrtPic('Flags/'+img,750,50,200,100)#display the random flag picture
    if showAnswer: #Will be used to display the correct answer if true
        #Display the previous correct answer
        Dtext("Correct Answer Was: ",750,1,size=15,col=black)
        Dtext(oldCountry,775,13,size=15,col=black)
    #Display the frist hint on the screen
    if Hint1:
        if Continentd==Africad:
            Dtext("It's in Africa",750,157,col=black,size=20)
        elif Continentd==Oceaniad:
            Dtext("It's in Oceania",750,157,col=black,size=20)
        elif Continentd==NAd:
            Dtext("It's in North America",750,157,col=black,size=20)
        elif Continentd==SAd:
            Dtext("It's in South America",750,157,col=black,size=20)
        elif Continentd==Europed:
            Dtext("It's in Europe",750,157,col=black,size=20)
        elif Continentd==Asiad:
            Dtext("It's in Asia",750,157,col=black,size=20)
    #Display the second hint on the screen
    if Hint2:
        Dtext(value[3],750,183,col=black,size=20)
    if Hint3:
        country=value[0]
    #Display lives on the screen
        Dtext("It starts with letter "+country[0],750,210,col=black,size=20)
    if Live1:
        insrtPic("OtherPics/heart.jpg",2,40,xScale=20,yScale=20)
    if Live2:
        insrtPic("OtherPics/heart.jpg",23,40,xScale=20,yScale=20)
    if Live3:
        insrtPic("OtherPics/heart.jpg",44,40,xScale=20,yScale=20)
    if Live4:
        insrtPic("OtherPics/heart.jpg",65,40,xScale=20,yScale=20)
    if Live5:
        insrtPic("OtherPics/heart.jpg",86,40,xScale=20,yScale=20)
    button("Pause",850,275,150,75,action="exitGamenow")#Pause button
Frame=0#will be used to displaythe rotating globe frames
    
def MainLoop(): #The main loop to navigate between windows 
    global BG1,BG2,BG1col,BG2col,play,intro,wnd,wrldMap,instructions,Africad,Score,img,Oceania,Africa,Europe,NA,Asia,SA,Hint1,value,Hint3,Live1,frame_rate
    global leave,instruction1,instruction2,instruction3,instruction4,instruction5,instruction6,instruction7,instruction8,Frame
    cur = pygame.mouse.get_pos()
    col=wnd.get_at(cur)
    click = pygame.mouse.get_pressed()
    pygame.display.set_caption('Match the Flag')#Add the caption to the  window
    Exitgame=False
    while Exitgame is False:#Game loop
        for event in pygame.event.get():#get the event (action) done by  the user
            if (event.type==pygame.QUIT):#if the x button is clicked
                playExit=True#stop the while loop
                pygame.quit()#exit the window in pygame
                quit()#exit shell
    #This will be used to navigate between windows(loops)        
        if intro is True:
            instruction1=False
            instruction3=False
            instruction4=False
            instruction5=False
            instruction2=False
            instruction7=False
            instruction8=False        
            instruction6=False
            introLoop()
            xtime=50#delay time variable, will be used to control the speed of the sprite
            #Add the rotating globe sprite to the main menu, (keeps incrimenting a new frame)
            if Frame>47:
                Frame=0
            else:
                insrtPic("GlobeSprites/GS"+str(Frame)+".bmp",20,20,300,300)
                Frame+=1

        if play is True:
            intro=False
            Africa=False
            Asia=False
            NA=False
            SA=False
            Europe=False
            Oceania=False
            playLoop()
            showState()
        if instruction1:
            intro=False
            instruction2=False
            instruction3=False
            instruction4=False
            instruction5=False
            instruction6=False
            instruction7=False
            instruction8=False
            instr1()
        if instruction2:
            intro=False
            instruction1=False
            instruction3=False
            instruction4=False
            instruction5=False
            instruction6=False
            instruction7=False
            instruction8=False        
            instr2()
        if instruction3:
            intro=False
            instruction1=False
            instruction2=False
            instruction4=False
            instruction5=False
            instruction6=False
            instruction7=False
            instruction8=False        
            instr3()
        if instruction4:
            intro=False
            instruction1=False
            instruction3=False
            instruction2=False
            instruction5=False
            instruction6=False
            instruction7=False
            instruction8=False        
            instr4()
        if instruction5:
            intro=False
            instruction1=False
            instruction3=False
            instruction4=False
            instruction2=False
            instruction6=False
            instruction7=False
            instruction8=False        
            instr5()
        if instruction6:
            intro=False
            instruction1=False
            instruction3=False
            instruction4=False
            instruction5=False
            instruction2=False
            instruction7=False
            instruction8=False        
            instr6()
        if instruction7:
            intro=False
            instruction1=False
            instruction3=False
            instruction4=False
            instruction5=False
            instruction6=False
            instruction2=False
            instruction8=False        
            instr7()
        if instruction8:
            intro=False
            instruction1=False
            instruction3=False
            instruction4=False
            instruction5=False
            instruction6=False
            instruction7=False
            instruction2=False        
            instr8()
        if Africa is True and click[0]==0:
            intro=False
            play=False
            instructions=False
            Oceania=False
            AfricaLoop()
            showState()
        if Oceania is True:
            intro=False
            play=False
            instructions=False
            Africa=False
            OceaniaLoop()
            stringScore=str(Score)
            showState()
        if Europe is True:
            intro=False
            play=False
            instructions=False
            Africa=False
            Oceania=False
            EuropeLoop()
            showState()
        if Asia is True and click[0]==0:
            intro=False
            play=False
            instructions=False
            Africa=False
            AsiaLoop()
            showState()
        if NA is True:
            intro=False
            play=False
            instructions=False
            Africa=False
            NALoop()
            showState()
        if SA is True:
            intro=False
            play=False
            instructions=False
            Africa=False
            Asia=False
            Oceania=False
            NA=False
            Europe=False
            SALoop()
            showState()
        if End:
            endScreen()
        if leave:
            intro=False
            play=False
            instructions=False
            Africa=False
            Asia=False
            Oceania=False
            NA=False
            Europe=False
            SA=False 
            exitScreen()
        clock.tick(30)#frames displayed per second
        pygame.display.update()
MainLoop()    
#References :https://github.com/buckyroberts/Source-Code-from-Tutorials/tree/master/Pygame
#images:http://www.freeusandworldmaps.com/html/WorldRegions/WorldRegionsPrint.html
#http://www.clipartbest.com/black-and-white-map-of-europe-printable
#http://www.georgethegeographer.co.uk/Base_maps/Base_maps.html
#http://www.worldatlas.com/webimage/countrys/africa/afoutl.htm
#http://www.clipartkid.com/clip-art-world-map-with-countries-cliparts/
#http://www.helixsoft.nl/articles/sphere/sphere.html
