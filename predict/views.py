from django.shortcuts import render, redirect
from .forms import AgregarTarea, UploadFileForm
from .utils import get_image
import pandas as pd

import matplotlib.pyplot as plt



# Create your views here.

tareas = ["aprender django", "estudiar examen", "cls"]

def home(request):
    context = {'tareas':tareas}
    return render(request, 'predict/home.html', context)

def add(request):
    if request.method == 'POST':
        form = AgregarTarea(request.POST)
        # print("-----------------------")
        # print(form)
        # print("-----------------------")
        if form.is_valid():
            tarea = form.cleaned_data["tarea"]
            # print("-----------------------")
            # print(tarea)
            # print("-----------------------")
            tareas.append(tarea)
            return redirect('home')
    else:
        form =  AgregarTarea()

    context = {
        'form':form
    }
    return render(request, "predict/add.html", context)

# Nota: def predict(request):
#       El nombre sale de urls.py [ name='predict'  ]



def predict(request):
    if request.method == 'POST':
        upload = UploadFileForm(request.POST, request.FILES)
        # print("----------[1]-------------")
        # print(upload)
        # print("-----------------------")
        if upload.is_valid():
            title = upload.cleaned_data["title"]
            file = upload.cleaned_data["file"]
            print("-----------[2]------------")
            # print(type(title))
            # print("-----------[convirtiendo a float]------------")
            # print(float(title))
            # print(type((float(title))))
            # print("---------[str]--------------")
            print(title)
            print("-----------------------")
            print("---------[3]--------------")
            print(type(file))
            print(file)
            print("------------ [PANDAS] -----------")
            df = pd.read_csv(file)
            print(type(df))
            print("-----------Views df------------")
            print(df.head(10))
            print("-----------selecionando la fila [0]------------")
            # selecionn de columnas o filas con pandas
            # https://www.analyticslane.com/2019/06/21/seleccionar-filas-y-columnas-en-pandas-con-iloc-y-loc/

            print((df.iloc[0])[0]) # Primera fila
            print((df.iloc[0])[1]) # Primera fila
            print((df.iloc[0])[2]) # Primera fila
            print((df.iloc[0])[3]) # Primera fila
            print((df.iloc[0])[4]) # Primera fila

            print("---------- haciendo uso de utils------------")
            #-----------------------------FIgura Uno--------------------------------
            plt.switch_backend('agg')
            plt.xticks(rotation=45)

            print("-------Figura-----1-----")
            x = [1,2,3,4,5]
            y = [50,40,70,80,20]
            y2 = [80,20,20,50,60]
            y3 = [70,20,60,40,60]
            y4 = [80,20,20,50,60]
            plt.plot(x,y,'g',label='Enfield', linewidth=5)
            plt.plot(x,y2,'c',label='Honda',linewidth=5)
            plt.plot(x,y3,'k',label='Yahama',linewidth=5)
            plt.plot(x,y4,'y',label='KTM',linewidth=5)
            plt.title('bike details in line plot')
            plt.ylabel('Distance in kms')
            plt.xlabel('Days')
            plt.legend()
                    
            plt.tight_layout()
            graph = get_image()

            print("-------Figura-----1-----")
            #-----------------------------FIgura Dos--------------------------------
            print("-------Figura-----2-----")
            plt.switch_backend('agg')
            plt.xticks(rotation=45)

            
            x1 = [1,2,3]
            y2 = [50,40,70]
            y21 = [80,20,20]
            y31 = [70,20,60]
            y41 = [80,20,20]
            plt.plot(x1,y2,'g',label='Enfield', linewidth=5)
            plt.plot(x1,y21,'c',label='Honda',linewidth=5)
            plt.plot(x1,y31,'k',label='Yahama',linewidth=5)
            plt.plot(x1,y41,'y',label='KTM',linewidth=5)
            plt.title('bike details in line plot')
            plt.ylabel('Distance in kms')
            plt.xlabel('Days')
            plt.legend()
                    
            plt.tight_layout()
            graph2 = get_image()
            print("-------Figura-----2-----")

            context = {
                'upload':upload,
                'graph':graph,
                'graph2':graph2,
            }
            return render(request, "predict/predict.html", context)

    else:
        upload = UploadFileForm()
    #------------------------------------------------------------------------------------------------------------
    #----------------------                 [FUNCIONA MUY BIEN SIN EL IF]         ---------------------------------------------------------------
    #------------------------------------------------------------------------------------------------------------
    # print("---------- haciendo uso de utils------------")
    # #-----------------------------FIgura Uno--------------------------------
    # plt.switch_backend('agg')
    # plt.xticks(rotation=45)

    # print("-------Figura-----1-----")
    # x = [1,2,3,4,5]
    # y = [50,40,70,80,20]
    # y2 = [80,20,20,50,60]
    # y3 = [70,20,60,40,60]
    # y4 = [80,20,20,50,60]
    # plt.plot(x,y,'g',label='Enfield', linewidth=5)
    # plt.plot(x,y2,'c',label='Honda',linewidth=5)
    # plt.plot(x,y3,'k',label='Yahama',linewidth=5)
    # plt.plot(x,y4,'y',label='KTM',linewidth=5)
    # plt.title('bike details in line plot')
    # plt.ylabel('Distance in kms')
    # plt.xlabel('Days')
    # plt.legend()
                    
    # plt.tight_layout()
    # graph = get_image()
    # print("-------Figura-----1-----")
    # #-----------------------------FIgura Dos--------------------------------
    # print("-------Figura-----2-----")
    # plt.switch_backend('agg')
    # plt.xticks(rotation=45)

            
    # x1 = [1,2,3]
    # y2 = [50,40,70]
    # y21 = [80,20,20]
    # y31 = [70,20,60]
    # y41 = [80,20,20]
    # plt.plot(x1,y2,'g',label='Enfield', linewidth=5)
    # plt.plot(x1,y21,'c',label='Honda',linewidth=5)
    # plt.plot(x1,y31,'k',label='Yahama',linewidth=5)
    # plt.plot(x1,y41,'y',label='KTM',linewidth=5)
    # plt.title('bike details in line plot')
    # plt.ylabel('Distance in kms')
    # plt.xlabel('Days')
    # plt.legend()
                    
    # plt.tight_layout()
    # graph2 = get_image()
    # print("-------Figura-----2-----")

    context = {
        'upload':upload,
    }
    return render(request, "predict/predict.html", context)

#---------------------------------------------------------

# def predict(request):
#     return render(request, 'predict/predict.html')

def visualizar_datos_online(request):
    return render(request, 'predict/views_datos_online.html')

def visualizar_controles(request):
    return render(request, 'predict/views_controles.html')