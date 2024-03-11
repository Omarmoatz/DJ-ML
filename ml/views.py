from django.shortcuts import render
import pandas as pd

from .models import Iris
from .form import IrisForm

def predection(request):
    if request.method == 'POST':
        form = IrisForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            sepal_length = form.cleaned_data['sepal_length']
            sepal_width = form.cleaned_data['sepal_width']
            petal_length = form.cleaned_data['petal_length']
            petal_width = form.cleaned_data['petal_width']

            model = pd.read_pickle('model.pickle')  # Load the trained model
            result = model.predict([['sepal_length','sepal_width','petal_length','petal_width']])

            predict = result[0]
            my_form.species = predict
            my_form.save()
            return render(request , 'iris.html',{'form':form,'predect':predict})
    else:
        form = IrisForm()
    return render(request , 'iris.html',{'form':form})

