from django.shortcuts import render
from .forms import AccountForm
from .models import Account_Data

def add_credit_debit(request):
    if request.method=='POST':
        form_object=AccountForm(request.POST)
        if form_object.is_valid():
            u_name_=request.user.username
            d_or_c_=form_object.cleaned_data['d_or_c']
            name_=form_object.cleaned_data['name']
            m_no_=form_object.cleaned_data['m_no']
            date_=form_object.cleaned_data['date']
            amount_=form_object.cleaned_data['amount']
            paid_=form_object.cleaned_data['paid']
            date_of_transaction_=form_object.cleaned_data['date_of_transaction']
            db_object=Account_Data(u_name=u_name_,d_or_c=d_or_c_,name=name_,m_no=m_no_,date=date_,amount=amount_,paid=paid_,date_of_transaction=date_of_transaction_)
            db_object.save()
            form_object2=AccountForm()
            query_set_=Account_Data.objects.filter(u_name=u_name_)
            return render(request,'account/show_account.html',{'query_set':query_set_})
        else:
            form_object=AccountForm()
    else:
        form_object=AccountForm()
    return render(request,'account/add_credit_or_debit.html',{'form':form_object})

def show_account(request):
    user_name=request.user.username
    query_set_=Account_Data.objects.filter(u_name=user_name)
    return render(request,'account/show_account.html',{'query_set':query_set_})

def delete_data(request,id):
    if request.method=='POST':
        del_row = Account_Data.objects.get(pk=id)
        del_row.delete()
    
    user_name=request.user.username
    query_set_=Account_Data.objects.filter(u_name=user_name)
    return render(request,'account/show_account.html',{'query_set':query_set_})

def update_data(request,id):
    if request.method == 'POST':
        db_object=Account_Data.objects.get(pk=id)
        form_object=AccountForm(request.POST,instance=db_object)
        if form_object.is_valid():
            form_object.save()
            user_name=request.user.username
            query_set_=Account_Data.objects.filter(u_name=user_name)
            return render(request,'account/show_account.html',{'query_set':query_set_})
            
    else:
        db_object=Account_Data.objects.get(pk=id)
        form_object=AccountForm(instance=db_object)

    return render(request,'account/update_data.html',{'form':form_object})