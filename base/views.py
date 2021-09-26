from base.models import NotificationImage, userToken
from django.shortcuts import render
import firebase_admin
from firebase_admin import credentials , messaging

from base.FCMmanage import sendPush

def dashboard(request):
    return render(request, 'base/dashboard.html')

def sendNotifications(request):
    if request.method == 'POST':
        title = request.POST['Title']
        desc = request.POST['Descriptions']
        try:
            img = request.FILES['image']
            try:
                imageObject = NotificationImage.objects.get(id=1)
                imageObject.image = img
                imageObject.save()
            except NotificationImage.DoesNotExist:
                NotificationImage.objects.create(image=img)
        except:
            print("")
        
        image = NotificationImage.objects.all()
        tokens = userToken.objects.all()
        allTokens = []
        push_img = {}
        for tokenlist in tokens:
            allTokens.append(tokenlist.token)
        if image:
            push_img = {'image': image[0].image.url}

        sendPush(title,desc,allTokens,push_img)

        return render(request, 'base/dashboard.html')

    else:
        return render(request, 'base/dashboard.html')



        
