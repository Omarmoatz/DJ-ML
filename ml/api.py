from rest_framework.response import Response
from rest_framework import generics,status
import pandas as pd

from .models import Iris

class IrisAPI(generics.GenericAPIView):

    def post(self, request, *args, **kwargs):
            data = request.data

            sepal_length = data['sepal_length']
            sepal_width = data['sepal_width']
            petal_length = data['petal_length']
            petal_width = data['petal_width']

            model = pd.read_pickle('model.pickle') # Load the trained model
            result = model.predict([['sepal_length','sepal_width','petal_length','petal_width']])
            predict = result[0]  # The prediction is in the first

            Iris.objects.create(
                  sepal_length = sepal_length,
                  sepal_width= sepal_width,
                  petal_length= petal_length,
                  petal_width= petal_width,
                  class_iris= predict  # Save it to the database with the predicted class
              )
            
            return Response({"prediction": f"The iris belongs to species {predict}"} 
                            ,status=status.HTTP_201_CREATED)
            