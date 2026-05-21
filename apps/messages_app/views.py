from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .models import PlatformMessage


@login_required
def inbox_list(request):
    messages = PlatformMessage.objects.filter(recipient=request.user).order_by('-created_at')
    return render(request, 'messages_app/inbox.html', {'messages_list': messages})


@login_required
@require_POST
def mark_message_read(request, pk):
    msg = get_object_or_404(PlatformMessage, pk=pk, recipient=request.user)
    msg.is_read = True
    msg.save(update_fields=['is_read'])
    return redirect('inbox_list')
