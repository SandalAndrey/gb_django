from django.shortcuts import render


def main(request):
    return render(request, 'contactsapp/contacts.html')
