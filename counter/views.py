from django.shortcuts import render,redirect
from .models import Counter
# tjHzkeo3hdPCYHnnZCY8KQ==h6w2WcJZe9T5sqsR
# Create your views here.
def calorie(request):
    import requests
    import json
    if request.method =='POST':
        query = request.POST['query']
        api_url ='https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query,headers={'X-Api-Key': 'tjHzkeo3hdPCYHnnZCY8KQ==h6w2WcJZe9T5sqsR'})
        try:
            api=json.loads(api_request.content)
            print(api_request.content)
        except Exception as e:
            api= "oops! There was an error"
            print(e)
        return render(request,'calorie.html',{'api':api})
    else:
        return render(request,'calorie.html',{'query':'Enter a valid value'})
def home(request):
    return render(request,'home.html')
def calorieintake(request):
    return render(request,'calorieintake.html')
def about(request):
    return render(request,'about.html')
def daily(request):
    foods=Counter.objects.all()
    return render(request,'daily.html',{'foods':foods }) 
def addfood(request):
    import requests
    import json
    if request.method=='POST':
        query = request.POST.get('query')
        api_url ='https://api.api-ninjas.com/v1/nutrition?query='
        api_request = requests.get(api_url + query,headers={'X-Api-Key': 'tjHzkeo3hdPCYHnnZCY8KQ==h6w2WcJZe9T5sqsR'}).json()
        # api=json.loads(api_request.content)
        cal=api_request[0].get('calories')
        print('Total Calories' , cal)
        Counter.objects.create(query=query,cal=cal)
        # try:
        #     api=json.loads(api_request.content)
        #     print(api_request.content)
        # except Exception as e:
        #     api= "oops! There was an error"
        #     print(e)
        # return render(request,'daily.html')
    return redirect('daily')
def added(request,food_id):
    food=Counter.objects.get(id=food_id)
    food.add=True
    food.save()
    return redirect('daily')

def delete(request,food_id):
    food=Counter.objects.get(id=food_id)
    food.delete()
    return redirect('daily')