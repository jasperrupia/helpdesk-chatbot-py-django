
from django.shortcuts import render, redirect
from .models import User, UserVisit, Docs, UserFeedback, Tag, Message, Response

from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password, make_password
from django.contrib import messages
from datetime import date



@login_required(login_url='')
def dashboard(request):

    user_visit_count = UserVisit.objects.all().order_by('date_visitad').values() 
    visit_trend = []
    visit_date = []
    for instance in user_visit_count[:7]:
        if date.today().strftime("%d/%m/%Y") == instance['date_visitad'].strftime("%d/%m/%Y"):
            visit_date.append('Today')
        else:
            visit_date.append(instance['date_visitad'].strftime("%d/%m/%Y"))
        visit_trend.append(instance['count_users']) 
    feedback_values = UserFeedback.objects.all().order_by('-date') 
    context = {
        'visit_date': visit_date,
        'visit_trend': visit_trend,
        'feedback_values': feedback_values  
    }
    return render(request, 'advanced/index.html', context)



@login_required(login_url='')
def feed_docs(request):
    if 'upload_doc' in request.POST:
        query = Docs(   name = request.POST['doc_name'],
                        doc = request.FILES['doc_file'],
                        trainer = request.user
                        )
        query.save()
        messages.success(request, 'The document successful uploaded')
    doc_values = Docs.objects.all().order_by('-date')
    context = {
        'doc_values': doc_values
    }
    return render(request, 'advanced/page_feed_docs.html', context)



@login_required(login_url='')
def test(request):
    return render(request, 'advanced/page_test_bot.html')



@login_required(login_url='')
def profile(request):
    return render(request, 'advanced/page_profile.html')



@login_required(login_url='')
def updateProfile(request):
    query = User.objects.get(id=request.user.id)
    if 'update_dp' in request.POST: 
        try:
            query.avata = request.FILES['avata']
            query.save()
        except:
            pass
    elif 'reset_dp' in request.POST:
        query.avata = 'users/no-profile.jpg'
        query.save()
    elif 'update_info' in request.POST:
        query.username = request.POST['username']
        query.email = request.POST['email']
        query.tel = request.POST['tel']
        query.save()
    elif 'update_pwd' in request.POST: 
        oldPassword = request.POST['oldPassword'] 
        check = check_password(oldPassword, request.user.password) 
        if check: 
            newPassword = request.POST['newPassword'] 
            confirmPassword = request.POST['confirmPassword'] 
            if newPassword == confirmPassword: 
                password = make_password(newPassword) 
                query.password = password 
                query.save() 
                #messages.success(request, ('Password updated')) 
                return redirect('adminPanel:profile') 
            else: 
                messages.warning(request, ('New Password & Confirm didn\'t match')) 
                return redirect('adminPanel:profile') 
        else: 
            messages.warning(request, ('Old Password incorrect!')) 
            return redirect('adminPanel:profile') 
    else:
        return redirect('profile')
    return redirect('adminPanel:profile')


@login_required(login_url='')
def feedbacks(request):
    feedback_values = UserFeedback.objects.all().order_by('-date') 
    context = {
        'feedback_values': feedback_values 
    }
    return render(request, 'advanced/page_feedbacks.html', context)


@login_required(login_url='')
def theme(request):
    return render(request, 'advanced/page_theme.html')