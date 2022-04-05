#from msilib.schema import Class
#from sre_constants import SUCCESS
#from telnetlib import STATUS
#from django.urls import reverse_lazy
#from rest_framework import status
#from rest_framework import generics
#from rest_framework import viewsets
#from rest_framework.response import Response
from django.shortcuts import get_object_or_404, render
#from users.forms import FormularioUser
#from .models import UserProfile
#from .models import UserEducation
#from . import serializers
#from Portal.permissions import IsOwnerOrReadOnly
#from django.http import HttpRequest

#from django.contrib.auth.forms import UserChangeForm
#from django.views import generic
#from jobs.permissions import IsOwnerOrReadOnly
#from users.serializers import UserProfileSerializer

#from rest_framework.renderers import TemplateHTMLRenderer
#from rest_framework.views import APIView

#from django.views.generic import TemplateView


#class UserEditView(generic.CreateView):
#    form_class = FormularioUser 
#    template_name = 'users/edit_profile.html'
#    success_url = reverse_lazy('home')    



#class UserProfileViewSet(viewsets.ModelViewSet):
#    queryset = UserProfileSerializer.Meta.model.objects.all()
#    serializer_class = UserProfileSerializer
    #permission_classes = (IsOwnerOrReadOnly,)
#    template_name = 'users/edit2.html'
#    success_url = reverse_lazy('home')
    
    #def my(request):
    #    assert isinstance(request,HttpRequest)
    #    queryset = UserProfileSerializer.Meta.model.objects.all()
    #    serializer_class= UserProfileSerializer(queryset,many = True)
    #    return render(request, 'users/edit2.html',{'data':serializer_class.data})
    
    
    #def get_queryset(self,pk=None):
    #    if pk is None:
      #      return self.get_serializer().Meta.model.objects.all()
     #   return self.get_serializer().Meta.model.objects.filter(id=pk).first()

    #def list(self,request):
     #   userProfile_serializer = self.get_serializer(self.get_queryset(),many=True)
     #   return Response(userProfile_serializer.data,status=status.HTTP_200_OK)


    
    #def create (self,request):
    #    print ("Creating Meta")
    #    serializers=self.serializer_class(data = request.data)
    #    if serializers.is_valid():
    #        serializers.save()
    #        return Response({'message':'Usuario creado correctamente'},status=status.HTTP_201_CREATED)
    #    return Response(serializers.errors,status= status.HTTP_400_BAD_REQUEST)
    
    #def destroy(self, request,pk=None):
     #   userProfile= self.get_queryset().filter(id=pk).first()
      #  if userProfile:
      #      userProfile.active = False
      #      userProfile.save()
       #     return Response({'message': 'Usuario eliminado correctamente'},status= status.HTTP_201_CREATED)
       # return Response({'error':'No existe usuario con estos datos'},status= status.HTTP_400_BAD_REQUEST)
   
    #def update(self,request,pk=None):
     #   if self.get_queryset(pk):
     #       UserProfile_serializer=self.serializer_class(self.get_queryset(pk),data =request.data)
     #       if UserProfile_serializer.is_valid():
      #          UserProfile_serializer.save()
      #          return Response(UserProfile_serializer.data,status=status.htttp_200_OK)
      #      return Response(UserProfile_serializer.errors,status= status.HTTP_400_BAD_REQUEST)
    
      
            
        
    
    
    
    
    
#class formularioUserView(HttpRequest):
    
#    def index(request):
#        UserProfile= FormularioUser()
#        return render(request, 'users/RegistrarUsuario.html',{'form':UserProfile})
    
    #def  procesar_formulario(request):
          #UserProfile= FormularioUser()
          #if UserProfile.is_valid():
           #   UserProfile.save()
           #   UserProfile= FormularioUser()
            #  return render(request, 'users/RegistrarUsuario.html',{'form':UserProfile,'mensaje':'OK'})
          

