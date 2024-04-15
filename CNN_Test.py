import tkinter as tk
from tkinter import filedialog
import numpy as np
from keras.preprocessing import image
from keras.models import model_from_json
from tkinter import *
import tkinter.font as tkFont
a=["Apple Scab\n","A serious disease of apples and ornamental crabapples,\n apple scab(Venturia inaequalis) attacks both leaves and fruit.\n","Treatment","Myclobutanil (Spectracide Immunox Multipurpose Fungicide Spray Concentrate) is a synthetic fungicide that is effective against apple scab."]
b=["Apple Black rot\n","Black rot is an important disease of apple caused by the fungus Botryosphaeria obtusa.\n","Treatment\n","Myclobutanil (Spectracide Immunox Multipurpose Fungicide Spray Concentrate) is a synthetic fungicide that is effective against apple scab."]
c=["Apple Cedar-apple rust\n","Cedar apple rust is a member of the family Pucciniaceae,\n a group of fungi that contains many species that usually require two or more hosts to complete the life cycle.","Treatment","Fungicides with the active ingredient Myclobutanil are most effective in preventing rust."]
d="Healthy apple leaf"
e=["Corn spot gray disease\n","Gray leaf spot is typically the most serious foliar disease of corn in the U.S. corn belt\n","Treatment\n","Management techniques include crop resistance, crop rotation, residue management, use of fungicides, and weed control."]
f=["Corn common rush\n","Common rust is caused by the fungus Puccinia sorghi.\n","Treatment\n","Remove and destroy all leaves and plant parts affected by rust."]
g="Healthy corn leaf"
h=["Corn northern leaf blight\n","A foliar disease of corn (maize) caused by Exserohilum turcicum,\n the anamorph of the ascomycete Setosphaeria turcica.\n","Treatment\n","Use resistant hybrids. Fungicides may be warranted on inbreds for seed production during the early stages of this disease."]
i=["Grape black rot\n","Grape black rot is a fungal disease caused by an ascomycetous fungus, Guignardia bidwellii,\n that attacks grape vines during hot and humid weather.\n","Treatment\n","Remove the prunings, excess growth, diseased and overwintering berries, leaves, and tendrils from the vineyard, and burn or otherwise destroy them."]
j=["Grape esca\n","Bacterial blight of grapevine is a serious,\n chronic and systemic disease of grapevine that affects commercially important cultivars.","Treatment","Soak dormant cuttings for 30 mins in hot water at about 50°C. This treatment is not always effective and must therefore be combined with other methods."]
k="Healthy grape leaf"
l=["Grape leaf blight\n","Bacterial blight of grapevine is a serious,\n chronic and systemic disease of grapevine that affects commercially important cultivars.\n","Treatment\n","All affected portions of the vine should be removed at the time of pruning and destroyed immediately"]
m=["Potato early blight\n","Early blight is primarily a disease of stressed or senescing plants.\n","Treatment\n","Early blight can be minimized by maintaining optimum growing conditions, including proper fertilization, irrigation, and management of other pests"]
n="Healthy potato leaf"
o=["potato late blight\n","Late blight caused by the fungus Phytophthora infestans is the most important \n disease of potato that can result into crop failures in a short period if appropriate control measures are not adopted.\n","Treatment\n","Late blight is controlled by eliminating cull piles and volunteer potatoes, using proper harvesting and storage practices, and applying fungicides when necessary."]
p=["Tomato Bacterial spot\n","Late blight is controlled by eliminating cull piles and volunteer potatoes,\n using proper harvesting and storage practices, and applying fungicides when necessary\n.", "Treatment\n","Hot water treatment at 122°F for 25 min is effective in reducing bacterial population on the surface and inside the seeds, but may affect seed germination when the temperature is not properly controlled"]
q=["Tomato Early blight\n","Early blight is one of the most common tomato and potato diseases,\n occurring nearly every season in Minnesota.\n","Treatment\n","Use pathogen-free seed, or collect seed only from disease-free plants."]
r="Healthy tomato leaf"
s=["Tomato Late blight\n","Leaf symptoms of late blight first appear as small,\n water-soaked areas that rapidly enlarge to form purple-brown, oily-appearing blotches.\n","Treatment\n","Tomato varieties resistant to certain races of the late blight fungus are grown where the disease occurs regularly."]
t=["Tomato Leaf Mold\n"," Leaf mould is a fungal disease that affects the foliage of tomatoes, particularly those grown in greenhouses.\n","Treatment\n","Applying fungicides when symptoms first appear can reduce the spread of the leaf mold fungus significantly"]
u=["Tomato Septoria leaf spot\n","Septoria leaf spot is caused by the fungus Septoria lycopersici.\n","Treatment\n","Fungicides are very effective for control of Septoria leaf spot and applications are often necessary to supplement the control strategies previously outlined."]
v=["Tomato Spider mites Two spotted spider mite\n","The two-spotted spider mite is the most common mite species that attacks vegetable and fruit crops in New England.\n", "Treatment\n","With most miticides (excluding bifenazate), make 2 applications, approximately 5-7 days apart."]
w=["Tomato target spot\n","Target spot of tomato is caused by the fungal pathogen Corynespora cassiicola.\n","Treatmeat\n","Warm wet conditions favour the disease such that fungicides are needed to give adequate control."]
x=["Tomato Yellow Leaf Curl Virus\n","Tomato yellow leaf curl virus (TYLCV) can infect over 30 different kinds of plants, but it is mainly known to cause devastating losses of up to 100 per cent in the yield of tomatoes.\n","Treatment\n","Use a neonicotinoid insecticide, such as dinotefuran (Venom) imidacloprid (AdmirePro, Alias, Nuprid, Widow, and others)"]
y=["Tomato mosaic virus\n","The fruit may be distorted, yellow blotches and necrotic spots may occur on both \n ripe and green fruit and there may be internal browning of the fruit wall.\n","Treatment\n","Remove all infected plants and destroy them. Do NOT put them in the compost pile, as the virus may persist in infected plant matter."]
   

win=tk.Tk()

def b1_click():
    global path2
    try:
        json_file = open('model1.json', 'r')
        loaded_model_json = json_file.read()
        json_file.close()
        loaded_model = model_from_json(loaded_model_json)
        # load weights into new model
        loaded_model.load_weights("model1.h5")
        print("Loaded model from disk")
        label=[a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x,y]

        path2=filedialog.askopenfilename()
        print(path2)

        test_image = image.load_img(path2, target_size = (128, 128))        
        test_image = image.img_to_array(test_image)
        test_image = np.expand_dims(test_image, axis = 0)
        result = loaded_model.predict(test_image)
        print(result)
        label2=label[result.argmax()]
        print(label2)
        lbl.configure(text=label2)
        win.mainloop()
        

    except IOError:
        pass

fontObj = tkFont.Font(size=25)
fontObj1 = tkFont.Font(size=15)
label1 = Label(win, text="Leaf Classification and Disease Detection using CNN",width=50,height=10,font=fontObj,fg ='green')
label1.pack()
    
b1=tk.Button(win, text= 'browse image',width=25, height=5,fg ='red', command=b1_click)
b1.pack()
lbl = Label(win, text="Result",width=200,height=10,font=fontObj1, fg ='gray7')
lbl.pack()

win.geometry("550x250")
win['background']='#48483D'
win.title("Leaf Disease Detection using CNN")
win.bind("<Return>", b1_click)
win.mainloop() 
