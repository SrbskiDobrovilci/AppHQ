from django.shortcuts import render
from django.http import HttpResponse
from mainApp.models import Groups, Products, Lessons, Students, Accesses
import pickle

def home(request):
    return HttpResponse("matie bal")

def add_vision(request, userId, productId):
    acces = Accesses(userId = userId, productId = productId)
    acces.save()
    acceses = Accesses.objects.all()
    acceses = pickle.loads(pickle.dumps(acceses.query))
    
    students = list(Students.objects.all())
    students = pickle.loads(pickle.dumps(students.query))
    
    products = Products.objects.all()
    products = pickle.loads(pickle.dumps(products.query))
    
    
    counterStudInProduct = {}
    
    groups = {}
    
    """amount = Accesses.object.raw("SELECT productId, COUNT(userId) as userCount FROM Accesses GROUP BY productId " )
    
    amntOfGroup = {}
    
    for product in amount:
        amntOfGroup[product.productId] = max( (int(product.userCount) - 1) / Products.objects.get(id = int(product.productId)).maxUser    + 1, Products.objects.get(id = product.productId).minUser)
    
    """
    for acces in acceses:
        prodId = acces['productId']
        stId = acces['userId']
        if (int(counterStudInProduct[prodId]) % Products.objects.get(id = int(prodId)).maxUser == 0 ):
            groups[prodId] = Groups(name = "smName", productId = prodId)
        
        counterStudInProduct[prodId] += 1
        stud = Students.objects.get(id = int(stId))
        stud.groupId = groups[prodId]
        stud.save()
        
    
                
    return HttpResponse()