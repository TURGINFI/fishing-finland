from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from .models import PlatformMessage


@login_required
def inbox_list(request):
    messages = PlatformMessage.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'messages_app/inbox.html', {'messages_list': messages})


@login_required
def mark_message_read(request, pk):
    msg = get_object_or_404(PlatformMessage, pk=pk, recipient=request.user)
    msg.is_read = True
    msg.save()
    return redirect('inbox_list')
