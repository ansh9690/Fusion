from django.http import HttpResponseRedirect
from django.urls import reverse
from notifications.utils import id2slug, slug2id
from django.shortcuts import get_object_or_404, redirect
from notifications.models import Notification

def RepresentsInt(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False
        
def mark_as_read_and_redirect(request, slug=None):
    notification_id = slug2id(slug)
    notification = get_object_or_404(
        Notification, recipient=request.user, id=notification_id)
    notification.mark_as_read()
    complaint_id=notification.description

    # This conditional statement is True only in
    # case of complaint_module.

    if(RepresentsInt(complaint_id) is True):
        print('Yes it is an id')
        return HttpResponseRedirect(reverse(notification.data['url'],kwargs={'detailcomp_id1':complaint_id}))
    else:
        return HttpResponseRedirect(reverse(notification.data['url']))

